# Screencast vivant

## 1. Identité

- **Nom** : Screencast vivant (faux enregistrement d'écran habité par une mascotte).
- **Inspiration** : les enregistrements d'écran « produits » (zoom automatique sur le curseur, curseur lissé, fenêtre posée sur un fond d'écran), les visites guidées de logiciels (vraie interface, voix calme, une fonction par phrase), les mascottes animées d'applications grand public (écrasement, anticipation, un personnage qui joue dans l'interface). On n'en recopie ni personnage, ni interface, ni musique, ni image.
- **Ce qui le fait reconnaître** : le film **ressemble à un enregistrement du vrai produit, mais n'en est pas un** : chaque fenêtre, menu, ligne et bouton est **redessiné en HTML/CSS/SVG**, donc la caméra va partout et le texte reste net à tout zoom. Dans ce monde en haute définition vit une **mascotte faite de gros pixels carrés**. Le choc des deux résolutions, c'est le look.
- **Deux acteurs, jamais une main** : le **curseur** est l'utilisateur ; la **mascotte** est le logiciel. Quand le logiciel lit, elle court le long des lignes ; quand il planifie, elle tient un crayon en pixels ; quand il teste, elle saute sur le bouton.
- **Marche pour** : tutoriel de produit, lancement de fonction, accueil des nouveaux utilisateurs, démonstration d'un outil en ligne (45 à 75 s).
- **Ne marche pas pour** : un produit sans interface, un sujet abstrait, un logiciel dont on n'a pas la documentation (on ne peut pas inventer ses écrans). Ce n'est pas une `keynote-sombre` (pas de scène noire ni d'interface abstraite inventée), ni un jeu en pixel art (seule la mascotte est en pixels), ni une vraie capture.
- **Mascotte** : celle du client, ou un **personnage original en pixels**. Jamais la mascotte d'une marque tierce (la démo d'origine en utilise une : on ne la reprend pas).

## 2. Palette, typographie, matières

- **Les couleurs de l'interface du produit commandent** : suivre exactement ses thèmes clair et sombre réels.
- La mascotte garde la couleur de la marque, ou **une teinte saturée qu'aucun élément d'interface n'utilise**, pour que l'œil la trouve dans n'importe quelle image.
- Les surcouches (pastille de chapitre, affichage des touches, sous-titres) sont en verre dépoli neutre ; un accent au plus, pris au produit.

| Rôle | Exemple (thème clair / thème sombre) |
|---|---|
| Fond d'écran derrière la fenêtre | dégradé doux `#dfe6f0` → `#f4efe8` / `#14161c` → `#1e2230` |
| Fenêtre | `#ffffff` / `#1b1d23`, ombre douce large |
| Texte d'interface | `#1c1e22` / `#e8eaee` |
| Surcouches | blanc ou noir à 60 %, flou d'arrière-plan |
| Mascotte | une teinte vive absente de l'interface, par exemple `#ff7a3d` |

(Valeurs d'exemple : la règle est « les vraies couleurs du produit ».)

- **Polices** : celles du produit, ou des équivalents libres (Inter, JetBrains Mono, une police à empattement pour une interface éditoriale).
- **Police de repli** : aucune à prévoir, Inter et JetBrains Mono sont fournies par HyperFrames et se chargent par leur nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/inter`, `@fontsource/jetbrains-mono` (vérifié par `npm view` le 11/11/2026). La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Interface réelle, redessinée** : chaque libellé, nom de mode et raccourci correspond au vrai produit ; aucune capture, aucun faux texte. Le contenu de démonstration (code, données, résultats) est cohérent, et ce qui est modifié change vraiment.
- **La grille de pixels est sacrée** : la mascotte, ses accessoires (crayon, « ! », étincelles, cœur, poussière) et ses traînées partagent **une seule grille de pixels carrés à bords nets**.
- **Profondeur** seulement au service de l'attention : mise au point sur un panneau (flouter celui qui ne compte pas), projecteur par assombrissement des bords. **Jamais de flou sur un texte à lire.**

## 3. Composition 9:16

- Une fenêtre d'ordinateur est large : en vertical, **on ne la montre presque jamais en entier**. La caméra reste zoomée (zoom de 1,6 à 3) sur une colonne de l'interface et voyage de panneau en panneau. Plan d'ensemble de la fenêtre : rare, court, pour situer.
- Si le produit a une version mobile, la préférer : elle remplit le cadre naturellement.
- Le texte d'interface que l'on doit lire fait **au moins 30 px à l'écran** après zoom.
- **La gravité, ce sont les bords supérieurs de l'interface** : la mascotte ne se tient que sur le bord supérieur d'un vrai élément (champ de saisie, menu, ligne de liste, ligne de code, bouton, lettres d'un titre). Taille : 8 à 12 % de la hauteur du cadre.
- **Couches d'information, et rien d'autre** : une pastille de chapitre (01 à 04) en haut à gauche sous y 160 ; un affichage des touches pressées ; des sous-titres en pilule de verre dépoli entre y 1400 et y 1540 (46 à 50 px) ; à l'occasion une étiquette « ▶▶ 4× » pour un accéléré.
- Le sous-titre n'est jamais sur l'élément dont on parle ni sous la mascotte. Prévoir une **voie sans texte** pour elle.
- **Titre dans l'interface** : s'il y en a un, il apparaît comme un élément du produit (titre d'un écran vide, titre de fenêtre, notification).
- Rien d'important à droite de x 945.

## 4. Ce qui bouge

- **Action principale** : chaque action de la mascotte déclenche un **vrai changement d'état** de l'interface ; chaque action de l'utilisateur est un déplacement de curseur, un clic ou une touche affichée.
- **Boucles de fond** : (1) la mascotte au repos respire (petit écrasement) sur le temps de la musique et cligne des yeux irrégulièrement ; (2) une dérive lente de la caméra quand on écoute.
- **Autorisés** : travelling avant `#027` vers le curseur, panoramique filé `#043` entre deux panneaux (avec flou de mouvement), bascule de mise au point `#033`, suivi `#174` de la mascotte le long d'une liste, écrasement et étirement `#011`, anticipation `#121`, rebond `#123` amorti à la réception, machine à écrire `#006`, écran partagé `#144`, accéléré `#039` avec son étiquette, pixellisation `#141` (volet en pixels), iris `#188` (cercle qui révèle un changement de thème), plan-séquence `#172`, notification `#056`, et tous les composants d'interface `#049` à `#072` **tels que le produit les a**.
- **Interdits** : fondu enchaîné `#044`, capture d'écran réelle, main ou doigt à l'écran, zoom arrière au-delà de l'écran (zoom toujours supérieur ou égal à 1), effets d'interface que le produit n'a pas, curseur qui se téléporte, flou sur un texte à lire.
- **Jeu de la mascotte** : saut avec accroupissement d'élan, étirement au décollage, jambes repliées, écrasement à la réception avec rebond amorti et poussière. **Les yeux portent le jeu** (neutre, gauche, droite, haut, bas, grands ouverts, contents, fermés) : ils regardent ce qui compte. Bras : baissés, levés, salut.
- **Curseur** : trajectoires lissées à ressort, petite poussée de caméra au clic.
- La position de la mascotte s'accroche aux demi-pixels de sa grille : son mouvement est légèrement saccadé, celui de l'interface est fluide.

## 5. Rythme et montage

- **Un plan-séquence** à l'intérieur de l'écran ; les coupes n'existent que sous les transitions de chapitre.
- Trois ou quatre chapitres, une fonction par phrase de voix ; chaque événement visuel est accroché à un **mot dit**.
- Transitions : volet de la pastille de chapitre, volet en pixels, cercle de changement de thème.
- **Le gel-projecteur** : pousser et assombrir autour de la seule pastille qui porte la promesse (« Enregistré », « Chiffré »), avec une courte chute du son.
- Un travail long passe en accéléré avec son étiquette.

## 6. Recette technique

- **Moteur** : HyperFrames, en HTML/CSS/SVG : c'est le moteur idéal pour ce style (l'interface est du vrai HTML).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `interface.js` (un état → le HTML de chaque écran), `mascotte.js` (grille du personnage, poses, accessoires en pixels), `film.js` (voix à heures fixes, événements accrochés aux mots, mouvements de caméra, segments de la mascotte, curseur, événements sonores), `scene.js` (couches claire et sombre, mesure des ancres, flou de mouvement, surcouches).

```js
// la mascotte se tient sur le bord supérieur d'un VRAI élément, mesuré à chaque image
function solDe(sel) { const r = document.querySelector(sel).getBoundingClientRect(); return { x: r.left + r.width / 2, y: r.top }; }
const accrocher = (v, pixel) => Math.round(v / (pixel / 2)) * (pixel / 2);          // demi-pixels de la grille
function placerMascotte(sel, pixel) { const s = solDe(sel); mascotte.style.transform = `translate(${accrocher(s.x, pixel)}px, ${accrocher(s.y, pixel)}px)`; }
// chaque événement visuel part sur un mot de la voix
tl.add(() => etat.menuOuvert = true, motDit("phrase3", "menu"));
```

- **Techniques clés** : image nette des pixels (`image-rendering: pixelated`) ; flou de mouvement tiré de la vitesse de la caméra, appliqué à **un conteneur non transformé**, seulement pendant les filés.
- **Pièges** : **fonctions inventées ou modes renommés** : vérifier chaque bouton, mode et raccourci dans la documentation du produit ; ce qui n'y est pas n'est pas dans le film ; une mascotte placée par coordonnées fixes flotte ou dérive ; un flou de mouvement sur une couche transformée bave sur les pixels ; un bruit de touche qui tombe sur le nom du produit le masque (décaler les bruitages hors des débuts de mots) ; une voix de synthèse qui prononce mal le nom du produit (essayer d'autres orthographes, vérifier par transcription).

## 7. Son

- **Deux résolutions dans la musique aussi** : une couche haute fidélité (piano, basse, batterie aux balais, glockenspiel) est le monde ; **une voix 8 bits (onde carrée) est la mascotte**. Elles se répondent, jouent ensemble ou fusionnent.
- Options : une version « nuit » filtrée pour le thème sombre ; un roulement à chaque changement de chapitre ; retirer la batterie pour tendre ; une nappe tenue sous un gel.
- **Bruitages** : clavier (avec l'irrégularité d'une frappe humaine), clics, panneaux qui glissent, menus qui s'ouvrent, tintement de notification. Les pas, sauts et réceptions de la mascotte sont en 8 bits (ici la synthèse est le bon choix).
- **Silence** : une courte chute vers l'ambiance de la pièce avant la promesse clé.
- **Voix** : calme, une fonction par phrase.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Rien n'est une capture d'écran : toute l'interface est redessinée et nette au zoom.
- [ ] Chaque libellé, mode et raccourci existe dans la documentation du produit.
- [ ] La mascotte est seule en pixels, sur une grille unique à bords nets.
- [ ] La mascotte se tient toujours sur le bord supérieur d'un vrai élément.
- [ ] Elle ne couvre jamais un texte à lire, et n'est jamais sous un sous-titre.
- [ ] Le curseur est le seul signe de l'utilisateur : aucune main.
- [ ] Chaque action a un effet visible dans l'interface.
- [ ] Le texte d'interface à lire fait au moins 30 px ; le zoom ne sort jamais de l'écran.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 30

## 9. Aperçu

- Film de démo d'origine (59 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/living-screencast.mp4
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0. **Ce film est un « film de fan »** : il met en scène la mascotte et l'interface d'une marque tierce, non affiliée. Le donner en lien pour montrer la technique ; **ne pas l'utiliser comme visuel de vente** et ne reprendre ni sa mascotte ni son interface.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/living-screencast/STYLE.md`, `DEMO.md`, `demo/film.js`, `demo/ui.js`, `demo/main.js` (le fichier de mascotte de la démo n'est pas repris).
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images (hors marques tierces).
- Adaptation Flot Web : traduction, cadrage vertical zoomé, couleurs d'exemple, mascotte originale obligatoire, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
