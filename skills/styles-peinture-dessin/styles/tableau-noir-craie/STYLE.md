# Tableau noir à la craie

## 1. Identité

- **Nom** : Tableau noir à la craie (« Chalkboard »).
- **Inspiration** : une leçon d'école primaire sur un tableau coulissant à deux panneaux ; la façon dont un professeur souligne les parties d'un mot, entoure un élément et efface une ligne fausse. On prend l'ordre d'une leçon, pas l'écriture d'un professeur.
- **Ce que c'est** : un vrai tableau de classe sur lequel **la craie écrit seule**, trait par trait, dans le bon ordre, **sans main, sans bâton de craie, sans brosse à l'image**. Une ardoise **propre, fraîchement essuyée** : un vert encre profond et régulier, avec son grain fin. **Trois craies au plus.** Un vrai objet dans une vraie pièce : cadre en bois, rigole avec des craies, panneaux coulissants, mur, horloge. **Peu de mots, de grandes lettres** : le tableau porte les mots-clés, l'explication est dite.
- **Geste central** : écrire ce que les gens croient, l'effacer d'un seul passage, écrire le vrai **au même endroit**.
- **Marche pour** : une idée reçue corrigée, l'origine d'un mot, un problème résolu pas à pas, une règle de grammaire ou de calcul, une leçon courte.
- **Ne marche pas pour** : plusieurs idées reliées (prends `tableau-blanc`), un sujet sans voix, de l'émotion, un produit.
- **À ne pas confondre** : le tableau blanc est clair, brillant, avec des feutres qui flottent, des aimants, des fantômes et une caméra qui voyage sur une carte d'idées. Ici : ardoise sombre et mate, rien qui flotte devant, une question par tableau, caméra bien de face. Ce n'est pas une diapositive non plus : rien n'est typographié, rien n'apparaît en fondu.

## 2. Palette, typographie, matières

| Rôle | Hex (exemple) |
|---|---|
| Ardoise | `#1f3a33` (vert encre), mouchetée très lentement |
| Craie blanche : toute la structure (mots, lignes, étiquettes, flèches) | `#f1efe6` |
| Craie d'accent : **le seul** élément que la leçon suit | `#e8a14a` |
| Craie pâle : l'écriture d'une autre personne (un élève) | `#efe08a` |
| Cadre bois, mur blanc chaud, soubassement coloré | `#8a623a` · `#efe9dc` · `#6f8f7a` |

- L'accent ne décore jamais et ne trace ni flèche ni soulignement qui ne soit pas l'élément suivi. Ni arc-en-ciel, ni dégradé, ni lueur. Les lignes peintes sur le tableau (quadrillage, lignes d'écriture) sont ternes et fines : la craie gagne toujours.
- **Typographie** : au tableau, une **écriture monoligne** (police OFL à trait unique, par exemple la famille EMS) dessinée par le moteur de craie ; flèches et signes absents de la police dessinés comme des traits. Plaque de sous-titres : une serif sobre libre (par exemple Lora ou Source Serif).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Source Serif. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/source-serif-4` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La famille EMS (trait unique) n'a pas de paquet `@fontsource` : à vérifier ; à défaut, tracer les lettres par le moteur de trait.
- **Matières** : chaque trait est calculé une fois (couverture, longueur parcourue, position latérale) ; un trait partiel révèle les pixels jusqu'à la longueur courante, avec un front arrondi ; **le grain de l'ardoise décide quels grains prennent la craie**. Bords de craie fermes ; poussière seulement au décollage d'un trait (2 à 5 grains). Profil de largeur par type de trait (appui au départ et aux angles, pointe qui se lève) et pression plus forte aux deux bouts ; les traits droits se cambrent un peu ; les horizontales montent de 2 à 3° vers la droite.
- **Effacement** : une bande floue le long d'un seul trajet lisse, sur un calque qui ne contient que les traits à effacer ; elle laisse un voile très fin et régulier. **Un effacement par vidéo suffit.**
- **Trace humide** (tableau essuyé à l'éponge) : un masque doux qui assombrit légèrement l'ardoise, avec un bord qui sèche en flou large ; jamais de bord net.
- **Lumière** : douce baisse en s'éloignant des fenêtres, au plus une tache chaude ; elle ne dessine jamais de forme sur l'écriture en plan rapproché.

## 3. Composition 9:16

- La caméra est **toujours de face**, sans inclinaison de perspective. Un panneau vertical convient : la question en haut, l'objet au milieu, la réponse en bas.
- **Tailles en 1080 de large** : grands mots 220 à 380 px de haut ; étiquettes ≥ 48 px ; la petite écriture reçoit une craie plus épaisse, **aucun trait sous 3 px**.
- **Plaque de sous-titres** discrète au-dessus de la zone d'interface : plaque sombre douce, texte clair, une ligne (deux au plus), vers y ≈ 1400 à 1520. **Rien à lire au tableau derrière la plaque** : compose les plans au-dessus de y = 1340.
- En plan rapproché, le sujet n'est jamais plus petit qu'un tiers du cadre ; un bloc de texte n'est jamais coupé par le bord pendant qu'on le lit ; **jamais de tableau vide plus d'une demi-seconde**.
- **La pièce fait partie du style** : au moins une fois, le cadre s'ouvre assez pour lire tableau, cadre en bois, rigole et mur comme une salle de classe. En vertical : recule jusqu'à voir la rigole en bas et l'horloge ou le haut du cadre.
- 16:9 : deux panneaux côte à côte, plan large du mur entier en conclusion.

## 4. Ce qui bouge

- **Action principale** : la craie qui écrit. Un grand mot ≈ 0,1 s par trait, espaces compris ; une étiquette ≈ 0,04 s par trait. En dessous de ≈ 0,07 s par trait, un grand mot ne ressemble plus à une main.
- **Boucle de fond 1** : la poussière au décollage des traits et la trace humide qui sèche lentement.
- **Boucle de fond 2** : la pièce (aiguille de l'horloge, tache de lumière qui glisse à peine).
- **Gestes natifs** : écrire, effacer, réécrire au même endroit (même cadrage) ; l'élément suivi en craie d'accent, qui garde sa couleur et sa hauteur d'une forme à l'autre ; **le panneau qui coulisse** et révèle un tableau propre derrière ; une ligne qui coud deux panneaux ; la trace humide qui révèle ce qui n'a pas été touché ; la seconde main (un élève) ; la craie comme outil de mesure.
- **Autorisés** : `#004` tracé de ligne, `#175` plan fixe, `#025` panoramique latéral lent le long d'une ligne, `#028` recul vers un plan moyen fixe, `#043` panoramique filé (≤ 0,5 s) vers un autre panneau, `#041` même cadre plus tard (jugement), `#046` coupe franche, `#080` soulignement.
- **Interdits** : `#044` fondu, `#140` page tournée, `#001` apparition en rebond, `#022` balayage de lumière, lueur, poussière qui flotte, vieux gribouillis sur l'ardoise, main ou craie visible. Les choses n'apparaissent **que** par écriture, effacement, panneau qui coulisse ou séchage.
- Caméra : accélérations et décélérations douces, jamais de rebond sauf à l'arrivée d'un panoramique filé.

## 5. Rythme et montage

- 30 i/s, continu. La durée suit le nombre d'étapes de la leçon (30 à 50 s en général).
- **Temps de lecture** : chaque bloc reste entièrement dans le cadre au moins (nombre de caractères ÷ 15 + 1,5) s après avoir été complètement écrit.
- Quand temps de lecture et vitesse de craie se gênent, **change les mots, pas la main** : moins de blocs, plus courts ; grands mots seulement pour ce que la leçon suit ; commence un bloc pendant que la voix finit la phrase d'avant ; tiens le cadre.
- Pauses entre deux phrases : 0,25 à 0,4 s ; **une** tenue plus longue (≈ 1,5 s) pour le verdict. L'action du tableau (panneau, effacement) se déroule sous la voix.
- Transitions : coupe franche, panneau qui coulisse, ligne qui traverse la jointure.
- **Version courte (8 à 12 s)** : une seule étape de la leçon : une phrase écrite, un schéma, le verdict tenu 1,5 s.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour tout le visible, WebGL seulement pour la passe finale (flou de mouvement de caméra, léger vignettage, étalonnage).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `craie.js` (trait, pré-calcul, révélation partielle), `main.js` (écrire un mot, une ligne ; renvoie l'instant où finit le dernier trait), `grain.js` (tuile de grain, dépôt), `salle.js` (ardoises, cadre, rigole, horloge, mur, lignes peintes), `film.js` (chaque trait, temps, cadrage, début de voix et sous-titre, **comme des données**).
- **Techniques clés** :
  ```js
  // révélation d'un trait : pixels dont la longueur parcourue <= s(t), front arrondi
  const s = longueur * clamp((t - t0) / (t1 - t0), 0, 1);
  // le grain décide du dépôt : la craie n'accroche que les sommets
  const depot = couverture * step(seuil - pression, grain);
  // effacement : bande floue en "destination-out" sur le calque des seuls traits effacés
  ```
  - Calques : panneau avant (qui coulisse), panneau de droite, tableau du fond (dessiné seulement quand le panneau a bougé).
  - Déclare chaque bloc de texte avec sa boîte et sa fenêtre de temps pour le contrôle de lecture.
- **Pièges** :
  - Tableau sale (vieux tourbillons, fantômes, poussière) = « négligé », pas « réel » : garde l'ardoise propre, le grain porte le réalisme.
  - Traits d'épaisseur constante = traceur de plans : profils de largeur et de pression.
  - Petite écriture avec la même craie que la grande : elle disparaît.
  - Texte écrit pendant que la caméra s'éloigne : temps de lecture manqué.
  - Un halo doux au front de la craie se lit comme une lueur : garde les grains, pas le dégradé.
  - Trace humide à bord net = découpage.
  - Voix qui épelle des noms d'éléments sans dire ce qu'ils veulent dire : incompréhensible.

## 7. Son

- **La voix d'abord** : c'est l'élément le plus fort ; la musique est 15 à 18 dB en dessous et ne remonte que dans les pauses. Une voix calme de professeur, phrases courtes, dites pendant que la craie correspondante apparaît.
- **Bruitages** : de **vrais enregistrements de craie** découpés en grains, une chaîne de grains par trait, niveau selon la taille du trait ; léger choc à l'atterrissage ; la craie d'accent un peu plus douce et sourde. Un passage de feutrine pour l'effacement, le roulement grave d'un panneau qui coulisse et sa butée, ton de salle très bas ; une cloche d'école lointaine seulement comme ponctuation. L'écriture est une texture continue ; le budget (≈ 5 par 10 s) sert à l'effacement, au panneau, à la cloche, au verdict.
- **Musique** : cordes pincées rares (guitare nylon), marimba, contrebasse en pizzicato ; une note peut « naître » d'un élément dessiné. Silence pendant qu'on lit une question ou un verdict.
- Mix final −14 LUFS, crête ≤ −1,5 dB.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : ardoise sale ; craie qui brille ; plus de trois craies ; accent partout ; texte qui apparaît en fondu ; tableau vide ; trop de mots.

- [ ] Ardoise propre : un seul vert, du grain, aucun ancien tracé.
- [ ] Trois craies au plus ; l'accent ne touche que l'élément suivi.
- [ ] Chaque trait a un départ appuyé et une fin qui se lève ; aucun trait sous 3 px.
- [ ] Rien n'apparaît autrement que par écriture, effacement, panneau ou séchage.
- [ ] Au moins un « écrire, effacer, réécrire au même endroit », même cadrage.
- [ ] Chaque bloc est lu en entier dans le cadre (caractères ÷ 15 + 1,5 s).
- [ ] La salle de classe est visible au moins une fois.
- [ ] Rien à lire derrière la plaque de sous-titres ni sous y = 1560.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Film de démo d'origine (49 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/chalkboard.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/chalkboard.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 pour l'image. **La piste de voix de ce film est exclue de la licence** (voix d'un service en ligne) : ne pas le rediffuser avec son son ; montrer l'affiche, le film muet, ou renvoyer vers la galerie officielle.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/chalkboard/STYLE.md`, `DEMO.md`, `demo/js/chalk.js`, `hand.js`, `r2d.js`, `stage.js`, `post.js`, `app.js`, `tools/foley_lib.py`. Licence MIT, © 2026 LemoLab ; image du film CC BY 4.0, voix exclue.
- Adaptation Flot Web : traduction ; la démo enseigne des caractères chinois avec des données de traits écrites à la main : cette partie (ordre des traits des caractères, sous-titres bilingues) n'est pas reprise, la fiche vise l'écriture latine. Mise en page verticale, mix ramené à −14 LUFS.
