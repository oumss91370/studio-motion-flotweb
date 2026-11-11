# Lancement narré, calé mot à mot sur la voix

## 1. Identité
- **Nom** : Lancement narré mot à mot. Identifiant : `lancement-narre-mot-a-mot`.
- **Inspiration** : le film de lancement classique d'un produit numérique : une voix qui défend une affirmation, des cartes d'interface filmées avec une vraie caméra, une preuve chiffrée, un appel à l'action.
- **Principe** : **la voix d'abord.** On écrit le script, on enregistre ou on génère la voix, on la transcrit mot à mot, et **chaque révélation à l'écran tombe sur le mot qu'elle illustre** : ni sur une grille de temps, ni sur une estimation. Le film alterne deux registres : **sombre pour l'argument** (problème, affirmation, preuve, appel à l'action) et **clair pour le produit** (interfaces, cartes, listes). Des outils de contrôle au vert ne disent pas qu'un film est bon : c'est le travail du réalisateur.
- **Pour quels sujets** : lancement d'un produit ou d'une offre, annonce de fonction, vidéo de page d'accueil, publicité de 30 à 60 s, explicatif produit avec voix.
- **Ne marche pas pour** : un produit sans rien de vrai à montrer (pas d'écran, pas de chiffre, pas de client), une boucle muette (voir `forme-continue-sur-la-musique`).
- À lire avant : `references/script-de-lancement.md` (angle, arc, écriture pour l'oreille, vérité).

## 2. Palette, typographie, matières
- **Deux fonds, pas trois** : un registre sombre (`#100e19`, jamais `#000`, avec une nappe de marque qui tombe d'en haut) et un registre clair (`#fafafb`, deux nappes de marque à 5-6 % dans les coins du haut). Chaque plan est l'un ou l'autre ; la bascule est un temps fort.
- **Palette dérivée de la marque** (fiche « ma chaîne ») : accent, accent 2 (en dégradé seulement), accent clair, encre, fond clair, un gris de texte, et un **accent lisible** foncé jusqu'à 4,5:1 sur blanc pour les petits textes. Tableau complet : `references/etalonnage.md` §10. Une troisième teinte est presque toujours une erreur.
- **Typographie** : la police de la marque, sinon une sans nette (DM Sans, Inter, Geist). Surtitre en petites capitales espacées ; affirmation en très grand ; un seul gris pour tout le secondaire.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de DM Sans et de Geist ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/dm-sans`, `@fontsource/geist` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** : cartes blanches sur fond clair, ombres douces ; « verre » fait de deux anneaux (bande givrée + filet), jamais `backdrop-filter`. Passe d'étalonnage unique sur tout le film : grain fin (0,1), vignette faible (0,15 dans les coins), trois balayages de lumière.
- **Vrais écrans, vrais chiffres, vrais logos** uniquement (fichiers du client).

## 3. Composition 9:16
- **Affirmation** (registre sombre) : 2 à 3 lignes, 110 à 150 px, centrée entre y 600 et y 1100, tenue **immobile** 2 à 3 s.
- **Carte d'interface** (registre clair) : largeur 880 à 940 px, centrée vers y 820, dans un montage caméra à deux nœuds ; rotation réduite en vertical (−5° → −1°).
- **Sous-titres de la voix** : y 1380 à y 1540, 2 lignes au plus ; la zone sous y 1560 reste vide (interface de l'application). Calculer chaque poussée de caméra contre cette limite : `bas_après = bas + (bas − origine_y) × (échelle − 1)`.
- **Compteur héros** : 200 à 280 px, avec sa source en 28 px dessous (jamais moins : 28 px est le plancher de lecture du studio).
- **Carte de fin** : nom, appel à l'action mot pour mot, tenue ≥ 3 s ; la marque en dernier.
- Curseur : 60×74 px, blanc à contour sombre.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : carte 1344×744 environ, bande basse de ~17 % réservée aux sous-titres.

## 4. Ce qui bouge
- **Action principale** : la révélation sur le mot. Un mot = une révélation ; le curseur part 0,2 à 0,3 s avant pour que **le clic** tombe sur le mot.
- **Boucles de fond** : (1) la rotation lente de tout le plan (la caméra qui se pose) et la parallaxe de deux plans en sens opposés ; (2) la dérive de l'aurore derrière un long plan de texte (≈ 28 px en 4 s).
- **Caméra** : montage à deux nœuds (travelling dehors, rotation dedans) ; poussée posée **avant** le clic, immobile pendant, relâchée après ; origine de la poussée exactement sur le bouton cliqué ; profondeur par des `z` de 12 à 22 px ; bascule de mise au point (flou 2,6 px + opacité 0,55) sur ce qui a déjà servi.
- **Le clic en trois couches** : halo qui précède de 0,1 s, appui du curseur, onde ; et le bouton s'enfonce de 6 %.
- **Rien ne finit en mouvement** : chaque plan se pose avant la coupe ; les tenues sont voulues.
- **Catalogue de plans** (en choisir 6 à 10) : typographie cinétique, plan « encombrement » (le problème), affirmation tenue, champ de demande, surface de résultats, espace à deux volets, suivi d'étapes, compteur héros, témoignage avec visage (accord obligatoire), colonnes de comparaison, carte de fin.
- **Autorisés** : #027 poussée, #033 bascule de mise au point, #016 parallaxe (un mouvement par plan), #083 curseur, #085 onde, #007 compteur, #005 révélation par masque, #002 décalage en cascade, #022 balayage de lumière (3 par film), #020 traversée de zoom, #137 poussée de plan, #044 fondu court, #046 coupe.
- **Interdits** : dérive par élément façon écran de veille, particules et formes flottantes derrière le texte, rotation qui finit à 0° ou continue après le plan, caméra qui bouge pendant un clic, #006 machine à écrire sur un titre, #111 aberration chromatique sur du texte tenu, halo lumineux sur le registre clair.

## 5. Rythme et montage
- **Durée** : 40 à 60 s (script de 100 à 150 mots) ; version réseaux 20 à 30 s.
- **Arc** : problème (4 s) → aggravation (4 s) → affirmation (2 à 3 s) → 3 à 4 temps produit (14 à 16 s) → preuve (10 s) → contraste (5 s) → appel à l'action (4 s). **L'affirmation dans les 10 premières secondes.**
- **La durée de chaque plan est mesurée sur la voix**, jamais devinée ; la transition part à l'instant où la narration du plan finit.
- Transitions entre plans : fondu court, traversée de zoom, poussée, coupe ; choisies par le sens.
- Trois balayages de lumière : sur l'affirmation, à l'ouverture de la preuve, sur l'appel à l'action.
- Avant un coup grave (affirmation, appel à l'action) : ~0,3 s de quasi-silence.
- **Version courte (8 à 12 s)** : l'affirmation (2 s), deux temps produit de 3 s (une révélation par mot), l'appel à l'action (2 à 3 s) ; couper problème, aggravation, preuve et contraste ; 25 à 30 mots de voix.

## 6. Recette technique
- **Moteur** : HyperFrames + GSAP (c'est le moteur d'origine de ce style).
- **Ordre de fabrication** : brief → trois directions dont deux éliminées → passe vérité (liste des chiffres approuvés) → script → **voix** → transcription mot à mot → storyboard → plans → assemblage → transitions → son → étalonnage → contrôles → master → vérification dans le fichier livré.
- **Table des repères** : la transcription donne `mot("cherche").debut` ; chaque animation et chaque son s'y accroche.
```js
const T = (m, n = 0) => mots.filter(w => w.texte === m)[n].debut - debutPlan;   // temps local au plan
const phrase = "Trouve-moi 20 profils", e = {n: 0};                              // frappe dans le champ, sans extension
tl.to(e, {n: phrase.length, duration: 0.7, ease: "none",
  onUpdate: () => champ.textContent = phrase.slice(0, Math.round(e.n))}, T("demande"));
clic(1, T("partie"));                                   // le clic tombe SUR le mot
tl.fromTo(".resultat", {y: 24, opacity: 0}, {y: 0, opacity: 1, stagger: 0.07, duration: 0.4}, T("résultats") - 0.05);
```
- **Caméra, profondeur, curseur** : `references/camera-et-curseur.md`. **Fonds, verre, grain, vignette, balayages, palette** : `references/etalonnage.md`. **Repères sonores, loi du volume, mastering** : `references/son-et-mastering.md`.
- **Contrôle du contraste** sans la piste d'étalonnage, livraison avec.
- **Pièges** : aucun `mix-blend-mode` ni `backdrop-filter` dans une piste de surimpression (le film entier vire au blanc) ; `filter: blur(0px)` explicite avant d'animer un flou ; ne pas faire se toucher deux animations de la même propriété (laisser 0,01 s) ; `immediateRender: false` sur les ondes ; rendus numérotés, jamais écrasés ; vérifier cinq révélations au hasard contre la transcription.

## 7. Son
- Trois couches : voix (la plus forte), lit musical très bas, bruitages placés et mesurés un par un.
- Chaque repère nomme son mot ; un repère par évènement ; rien ne sonne plus de deux fois en 45 s ; pas de carillon sur un clic.
- Coup grave long et discret sous l'affirmation et sous l'appel à l'action seulement.
- Vrais enregistrements d'abord (skill `son`) ; niveler tout fichier trop faible au lieu de monter son volume.
- Mastering en deux passes, **−14 LUFS, crête ≤ −1,0 dBTP**, limiteur sans gain de rattrapage ; mesure sur le fichier livré.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] L'affirmation tient en sept mots, est dite avant 10 s et reste immobile 2 à 3 s.
- [ ] Trois directions ont été écrites, deux éliminées, le choix est noté.
- [ ] Chaque nombre, logo, visage, capture et témoignage est réel et figure dans la liste approuvée.
- [ ] Cinq révélations prises au hasard tombent sur leur mot (écart ≤ 2 images).
- [ ] Quatre temps produit au plus ; chaque plan est sombre ou clair, jamais entre les deux.
- [ ] La caméra est immobile pendant chaque clic ; le curseur disparaît quand il a fini.
- [ ] Trois balayages de lumière au plus, chacun sur un temps fort nommé ; aucun noir pur.
- [ ] −14 LUFS et crête mesurés sur le fichier livré ; rien d'important sous y 1560.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 3
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Le film de référence et l'image fixe du dépôt d'origine appartiennent à un client de l'auteur : **aucune réutilisation**. Aperçu Flot Web à produire.

## 10. Origine
- Dépôt : AbubakrChan/product-launch-motion, commit `edbfb10` (version 1, dossier `legacy/`). Fichiers : `legacy/SKILL.md`, `legacy/references/02-story-and-truth.md`, `03-word-locked-sync.md`, `05-camera-3d-cursor.md`, `06-look-and-grade.md`, `07-sound-and-master.md`, `09-shot-catalog.md`.
- Licence : MIT ; films et image d'exemple exclus par la notice du dépôt.
- Adaptations Flot Web : français, 9:16, zones d'interface du plugin, voix et transcription par les outils des skills `son` et `rendu`, scripts d'origine non repris.
