# Ce que le pantin du kit sait faire, et ce qu'il ne sait pas faire

Le kit 2.5D de la catégorie `styles-2-5d-histoire-vraie` (`kit/personnages.py` pour le dessin, classe `Perso` de `kit/bl_lib.py` pour le montage dans Blender) fournit un pantin plat. Ce document dit honnêtement où il s'arrête, pour qu'on écrive la liste de plans **en fonction de ce qu'il sait faire**, et non l'inverse.

**D'où ça vient.** Un film réel de 61,5 s, 36 plans et huit pantins, fabriqué par le studio le 11/11/2026 (essai interne, non publié). Son compte rendu le dit sans détour : « aujourd'hui un personnage ne peut être vu que de face ». Plusieurs corrections imposées par la critique venaient de là. Ce qui suit distingue ce qui a été **vu** sur ce film, ce qui a été **essayé** en écrivant le kit, et ce qui est **écrit sans essai**.

## Ce que le pantin sait faire

| Capacité | Comment | État |
|---|---|---|
| Rester plat et à sa couleur dans un décor éclairé | plans à matériau émissif, découpés par la transparence, sans ombre portée ; vue « Standard » | vu sur le film, refait avec le kit |
| Être posé au sol | disque d'ombre de contact sous les pieds | vu, refait |
| Faire face à la caméra | `place(…, vers=(x, y de la caméra))` : rotation autour de l'axe vertical seulement | vu, refait |
| Changer d'expression | yeux, bouche et extra échangés image par image (`visage()`), clignement (`cligne()`) | vu, refait |
| « Regarder » quelque chose | le visage entier glisse sur la tête (`tete_(dx=…, dy=…)`) et les yeux passent à `cote` | vu, refait |
| Incliner la tête, pencher le tronc | rotation dans le plan de l'image (`tete_(incl=…)`, `tronc_(incl=…)`) | vu, refait |
| Lever un bras | rotation du bras entier autour de l'épaule, dans le plan de l'image (`bras_()`), avec anticipation et tenue (`geste()`) | vu, refait |
| Se déplacer en glissant, puis **s'arrêter** | `deplace(f0, f1, x=…)` : la clé d'arrivée est tenue | le défaut a été vu sur le film ; la correction est essayée avec le kit |
| Paraître marcher de loin | `marche()` : petit rebond du tronc à chaque appui | vu sur le film |
| Servir de figurant | une autre entrée de `PERSOS` : mêmes pièces, autres couleurs, autre hauteur | vu (8 pantins sur le film) |

## Ce qu'il ne sait pas faire

| Limite | Ce qu'on voit à l'écran | Constat |
|---|---|---|
| **Une seule vue : de face.** Pas de trois quarts, de profil ni de dos. | Tous les personnages regardent la caméra, même quand ils regardent un objet. Trois personnages reviennent quatre fois dans le même axe. | vu : « répétitions » relevées par la critique |
| **Il ne tourne pas la tête.** Le regard est un glissement du visage. | Les pupilles ne visent pas franchement l'objet. | vu : resté ouvert après deux tours |
| **Les mains ne pointent pas.** Le bras est une seule pièce raide (pas de coude, pas de poignet), la main n'a pas de doigt. | Un bras « pointé » est un bâton levé. Il ne peut désigner qu'**à gauche, à droite, en haut ou en bas de l'image**, jamais vers le fond ni vers la caméra. Tendu, il sort facilement du cadre. | vu : un bras pointé sortait du cadre, il a fallu pointer de l'autre bras et resserrer |
| **Il ne tient rien.** Aucun point d'attache dans la main. | Un objet « tenu » est un objet posé près de la main : il flotte dès que le bras bouge. | vu : un pinceau tenait debout tout seul, à 40 cm de la main |
| **Il ne marche pas.** Les deux jambes sont une seule pièce ; il n'y a pas de cycle de marche. | Le personnage glisse en rebondissant. Lisible petit dans un plan large, faux en plan moyen. | vu |
| **Il ne s'assoit pas, ne se penche pas en avant, ne se retourne pas.** | S'asseoir se triche en le descendant derrière un meuble ; un bout de costume peut dépasser dessous. | vu : une robe dépassait sous une table |
| **Les bras passent toujours devant le corps.** L'ordre des pièces est fixe. | Impossible de passer un bras derrière le dos ou derrière un objet tenu. | écrit d'après le code |
| **La bouche ne suit pas les syllabes.** | Elle change sur les mots accentués seulement. C'est voulu (skill `personnages`), mais ce n'est pas une synchronisation labiale. | vu |
| **Un trait peut se lire à contresens.** | Une barbe en arc se lisait comme un grand sourire, à l'opposé du jeu. | vu : redessinée en bouc plein |
| **Caméra contrainte.** Au-delà d'environ 25° de biais, le plan paraît mince ; une plongée forte l'écrase. | Les caméras restent près de l'axe du personnage. | règle du skill, non remesurée |

## Écrire la liste de plans avec ces limites

- **Le personnage réagit, l'objet agit.** Les plans qui portent l'histoire sont ceux de l'objet héros, en vraie 3D, filmé sous tous les angles. Le pantin apporte le regard, la surprise, le doute.
- **Varier par le cadre, pas par la pose** : plan large, plan taille, plan poitrine, gros plan du visage ; un personnage à gauche, puis à droite ; un amorce de décor floue devant lui.
- **Désigner** : placer l'objet **à côté** du personnage dans l'image, pas derrière lui. Vérifier que le bras tendu reste dans le cadre, sur l'image de la tenue.
- **Arriver, plutôt que marcher** : couper sur le personnage déjà là ; ou le montrer petit dans un plan large ; ou le cadrer à la taille pendant qu'il glisse ; ou faire bouger autre chose (une porte qui s'ouvre).
- **Tenir** : éviter. Sinon, voir « Faire tenir un objet » plus bas, et contrôler le contact en pleine taille.
- **Pas plus de deux plans de suite** avec le même personnage dans le même axe.
- **Jamais de changement de vue pendant un plan** : un personnage plat ne tourne pas en perspective.

## Ajouter une vue : la marche à suivre minimale

Une vue de plus (profil, trois quarts, dos) est **un second jeu de pièces**, monté comme un second personnage, qu'on échange avec le premier **à une coupe**. Compter une demi-heure à une heure par vue, planche comprise (estimation, non mesurée).

Ce qui est en place dans le kit et a été essayé (mécanique seulement, voir « État des essais ») : une entrée de `rig.json` peut porter ses propres visages, et `place(…, miroir=True)` retourne le dessin gauche-droite. Ce qui reste à faire, c'est **le dessin**.

1. **Décider d'après la liste de plans.** Lister les plans qui demandent cette vue. Moins de trois plans : recadrer plutôt que dessiner. Ne dessiner que les vues qui servent.
2. **Dessiner les pièces de la vue** dans `personnages.py` : une fonction sœur de `pieces()` (par exemple `pieces_profil(c)`) qui renvoie **les mêmes noms** (`jambes`, `corps`, `bras_g`, `bras_d`, `tete`), dans le même repère 600 × 1000, pieds sur y = 980, même hauteur totale, même épaisseur de contour, mêmes couleurs. Dans un profil : la tête garde sa silhouette mais le visage se décale vers l'avant, un seul bras est visible en entier (l'autre peut être une pièce minuscule cachée derrière le corps), les pieds pointent dans le sens du regard.
3. **Dessiner ses visages** : un profil n'a qu'un œil, un dos n'en a pas. Un dictionnaire par famille (`YEUX_PROFIL`, `BOUCHES_PROFIL`), avec **les mêmes clés** que la vue de face (`neutre`, `fermes`, `fermee`, `sourire`…) pour que les appels `visage()` restent les mêmes.
4. **Les déclarer dans `rig.json`** : dans `main()`, enregistrer la vue comme une entrée de plus, par exemple `galet_profil`, avec ses pièces, la même hauteur `h`, et deux champs en plus : `"visages": {…boîtes…}` et `"dossier_visages": "_visages_profil"` (les PNG vont dans `personnages/png/_visages_profil/`). Pour un dos : `"visages": {}`.
5. **Faire la planche** : la vue de face et la nouvelle côte à côte, à la même échelle. Même hauteur, même trait, mêmes couleurs, même costume reconnaissable. La faire valider avant d'animer.
6. **Monter et échanger à la coupe**, dans `bl_film.py` :

```python
galet = L.Perso("galet")
galet_p = L.Perso("galet_profil", "galet_p")       # même personnage, autre vue

a = PL[7]["a"]                                      # début du plan où il est de profil
galet.range_(a)                                     # la vue de face sort du film
galet_p.place(a, x, y, vers=camera_xy, miroir=True) # la vue de profil entre ; miroir = il regarde de l'autre côté
galet_p.neutre(a)
galet_p.visage(a, "neutre", "fermee", None)
```

7. **Contrôler** : la dernière image du plan d'avant et la première du plan d'après, côte à côte (`python outils/rendre.py --controle images v_ 25 <image>,<image>`) : même taille, pieds au même niveau, pas de saut de couleur. Puis une image pleine taille.

Règles : **un changement de vue se fait toujours sur une coupe** ; le miroir ne se change pas en cours de plan ; avec un profil, la caméra se place face au plan du dessin, comme pour la vue de face (c'est le dessin qui est de profil, pas le plan).

### Une main qui pointe

Même mécanisme, plus léger : une variante du personnage dont **un seul bras** est redessiné (bras tendu, main avec un index). La déclarer comme une vue (`galet_pointe`), l'échanger à la coupe qui précède le geste. Le bras reste une pièce raide : il pointe dans le plan de l'image. Écrit sans essai.

### Faire tenir un objet

Donner l'objet pour enfant à la pièce du bras, posé à l'endroit de la main, pour qu'il suive la rotation du bras :

```python
objet.parent = galet.bras["bras_d"]
objet.location = (0, -0.01, -longueur_du_bras)      # dans le repère du bras : la main est en bas du bras au repos
```

Puis contrôler le contact sur une image pleine taille à **chaque** pose clé. Écrit sans essai : sur le film réel, la correction a été faite autrement (la manche et la main redessinées autour de l'objet).

### Une vraie marche

Elle demande ce que le kit n'a pas : deux pièces de jambe séparées avec un pivot à la hanche, une vue de profil, et un cycle (contact, passage, contact) calé sur le déplacement pour que les pieds ne glissent pas. C'est un chantier à part ; tant qu'il n'est pas fait, écrire les plans sans marche.

## État des essais

| Point | État |
|---|---|
| Vue de face du kit : dessin, montage, expressions, regard, bras levé, ombre, rendu | essayé pour de vrai le 11/11/2026 (exemple du kit, Blender 5.3) |
| Clé d'arrivée tenue (`deplace`) et détection d'un glissement | essayé : une clé non tenue est signalée, la position reste fixe après l'arrivée |
| Visages propres à une entrée de `rig.json`, et `miroir=True` | mécanique essayée avec un double du personnage de face ; **aucune vue de profil n'a été dessinée** |
| Dessin d'un profil, d'un trois quarts, d'un dos | **non fait** : à dessiner et à valider par un humain |
| Main qui pointe, objet tenu, marche | **écrit sans essai** |

Ce qui manque pour une série, d'après le compte rendu du film : un kit de pantins avec plus de vues, des mains qui pointent, des jambes qui marchent et un générateur de costumes par époque. Rien de cela n'existe encore dans le plugin.
