# Livre pop-up

## 1. Identité

- **Nom** : Livre pop-up (livre animé en papier).
- **Inspiration** : les jeux où des héros en papier plat à bord blanc évoluent dans un diorama en 3D (bulles qui se tapent avec des bips), les grands livres animés d'ingénieurs papier (plis en V superposés, pièces qui se lèvent de l'arrière vers l'avant, tirettes), et la photo macro de « petit monde sur un vrai bureau ». On n'en copie ni les personnages, ni les logos, ni l'interface, ni la musique, et on ne les nomme pas.
- **Ce que c'est** : deux mondes dans une image. **Le monde réel** à taille humaine : une surface réaliste éclairée comme une pièce, quelques vrais objets, un objectif macro (faible profondeur de champ, lumière chaude, ombres de contact douces). **Le monde de papier** : un livre relié ; quand il s'ouvre, une planche se dresse comme **toile de fond** et la page du bas devient le sol. Chaque élément de décor est une **carte plate découpée** qui repose sur la page et **se lève** autour de son bord inférieur. Les personnages aussi : quelques centimètres, plats, avec une large bordure blanc cassé, une tranche de carton gris et du grain.
- Ce qui convainc : **le décalage d'échelle et de matière**. Garde le papier graphique ; laisse la lumière et l'objectif le rendre réel.
- **Marche pour** : lancement de projet (« le livre s'ouvre »), étapes d'un processus (une page = une étape), histoire pour enfants, recette, avant/après par tirette, un vrai produit posé à côté d'une histoire en papier ; et, en **histoire vraie** (catégorie `styles-2-5d-histoire-vraie`), une vie ou une histoire en **chapitres** (une page = un chapitre) : biographie, invention en étapes, récit de voyage, souvenir, ton tendre ou familial.
- **Ne marche pas pour** : sujet technique dense, ton sérieux ou sombre (le style impose une pièce claire), sujet abstrait sans lieux, histoire d'un seul instant (il faut au moins trois pages), action rapide ou montage nerveux, émotion par le visage (les visages sont simples).
- Ce n'est ni un film de silhouettes découpées, ni un cartoon 3D (rien n'est modelé en rond), ni de la pâte à modeler (le papier s'articule, se plie, s'enroule, glisse : il ne s'écrase jamais).
- **Deux emplois, une seule fiche** : le **conte** (par défaut : personnages de livre d'enfant, bulles, mots d'action) et l'**histoire vraie en chapitres** (une voix de conteur, jeu sobre, un seul mouvement continu). Ce qui change pour l'histoire vraie est réuni dans l'encadré « Variante histoire vraie » de la section 5.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Encre (brun foncé, jamais noir) | `#3A2A24` |
| Bordure blanc cassé des découpes | `#FFFDF7` |
| Tranche de carton | `#B9AD9C` |
| Bureau (noyer, teinte) | `#C9A88A` |
| Bureau en noyer foncé (variante du look n° 67) | `#6B3E1E` |
| Accent du personnage principal (histoire vraie) | une seule couleur vive, par exemple une casquette `#C8362C` |

- Couleur de livre d'enfant saturée, **jamais fluo** ; le monde réel reste naturel et un peu chaud.
- **Une famille de teinte dominante par double page** : tourner la page, c'est aussi changer de couleur. Quelques accents (un rouge, un jaune, un or) reviennent d'une page à l'autre pour coudre le livre. Exemples : prairie verte sous ciel bleu ; marché rose et lilas à accents menthe ; désert ocre à oasis turquoise.
- Les pages « hors de l'histoire » perdent la couleur : graphite sur crème.
- **Lumière du jour constante** : par défaut, le jour clair d'une fenêtre en haut à gauche, avec des ombres douces entre les couches. Les couleurs d'impression et la lumière de la pièce restent celles du jour **quelle que soit l'heure de l'histoire** : la nuit ou le soleil couchant n'existent que dans le dessin imprimé ; la vraie lampe garde sa chaleur.
- **Le carton reçoit la lumière.** Les cartes (décors et personnages) sont du papier mat éclairé par la pièce : elles prennent la lumière de la fenêtre et **projettent leur ombre** sur la page et sur les cartes de derrière. C'est une exception voulue à la règle « personnages émissifs » du skill `personnages` : ici le personnage est une carte de papier dans la lumière, toujours plat et sans modelé.
- **Impression** : au choix, encre et aplats de livre d'enfant (voir « Dessin »), ou aquarelle transparente et hachures de crayon de couleur à gros grain (look n° 67). Jamais d'aplat numérique lisse.
- **Typographie** (OFL) : **Fredoka** (sous-titres, bulles, panneaux), **Lilita One** (couverture, banderoles, mots d'action), **IM Fell English** (phrases de conte). En histoire vraie : titres de page en écriture manuscrite lisible (Caveat, Patrick Hand) imprimée sur la page, sous-titres en Montserrat ExtraBold blanc à contour sombre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka et de Caveat et de Patrick Hand ; Archivo Black à la place de Lilita One ; EB Garamond à la place d'IM Fell English ; Montserrat : déjà fournie. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka`, `@fontsource/lilita-one`, `@fontsource/im-fell-english`, `@fontsource/caveat`, `@fontsource/patrick-hand` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Dessin** : contour épais (≈ 9 px à la résolution du dessin) + trait de détail plus fin (≈ 5 px), jonctions rondes ; ombrage = **un croissant dur** ; formes tremblées, jamais de géométrie parfaite ; visages simples (grands yeux ovales noirs à deux reflets, bouche courbe, joues roses).
- **Finition « découpe »** : la silhouette du dessin est dilatée en une tranche de carton gris décalée vers le bas (l'épaisseur) et en une large bordure blanc cassé ; un grain de papier commun par-dessus. Chaque bord coupé montre une âme blanche et un carton gris : c'est ce qui prouve que c'est du papier ; une carte qui a l'air pleine casse le style.
- **Échelle réelle** : page de 0,3 à 0,5 m de large, acteurs de 3 à 5 cm.

## 3. Composition 9:16

- 1080×1920 ; zones d'interface : table de `rendu/references/zones-interface.md`.
- **Plan signature** : vue haute de trois quarts sur toute la double page, le bord du bureau visible en bas et sur un côté.
- En vertical, **tourne le livre** : la planche dressée (le ciel) occupe le haut de l'image (y 200 à 950), la page au sol descend vers le spectateur (y 950 à 1500), le bord du bureau et un objet réel flou ferment le bas. Le livre se lit alors comme une petite scène de théâtre haute.
- Caméra macro à hauteur d'acteur pour l'histoire (acteur ≥ 1/3 de la hauteur dans les plans de jeu), vue de trois quarts en plongée pour montrer le mécanisme, vue du dessus pour un trajet ou un plateau de jeu.
- **Plan rapproché** : la caméra plonge dans la page ; les cartes du premier plan sont floues en bas du cadre, le personnage net au milieu (entre y 600 et y 1200), le fond imprimé en haut.
- Les décors se superposent en profondeur vers le haut : c'est un atout du format.
- **Sous-titres de narration** : ≈ 46 px, crème à gros contour brun foncé et ombre douce, vers y 1450 (conte). En histoire vraie : 1 à 2 mots à la fois, 96 à 112 px, ligne de base entre y 1400 et y 1500, sur la page à plat ou le bureau, jamais sur une carte de personnage. **Bulles** dans le monde de papier : carte blanche à contour d'encre, queue projetée à chaque image vers celui qui parle ; elles surgissent avec dépassement et se tapent avec des bips.
- **Les titres sont des objets en papier** : un panneau de carton qui descend sur des ficelles et se balance ; la couverture du livre est le titre du film.
- Garde les décors proches hors du trajet de l'objectif : ils remplissent l'image de flou.
- 16:9 : format d'origine ; la double page s'étale en largeur.

## 4. Ce qui bouge

- **Action principale** : le livre s'ouvre, le monde se lève (les cartes se dressent sur leurs plis) ; un petit acteur traverse la page, ou une carte de personnage coulisse ou pivote sur sa languette. Une action par page.
- **Boucle de fond 1** : plantes et petits accessoires qui oscillent de quelques centièmes de radian autour de leur base.
- **Boucle de fond 2** : choses suspendues à des ficelles (ressort amorti), feuille de page qui frémit, lumière de la fenêtre qui varie de ± 3 à 5 % (un nuage passe). En option : un petit élément porté par l'air (plume, feuille, flocon) qui guide la caméra d'une page à l'autre.
- **Autorisés** : `#140` page qui tourne (la transition du style), `#010` dépassement des décors qui se lèvent, `#123` saut en parabole (écrasement aux deux bouts, petit nuage de papier à l'atterrissage), `#011` écrasement et étirement **des personnages seulement**, `#033` bascule de point papier ↔ objet réel ou d'une couche à l'autre, `#016` parallaxe entre les couches, `#027` descente de la hauteur humaine à l'échelle du livre, `#031` grue qui laisse le livre tout petit, `#181` vue du dessus, `#006` texte tapé (bulles), `#175` plan fixe sur une tirette.
- **Interdits** : `#044` fondu enchaîné à l'intérieur du livre, rotation d'une carte sur son axe vertical (on voit sa tranche, puis son dos vide), tout volume modelé, déformation molle du papier, mouvement de la pièce (elle ne bouge jamais), `#034` caméra à l'épaule, `#043` panoramique filé, `#023` glitch, `#187` fondu au noir entre les pages (on tourne la page), coupe franche au milieu d'une page.
- **Les décors se lèvent de l'arrière vers l'avant** (le retard grandit avec la distance au lecteur) et se couchent dans le même ordre.
- Personnages : cartes plates redessinées à chaque pose quantifiée ; la phase de marche suit la distance parcourue (les pieds ne glissent pas). **Se retourner = un retournement horizontal du dessin** entre une vue de face et une vue de dos.

## 5. Rythme et montage

- Mouvement fluide (pas de saccade) : le charme vient des courbes d'arrivée, pas d'une cadence basse.
- **Tourner la page = changer de scène** : les anciennes pièces se couchent pendant que les nouvelles jaillissent. Autres transitions : le livre se ferme et se rouvre ; une coupe franche sur un bruit de papier.
- Une double page = 6 à 12 s. Film court : 2 à 4 doubles pages, 25 à 50 s.
- **Silence** = le livre immobile avec seulement le ton de la pièce, avant une page qui compte.
- Mots d'action (lettrage incliné, double contour, rayons) avec parcimonie, comme une note dans un jeu.

**Variante histoire vraie** (catégorie `styles-2-5d-histoire-vraie`, parcours dans son `references/pipeline.md`) :

- **Un seul mouvement continu** : plonger dans une page, reculer, tourner la page au lieu de couper, plonger dans la suivante. Aucune coupe franche ; le tour de page dure 20 à 30 images, calé sur la fin d'une phrase.
- 3 à 5 pages pour 60 s, soit 10 à 18 s par page, chacune découpée en 3 à 5 **moments** (arrivée, action, détail, recul) qui tiennent lieu de plans : « un plan par idée » devient « un cadrage par idée ». Repère du look d'origine : 12 moments sans coupe, avec deux tours de page.
- Ouverture : le livre fermé sur le bureau s'ouvre et la première scène se dresse. Fin : le livre se referme, ou la caméra recule sur la dernière page.
- **Jeu sobre** : par la pose imprimée et le déplacement de la carte. Pas de visage de dessin animé (traits d'illustration discrets), pas d'écrasement-étirement `#011`, pas de bulles ni de mots d'action. Deux ou trois cartes par personnage (assis, debout, en marche), une par page.
- **Objet héros en volume** (ce dont parle l'histoire), posé sur la page ou sur le bureau à côté du livre ; il a son gros plan.
- Une seule voix, de conteur ; sous-titres de 1 à 2 mots (section 3).
- **Version courte (8 à 12 s)** : une seule double page : ouverture du livre (1,5 s), le monde se lève, un acteur traverse, tenue de 2 s ; couper la seconde page et la fermeture.

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`) pour la lumière de pièce et le flou macro ; **Three.js** convient aussi (c'est le moteur d'origine) si la page tournée et le flou sont déjà maîtrisés.

| | Blender | Three.js |
|---|---|---|
| Cartes découpées | plans avec le dessin en couleur **et en transparence**, matériau qui reçoit la lumière ; l'ombre prend la forme de la découpe (Cycles : d'elle-même ; EEVEE : méthode de rendu « dithered ») | plans à alpha découpé + **matériau de profondeur avec la carte alpha**, sinon l'ombre est un rectangle |
| Page qui tourne | maillage en bandes animé par clés ou par un modificateur de courbure | bande à nombreux segments dont la courbure est intégrée le long de la page |
| Pièce et flou | ciel d'intérieur et accessoires CC0 importés, profondeur de champ de la caméra | HDRI + flou de profondeur écrit à la main (le flou « de série » fait faux à cette échelle) |
| Dessins | faits en canvas 2D (mêmes fonctions), exportés en images, appliqués comme textures | canvas 2D directement en textures, redessinés seulement au changement de pose |
| Durée | minutes par double page | rapide |

- **Structure** : `papier` (finition découpe, grain, croissant), `decoupes` (carte à dos de papier nu, ficelles), `livre` (ouverture, feuille qui s'enroule), `dessins` (à échelle fixe, en pixels par mètre), `acteurs` (personnages plats posables), `decors` (doubles pages, ordre de levée), `titres` (sous-titres, bulles, banderoles).
- **Techniques clés** :
  ```js
  // levée d'un décor : rotation autour de son bord inférieur, avec dépassement
  const u = clamp((t - t0 - 0.06 * rang) / 0.45, 0, 1);    // rang = distance au lecteur
  carte.rotation.x = -Math.PI / 2 * (1 - backOut(u));       // couché -> debout
  // demi-tour d'un personnage : jamais rotation.y
  perso.scale.x = regardeADroite ? 1 : -1;                  // (ou dessiner la vue miroir)
  ```
  - Tout objet « en volume » est fait de plusieurs cartes plates (une devant, une derrière, le contenu entre les deux).
  - Courbe de tons **neutre** : une courbe filmique décale les couleurs du papier.
  - Une page qui se tourne devient noire face opposée aux lampes : donne-lui une émission égale à sa couleur.
- **Voie Blender, structure** (skill `blender` ; assemblage dans HyperFrames) : un seul fichier, un bureau, un livre, **une collection par page**.
  - Le livre : deux plats de couverture et des pages articulées autour de la reliure (un objet vide par page, sur l'axe du dos).
  - Chaque double page : une page à plat, une page de fond relevée à 90°, et 4 à 8 cartes dressées entre les deux, parallèles au fond, chacune parentée à un objet vide placé **sur son pli** pour se rabattre à plat. Les cartes ne se dressent pas toutes à la même image : 3 à 6 images de décalage, du fond vers l'avant.
  - **Matériau des cartes** : Principled mat (rugosité élevée), image imprimée en couleur de base, transparence par l'alpha de l'image. **Pas de matériau émissif** et `visible_shadow` laissé actif : le carton reçoit la lumière et porte son ombre (pas de disque d'ombre de contact, contrairement à `personnages/references/import-blender.md`).
  - **Tranche du carton** : un modificateur d'épaisseur posé sur un plan rectangulaire n'épaissit que le rectangle, pas la découpe. Deux façons justes : (a) peindre la tranche dans l'image (finition « découpe » de la section 2), suffisant à distance de lecture ; (b) pour les gros plans, découper le maillage le long de la silhouette, puis lui donner 1 à 1,5 mm d'épaisseur avec un second matériau gris clair sur la tranche.
  ```python
  import bpy, math

  # dresser une carte : rotation autour de son pli, de couchée (90°) à debout (0°), avec un léger dépassement.
  # Le signe dépend du côté où la carte est couchée : vérifier sur la première carte, par une capture.
  pli = bpy.data.objects["P2_carte_banc_pli"]            # objet vide placé sur le pli, parent de la carte
  for image, angle in ((310, 90), (328, -4), (336, 0)):
      pli.rotation_euler.x = math.radians(angle)
      pli.keyframe_insert("rotation_euler", frame=image)

  # carte découpée le long de sa silhouette (cas b) : épaisseur de 1,2 mm, tranche dans le 2e matériau
  carte = bpy.data.objects["P2_carte_banc"]
  ep = carte.modifiers.new("Epaisseur", "SOLIDIFY")
  ep.thickness = 0.0012
  ep.material_offset_rim = 1

  # ombre à la forme de la découpe en EEVEE (4.2 ou plus récent) ; Cycles n'en a pas besoin
  mat = carte.active_material
  if hasattr(mat, "surface_render_method"):
      mat.surface_render_method = "DITHERED"
  ```
  - **Lumière** : une grande lumière de zone à la place de la fenêtre (haut, gauche), une HDRI d'intérieur clair de Poly Haven (CC0) pour le reste.
  - **Profondeur de champ physique**, mise au point sur la couche du personnage (f/2 à f/2,8 : le livre est petit, le flou est fort).
  - Recette écrite sans démo Blender d'origine et **non essayée** : à valider par un rendu réel (voir aussi les noms de propriétés selon la version dans `blender/references/bpy-portable.md`).
- **Pièges** : cartes qui ont l'air pleines (pas de tranche) ; pièce sombre et dramatique (le style veut le jour) ; cartes qui se traversent en se dressant ou en se rabattant (vérifier en fil de fer) ; ombres rectangulaires (elles tuent l'illusion) ; acné d'ombre sur des cartes minces (biais serré, grande carte d'ombre) ; décor proche de l'objectif qui noie l'image de flou ; échelle négative qui inverse recto et verso des accessoires (dessine la version miroir).

## 7. Son

- **Le papier est la signature** (vrais enregistrements : c'est facile à capter) : page qui glisse, carton qui tombe à plat, claquement d'un décor qui se lève, pli et froissement, tirette qui coulisse, pas en petits tapotements froissés, craquement du dos du livre, livre qui se referme. Le **carton qui se déplie** à chaque page est le bruitage signature ; petit choc de l'objet héros sur le bureau.
- **Voix des personnages en bips de frappe** : une forme d'onde et une hauteur par personnage, un bip toutes les deux lettres.
- **Narration** : un conteur chaleureux, phrases de livre d'images.
- **Musique** : fantaisiste, acoustique ou jouet : boîte à musique, pizzicati, clarinette, glockenspiel, ukulélé, piano jouet, balais. En histoire vraie : piano ou guitare seuls, une respiration à chaque tour de page, résolution sur la dernière image ; pas de voix en bips.
- **Ambiance** : ton de pièce et horloge pour le bureau ; un lit sonore par double page pour le monde de papier. Voix bien au-dessus de la musique ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Deux mondes visibles : papier graphique net, pièce réelle floue et plus terne, éclairée comme en plein jour quelle que soit l'heure de l'histoire.
- [ ] Chaque découpe a sa bordure blanc cassé et sa tranche de carton.
- [ ] Le carton reçoit la lumière : l'ombre de chaque carte a la forme de sa découpe et tombe sur la page ou la carte de derrière.
- [ ] Les décors se lèvent de l'arrière vers l'avant, avec dépassement.
- [ ] Aucune carte vue par la tranche ou de dos, aucune carte qui en traverse une autre ; les demi-tours sont des retournements.
- [ ] Les changements de scène passent par la page, le livre ou une coupe sur un son de papier (histoire vraie : par le tour de page seulement).
- [ ] Une teinte dominante par double page ; aucune couleur fluo.
- [ ] Acteur net, ≥ 1/3 de la hauteur dans les plans de jeu ; aucun personnage ni logo existants.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *Pip's Paper Adventure* (133 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/paper-popup.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/paper-popup.jpg
- Second aperçu, look n° 67 « livre pop-up sur un vrai bureau » : extrait de 5 s (de 3:18 à 3:23) du film collectif https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/opuscar98.mp4 · page des styles : https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles. **À consulter seulement, ne pas afficher sur une page de vente** : l'extrait met en scène une mascotte tierce et l'adaptation d'une œuvre protégée.
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/paper-popup/STYLE.md`, `DEMO.md`, `demo/paper.js`, `cutmesh.js`, `book.js`, `art.js`, `actors.js`, `sets.js`, `post.js`, `hud.js` (moteur d'origine : three.js r170 + canvas 2D). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices Fredoka, Lilita One, IM Fell English (SIL OFL 1.1) ; accessoires et ciel Poly Haven (CC0).
- Même dépôt, même commit : `styleboard/opuscar98_styles.json`, entrée n° 67 (« Pop-up Book on a Real Desk », rendu 2.5D), champs `prompt_en`, `desc_en`, `blend_en`, `shots`, `direction_en` (MIT). Repris : cartes sur plis parallèles et page de fond à 90°, impression aquarelle et crayon, tranches à âme blanche, lumière du jour constante, bureau en noyer foncé, plan signature, mouvement continu avec tours de page, liste « à éviter ». Retirés : le titre et les personnages de l'œuvre adaptée, la mascotte.
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, livre tourné pour le 9:16, voie Blender et tableau comparatif (non testés par un rendu), numéros du dictionnaire, variante « histoire vraie » ; la police chinoise de la démo n'est pas reprise. Cette fiche réunit les deux fiches `livre-pop-up` écrites séparément (catégories « Matières et 3D » et « 2.5D histoire vraie ») ; la seconde catégorie y renvoie.
