# Survol de bureau

## 1. Identité

- **Nom** : Survol de bureau.
- **Inspiration** : les visites de bureau en un seul plan des films de lancement de logiciels (des fenêtres posées à plat comme des lieux, un petit assistant pour guide), la photo de jouets en macro (soleil bas et chaud, longues ombres douces) et les sprites en pixel art (l'allure de la distribution). On n'en copie ni les personnages, ni les mises en page, ni les icônes, ni la musique.
- **Ce que c'est** :
  - **le bureau est le monde** : un tapis de papier mat à grille de points régulière, posé sur un bureau en bois clair, éclairé par **un seul soleil bas et chaud** venu d'une fenêtre. Tout y repose et projette une ombre longue et douce. Quelques objets du quotidien (stylo, notes adhésives, tasse) en avant-plan et en arrière-plan ;
  - **les interfaces sont des cartes de papier** : dalles arrondies de quelques millimètres d'épaisseur, l'interface imprimée dessus. Ce sont des **lieux** : les personnages s'y tiennent et y sautent, des morceaux d'interface en sortent en petits objets 3D ;
  - **la distribution : des sprites pixel devenus solides** : un cube biseauté par pixel, plus épais au centre qu'au bord, les yeux en relief. Couchés sur une carte, ce sont des autocollants ; ils se lèvent en jouets ;
  - **chaque étape est animée** par autre chose que l'action principale (débris, cubes de données qui sautillent, lampe qui clignote) ;
  - **un seul plan**, sans coupe, qui finit sur tout le bureau ;
  - **tout tombe sur le temps**, et chaque action a un son.
- **Marche pour** : le trajet d'un fichier, d'une commande ou d'un message entre plusieurs outils ; le fonctionnement d'une appli en 3 ou 4 étapes ; une automatisation ; une compression, une sauvegarde, une notification ; un récapitulatif de chaîne de travail.
- **Ne marche pas pour** : émotion, portrait, produit physique, sujet sans interface, texte long.
- Ce n'est ni une capture d'écran (pas de curseur, pas d'écran lumineux, **aucune interface ni logo d'une appli réelle tierce**), ni un film de briques ou d'argile, ni une infographie isométrique (caméra en perspective, vraie lumière), ni du motion design plat (tout a une épaisseur et une ombre).

## 2. Palette, typographie, matières

Un fond clair, une encre sombre, **un accent réservé à ce qui compte maintenant** (le trajet, la pastille de l'étape en cours, le bouton d'envoi, le mot clé). Deux gammes de départ :

| Rôle | « Gris froid et ambre » (argent, logistique, énergie, alimentation) | « Lilas et violet » (création, musique, apprentissage) |
|---|---|---|
| Papier / point | `#E5E9ED` / `#C8CFD7` | `#E7E4F3` / `#CBC5E2` |
| Carte | `#FDFDFC` | `#FCFBFF` |
| Encre / discret / filet | `#20252B` / `#7F8790` / `#E0E4E8` | `#1D1A2E` / `#807A96` / `#E2DFEE` |
| **Accent** | ambre `#E8890C` | violet `#6B4CE6` |
| Soutiens | bleu sarcelle `#2F8FB0`, prune `#8A5A9E`, crème `#F4E3B5` | abricot `#F39A5B`, ciel `#5FB4E8`, citron `#F2C94C` |
| Échec / réussite | `#D23A3A` / `#3C9C6E` | `#E2483D` / `#3FA57A` |

- La gamme « lilas et violet » reste claire, mais **mesure la part de bleu-violet** avant livraison ; préfère la gamme ambre par défaut.
- **Rouge seulement pour l'échec, vert seulement pour la réussite.** Deux ou trois teintes de soutien moyennement saturées pour la distribution, jamais fluo ; un personnage chaud sur le fond froid.
- **Avec la marque du client** : sa couleur devient l'accent ; les couleurs de son interface s'impriment sur les cartes ; le fond reste clair.
- **Typographie** (OFL), trois rôles : une chasse fixe pour étiquettes et chiffres en capitales espacées (**IBM Plex Mono**, DM Mono ou JetBrains Mono), une linéale à graisse forte pour pastilles, titres et sous-titres (**Instrument Sans**, Manrope ou Space Grotesk). Les pixels appartiennent aux personnages : **pas de police pixel sur l'imprimé**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : IBM Plex Mono à la place de DM Mono ; Inter à la place d'Instrument Sans et de Manrope ; IBM Plex Mono, JetBrains Mono : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/dm-mono`, `@fontsource/instrument-sans`, `@fontsource/manrope` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier mat, bois de chêne clair, cartes à léger grain ; accessoires en formes simples, mates ou satinées. Impression plate : une encre, filets fins, gros chiffres. Un téléphone est une carte à bord sombre avec **une interface entière** (barre d'état, en-tête, contenu, commandes) : sans cela, il se lit comme une dalle blanche vide.

## 3. Composition 9:16

- En vertical, **dispose les stations en zigzag de bas en haut** du tapis (3 ou 4 cartes), pour que le trajet monte dans l'image et que le plan final tienne tout le bureau dans la hauteur. Laisse un espace libre pour le carton de titre final.
- **Pour lire une carte, monte à 55-70° de plongée** : un imprimé à plat vu à 20° est illisible. Le texte qu'une caméra basse doit lire se met sur un objet debout (un chevalet).
- Personnage : assez grand pour qu'on voie ses yeux, soit 1/5 à 1/3 de la carte où il se tient ; dans le plan final, **au moins ≈ 35 px de large** chacun, sinon rapproche ou agrandis.
- La caméra garde son sujet un peu **au-dessus du centre** (décalage vertical fixe) : rien d'important sous la barre de sous-titres.
- **Dans le monde, seulement des mots clés et des chiffres** : pastilles d'étape (un chiffre et un mot, face caméra), tailles, un nom sur un écran, un carton de titre.
- **Sous-titres** : une ligne par phrase dite, dans une barre discrète en bas au centre (boîte d'encre arrondie à ≈ 72 % d'opacité, vers y 1440 à 1520), texte gras ≈ 44 px. Une seule langue.
- **Les titres sont des objets sur le bureau** : un chevalet à côté de la première étape ; à la fin, une grande carte de papier qui tombe dans l'espace libre.
- Plans larges : les stations remplissent au moins 70 % de la largeur.

## 4. Ce qui bouge

- **Action principale** : un personnage (ou un objet de données) porte le travail de carte en carte ; la caméra vole derrière lui.
- **Boucle de fond 1** : personnages qui clignent des yeux toutes les deux secondes, sautillent sur le temps en attendant, se penchent vers ce qu'ils regardent.
- **Boucle de fond 2** : à chaque station, un ou deux petits mouvements secondaires (cubes de données, lampe, marques qui vibrent). Aucune immobilité de plus d'environ 1,5 s.
- **Autorisés** : `#172` plan-séquence, `#176` survol, `#043` panoramique filé de carte en carte (0,3 à 0,5 s, incliné dans le virage, en cloche si les cartes sont éloignées), `#030` glissé macro en orbite lente, `#174` suivi bas derrière le sujet, `#031` montée vers une vue presque du dessus, `#011` écrasement et étirement des sauts (étirement ≈ 14 %, écrasement ≈ 30 % pendant 0,2 s), `#010` dépassement, `#002` éléments d'interface qui s'animent en cascade sur les doubles croches, `#024` secousse à l'impact, `#143` morceau d'interface qui s'extrude.
- **Interdits** : toute coupe et tout fondu (`#041`, `#044`, `#046`), `#034` tremblement d'épaule, curseur de souris, écran lumineux, flou devant le sujet, papier ou cartes qui bougent (hors secousse), ombre d'une étiquette flottante sur un texte à lire.
- Gestes natifs : **l'autocollant qui se lève** en jouet (0,25 à 0,5 s : charnière avec dépassement, cubes qui s'extrudent depuis le centre, petit saut) et son inverse (le jouet se recouche en autocollant quand il est rangé ou livré) ; **la presse** (une plaque tombe sur le jouet, des débris de pixels roulent, le même personnage ressort en demi-résolution) ; **le tiroir** ; **le messager** qui vole en arc entre deux cartes en laissant un pointillé ; **le salut final** (chaque station sautille une fois, de gauche à droite).
- Les groupes avancent en file, chacun une double croche derrière le précédent.

## 5. Rythme et montage

- 30 i/s, mouvement fluide. **Un tempo régulier** (110 à 130 BPM) ; toute action sur la grille des doubles croches, les grands moments sur les premiers temps. À 120 BPM : une double croche = 0,125 s.
- **Un seul plan.** Les étapes sont séparées par des filés, jamais par des coupes. À la clé où part un filé, la cible se pose d'abord ; le décollage d'un personnage est le départ naturel d'un filé.
- Quand le film explique : une voix le dit, en phrases courtes, une idée chacune ; l'image montre ce que la voix dit à cet instant ; les mots sur les cartes ne sont que les mots clés de la phrase.
- Un texte à lire est tenu immobile le temps de sa lecture, cadré au-dessus de la barre de sous-titres.
- **Le film se ferme sur tout le bureau** : chaque étape et le trajet dans une seule image, tout bouge une fois, le titre tombe dans l'espace libre.
- Durée conseillée : 30 à 60 s pour 3 ou 4 stations.
- **Version courte (8 à 12 s)** : un seul vol : le personnage porte le travail d'une carte à la suivante, l'accent sur l'étape en cours ; couper les autres stations.

## 6. Recette technique

**Moteur conseillé : Three.js** pour un film de 3 ou 4 stations avec beaucoup d'évènements calés (moteur d'origine, cartes redessinées en direct) ; **Blender** (connecteur MCP `blender`) pour un rendu plus photographique du bureau (bois, papier, lumière de fenêtre, flou).

| | Three.js | Blender |
|---|---|---|
| Cartes et écrans | canvas 2D en texture, redessinés **seulement quand leur état change**, dessinés à 3 fois la taille pour rester nets | images de chaque état préparées en canvas, appliquées en textures ; les états animés deviennent des suites d'images |
| Personnages | cubes biseautés instanciés, un par pixel ; profondeur selon la distance au contour | même construction en Python (instances de cubes) |
| Lumière | un soleil à ≈ 20° de hauteur, carte d'ombre douce qui suit la caméra, appoint ciel froid / sol chaud | soleil + ciel ; ombres douces et rebonds exacts ; bois et accessoires libres importés |
| Netteté | 16 à 24 sous-images décalées par image (anticrénelage + léger flou de mouvement), flou **derrière** le plan de point seulement | flou de mouvement et profondeur de champ de la caméra |
| Lisibilité | à contrôler : chaque texte à lire déclaré avec ses coins à l'écran | même contrôle sur les images rendues |
| Coût | modéré (sous-images) | long, un seul plan de 30 à 60 s à rendre d'un bloc |

- **Structure** : `monde` (tapis, bureau, soleil, cartes, pastilles), `cartes` (palette unique du film, dessin des interfaces), `voxel` (personnages), `anim` (sauts, levée, rebond sur le temps), `camera` (clés : cible, distance, azimut, élévation, focale), `film` (cartes, distribution, timeline, évènements sonores, zones de lecture).
- **Techniques clés** :
  ```js
  // personnage : couché (autocollant) -> debout (jouet)
  perso.set({ pos, yaw, e: 0, hinge: 0 });           // e : extrusion 0..1 ; hinge : charnière 0..1
  // largeur à l'écran d'un personnage, pour vérifier le plan final :
  // px = largeur * 1080 / (2 * distance * Math.tan(focale / 2))   -> viser ≥ 35 px
  ```
  - Le tapis a des dimensions multiples de deux pas de points, pour que les points imprimés s'alignent avec les éléments 3D.
  - Les pixels noir pur d'un sprite sont ses **yeux** : ils dépassent et clignent.
  - Les données qui sortent d'une carte sont extrudées depuis leur forme imprimée : elles se lisent encore du dessus.
  - Anneau d'impact : un fin anneau couleur d'accent qui s'étend sur le papier et s'efface en une seconde.
- **Pièges** : flou qui réduit le sujet ou ses mots en bouillie (flou ≤ 5 px, seulement derrière ; traînée ≤ 8 px) ; jouet debout qui cache la ligne derrière lui ; ombre longue d'une pastille flottante qui grise l'imprimé (les pastilles ne projettent pas d'ombre) ; sprite vu de profil qui se lit en rayures (tourne-le vers la caméra) ; filé au-dessus du papier nu ; barres 3D dressées qui deviennent des taches vues du dessus (couche-les) ; musique faite de fragments (écris des phrases entières).

## 7. Son

- **Musique** : claire et chaude, d'allure acoustique : marimba (avec vibraphone sous les notes longues), basse pincée, kick synthétique doux, claquements de mains, shaker, nappe de cordes discrète. Une tonalité, à peu près un accord par mesure. Sous une voix, la musique est un lit léger baissé d'environ 16 dB ; le thème complet joue là où personne ne parle.
- **Bruitages** : la source donne un son à chaque action ; applique le budget du studio (≈ 5 par 10 s) en gardant les plus lisibles et en laissant les notes accordées de la musique porter le reste. Levée : une note de marimba de l'accord en cours + un glissé montant. Saut : un tic doux. Atterrissage : un choc feutré. Presse ou tampon : choc grave. Frappe : clics secs (vrais enregistrements). Filé de caméra : un souffle proportionné à la vitesse.
- Les bruitages accordés prennent leurs notes dans la grille d'accords et se posent sur les doubles croches.
- **Voix** en tête ; −14 LUFS ; l'accord final tient jusqu'à la dernière demi-seconde.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Un seul plan, sans coupe ni fondu, qui finit sur tout le bureau.
- [ ] Un seul soleil bas : ombres longues et douces, teintées par le ciel ; tout a une épaisseur.
- [ ] Les interfaces sont des cartes imprimées, complètes, sans curseur ni lueur d'écran.
- [ ] Chaque texte à lire est vu à 55-70° ou sur un objet debout, tenu le temps de lecture, au-dessus de la barre de sous-titres.
- [ ] Les yeux de chaque personnage se voient ; personnages ≥ 35 px de large dans le plan final.
- [ ] Actions sur la grille des doubles croches ; aucune immobilité de plus de 1,5 s.
- [ ] Un seul accent ; rouge = échec, vert = réussite, rien d'autre.
- [ ] Aucune interface, icône ou logo d'une appli tierce ; part de bleu-violet mesurée si la gamme est lilas.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Affiche du film de démo d'origine *Before the Ding* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/posters/desktop-flythrough.jpg · film sur la galerie officielle : https://lemomo-ai.github.io/lemo-opuscar/#materials-3d
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 **pour l'image**. La piste de voix de ce film est **exclue** de la licence (voix de synthèse d'un service en ligne) : ne pas héberger ni rediffuser le film avec son ; montrer l'affiche, ou renvoyer vers la galerie d'origine.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/desktop-flythrough/STYLE.md`, `DEMO.md`, `demo/src/world.js`, `cards.js`, `voxel.js`, `anim.js`, `camera.js`, `post.js`, `demo/CREDITS` (moteur d'origine : three.js r170 + canvas 2D). Licence MIT, © 2026 LemoLab ; images CC BY 4.0, voix exclue. Polices Instrument Sans, IBM Plex Mono (SIL OFL 1.1).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, disposition en zigzag et tailles 9:16, sous-titres en une seule langue (la source prévoit deux lignes bilingues), budget de bruitages du studio, tableau des moteurs (voie Blender non testée), numéros du dictionnaire.
