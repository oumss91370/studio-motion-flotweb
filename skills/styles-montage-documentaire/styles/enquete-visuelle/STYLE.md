# Enquête visuelle

## 1. Identité
- **Nom** : Enquête visuelle. Identifiant : `enquete-visuelle`.
- **Inspiration** : les enquêtes vidéo des grands journaux, les reconstitutions d'architecture d'investigation, les cellules de vérification des télévisions. Grammaire seulement : jamais leur nom, leur habillage ou leurs plans.
- **Principe** : un bureau d'enquête froid. Vidéos, photos, documents, sons et cartes d'**un événement réel** sont posés sur **une seule horloge** pour se recouper. L'horloge vit dans l'image (heure sur chaque pièce, curseur sur un graphique, chronomètre `T+xx,x` sur les secondes décisives). On fige, on entoure, on agrandit ; on surligne la citation sur la page d'où elle vient ; un plan montre où étaient les caméras ; ce qui est su et ce qui ne l'est pas restent séparés ; à la fin, toutes les preuves convergent sur une carte.
- **Règle d'or** : la récompense de chaque partie est que deux sources indépendantes ou plus désignent le même endroit ou la même seconde. Les points de coupe sont des points de synchronisation.
- **Pour quels sujets** : reconstitution d'un incident, vérification d'une affirmation, litige sportif (plusieurs angles + règlement), panne ou échec technique (caméras, mesures, rapport), accident de la route (caméras embarquées, procès-verbal).
- **Ne marche pas pour** : un sujet sans au moins trois types de sources réelles, une opinion, un sujet léger. Retenue obligatoire : pas de ralenti de la catastrophe, pas de musique qui dicte l'émotion, victimes en points comptés et en chiffres.

## 2. Palette, typographie, matières
| Rôle | Valeur |
|---|---|
| Fond | `#0B0C0E` |
| Panneaux | `#141619` |
| Filets, cadres | `#2E3238` |
| Texte / texte secondaire | `#ECEAE4` / `#8B9097` |
| Graduations, « incertain » | `#4A4F57` |
| **Seul accent : ici / maintenant / concordance** | `#FF4A2E` |
| Cartes papier (messages recomposés) | `#E4E0D4`, encre `#1D1D1B` |

Les sources sont en niveaux de gris ; le rouge ne fait que **désigner** : cercles, curseur, lignes de synchronisation, surlignages, coches, zone de convergence, colonne « non résolu », rature d'une affirmation fausse.
- **Polices libres** : titres et constats en sans gras ; étiquettes, codes de temps et graduations en IBM Plex Mono ; citations en Source Serif 4 Italic.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Source Serif 4 ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/source-serif-4` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Étalonnage unique** : images et photos `grayscale(1) contrast(1.22) brightness(0.94)` ; papier `grayscale(1) contrast(1.05) brightness(0.86)` ; cartes en gris, inversées, `brightness(.62)`. Grain seulement sur les sources (0,22 sur images, 0,10 sur papier), jamais sur la typo ni les traits.
- Les dessins de preuve (plan, schéma, graphiques, matrice de points) sont en trait fin et marqués « schématique » s'ils ne sont pas mesurés.

## 3. Composition 9:16
- Marges 60 px ; contenu entre y 170 et y 1250 ; sous-titres entre y 1300 et y 1540 ; rien d'important au-dessus de y 160, sous y 1560, à droite de x 945. Aucune bande n'est réservée à une frise de temps (elle resterait vide).
- **Panneaux à bords durs**, cadre 1 px, empilés verticalement ; un panneau vidéo garde le format de sa source.
- Mises en page types en vertical : **carte puis plan** en haut, photo de référence et vidéo dessous ; **une grande affirmation + une citation + un schéma large** ; **tableau à trois sources** empilées sous un seul chronomètre, chaque étage s'allumant quand sa source commence ; **bande de document + verdict en deux blocs** ; **carte des preuves** finale.
- **Peu de mots par image** : le relevé de temps ou le titre, la citation surlignée, une étiquette de source par pièce (pastille + `type · source`, ≤ 12 caractères, 28 px minimum, juste au-dessus du cadre). Pas de double libellé, pas de numéro d'archive, pas de note de bas d'image.
- Constat : 60 à 110 px. Chronomètre : 110 à 140 px.
- **16:9** : contenu y 60 à 900, sous-titres y ≈ 950 à 1030, tableau à cinq sources (trois cadres en haut, son et rapport en bas, schéma à droite).

## 4. Ce qui bouge
- **Action principale** : « figer, entourer, agrandir ». Arrêt sur image avec flash blanc ; cercle rouge de 2,5 px tracé dans le sens horaire en 0,5 s ; à 60 % du tracé, un trait de rappel et un libellé gras ; une loupe ×2 s'ouvre à côté, recadrée dans les mêmes pixels (jamais au-delà d'1 pixel source par pixel écran).
- **Boucles de fond** : (1) l'horloge de l'événement (curseur du graphique, chronomètre) qui avance à vitesse constante, un tic = une vraie seconde ; (2) poussée lente à l'intérieur d'un cadre (≤ 1,06× sur une photo, ≤ 1,9× sur une carte).
- Les éléments **apparaissent par coupe** (≤ 0,1 s d'opacité) avec un flash blanc de 3 à 4 images, comme sortis du coffre à preuves. Seul ce qui est *dessiné* est progressif : cercles, traits de liaison (0,4 à 0,8 s), plans trait par trait, surlignages, machine à écrire pour les messages.
- **Autorisés** : #040 arrêt sur image, #004 tracé de ligne, #080 surligneur, #006 machine à écrire (messages datés seulement), #164 chronomètre, #144 écran partagé, #046 coupe sèche, #163 points d'intérêt, rembobinage en ouverture.
- **Interdits** : tout ce qui vole, rebondit ou grossit en « pop » (#001, #010, #123), #044 fondu, #140 page qui tourne, #037 ralenti sur le drame, mouvement de la « caméra » elle-même (les mises en page changent par coupe).

## 5. Rythme et montage
- Coupes sèches sur une grille de 0,5 s, flashs blancs (2 par seconde au plus sur cette grille, jamais plus de 3 : au-delà, c'est un clignotement en plein cadre), rembobinage. Quelque chose change au moins chaque seconde ; les tenues sont réservées aux verdicts (≥ 2,5 s, chaque élément entièrement visible).
- **Un constat par mise en page.** Cinq sources au plus sur un tableau.
- **L'échelle de temps change aux coupes de partie** (heures → minutes → secondes → jours), portée par le relevé qui change de forme (heure → chronomètre → date).
- Trois structures : ouverture à froid sur l'image décisive figée, puis rembobinage et reconstruction ; une question (« où cela a-t-il commencé ? ») résolue source après source ; une horloge stricte où les constats tombent là où ils arrivent.
- Temps de lecture : chaque texte clé reste immobile et entier (lettres ÷ 15 + 1,5) s ; les compteurs en sont dispensés.
- **Version courte (8 à 12 s)** : une seule preuve : figer, entourer, agrandir (4 s), puis le constat tenu 2 s ; couper les changements d'échelle de temps.

## 6. Recette technique
- **Moteur** : HyperFrames. Panneaux en HTML/CSS absolu, vidéos en `<video class="clip">`, cercles et liaisons en SVG animés par `stroke-dashoffset`, loupe = second `<canvas>` ou second élément vidéo recadré de la même source.
```js
tl.set(cadre, {opacity: 1}, T).fromTo(flash, {opacity: .8}, {opacity: 0, duration: 0.12}, T);
tl.fromTo(cercle, {strokeDashoffset: L}, {strokeDashoffset: 0, duration: 0.5, ease: "power3.out"}, T + 0.1);
tl.set([rappel, libelle], {opacity: 1}, T + 0.4);       // à 60 % du tracé
```
- **Point de synchronisation dur** : choisir un instant que chaque source reconnaît (impact, flash, horloge publique, pic sonore) et y aligner chaque source. Une source qui commence tard apparaît tard dans sa colonne ; jamais de boîte grise « pas d'image » (elle ressemble à un rendu cassé).
- **Chaîne archive** (film ancien, ≤ 2,5×) : désentrelacer `bwdif=0` → recadrer → `hqdn3d=2:2:3:3` → `lanczos` → `unsharp=5:5:0.5` → gris. Image récente ≤ 1,5×.
- **Documents** : la page scannée est montrée telle quelle, seule la ligne décisive est surlignée (rouge, `multiply`, opacité ≈ 0,6, de gauche à droite). Un texte qui n'existe qu'en transcription est recomposé et **étiqueté « transcription »**.
- **Son d'origine** montré comme une forme d'onde avec un trait de lecture rouge et les mots qui s'allument un à un.
- **Pièges** : fuseaux et heure d'été (en choisir un, l'écrire une fois sur le premier relevé) ; raccords cachés dans un plan « continu » (prendre les durées dans le rapport officiel et dire la marge d'erreur) ; le sous-titre ne répète jamais le titre mot pour mot.

## 7. Son
- **Lit** : note grave tenue (contrebasses), bruit de pièce très bas.
- **Mécanique** : tic de pendule toutes les 0,5 s dans les parties à l'échelle de la minute ; dans un passage chronométré, un tic par seconde d'événement (accent toutes les 5).
- **Bruitages** (budget du skill `son`) : papier pour un document, obturateur pour une photo, frappes pour un message, balayage de rembobinage, **un seul** coup sourd à l'instant de l'impact, puis presque silence. Aucun bruitage sur les morts.
- **Son d'origine** (commentaire d'époque, radio) : passe-bande 180 Hz à 5,5 kHz ; il alterne avec la musique, jamais les deux forts.
- **Voix** calme et plate ; musique 9 dB dessous. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Au moins trois types de sources réelles ; aucune image générée pour remplacer une image d'époque.
- [ ] Chaque partie se termine sur une concordance entre au moins deux sources.
- [ ] Toute position de caméra, heure de photo ou décalage estimé porte `≈`, « déduit » ou « non localisé » à l'écran et dans `FAITS.md` (affirmation → adresse → phrase citée, déductions listées à part).
- [ ] Les premiers rapports et les actualités d'époque servent d'images ou d'affirmations à vérifier, jamais de source d'un chiffre.
- [ ] Le rouge ne sert qu'à désigner ; aucune autre couleur.
- [ ] Pas de panneau vide, pas de bande basse réservée.
- [ ] Verdict et tableau « su / non résolu » tenus ≥ 2,5 s.
- [ ] Ni ralenti ni plein écran de flammes ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : fixe
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/visual-investigation.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/visual-investigation.jpg
- Crédit : « The Hindenburg: Four Minutes, 32 Seconds », LemoLab, CC BY 4.0. Archives de tiers : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/visual-investigation/STYLE.md`, `style.json`, `demo/index.html` (`plate()`, `ring()`, `cover()`, `wave()`, `playhead()`, `planPanel()`), `demo/film.json`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, panneaux empilés en 9:16, HyperFrames. Sources et droits : `references/materiel-et-droits.md`.
