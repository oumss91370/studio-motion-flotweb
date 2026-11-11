# Principes de mouvement pour la vidéo verticale

Tout est exprimé pour le format par défaut du studio : **1080 × 1920, 30 images par seconde**, moteur HyperFrames (HTML + GSAP). Quand une règle est donnée en images, la conversion est : 1 image = 0,033 s ; 3 images = 0,1 s ; 15 images = 0,5 s ; 90 images = 3 s. En GSAP on écrit des **secondes** : `durée = images / 30`.

Sommaire : 1. règles chiffrées — 2. courbes et ressorts — 3. les 12 principes adaptés — 4. chorégraphie — 5. composition 9:16 — 6. règles de goût — 7. règles « anti-motion IA » — 8. ce qui ne s'applique pas.

Sources en fin de fichier.

---

## 1. Les règles chiffrées

| # | Règle | En images (30 i/s) | En secondes (GSAP) |
|---|---|---|---|
| 1 | **Aucune vitesse constante** sur un déplacement, une échelle, une opacité | — | jamais `ease: "none"` hors exceptions ci-dessous |
| 2 | **Décalages** entre éléments d'un même groupe | 3 à 6 images : mots 3, éléments de liste 4 à 5, gros blocs 6 | 0,10 s / 0,13 à 0,17 s / 0,20 s |
| 3 | **Sorties plus courtes que les entrées** | ≈ 10 images contre ≈ 20 | ≈ 0,33 s contre ≈ 0,67 s |
| 4 | **Pause après une frappe** (rien ne bouge au premier plan) | 15 à 20 images | 0,5 à 0,67 s |
| 5 | **Quelque chose bouge dès le début** de chaque scène | avant l'image 15 | avant 0,5 s |
| 6 | **Rien de figé trop longtemps** : un nouvel élément ou un changement visible | au plus tard toutes les 90 images | toutes les 3 s au plus |
| 7 | **Texte important dans la zone utile** | hors des zones d'interface | zone utile de `rendu/references/zones-interface.md` (voir section 5) |
| 8 | **Le son tombe sur l'impact, jamais avant** | attaque du bruitage sur l'image du contact | +0,008 s visé ; toléré de −0,045 s à +0,075 s |
| 9 | **Sécurité : pas d'éclairs en rafale** sur une grande surface | au plus 3 éclairs ou changements brusques par seconde ; au moins 10 images entre deux | au moins 0,33 s entre deux |

Précisions :

- **Règle 1, exceptions au linéaire** : rotation continue (roue, indicateur d'attente), dérive lente de fond, défilement d'un bandeau, grain, barre de progression, suivi d'un objet à vitesse constante (#029). Tout le reste a une courbe.
- **Règle 2, budget** : la somme des décalages d'un groupe reste **sous 0,5 s**. Avec 12 éléments, on descend à 0,04 s par élément plutôt que de dépasser. Tous les éléments décalés gardent **la même courbe et la même durée** ; seul le départ change.
- **Règle 3** : une sortie se fait en accélération (`power2.in`, `expo.in`), sur une petite distance (40 px environ) : ce qui sort ne mérite pas l'attention.
- **Règle 4, rythme d'une scène** : FRAPPE → pause → construction → FRAPPE. Au moins **3 moments d'immobilité** par vidéo. Pendant la pause, les boucles de fond continuent ; c'est le premier plan qui se tait.
- **Règle 6** n'autorise pas l'agitation : un texte en cours de lecture reste immobile (section 6). On relance par un nouvel élément, un changement de cadre, une mise en avant.
- **Règle 8** : c'est la règle du skill `son` (sa règle 8), et c'est lui qui fait foi. Le calage se fait sur l'**attaque** du son, pas sur le début du fichier : elle tombe sur l'image de l'impact avec 8 ms de retard visé, jamais avant (un son en avance se lit comme une erreur de montage). L'ancienne formule « le son part 2 à 3 images avant l'impact » ne vaut que pour le **début** des sons qui s'établissent lentement : un souffle a son pic sur le pic de vitesse du mouvement, une montée finit 30 à 250 ms avant le coup. Les instants viennent du code de la vidéo (étiquettes de la timeline) et sont posés par `son/scripts/caler.py`.
- **Règle 9, sécurité (personnes photosensibles)** : elle passe avant le style et avant la demande du client.
  - **Ce qui compte comme un éclair** : un aller-retour clair → sombre (ou l'inverse), ou un changement brusque de couleur ou de luminance, fait en moins de 3 images, sur une **grande surface** : plus d'un quart de l'image (en 1080 × 1920, plus qu'un rectangle de 540 × 960 environ). Un changement de plan plein cadre entre une image claire et une image sombre compte ; une suite d'aplats de couleur plein cadre aussi.
  - **Limite** : au plus **3 par seconde**, sur n'importe quelle seconde du film. À 30 i/s : au moins 10 images entre le début de deux éclairs ; un aplat plein cadre tient au moins 10 images (0,33 s) avant de changer. Le rouge saturé est le plus risqué : jamais en rafale.
  - **Ce qui reste permis** : les effets rapides sur de **petites surfaces** (moins d'un dixième de l'image : voyant qui clignote, étincelles, trait vibrant #136, curseur de texte, pixels d'un sprite) et les variations à **faible contraste** (grain, scintillement d'un fond, papier qui vit : moins de 10 % d'écart de luminance, soit environ 25 niveaux sur 255). Entre un dixième et un quart de l'image, garder un contraste faible ou ralentir.
  - **Comment faire quand le style demande une rafale** (stroboscope, glitch #023, onomatopée qui change de couleur, montage au temps) : ralentir à 3 par seconde, réduire la surface (l'effet sur un objet, pas sur le fond), ou baisser le contraste (deux teintes voisines, voile à 20 % au lieu d'un blanc plein). Un seul éclair blanc plein cadre sur un impact (#024, 2 à 3 images) reste permis : c'est la répétition qui est en cause.
  - **Contrôler** : sur la planche d'images du rendu, compter les changements plein cadre dans chaque seconde ; dans le code, chercher les `repeat` à cadence rapide et les `steps` appliqués à un fond.

Écriture type en GSAP (décalage, sortie rapide, pause) :

```js
const tl = gsap.timeline({ paused: true });
tl.addLabel("frappe", 0.2)
  .from(".mot", { y: 40, autoAlpha: 0, duration: 0.67, ease: "expo.out", stagger: 0.1 }, "frappe")
  .addLabel("construction", ">+0.6")            // pause : 18 images
  .from(".carte", { scale: 0.94, autoAlpha: 0, duration: 0.6, ease: "expo.out", stagger: 0.15 }, "construction")
  .to(".mot", { y: -42, autoAlpha: 0, duration: 0.33, ease: "expo.in", stagger: 0.03 }, ">+1.2");
```

### Durées de référence en vidéo

| Mouvement | Durée |
|---|---|
| Entrée d'un élément | 0,4 à 0,7 s |
| Sortie | 0,2 à 0,35 s (50 à 75 % de l'entrée) |
| Déplacement rapide à l'écran | 0,3 à 0,6 s |
| Transition faite main entre deux plans | 8 à 14 images (0,27 à 0,47 s) |
| Panoramique filé (#043) | ≈ 1 500 px en 6 images, avec flou |
| Maintien d'un texte à lire | au moins 1 s, plus 0,25 s par mot au-delà de 3 mots ; au moins 2 s pour la phrase finale (valeurs de la porte de livraison, `studio-coeur/references/controles.md`) |
| Décalage entre mots | 0,06 à 0,12 s ; entre lettres : 1 image |

**La distance allonge la durée** (rapport à garder, quelle que soit la base) : 50 px ×0,8 ; 100 px ×1 ; 200 px ×1,3 ; 400 px ×1,6 ; traversée de l'écran ×1,8 à 2. Au-delà de 30 px par image, ajoute un flou de mouvement.

### Structure d'un court de 30 s

| Temps | Rôle |
|---|---|
| 0 à 1,5 s | Accroche : la promesse est à l'écran, en mouvement |
| 1,5 à 3 s | Contexte |
| 3 à 22 s | Corps, en 3 ou 4 temps |
| 22 à 27 s | Résultat : **la plus grosse animation de la vidéo** |
| 27 à 30 s | Appel à l'action, tenu au moins 2 s |

---

## 2. Courbes et ressorts

### Trois courbes suffisent

| Rôle | Courbe | GSAP |
|---|---|---|
| **Entrée** (arrive vite, se pose doucement) | `cubic-bezier(0.16, 1, 0.3, 1)` | `expo.out` |
| **À l'écran** (déplacement d'un point à un autre, zoom lent sur une image) | `cubic-bezier(0.83, 0, 0.17, 1)` ou `(0.65, 0, 0.35, 1)` | `power4.inOut` / `power2.inOut` |
| **Sortie** (part en accélérant) | `cubic-bezier(0.7, 0, 0.84, 0)` | `expo.in` |

Et pour le reste : boucle d'ambiance en `sine.inOut` ; valeur qui « atterrit » avec un léger dépassement : `back.out(1.4)`.

**Une famille de courbes par vidéo.** La fiche de style donne la courbe signature (environ 80 % des animations), trois durées et un motif d'entrée : c'est l'identité de mouvement du style. Ne mélange pas `expo`, `back`, `elastic` et `bounce` dans un même film sans raison.

Attention au défaut qui « fait généré » : `power2.out` à 0,5 s appliqué partout. Les valeurs par défaut de la timeline doivent venir de la fiche de style, pas de l'habitude.

### Ressorts

GSAP n'a pas de ressort physique natif. Trois façons d'en obtenir un, de la plus simple à la plus exacte :

| Caractère | Usage | Approximation GSAP |
|---|---|---|
| Net, sans rebond (amortissement 1,0) | caméra, texte | `expo.out` ou `power3.out` |
| Vif, léger dépassement (amortissement 0,72 à 0,9) | mots, éléments d'interface | `back.out(1.2)` à `back.out(1.7)` |
| Souple, gros éléments | cartes, panneaux | `power3.out` sur 0,7 à 0,9 s |
| Rebondissant | logo, mascotte, **un seul moment héros par vidéo** | `elastic.out(1, 0.5)`, ou `CustomBounce` |

Pour un ressort exact (formule d'une fiche du dictionnaire, par exemple `1 − e^(−6.5t)·cos(15t)`), calcule la valeur **à partir du temps de la timeline** dans un `onUpdate` — jamais avec une horloge ou une simulation image après image (le rendu saute d'une image à l'autre dans le désordre).

Si une valeur doit **arriver** à un instant précis (sur un temps musical), lance son ressort environ 0,3 s avant.

---

## 3. Les 12 principes de l'animation, adaptés au vertical

Les principes viennent de l'animation traditionnelle. Les valeurs d'origine de notre source sont calibrées pour des interfaces (où l'utilisateur déclenche le mouvement et attend la réponse). En vidéo, le spectateur regarde et lit : **on garde les proportions, pas les durées web.** Chaque ligne donne donc un rapport, puis une façon de l'écrire en GSAP.

| # | Principe | Ce qu'il faut garder (proportions) | En vertical 30 i/s, avec GSAP | Mouvements liés |
|---|---|---|---|---|
| 1 | **Écrasement et étirement** | Le volume est conservé : si la hauteur passe à 0,8, la largeur passe à 1,2. Impact court, retour deux fois plus long | Impact 2 à 4 images, retour 4 à 8 images. `scaleY: 0.8, scaleX: 1.2` puis retour en `back.out`. `transformOrigin` au point de contact | #011, #123 |
| 2 | **Anticipation** | Un petit mouvement **à contresens**, de 10 à 20 % de l'action principale en amplitude comme en durée | Un tween inverse juste avant : pour une montée de 300 px en 0,6 s, descente de 30 à 45 px en 0,1 à 0,15 s (`power1.inOut`), puis l'action | #121, #003 |
| 3 | **Mise en scène** | Une seule action principale par temps. Le secondaire est atténué (opacité 40 à 60 %, flou de 2 à 4 px). Le héros n'arrive jamais en même temps que le reste | Le héros entre 3 à 6 images après (ou avant) les éléments secondaires. Position `"<0.15"` sur la timeline | #033, #182 |
| 4 | **Pose par pose** | On décide d'abord les poses clés (états lisibles en image fixe), puis les passages | Écris les états comme des étiquettes (`addLabel`) : chaque étiquette doit donner une image fixe compréhensible | — |
| 5 | **Mouvements de suite et chevauchements** | Les parties accrochées suivent avec retard et s'arrêtent après le corps | Enfant : même tween, décalé de 2 à 4 images (`"<0.08"`) ; il se pose 3 à 6 images après le parent, avec une courbe à dépassement | #122 |
| 6 | **Accélération et ralenti** | Entrée : ralentit à l'arrivée. Sortie : accélère au départ. À l'écran : les deux | `expo.out` / `expo.in` / `power2.inOut` (section 2) | #009 |
| 7 | **Arcs** | Un trajet naturel est courbe : décalage perpendiculaire de 5 à 10 % de la distance à mi-parcours (plus pour un style ludique, presque rien pour un style sobre) | `x` et `y` animés avec **deux courbes différentes** (par exemple `x` en `power1.inOut`, `y` en `power2.out`), ou `MotionPathPlugin` | #126, #013 |
| 8 | **Action secondaire** | Un mouvement d'accompagnement de 30 à 50 % de l'amplitude principale, légèrement en retard, avec une autre courbe | Ombre qui s'élargit, reflet, poussière : départ 2 à 3 images après, `"<0.08"` | #022, #024 |
| 9 | **Rythme (timing)** | La durée dit le poids : léger = court, lourd = long avec ralenti marqué. Les durées d'un même film tiennent en **3 valeurs** | Trois durées dans la fiche de style (par exemple 0,33 / 0,5 / 0,67 s), rien d'autre | #010, #123 |
| 10 | **Exagération** | Selon le caractère : sobre 0 %, ludique 15 à 25 %, énergique 20 à 30 % de dépassement | `back.out(1.2)` (discret) à `back.out(2.5)` (cartoon) ; `expo.out` pour un style sobre | #001, #010 |
| 11 | **Dessin solide** | Les formes gardent leur volume et leur perspective ; un seul système de formes du début à la fin | Mêmes rayons, mêmes épaisseurs de trait, mêmes ombres dans toutes les scènes | #143 |
| 12 | **Attrait** | Un élément, une idée, un point focal par image | Une seule couleur d'accent, sur un seul élément par image | — |

### Caractères de mouvement

La fiche de style choisit un caractère ; il règle la courbe, le dépassement et la vitesse **relative** :

| Caractère | Courbe | Dépassement | Vitesse relative |
|---|---|---|---|
| Sobre, haut de gamme | `power3.out`, `power2.inOut` | aucun | lente (×1,3) |
| Institutionnel | `power2.out` | aucun | normale |
| Ludique | `back.out(1.7)` | 10 à 20 % | rapide (×0,8) |
| Énergique | `expo.out` | 15 à 30 % | très rapide (×0,7) |

Matières : rigide ×1,2 sans dépassement ; élastique ×0,8 avec 15 à 25 % de dépassement ; fluide ×1,5 ; gazeux ×2.

---

## 4. Chorégraphie (plusieurs éléments)

- **Trois couches de mouvement** dans chaque plan : **principale** (l'action du plan), **secondaire** (ce qui l'accompagne), **ambiante** (deux boucles de fond lentes : dérive, flottement, grain, trait qui vibre). Une image sans couche ambiante paraît morte ; une image où tout est principal est illisible.
- **Règle du tiers, distance** : aucun élément ne parcourt plus d'un tiers de l'écran (640 px en hauteur, 360 px en largeur) d'un seul trait sans point d'appui intermédiaire — sauf transition plein cadre voulue.
- **Règle du tiers, quantité** : au plus un tiers des éléments en mouvement au même instant.
- **Une direction par scène** : tous les éléments entrent du même côté. En vertical, privilégie l'axe haut-bas (entrée par le bas, sortie par le haut) : le plan suivant entre dans la direction de la sortie du précédent.
- **Contre-mouvement du fond** : 20 à 30 % de la vitesse du premier plan, en sens opposé.
- **Profondeur** : premier plan ×1, plan moyen ×0,5, fond ×0,2 (voir #016).
- **Phases d'un plan** : mise en place 20 à 30 % de la durée, action 30 à 40 %, résolution 30 à 40 %, puis une courte immobilité avant la coupe.
- **Pas de trou entre deux scènes** : la suivante commence pendant que la précédente finit (chevauchement de 3 à 6 images). Un vide se lit comme un chargement.
- **Jamais l'opacité seule** : une entrée combine 2 à 3 propriétés (opacité + déplacement de 40 px, opacité + échelle 0,94 → 1, masque + déplacement…). Et **varie les entrées** dans un même film : le même « fondu + montée » partout fait généré.
- **Zoom lent sur une image fixe** : échelle 1 → 1,08 à 1,10 avec un glissement de 25 px environ ; alterne avant et arrière d'un plan à l'autre. Pas sur tous les plans (voir `camera.md`).

---

## 5. Composition en 9:16

### Zones d'interface (rien d'important dedans)

Les applications recouvrent une partie de l'image : nom du compte, légende, boutons.

La table chiffrée (haut, bas, droite, marge gauche, zone utile, place des sous-titres) est tenue à un seul endroit : **`rendu/references/zones-interface.md`**. Ne recopie pas d'autres valeurs ici ni dans une fiche : en cas de doute, c'est cette table qui fait foi, et c'est elle que la porte de livraison contrôle.

### Zone de texte

- **Texte important dans la zone utile** de la table de référence, jamais dans les zones d'interface. (La règle d'origine, « 75 % centraux de la hauteur », descendait jusque dans la zone du bas : elle est remplacée par la table.)
- Le message principal vise le **carré central 1080 × 1080** (y = 420 à 1500) : c'est ce qui survit à tous les recadrages.
- **Sous-titres** : position et nombre de mots dans `rendu/references/sous-titres.md` (vers 65 % de la hauteur).
- Contrôle : réduis l'image à **360 px de large** ; tout texte important doit rester lisible.

### Typographie

- Titres de 80 à 140 px pour 1080 de large, graisse 600 à 800, interlettrage −0,02 à −0,03 em, interligne 1,05.
- 3 familles de polices au plus ; un seul mot accentué par ligne.
- Chiffres animés en `font-variant-numeric: tabular-nums` (sinon le nombre tremble en défilant).
- Écarts entre gros blocs de texte **en px**, pas en em (un em de 140 px fait un trou énorme).
- Chaque titre tient sur une ligne ou est coupé à la main ; jamais de coupe automatique en plein groupe de mots.

### Couleur et couches

- Répartition 60 / 30 / 10 ; **une seule couleur vedette, sur un seul élément par image**.
- Ordre des couches : fond → médias → graphismes → étalonnage → grain (opacité ≈ 0,05 à 0,09) → vignette légère.
- Noirs relevés (jamais `#000` pur). « Si le spectateur peut nommer l'effet, il est trop fort. »

---

## 6. Règles de goût

- **Dans le doute, tenir plus et animer moins.**
- **Un texte ne bouge pas pendant qu'on le lit.** Il entre, il tient, il sort.
- **Un point focal par image.** Si deux choses réclament le regard, l'une attend.
- **Un moment héros par vidéo** (le dépassement élastique, la grosse transition, le grand zoom). Ne le dépense pas dans les trois premières secondes, sauf si c'est l'accroche elle-même.
- **Objets persistants** : un même élément qui change de rôle (le point devient un bouton, le bouton devient la carte) vaut mieux que dix apparitions. Les transitions sont **motivées par un objet** du cadre (#017, #020, #042, #161).
- **Rien de mort, rien d'agité** : même la carte de fin a une micro-dérive ; mais aucune boucle de « respiration » sur un titre ou un texte — les boucles vont sur les personnages et le fond.
- **Tout ce qui apparaît en même temps, ou avec la même durée, est une faute** : décale et hiérarchise.
- **Sorties géométriques rapides** ; le plan suivant est déjà en mouvement quand il arrive.
- **L'image 0 n'est jamais vide** : c'est souvent elle qui sert de vignette.
- **La lueur dépend de l'état, pas du temps** : un élément brille parce qu'il est actif, pas parce qu'une boucle tourne.
- **Un son par événement, pas par élément** ; un seul grand impact et une seule montée par vidéo (détail dans le skill `son`).
- **Pas de stroboscope** : jamais plus de 3 éclairs ou changements brusques de couleur par seconde sur une grande surface (règle 9 de la section 1) ; les effets rapides vivent sur de petites surfaces et à faible contraste.
- **Raccords de coupe** : coupe au pic de vitesse, avec la même direction et la même vitesse des deux côtés. Jamais de flou de mouvement à travers une coupe franche.

---

## 7. Règles « anti-motion IA »

Ce qui fait dire « c'est généré » au premier regard, et l'antidote.

| Symptôme | Règle |
|---|---|
| Tout bouge tout le temps | **Une seule chose bouge à la fois** au premier plan |
| Plusieurs couleurs vives | **Une seule couleur d'accent**, qui a un sens |
| Bleu-violet et dégradés arc-en-ciel | Pas de dégradé arc-en-ciel ; pas de dominante bleu-violet saturée (au-delà de 30 % du film, la porte de livraison du studio refuse) ; le bleu marine à plat est permis |
| Lueurs, chrome lumineux, néon | Aucune lueur décorative ; pas de dégradé sur les éléments d'interface |
| Explosions de particules | Pas de particules gratuites (#015 seulement si la fiche de style l'autorise, et une fois) |
| Tout rebondit | Ressorts amortis (amortissement ≥ 0,72) ; un seul rebond franc par vidéo |
| Retournements 3D sans raison | #021 et #139 seulement quand il y a vraiment deux faces |
| Formes disparates | **Un seul système de formes** du début à la fin (mêmes rayons, mêmes traits, mêmes icônes) |
| Emoji, faux texte, chiffres inventés | Aucun emoji décoratif, aucun texte de remplissage ; tout chiffre à l'écran a une source, sinon pas de chiffre |
| Même entrée partout, même durée partout | Entrées variées, 3 durées, décalages |
| Zoom avant sur chaque plan | La caméra est une ponctuation (voir `camera.md`) |
| Écran figé puis coupe | Couche ambiante, chevauchement des scènes |
| Éclairs, clignotements et couleurs qui alternent plein cadre | Au plus 3 par seconde sur une grande surface (règle 9) : c'est une règle de sécurité avant d'être une règle de goût |
| Rangée de logos « ils nous font confiance » | Les logos arrivent un par un, sur le rythme |

**Test muet en une phrase** : montre la vidéo sans le son à quelqu'un (ou à un agent neuf, à partir des images seules). S'il résume le message en une phrase, le mouvement fait son travail.

---

## 8. Ce qui ne s'applique pas à la vidéo

Les sources parlent parfois d'interfaces en temps réel. À ignorer dans une vidéo rendue :

- durées « réactives » de 100 à 300 ms : justes pour un bouton, **trop rapides** pour un spectateur qui lit ;
- survol, clic, défilement réels : dans une vidéo, ils sont **joués** par la timeline ;
- réglages d'accessibilité du navigateur, adaptation à la taille d'écran, fluidité à 60 i/s en temps réel : seule compte l'image rendue ;
- « tout élément affiché plus de 2 s doit respirer » : non pour les textes et les titres (voir section 6) ;
- « toujours fondu + montée + échelle » : non, on varie les entrées.

**Ordre de priorité en cas de conflit** : la référence fournie par le client, puis la fiche de style, puis les règles du moteur (skill `rendu`), puis ce document.

---

## Sources

- Règles chiffrées, courbes, structure du court de 30 s, zone des 75 %, son avant l'impact : **haidrrrry/claude-remotion-skill** (MIT, © 2025 haidrrrry, commit `1dcbe5e`). Seules les règles sont reprises et transposées à GSAP ; aucun code Remotion n'est recopié. La règle d'origine « son 2 à 3 images avant l'impact » n'est pas retenue pour les coups : le studio applique la règle mesurée du skill `son` (attaque sur l'image, +8 ms, jamais avant).
- Les 12 principes, caractères, matières, chorégraphie, rapport distance / durée : **LottieFiles/motion-design-skill** (MIT, © 2025 LottieFiles, commit `f9a8a04`). Proportions conservées, durées recalculées pour la vidéo.
- Règles de goût (tenue de lecture, moment héros, objets persistants, anti-patterns) : **whaleyxbt/claude-motion** (MIT, © 2026 whaleyxbt, commit `6f80380`).
- Règles « anti-motion IA », test muet, raccords de coupe : **howseen-ai/claude-motion-design** (MIT, © 2026 Howseen AI, Raphaël Aubry, commit `3d90d34`).
- Règle de sécurité sur les éclairs (règle 9) : limite de trois éclairs par seconde reprise du critère de succès 2.3.1 des WCAG du W3C (« trois flashs ou sous le seuil ») ; les surfaces chiffrées (un quart, un dixième de l'image) sont une simplification du studio, pas le seuil officiel.
- Seuil bleu-violet : **alchaincyf/huashu-art-motion** (MIT, © 2026 alchaincyf, commit `1468196`).
- Ressorts amortis, étalonnage discret : **AbubakrChan/product-launch-motion** (MIT, © 2026 Abubakr Chan, commit `edbfb10`).
