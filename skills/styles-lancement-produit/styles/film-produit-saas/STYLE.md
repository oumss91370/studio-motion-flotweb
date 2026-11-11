# Film produit SaaS (la chaîne où chaque étape produit la suivante)

## 1. Identité
- **Nom** : Film produit SaaS. Identifiant : `film-produit-saas`.
- **Inspiration** : le film de page d'accueil d'un logiciel en ligne : 45 à 75 secondes qui montrent **tout le produit en action**, lisibles sans le son.
- **Principe** : **l'histoire est une chaîne.** Le problème, dit avec les mots du client (3 à 5 s) → chaque étape **produit** ce que la suivante utilise (l'objet qui sort d'une étape devient la scène suivante, une seule caméra continue, pas de coupe franche) → le résultat mesurable à l'écran → la surprise du prix → l'appel à l'action. Les écrans sont **reconstruits en code** à partir de captures, jamais collés.
- **Pour quels sujets** : logiciel en ligne, application, outil interne, plateforme : tout produit à plusieurs écrans dont on veut montrer le parcours complet.
- **Ne marche pas pour** : un produit à un seul écran (voir `demo-produit-epuree` ou `forme-continue-sur-la-musique`), un produit dont on n'a pas de captures, un teaser de 15 s (voir `teaser-haute-energie`).
- **Deux niveaux** : **passe légère** d'abord (une langue, un format, sans voix) ; traitement complet seulement si le client le demande (voix, deux langues, plusieurs formats).

## 2. Palette, typographie, matières
- **Un seul fichier de jetons d'interface** (`jetons-interface`), extrait des captures du client : couleurs exactes **par échantillonnage de pixels**, polices, rayons, ombres, bordures, espacements. Tout écran reconstruit lit ce fichier ; rien n'est choisi à l'œil.
- Les couleurs du film autour des écrans (fonds, titres) viennent de la fiche « ma chaîne » ; **une seule couleur d'accent**.
- **Typographie cinétique** pour le message (le film est d'abord muet) : la police de titre de la marque ; **chaque titre sur UNE ligne**.
- **Police de repli** : Inter pour l'interface, Montserrat ou Archivo Black pour les titres, quand la police de la marque manque. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : la police de la marque : fichier fourni par le client, copié dans `assets/fonts/` ; à vérifier (licence et accents).
- **Écrans** : composants qui s'animent élément par élément (lignes en cascade, compteurs, jauges, frappe, curseur, interrupteurs). Comparer chaque écran reconstruit **côte à côte avec sa capture** jusqu'à ce qu'il soit reconnaissable au premier coup d'œil.
- **Anonymisation** : **une seule entreprise fictive utilisée partout** (même nom de domaine, mêmes produits, mêmes concurrents) ; aucun vrai client, concurrent ou personne ; avatar neutre. Les images qui contiennent du texte sont reconstruites (en code, ou partie photo seule + texte retapé).
- **Interdits de matière** : dégradés arc-en-ciel, particules, chrome lumineux, émojis, faux texte de remplissage, visages générés, retournements 3D gratuits.

## 3. Composition 9:16
- **Le 9:16 est une recomposition, pas un recadrage** : chaque écran est reconstruit pour le vertical (colonnes empilées, tableau réduit à ses 2 ou 3 colonnes utiles, panneau latéral passé dessous).
- **Marges sûres** : 80 px en 9:16 (110 px en 16:9), plus les zones d'interface du plugin : rien d'important au-dessus de y 160, sous y 1560, à droite de x 945.
- **Texte dans le carré central** (1080×1080, y 420 à y 1500) : décidé dès le storyboard.
- **Titre cinétique** : une ligne, 72 à 110 px selon sa longueur (raccourcir la phrase plutôt que passer sur deux lignes), entre y 240 et y 420 ; l'écran dessous, de y 460 à y 1480.
- **Résultat mesurable** : le chiffre en 200 à 280 px, avec son unité et la mention « données d'exemple » si les données sont illustratives.
- Chaque élément finit son animation et **reste lisible au moins 1,5 s**.
- **16:9** : le format maître d'origine ; les deux se déclinent **depuis la même ligne de temps**.

## 4. Ce qui bouge
- **Action principale** : le **passage d'objet** d'une étape à la suivante : la ligne sélectionnée devient la fiche, la fiche devient le message, le message devient la ligne du tableau de bord. Un élément partagé à chaque passage, une caméra continue.
- **Boucles de fond** : (1) micro-dérive permanente : **aucune image figée sauf la tenue finale** (et même la carte de fin dérive imperceptiblement) ; (2) un compteur ou une jauge qui vit dans l'écran en cours.
- **Une seule chose bouge à la fois** ; un seul système de formes du début à la fin.
- **Ressorts** avec amortissement fort (pas de rebond visible). Repères : interface vive (raideur 320, amortissement 30), conteneurs et caméra (170 / 26), typographie lourde et logos (120 / 24).
- **Texte** : révélé par masque (montée de 105 %), mots décalés de 55 ms.
- **Caméra** : position et zoom interpolé en logarithme ; jamais un zoom avant suivi d'un zoom arrière dos à dos.
- **Sorties** environ 1,5 fois plus rapides que les entrées ; **le plan suivant entre déjà en mouvement, dans la direction de la sortie**.
- **Autorisés** : #161 élément partagé, #012 morphing, #020 traversée de zoom, #028 zoom, #005 révélation par masque, #002 cascade de lignes, #007 compteur, #083 curseur, #006 frappe dans un champ, #059 interrupteur, #172 plan-séquence.
- **Interdits** : coupes franches entre étapes, #044 fondu comme transition par défaut, #021 retournements 3D gratuits, #015 particules, plusieurs points d'attention à la fois, texte qui bouge pendant qu'on le lit.

## 5. Rythme et montage
- **45 à 75 s** ; chaque étape dure **2 à 7 s**. Rien d'immobile plus d'1 s (hors tenues de lecture) ; du nouveau toutes les 2 à 4 s.
- **Structure** : problème (3 à 5 s) → étape 1 → étape 2 → … (4 à 7 étapes) → résultat mesurable → prix → appel à l'action.
- **Muet d'abord** : la version de page d'accueil se lit sans le son ; c'est la typographie cinétique qui porte le message. On fait la **version muette en premier**, la voix ensuite si elle est demandée.
- **Brief de réalisateur avant tout code** : durée, format maître, déclinaisons, promesse en une ligne, public, canal, **un style de référence nommé** (jamais « moderne et premium »), états horodatés, liste des calques, plan sonore ; puis arrêt pour validation.
- **Quatre images fixes validées** avant le rendu complet.
- Test « une phrase » : si quelqu'un qui regarde le film sans le son le résume en une phrase, ça marche.
- **Version courte (8 à 12 s)** : le problème (2 s), deux étapes reliées par un passage d'objet (3 s chacune), le résultat mesurable tenu 2 s ; couper le prix et les autres étapes.

## 6. Recette technique
- **Moteur** : HyperFrames + GSAP.
- **Du produit aux jetons** : découper chaque capture en tuiles agrandies, relever couleurs (pixel par pixel), polices, rayons, ombres, bordures, espacements ; écrire le fichier unique ; reconstruire les composants en HTML/CSS.
```css
:root { /* jetons-interface : relevés sur les captures du client, jamais choisis à l'œil */
  --fond: #F6F7F9; --surface: #FFFFFF; --bordure: #E3E6EB; --texte: #14171C; --texte-2: #6B7380;
  --accent: #2E6BFF; --rayon-carte: 12px; --rayon-bouton: 8px; --ombre-carte: 0 1px 2px rgba(16,24,40,.06);
  --police: "Inter", sans-serif; --pas: 8px; }
```
- **Textes dans un dictionnaire dès le premier jour** (aucun texte codé en dur) : une clé par libellé, une colonne par langue. Le français reprend **exactement** les libellés des captures.
```js
const TEXTES = { fr: {titre1: "Tes relances partent toutes seules", bouton: "Lancer"},
                 en: {titre1: "Follow-ups that send themselves", bouton: "Run"} };
document.querySelectorAll("[data-t]").forEach(el => el.textContent = TEXTES[LANGUE][el.dataset.t]);
```
- **Passage d'objet** : l'élément garde son identité ; on anime sa position, sa taille et son rayon de l'emplacement A à l'emplacement B pendant que la caméra suit.
- **Chiffres** : un fichier de faits obligatoire (chaque chiffre avec source et date) ; sinon aucun chiffre réel à l'écran, et les données illustratives portent « données d'exemple ».
- **Contrôles** : planche à 2 images par seconde ; bande de 12 images autour de chaque mouvement rapide ; planche « téléphone » à 360 px de large ; recherche d'image-éclair isolée.
- **Revue notée par un relecteur séparé** (celui du skill `studio-coeur`) : accroche des 2 premières secondes, lisibilité à 360 px, qualité du mouvement, variété, composition, exactitude de la marque et des données, synchro du son ; les 3 pires défauts avec leur horodatage ; ne re-rendre que les secondes touchées. **Une nouvelle version ne remplace l'ancienne que si un juge la trouve meilleure en comparaison côte à côte** ; tenir un journal des versions.
- **Caméra et curseur** : `references/camera-et-curseur.md`. **Étalonnage** : `references/etalonnage.md`.
- **Pièges** : écran « presque » fidèle (le client voit tout de suite la différence : comparer côte à côte) ; titre sur deux lignes ; texte codé en dur qui bloque la seconde langue ; plusieurs rendus lourds en même temps sur la machine du client (un seul à la fois).

## 7. Son
- Version muette d'abord ; puis musique discrète calée sur les passages d'étape, le grand moment (le résultat) sur le temps fort du morceau. Voir `references/son-et-mastering.md` §7.
- Bruitages d'interface rares et précis (budget du skill `son`, vrais enregistrements d'abord) : clic, validation, arrivée de carte ; chacun placé à son pic.
- Voix éventuelle : baisser la musique d'environ 9 dB sous elle. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Chaque étape produit visiblement ce que la suivante utilise ; aucune coupe franche entre étapes.
- [ ] Chaque écran reconstruit a été comparé côte à côte à sa capture et se reconnaît au premier coup d'œil.
- [ ] Un seul fichier de jetons ; aucune couleur ni rayon hors du fichier.
- [ ] Une seule entreprise fictive partout ; aucun vrai client, concurrent ou personne ; aucun visage généré.
- [ ] Le film se comprend sans le son (résumé en une phrase par quelqu'un qui ne connaît pas le produit).
- [ ] Chaque titre tient sur une ligne ; chaque élément reste lisible ≥ 1,5 s.
- [ ] Aucun chiffre sans source ; « données d'exemple » écrit quand c'est le cas.
- [ ] Marges de 80 px et zones d'interface respectées ; lisible à 360 px de large.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Le seul aperçu du dépôt d'origine est le film de lancement de la marque de son auteur : on ne le reprend pas. Aperçu Flot Web à produire.

## 10. Origine
- Dépôt : howseen-ai/claude-motion-design, commit `3d90d34`. Fichier : `skill/motion-design/SKILL.md`, §11 « Product film mode », avec les règles des §8, §9b et §9c (brief de réalisateur, anti-« motion IA », revue notée).
- Licence : MIT (© 2026 Howseen AI, Raphaël Aubry).
- Adaptations Flot Web : français, HyperFrames, relecteur du skill `studio-coeur`. **Écartés** : mèmes téléchargés, visages générés, photos de remplissage, chemins et conventions personnels de l'auteur, fichiers de banques de sons embarqués.
