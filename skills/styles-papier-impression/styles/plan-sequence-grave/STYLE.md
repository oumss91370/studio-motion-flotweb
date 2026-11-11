# Plan-séquence gravé

## 1. Identité

- **Nom** : Plan-séquence gravé (« Printed Long Take »).
- **Inspiration** : la gravure sur bois de bout et l'illustration en carte à gratter (le ton fait par la largeur de tailles parallèles), les paysages d'estampe japonaise du XXᵉ siècle (plans superposés de montagne, de forêt, d'eau), et le long travelling sans coupe des documentaires de nature. On prend la taille, la superposition et le mouvement ininterrompu ; jamais une estampe, les figures d'un illustrateur ou le trajet d'un film.
- **Ce que c'est** : **un monde en trois dimensions rendu comme une estampe en carte à gratter** : de l'encre, du papier, **un seul rouge**, traversé par **un mouvement de caméra unique et ininterrompu**. Profondeur, météo et lumière sont des lignes taillées ; la caméra voyage **dans** l'estampe.
  - **Seulement de l'encre, du papier et un rouge.** Chaque valeur est de l'encre ou du papier ; le gris n'existe que comme densité de lignes. Le rouge est réservé à **un seul petit sujet**. Un jaune chaud peut paraître pour le soleil, une lampe ou une matière, jamais comme second accent.
  - **Le ton est taillé, pas ombré** : les versants à l'ombre portent des tailles qui descendent la pente ; le ciel est fait de tailles horizontales dont la largeur fait la lumière ; la neige est du papier avec quelques traits ; l'eau est de l'encre avec des rides taillées.
  - **Vraie profondeur, marques plates** : la scène est en 3D (relief, rivières, milliers d'arbres), mais chaque surface porte des marques plates fixées **dans le monde** : les plans glissent les uns devant les autres comme un diorama imprimé.
  - **Au moins trois plans dans toute image tenue** : ciel / bande de montagne ou de forêt / plan moyen (champs, eau, neige) / premier plan (branches, clôtures, poteaux). Encre et papier à peu près moitié-moitié.
- **Marche pour** : grand paysage, récit de nature, migration, saison, territoire, patrimoine, ouverture de documentaire, « le même lieu, une autre année ».
- **Ne marche pas pour** : gros plans de personnages (les objets 3D proches ont l'air de jouets), interface, humour, production rapide. **C'est le style le plus exigeant du catalogue.**
- **À ne pas confondre** : pas la `gravure-sur-bois` (planches plates, caméra presque fixe) ; pas l'estampe japonaise (aplats de couleur, pas de voyage en profondeur) ; pas de la 3D « dessin animé » (aucun ombrage lisse, aucun reflet) ; pas un croquis (chaque ligne est une taille : entrée franche, sortie effilée).

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Encre (noir chaud) | `#16171b` |
| Papier (blanc cassé chaud) | `#ede5cd` |
| Rouge, **un seul sujet** | `#c4332b` |
| Jaune de lumière (soleil, lampe, une matière) | `#dfa443` |

- Jamais de noir pur, de blanc pur, ni de troisième gris en aplat.
- **Le rouge** : petit (une crête, une lampe, un drapeau), jamais sous ≈ 4 px à l'écran (agrandis-le un peu plutôt que de le perdre) ; un point plat sans contour ni reflet, avec un mince anneau de papier seulement là où il repose sur de l'encre. Il peut passer dans la trace du sujet (son sillage), jamais sur un autre objet.
- **Ordre des valeurs en profondeur** : montagnes lointaines en papier avec des facettes d'ombre en encre ; bandes de forêt en encre pleine ; plan moyen en papier ; silhouettes de premier plan en encre. Le sujet est toujours sur la valeur opposée à ce qui est derrière lui.
- **Typographie** : **une seule serif grasse** (par exemple **Noto Serif** ou **Source Serif** en gras, OFL). **Le texte vit dans le monde** : taillé dans une planche, coulé dans une plaque, imprimé sur une affichette collée, ou taillé comme un bloc de caractères **dans le ciel**. Les mots du monde ne portent que des mots-clés et des chiffres ; ni carton de titre centré, ni en-tête. Trois tailles au plus par image.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Noto Serif et de Source Serif. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/noto-serif`, `@fontsource/source-serif-4` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : deux sortes de champ : **papier portant des tailles d'encre** (faces éclairées, neige, sable, nuage, écume, vapeur) ou **encre portant des tailles de papier** (faces d'ombre, ciel, eau, forêt, nuit). Relief à facettes plates. Arbres, animaux et vapeur : silhouettes plates dessinées, toujours face à la caméra. Passe finale « estampe » : fibres du papier, encre marbrée dans les sombres, taches grises douces vers le haut de la feuille, léger scintillement, léger vignettage.

## 3. Composition 9:16

- **L'horizon sur un tiers** (vers y ≈ 640 ou y ≈ 1280). En vertical, on gagne de la hauteur pour empiler les plans : grand ciel taillé en haut, montagnes, forêt, eau ou neige, premier plan en bas.
- Le sujet reconnaissable n'est jamais plus petit que **1/20 de la hauteur** (≈ 96 px) ; les animaux lointains sont dessinés **jusqu'à 3 fois plus grands** que nature (licence de graveur).
- **Texte** : jamais sous 36 px en vertical, chaque mot à au moins 5 % du bord, à gauche de x = 945 ; blocs alignés à gauche. Il apparaît comme le médium le fait : taillé de gauche à droite avec des copeaux, pressé par un sceau, révélé sous une feuille qu'on décolle.
- **Bandeau de sous-titre** (s'il y a une voix) : lettres papier sur une bande d'encre à ≈ 80 % d'opacité, une ligne, y ≈ 1420 à 1520 ; garde le sujet de chaque plan au-dessus.
- **Le ciel sort du cadre quand la caméra plonge** : en vertical le champ est plus haut, donc le ciel reste plus facilement ; sinon recule la caméra, monte-la, allonge la focale, ou étire les distances horizontales (chaque plan est une feuille).
- **Temps de lecture** : tenir chaque texte ≥ max(1,8 s ; caractères ÷ 15 + 1,5 s) ; une comparaison à juger reste immobile ≥ 2,5 s avant le verdict.

## 4. Ce qui bouge

- **Action principale** : **le mouvement de caméra continu** qui porte l'histoire : longues courbes sans à-coup ; la caméra garde son élan en passant par les positions clés et **ralentit avant chaque tenue**. Ni rebond, ni secousse (sauf une image pour un impact).
- **Boucle de fond 1** : la passe d'estampe qui respire : les fibres et les taches du papier (texture fine, faible contraste) changent **10 fois par seconde** (une image sur trois à 30 i/s ; 12 dans la source) ; le **scintillement d'ensemble**, c'est-à-dire la luminosité de toute la feuille, ne change pas plus de **3 fois par seconde**, et de 2 % au plus. Pourquoi : il touche tout le cadre, et une variation de tout le cadre plus rapide que 3 par seconde est un clignotement, risque pour les personnes photosensibles.
- **Boucle de fond 2** : les marques de papier : vapeur en mèches horizontales, neige en petits carrés, éclaboussures en arcs courts ; vols d'oiseaux (trois dessins d'ailes en cycle).
- **Ce qui ne bouge jamais** : montagnes, horizon, texture du ciel ; **les arbres ne se balancent pas**.
- **Animaux** : silhouettes plates à trois ou quatre poses par action ; jamais de métamorphose entre deux poses.
- **Gestes natifs** : **le ciel qu'on ouvre en le taillant** (de l'horizon vers le haut, une rangée à la fois : l'aube comme une gravure, pas comme un dégradé) ; **le rouge qui s'éveille** (point par point à travers le cadre) ; **la traversée de la vapeur** (un nuage de tailles de papier avale le cadre moins d'une demi-seconde ; de l'autre côté, autre échelle ou autre lieu) ; **le même lieu imprimé à nouveau** (cadre fixe ; la feuille du dessus se décolle par le coin et montre l'estampe de l'année suivante) ; les mots taillés dans le monde ; le bloc de caractères dans le ciel.
- **Autorisés** : `#172` plan-séquence, `#183` plan d'ensemble haut qui descend et avance, `#035`/vol bas au ras de l'eau ou de la neige, `#176` passage à travers une structure (pont, porte, arche, tunnel), `#175` cadre fixe (document, comparaison, compte), `#031` montée et recul vers l'angle d'ouverture, `#174` suivi d'un sujet qui vole ou tombe, `#042` raccord sur un sujet qui monte ou tombe, `#140` feuille décollée par le coin.
- **Interdits** : `#187` fondu au noir, `#044` fondu enchaîné, glissements, `#021` retournements de page, coupes en zoom, ombrage lisse, dégradés, reflets brillants, tailles espacées à l'écran (elles « nagent »).

## 5. Rythme et montage

- 30 i/s, caméra et monde en mouvement à chaque image.
- **Les coupes sont rares et dessinées** : un film de 40 à 60 s peut tenir en 1 à 3 plans. Transitions permises : à travers une structure, à travers la vapeur ou la neige (moins de 0,5 s de papier blanc), raccord sur un sujet, feuille décollée, sceau.
- **La parole et l'image avancent ensemble** : chaque phrase est dite pendant que le plan montre ce qu'elle nomme ; les passages silencieux (une tenue pour lire, une traversée, un envol) restent sans mots.
- Pulsation lente ou à trois temps qui peut s'arrêter ; **silence avant un verdict, puis un seul coup grave**.
- **Version courte (8 à 12 s)** : un seul plan-séquence de 10 s entre deux positions clés, avec une tenue. Accroche avant 3 s : un évènement dans le plan (une structure traversée, un personnage qui entre), pas une coupe.

## 6. Recette technique

- **Moteur recommandé : Blender** (connecteur MCP, skill `blender`) ; variante : Three.js dans HyperFrames (comme l'original, rendu en double résolution).
- **Voie Blender** :
  - Relief en maillages à facettes plates ; arbres et animaux en plans texturés (silhouettes à découpe nette) dispersés par milliers ; ciel sur une sphère qui suit la caméra.
  - **Matériaux sans éclairage lisse** : pour chaque face, un seuil sur l'angle avec **une** direction de lumière décide « face éclairée » ou « face d'ombre » ; à l'intérieur, un motif de tailles calculé en coordonnées **du monde** (ou de direction pour le ciel) décide encre ou papier. Sortie en couleurs pures, sans tonalité filmique.
  - Rends la séquence en 1080×1920 (ou en double puis réduis), puis passe dans HyperFrames pour la **passe d'estampe** (fibres et marbrure qui changent 10 fois par seconde, scintillement d'ensemble 3 fois par seconde au plus et de 2 % au plus, vignettage léger), le texte hors monde et le montage.
- **Règles d'un matériau** (l'allure en dépend) :
  1. Choisis d'abord son champ : papier à tailles d'encre, ou encre à tailles de papier.
  2. **Les tailles suivent la matière** : le long de la pente sur un versant, horizontales dans le ciel, le nuage et l'eau calme, en travers du courant dans l'eau vive, le long des crêtes pour les vagues, le long du fil pour le bois.
  3. **Espacement en mètres** (ou en angle pour le ciel), ancré au monde.
  4. La lumière choisit éclairé ou ombre **par face** ; aucun dégradé dans une face.
  5. **Fondu avec la distance** : dès qu'un quart de rangée ou plus tient dans un pixel, les tailles rejoignent la valeur du champ (sinon : bouillie grise).
  6. Un sol plat porte des marques rares et irrégulières ; un rythme régulier se lit comme une route ou une grille.
  7. Le rouge n'entre jamais dans un matériau : c'est une marque posée par-dessus, avec une **taille minimale à l'écran**.
  ```glsl
  float rang = coordMonde / pas;                         // pas en mètres, ancré au monde
  float k = step(largeur, abs(fract(rang) - 0.5) * 2.0);  // taille ou champ
  k = mix(k, valeurChamp, smoothstep(0.25, 0.7, fwidth(rang)));   // fondu à distance
  ```
- **Ordre de travail** : image de style du relief et du ciel avec la passe d'estampe → le sujet et son rouge → le trajet de caméra → dégagement du trajet et contrôles près de l'objectif → les mots.
- **Pièges** :
  - **Les gros plans trahissent l'ombrage plat** : garde les sujets vivants en plan moyen, en silhouettes ; donne aux accessoires proches de vraies matières taillées.
  - **Papier vide** : un champ de neige sans plans devient une page blanche.
  - **La caméra à travers les solides** : dégage arbres, poteaux, roseaux et pierres du trajet (un seul à un mètre de l'objectif remplit le cadre d'encre) ; échantillonne le trajet, vérifie image par image les passages bas.
  - **L'effet route** : une rivière sombre à lèvre claire et tirets réguliers se lit comme du bitume.
  - Une facette éclairée près de l'objectif devient une feuille blanche : facettes plus petites près du trajet.
  - Vignettage et taches trop forts : l'estampe a l'air sale.

## 7. Son

- **Trois couches.** *Le monde* : la matière du lieu (eau sous la glace, givre qui craque, vent en trois poids, ailes, pas dans la neige). *L'estampe* : couteau dans le papier ou le bois, choc d'un bloc, feuille arrachée, sceau pressé ; **seulement sur les transitions et les verdicts**, jamais en fond. *La musique* : un petit ensemble de chambre en vrais instruments.
- **Timbres** : vibraphone joué à l'archet, harpe, cor, cordes graves, contrebasse pizzicato, xylophone, glockenspiel, timbales. Évite nappes de synthé et batterie.
- **Bruitages** : ≈ 5 par 10 s ; les sons d'estampe sont les événements les plus forts. Cris d'animaux : enregistrements sous licence libre (CC0 ou CC BY), jamais « non commercial ».
- **Voix** éventuelle au-dessus : musique très baissée sous la parole (≈ 17 dB), elle remonte dans les passages silencieux. Mix final −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Encre, papier, un rouge (et au plus un jaune de lumière) : aucun gris en aplat, aucun dégradé.
- [ ] Au moins trois plans dans chaque image tenue ; encre et papier à peu près à parts égales.
- [ ] Les tailles ne « nagent » pas quand la caméra bouge (ancrées au monde) et ne font pas de bouillie grise au loin.
- [ ] Le rouge ne touche qu'un seul sujet et reste visible (≥ 4 px) à chaque image.
- [ ] Un mouvement continu porte le film ; 3 plans au plus ; aucune transition interdite.
- [ ] Aucune image presque toute noire ou toute blanche dans les passages bas (planche de contrôle tous les 0,1 s).
- [ ] Le texte est dans le monde, lisible le temps requis, immobile pendant sa lecture.
- [ ] Arbres et relief immobiles ; animaux en silhouettes à poses fixes.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Film de démo d'origine *Thirty-Three Cranes* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/printed-long-take.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/printed-long-take.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 pour l'image. **La piste de voix de ce film est exclue de la licence** (voix d'un service en ligne) : ne pas le rediffuser avec son son ; montrer l'affiche, le film muet, ou renvoyer vers la galerie officielle.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/printed-long-take/STYLE.md`, `DEMO.md`, `demo/scene.js` (rendu et passe d'estampe), `look.js` (encres et matériaux taillés), `world.js`, `textures.js`, `props.js`. Licence MIT, © 2026 LemoLab ; image du film CC BY 4.0, voix exclue.
- Adaptation Flot Web : traduction, **voie Blender ajoutée** (l'original est en three.js), cadrage vertical, sous-titre sur une seule ligne en français, mix ramené à −14 LUFS, numéros du dictionnaire de mouvements. La transposition des matériaux taillés dans Blender n'a pas encore été essayée : à valider par un rendu réel.
