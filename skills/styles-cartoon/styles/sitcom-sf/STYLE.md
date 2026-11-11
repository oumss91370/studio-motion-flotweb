# Sitcom SF (série animée pour adultes)

## 1. Identité

- **Nom** : Sitcom SF. Pour se comprendre avec le client : « style série animée de science-fiction pour adultes ».
- **Inspiration** : les sitcoms animées de science-fiction pour adultes des chaînes câblées : comédie de dialogue, gros plans de réaction, trait qui frémit, matériel futuriste traité comme de la ferraille de garage. On emprunte la grammaire, jamais les personnages.
- **Ce que c'est** : animation télé 2D d'aspect dessiné à la main : **gros contours sombres uniformes qui frémissent**, **aplats avec ombres à bord dur** (aucun dégradé), **grands yeux blancs à pupilles minuscules**, **bouches élastiques**, créatures dégoûtantes mais mignonnes. Le moteur comique : **un but minuscule et banal poursuivi avec des moyens de science-fiction démesurés**, et quelqu'un d'autre en paie le prix.
- **Marche pour** : comparer des versions d'un produit, prototypes ratés, duo expert / débutant, IA et son utilisateur, « et si… » en plusieurs mondes, pub à chute.
- **Ne marche pas pour** : public enfant (humour sec, longs silences), sujet solennel, explication sans personnages, vidéo sans voix (c'est un style de dialogue).
- **Lignes rouges (non négociables)** : ne jamais reproduire les personnages, silhouettes ou combinaisons de couleurs d'une série existante (par exemple un vieil homme à cheveux bleus hérissés en blouse blanche avec un enfant en t-shirt jaune), ni ses noms, répliques, gags de rot, logos, ni l'allure d'un pistolet à portails connu. Évite aussi le trio « vert acide + coulures gluantes + lettrage en bulles tremblées ». Invente ta distribution et ton appareil.

## 2. Palette, typographie, matières

- **Trait** : presque noir légèrement violacé `#1B1422`, 7 px pour personnages et objets, 4 à 6 px pour le détail des décors, jonctions rondes. Le trait et le blanc des yeux ne changent jamais d'un monde à l'autre.
- **Une palette par monde**, 3 à 5 couleurs, aussi différente que possible de la précédente en teinte **et** en valeur : le public lit « on a sauté » à la couleur seule.

| Monde (exemples de la démo) | Couleurs |
|---|---|
| Labo de départ | vert sauge `#A7C3B1`, sol olive, bois chaud, un accent orange |
| Monde gelée | bandes de ciel magenta `#FF4F9A` → `#FF9BCB`, gelée citron vert `#B8F03C`, cyan `#52E0E0` |
| Monde orange | ciel `#FF7A2F` → `#FFB862`, collines sarcelle `#2B9C98`, crème |
| Monde rouge | `#C3122F`, rose gencive `#FF8FA6`, blanc |
| Monde « normal » | beige `#F1E3C6` et brun, volontairement fade (c'est le gag) |

- **La lueur appartient à l'appareil de voyage** (portail ou autre) : rien d'autre ne brille, dans aucun monde. Choisis une couleur de lueur qui n'est pas le vert de la série la plus connue du genre.
- **Typographie** (OFL) : sous-titres en **Baloo 2 ExtraBold**, blanc avec contour noir ≈ 11 px ; titre en lettrage massif (**Titan One** ou **Bungee**) ; étiquette de monde en **VT323**, tapée lettre à lettre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Baloo 2 ; Archivo Black à la place de Titan One et de Bungee ; Space Mono à la place de VT323. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/baloo-2`, `@fontsource/titan-one`, `@fontsource/bungee`, `@fontsource/vt323` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Variante « trait fin »** (issue de la carte huashu) : contour gris anthracite `#222323` de 2,4 px (détails 1,6 à 2,6 px), aplats à bord dur, mur gris chaud `#CDBF96`, bois `#9B7752`, peau `#EFC4A0`, ciel `#A7D6EA`, sans frémissement. À choisir pour une scène calme à un seul lieu ; le reste de la fiche s'applique.
- **Matières** : aucune texture. Les ciels sont des **bandes de couleur plates**. Les lueurs sont 1 ou 2 anneaux translucides plats, pas des dégradés. Nourriture et liquides ont besoin d'indices (reflet, gouttes, vapeur) sinon ils se lisent comme autre chose.

## 3. Composition 9:16

- Le plan de base horizontal est le plan moyen à deux. En vertical : **les deux personnages l'un au-dessus de l'autre en diagonale** (le pince-sans-rire en bas à gauche, le paniqué en haut à droite), ou un seul visage par plan avec des coupes sèches de l'un à l'autre.
- Gros plan de réaction : visage sur toute la largeur utile (x 60 à 945), yeux vers y 700.
- Le portail est un ovale vertical (largeur ≈ 0,74 × hauteur) : il remplit naturellement le cadre 9:16, centré vers y 800.
- Sous-titres 54 à 60 px, deux lignes maximum, centrés vers y 1440, avec une petite **pastille du nom** à la couleur du personnage (contour qui frémit). Visages hors de la bande y > 1350. Étiquette de monde en haut à gauche sous y 160.
- 16:9 : plan moyen à deux classique ; sous-titres à 50 px, visages hors des 170 px du bas.

## 4. Ce qui bouge

- **Action principale** : un dialogue à deux où chaque image absurde est suivie d'un gros plan de réaction.
- **Boucle de fond 1** : **tout frémit**, y compris les poses tenues et les décors (3 dessins en cycle, amplitude ≈ 1,7 px). Une image fixe n'est jamais morte.
- **Boucle de fond 2** : vie au repos (respiration ±1 %, hochement piloté par le volume de la voix), spirale du portail qui tourne à pleine cadence.
- **Autorisés** : `#136` trait qui frémit, `#121` anticipation avant chaque geste, `#011` écrasement à l'atterrissage (≈ 22 %, amorti), `#010` dépassement doux à l'ouverture du portail (≈ 12 %, 0,3 s), `#043` panoramique filé entre deux visages, `#046` coupe sèche, `#020` zoom à travers le portail, `#024` secousse courte sur un mot, `#027` avancée très lente sur un silence, `#180` par-dessus l'épaule vers un écran.
- **Interdits** : `#044` fondu enchaîné, tout dégradé, `#015` particules génériques, `#022` balayage de lumière, yeux brillants façon animé.
- Jouer plutôt que bouger : poses tenues avec de petits changements (œil qui tressaute, pupilles qui glissent, déglutition, goutte de sueur). Tremblement nerveux : décalage aléatoire à graine de 3 à 6 px par dessin, qui grandit avec la panique.
- Dans une pause froide, **rien ne bouge sauf le frémissement**.

## 5. Rythme et montage

- Transitions : coupe sèche, ou volet en spirale à travers l'appareil de voyage. Aucun fondu.
- **Règle de trois qui devient mitraillette** : deux mauvaises réponses lentes, puis des mondes d'une seconde coupés sur le temps avec le même mot de refus.
- **Le silence est la chute** : coupe la musique net (queues de réverbération comprises) sur une révélation, garde seulement le bruit de pièce.
- Sous-titres : en dialogue rapide, durée ≥ max(voix + 0,35 s ; 0,9 s + caractères ÷ 17). Coupe-les avant un temps de silence : le silence se joue sur un écran propre.
- Même cadrage répété d'un monde à l'autre : seule la couleur change.
- **Version courte (8 à 12 s)** : garder deux mondes (une mauvaise réponse, puis la chute) et un gros plan de réaction ; couper la « mitraillette » de mondes et le dialogue d'installation. Accroche avant 3 s : le premier saut de monde (la palette change d'un coup).

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `toon.js` (pile de matrices, trait constant, frémissement en espace écran, ombrage plat), `persos.js` (yeux, bouches, mains paramétriques, membres souples), `mondes.js` (une fonction par monde, créatures, portail), `levres.js` (enveloppes de la voix).
- **Techniques clés** :
  ```js
  // frémissement : rééchantillonner le contour à l'écran (pas ≈ 7 px),
  // déplacer chaque point le long de la normale avec un bruit lent à graine
  const boil = Math.floor(tq * 15) % 3;          // 3 dessins en cycle
  p.x += nx * bruit(i * 0.35, boil) * 1.7;
  ```
  - Synchro des lèvres depuis l'audio : par réplique, volume (ouverture) et centre spectral (large ou rond), lus au temps du dessin. Exagérer pour un cri (bouche ×1,5 à 1,9).
  - Portail : bord bosselé à gros contour, bras en spirale, cœur pâle, étincelles en orbite, gouttes ; voile translucide plat sur la scène tant qu'il est ouvert.
  - Bouche paramétrique : ouverture, largeur, courbure, biais ; intérieur, dents, langue.
- **Pièges** : un rebond trop élastique du portail avale les acteurs ; la voix de synthèse lit les bégaiements écrits avec des tirets comme des mots (écris les syllabes) ; pour une vraie interruption, génère la réplique plus longue et coupe l'audio là où l'autre voix entre ; ce qui est derrière un meuble doit encore montrer visage et buste ; les silhouettes doivent se lire en noir plein.

## 7. Son

- **Musique** : synthétique : thème au son de thérémine (glissé entre les notes, vibrato qui arrive après l'attaque), basse analogique, arpège en onde carrée, boîte à rythmes rétro. Un **genre par monde** : guitare surf, accordéon polka, berceuse au piano jouet, bossa d'ascenseur, tuba et sifflet à coulisse.
- **Bruitages** (≈ 5 par 10 s) : ouverture du portail (grave + souffle descendant), « fwoump » de fermeture, pop, « glorp » mouillé, bip de clignement, jouet qui couine.
- **Voix** : deux voix contrastées : grave, plate et lente pour le pince-sans-rire ; plus aiguë et rapide pour le nerveux. La créature ne parle pas (bruitages) ou dit un ou deux mots. Musique baissée d'environ 7 dB sous le dialogue. −14 LUFS.
- **Bruit de pièce** dans les silences : néon qui bourdonne, tic-tac, frigo.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : dégradés, yeux brillants, trait figé, plan large sans réaction, musique qui continue pendant la chute, distribution qui rappelle une série existante.

- [ ] Tous les contours frémissent, même sur les poses tenues et les décors.
- [ ] Épaisseur de trait identique en plan large et en gros plan.
- [ ] Une palette par monde, nettement différente de la précédente en teinte et en valeur.
- [ ] Seul l'appareil de voyage émet de la lueur.
- [ ] Chaque image absurde est suivie d'un gros plan de réaction.
- [ ] Au moins un vrai silence (musique coupée net) sur la chute.
- [ ] Les deux silhouettes principales se reconnaissent en noir plein.
- [ ] Aucun personnage, costume, couleur d'appareil ou lettrage rappelant une série existante.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 18
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *Coffee Run* (58 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/scifi-toon.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/scifi-toon.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.
- Variante trait fin : pas d'aperçu isolé dans le dépôt huashu.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/scifi-toon/STYLE.md`, `DEMO.md`, `demo/toon.js`, `chars.js`, `worlds.js`, `voice.py`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : Baloo 2, Titan One, Bungee, VT323 (SIL OFL 1.1).
- **alchaincyf/huashu-art-motion**, commit `1468196` : `references/风格配方/37_rick_morty.md` (variante trait fin : valeurs de trait et de couleurs, découpage du personnage en groupes, queue construite depuis une ligne centrale). Licence MIT, © 花叔 Huashu. Carte notée ★★ par son auteur ; son exemple en SVG n'est pas repris.
- Adaptation Flot Web : fusion des deux sources, nom descriptif, section 9:16, numéros du dictionnaire.
