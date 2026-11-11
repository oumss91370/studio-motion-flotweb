# Histoire vraie à tête ronde

> Les valeurs marquées « rendu réel du 11/11/2026 » viennent d'un film complet de 61,5 s (36 plans, 1 845 images) fabriqué par le studio dans ce style, sur un PC à carte graphique intégrée, puis critiqué deux fois par un agent qui ne l'avait pas fait. Essai interne, non publié, non fourni. Le parcours et les outils : `references/pipeline.md` et `kit/`.

## 1. Identité

- **Nom** : Histoire vraie à tête ronde.
- **Inspiration** : le format de courts documentaires animés verticaux où un bonhomme plat à tête ronde raconte un fait d'histoire dans un décor éclairé comme au cinéma. On en reprend la grammaire (mélange 2D/3D, rythme, sous-titres), jamais un personnage, un dessin ou un texte existant.
- **Pour quels sujets** : une histoire vraie qui tient en une phrase étonnante. Objets et inventions (un instrument ancien au fonctionnement étonnant), anecdotes d'histoire, découvertes scientifiques, origines d'un mot ou d'une habitude, faits divers anciens.
- **À vous de le rendre vôtre** : « tête ronde » décrit une famille de dessin (tête simple, yeux réduits à un signe, contour unique), pas un personnage. Dessinez le vôtre (forme de tête, yeux, costume, couleur d'accent) et choisissez vos propres sujets ; ne reprenez ni le dessin, ni les sujets, ni la façon de faire reconnaissable d'une chaîne existante. Le personnage du kit, « Galet » (tête en galet carré, yeux en traits verticaux), n'est qu'un exemple à remplacer.
- **Ne marche pas pour** : l'actualité chaude et les sujets sensibles (le ton bonhomme les trahit), un tutoriel pas à pas, un sujet sans objet ni lieu à montrer, une histoire qui demande plus de 4 personnages, tout ce qui n'a pas de source vérifiable.

## 2. Palette, typographie, matières

Valeurs de départ du studio (à adapter au lieu et à l'époque de l'histoire).

| Rôle | Couleur |
|---|---|
| Lumière principale (fenêtre, fin de journée) | `#FFD9A0` |
| Sources chaudes (bougies, torches) | `#FF9A3C` |
| Ombres et ambiance (froid) | `#1E2A44` |
| Pierre et murs | `#8A7B6A` |
| Bois sombre | `#4A2F1E` |
| Tissu d'apparat (un par décor) | `#7A1F24` |
| Métal de l'objet héros (bronze, or vieilli) | `#B8862F` |
| Peau des personnages | `#F2C9A0` |
| Encre du contour | `#1B1410` |
| Accent du personnage principal (absent des décors) | `#2F6FB5` |
| Sous-titres | blanc `#FFFFFF`, contour `#14100C` |

- **Typographie** (polices libres) : sous-titres en Montserrat ExtraBold ou Anton ; aucun autre texte à l'image, sauf un chiffre ou une date sourcés.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : League Gothic à la place d'Anton ; Montserrat : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/anton` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Personnages** : aplats, un seul poids de contour épais, tête ronde, yeux en points, membres en bâtons. Aucun dégradé, aucune texture, aucun ombrage.
- **Décors** : matières réelles (pierre, bois, bronze, tissu) avec usure et variation ; rien de propre. Textures Poly Haven (CC0).
- Deux températures dans chaque image : une ambiance froide ou neutre contre des sources chaudes.

## 3. Composition 9:16

- 1080×1920, rendu à la taille exacte.
- **Zones sans rien d'important** : 160 px en haut, 360 px en bas, 135 px à droite.
- Personnage en plan moyen : un quart à un tiers de la hauteur du cadre, les yeux entre 600 et 900 px du haut. En gros plan, le visage occupe la moitié de la largeur.
- Le décor travaille **en hauteur** : piliers, tentures, fenêtres hautes ; un élément flou au premier plan, en bas du cadre ; le fond flou en haut.
- Objet héros en gros plan : centré, entre 500 et 1300 px du haut.
- **Le sujet tient dans les 65 % du haut** (au-dessus de y ≈ 1250) : visage, objet héros, action. C'est la critique du rendu réel du 11/11/2026 qui l'a établi : en plan taille, un personnage cadré « normalement » se retrouve sous les sous-titres. Le kit mesure ce point à la construction (`controle_sujet`).
- **Sous-titres** : 1 à 2 mots, capitales, Montserrat 900, **taille unique de 96 px** (un groupe trop long est coupé en deux, jamais rétréci), blanc, contour sombre de 18 px, centrés, **dans la bande y = 1385 à 1515**. Jamais sur un visage ni sur l'objet héros. Changement sec sur le début du mot ; léger « pop » (échelle 1,16 vers 1 en 0,14 s) sur les seuls mots accentués (32 sur 118 groupes dans le film réel).
- **Pourquoi cette bande** (rendu réel du 11/11/2026) : le repère général de HyperFrames et du skill `rendu` (600 à 700 px du bas, soit un bas de bloc entre y = 1220 et 1320) tombait sur les sujets en plan taille ; posés d'abord à y = 1215, les sous-titres couvraient les personnages sur six plans. La bande 1385–1515 reste **dans la zone utile** de `skills/rendu/references/zones-interface.md` (jusqu'à y = 1560 : 45 px de marge), mais elle est plus basse que le placement que ce fichier conseille (1220 à 1320, texte indispensable au-dessus de 1330) : c'est une dérogation de cette fiche, permise par `sous-titres.md`. Entre 1330 et 1560, la légende dépliée peut recouvrir le texte ; pour une publicité, revenir au repère de `rendu` et remonter les sujets.
- 16:9 : même décor, cadrages refaits (ne pas recadrer le vertical).

## 4. Ce qui bouge

- **Action principale** : une seule par plan. Soit le personnage joue sa ligne de jeu (regard, puis un geste), soit l'objet héros fait ce que dit le texte.
- **Deux boucles de fond** : (1) le vacillement des sources chaudes (force de la lumière ± 6 à 10 %, plusieurs sinus additionnés, jamais régulier) ; (2) la respiration des personnages au repos et un clignement de temps en temps. Poussière dans un rayon de lumière en option.
- **Caméra** : avancée lente (échelle apparente de 1,00 à 1,06 sur 60 images) ou travelling latéral court, avec une raison écrite dans la liste de plans. Plan fixe pour les réactions.

| Autorisés (dictionnaire `principes-mouvement`) | Interdits |
|---|---|
| `#027` avancée de caméra (dolly in) | `#030` orbite permanente autour du sujet |
| `#029` travelling d'accompagnement | `#034` caméra à l'épaule |
| `#033` bascule de mise au point | `#032` travelling compensé |
| `#031` élévation de grue (une fois, en ouverture ou en fin) | `#043` panoramique filé entre les plans |
| `#010` dépassement, sur une réaction de personnage | `#001` apparition en rebond sur chaque mot |
| `#024` secousse d'impact (une seule fois, sur l'événement central) | `#023` effet de parasite, `#036` cadre penché |

Interdits propres au style : rebond en boucle des personnages, tout qui apparaît en fondu, dérive de caméra sans motif.

## 5. Rythme et montage

- **Un plan par idée**, 1,5 à 3 s ; une coupe environ toutes les 2 s ; une trentaine de plans pour 65 s. Constat du rendu réel du 11/11/2026 : 36 plans pour 61,5 s (1,71 s en moyenne), six plans de 1,3 à 1,5 s quand l'idée tient en trois mots, aucun au-dessus de 2,5 s.
- **Une action peut se reprendre en recouvrement** : l'objet part à la fin d'un plan et arrive au début du suivant sous un autre angle (25 images de triche sur le film réel), tant que la chute elle-même garde sa durée physique.
- **Coupes franches**, calées sur le début d'un mot. Pas de transition décorative, pas de son de transition sur chaque coupe.
- Structure : accroche dès la première phrase (pas de titre), retournement vers la 40e seconde, dernière phrase qui tient la promesse.
- Tenue de 8 à 12 images sur chaque réaction ; 20 à 30 sur celle qui porte la chute.
- 3 à 5 décors, réutilisés avec d'autres caméras.
- **Version courte (8 à 12 s)** : garder l'accroche et la chute : 4 à 5 plans de 2 s dans **un seul décor**, une réaction tenue 20 à 30 images ; couper le retournement (prévu vers la 40e seconde) et les décors secondaires. Accroche avant 3 s : la première phrase dès l'image 0, sans titre.

## 6. Recette technique

- **Moteur** : Blender pour l'image (skill `blender`), HyperFrames pour l'assemblage (skill `rendu`).
- **Kit de départ** : `kit/` (lire `kit/LISEZMOI.md`). Liste de plans en données, bibliothèque de construction, boucle de rendu avec reprise, re-rendu par plages, planches de revue, assemblage HyperFrames. Son exemple de 2 plans tourne tel quel.
- **Structure** : collections `DECOR`, `LUMIERES`, `CAMERAS`, `HEROS`, `PERSONNAGES` ; une caméra par plan, liée à un repère de la ligne de temps ; numéros d'image = images de la vidéo. Avec le kit, **tout le film est une seule scène** (`decors/film.blend`), les décors construits loin les uns des autres : une correction est un numéro d'image, et on ne re-rend que les images touchées. À la main, un fichier `.blend` par décor reste possible.
- **Rendu** : profiler avant de lancer, un seul Blender à la fois, boucle de reprise ; skill `blender`, `references/rendu-long-et-fiable.md`. Mesure du rendu réel : 3,6 s par image en EEVEE sur carte intégrée (8 échantillons), soit 1 h 50 pour 1 845 images.
- **Mise au point** (rendu réel) : f/2 à f/2,8 sur les personnages (fond flou), f/4,5 à f/6,3 sur les gros plans de l'objet héros (objet net).
- **Décor** en 3 passes (formes et caméras, lumière motivée, habillage), contrôle visuel après chacune.
- **Personnages** : plans à matériau émissif, sans ombre portée, avec un disque d'ombre de contact (skill `personnages`, `references/import-blender.md`).
- **Vue « Standard »** pour que les aplats sortent à la couleur du dessin :

```python
s = bpy.context.scene
s.view_settings.view_transform = "Standard"
cam.data.dof.use_dof = True
cam.data.dof.focus_object = bpy.data.objects["MARQUE_P07"]
cam.data.dof.aperture_fstop = 2.8
```

- **Vacillement d'une bougie** (clés posées toutes les 2 images) :

```python
import math
for f in range(debut, fin, 2):
    k = 1 + 0.06 * math.sin(f * 0.61) * math.sin(f * 0.23) + 0.03 * math.sin(f * 1.7)
    lampe.data.energy = 25 * k
    lampe.data.keyframe_insert("energy", frame=f)
```

- **Pièges** : personnage monté avec un matériau ordinaire (il prend l'ombre du décor) ; personnage hors de la marque de mise au point (flou) ; lumière trop forte qui brûle en vue « Standard » ; décor pensé en largeur ; rendu plus grand puis recadré.
- **Pièges trouvés au rendu réel du 11/11/2026** : vue AgX laissée par défaut (la peau sort grise : passer en « Standard », et baisser les flammes et les fenêtres qui saturent alors plus vite) ; **clé de déplacement non tenue** (le personnage glisse vers sa place du plan suivant : `Perso.deplace()` du kit tient la clé d'arrivée) ; brume volumétrique en damier sur les gros plans à faible échantillonnage (la couper plan par plan) ; un double de l'objet héros resté dans le cadre ; un trait du dessin lu à contresens (une barbe en arc lue comme un sourire) ; tramage des aplats sombres en pleine taille à 8 échantillons.

## 7. Son

- **Ambiance** : l'air du lieu, très bas (salle de pierre, vent, feu qui crépite).
- **Bruitages** : seulement sur ce qui est physique (un objet tombe, une porte, un pas marqué, un tissu) ; **1 à 2 par 10 s** ; le pic du son sur l'image du contact ; coupes muettes. Le budget général du skill `son` (environ 5 par 10 s) vise le motion design ; une histoire narrée en porte bien moins (rendu réel du 11/11/2026 : 9 bruitages en 61,5 s, soit 1,5 par 10 s, écart médian de 12 ms avec l'image). `budget.py` dira « film calme » : c'est attendu.
- **Musique** : un seul thème discret sous la voix (cordes pincées, percussions légères, instrument de l'époque ou du lieu), qui s'efface sur le retournement (un silence de 20 images sur le film réel) et se résout sur la dernière image. **Instrument virtuel** (banque d'échantillons jouée par un musicien : ni enregistrement réel, ni synthèse pure) : permis si la licence du morceau est claire et couvre un usage monétisé ; à créditer avec la mention « instrument virtuel » ; jamais présenté comme un enregistrement d'époque. Détail : `references/pipeline.md`, étape 7.
- **Voix** : une seule, humaine de préférence. −14 LUFS. Avec une voix de synthèse, **contrôler l'écart entre ses repères de mots et le son réel** (107 ms constatés, soit trois images) : `outils/ecart_voix.py` du kit, arbitrage à la forme d'onde ; corriger une seule fois, au mixage.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : personnage ombré comme un objet 3D ; personnage qui flotte ; rebond permanent ; éclairage studio à trois points ; plan qui dure sans idée nouvelle ; objet de l'histoire dessiné à plat ; sous-titres par phrases entières ; titre centré sur un dégradé en ouverture.

- [ ] Aucun personnage ne reçoit d'ombrage du décor (aplats identiques au dessin) ; chacun a son ombre de contact et se tient à la marque de mise au point.
- [ ] Une lumière principale motivée et au moins une source chaude visible par décor ; ni blanc brûlé ni damier de brume.
- [ ] L'objet héros est en 3D, biseauté, avec au moins un gros plan ; **aucun double de l'objet dans le cadre ne contredit l'action**.
- [ ] Aucun plan de plus de 3 s (90 images) sans idée nouvelle ; coupes sur un début de mot.
- [ ] Chaque mouvement de personnage commence par un regard ; aucun rebond en boucle ; **aucun glissement** (clés de déplacement tenues).
- [ ] Sous-titres de 1 à 2 mots, taille unique, dans la bande y = 1385 à 1515, lisibles sur la planche « téléphone » à 360 px ; **le sujet tient dans les 65 % du haut**.
- [ ] Chaque affirmation et chaque chiffre à l'écran figure dans `sources.md` (tableau fait par fait, nuances écrites).
- [ ] Voix : écart entre repères de mots et son réel inférieur à une image, mesuré ; 1 à 2 bruitages par 10 s ; images pleine taille avec sous-titres vérifiées avant la critique.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 96

## 9. Aperçu

Pas d'aperçu tiers : le cours d'origine décrit le format d'une chaîne existante, dont les vidéos ne sont ni reprises ni montrées. **Aperçu à produire avec le plugin.** Le film du 11/11/2026 a servi à établir les règles de cette fiche ; c'est un essai interne qui reste non publié et n'est pas fourni (son sujet et sa grammaire suivaient de près une chaîne existante, ce qu'une vidéo publiée ne doit pas faire). L'exemple du kit (2 plans, personnage « Galet ») est un contrôle technique, pas un aperçu du style. Image de contrôle technique du studio : un bonhomme plat à matériau émissif, avec ombre de contact et profondeur de champ, rendu en Blender 5.3 lors de l'écriture de cette fiche.

## 10. Origine

- Cours « How to build a 2.5D motion studio with Opus 5.5 (Full Course) » : anatomie du format, règles de la maison, passes de décor, objet héros, personnages en plans, ligne de jeu, revue. Article public, auteur non indiqué dans la copie analysée ; idées reprises et reformulées, sans reprise de texte.
- Montage des personnages : manuel de Blender (« Images as Planes »).
- Connecteur : `ahujasid/mcp-for-blender`, commit `2e4b0bc`, MIT.
- Palette, tailles en pixels et valeurs d'animation : décisions du studio (non mesurées sur une vidéo existante).
- Règles marquées « rendu réel du 11/11/2026 » et kit de départ (`kit/`) : travail du studio, tirés de son essai interne du même jour (voir `licenses/styles-2-5d-histoire-vraie.md`).
