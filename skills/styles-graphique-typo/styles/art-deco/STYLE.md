# Art déco

## 1. Identité

- **Nom** : Art déco (affiche des années 1930 qui bouge).
- **Inspiration** : les affiches de voyage et de paquebots des années 1930 (géométrie géante, perspective raide, aérographe dans des bords nets), l'ornement des gratte-ciel de l'époque (gradins, rayons de soleil, chevrons), les ballets filmés du dessus (kaléidoscopes humains), le jazz symphonique. On n'en recopie ni affiche, ni bâtiment réel, ni personnage, ni dessin de police, ni mélodie.
- **Ce qui le fait reconnaître** : des **filets d'or sur un noir chaud**, des volumes à bords nets remplis à l'aérographe, **un axe vertical central**. L'ornement est l'image : un soleil rayonnant est un fond, une arche à gradins est un cadre, un cadran est une barre de progression, une enseigne à ampoules est une révélation. Le mouvement est mécanique et symétrique.
- **Marche pour** : luxe, hôtellerie, gala, invitation, lancement avec compte à rebours, remise de prix, tout ce qui a « du glamour et une horloge qui tourne ».
- **Ne marche pas pour** : un sujet quotidien ou drôle, un tutoriel, un public enfant, une marque très colorée. Ce n'est pas un diaporama doré (les choses ont du volume et bougent), ni de l'Art nouveau (aucune courbe en coup de fouet, aucune fleur), ni un générique années 60.

## 2. Palette, typographie, matières

Trois constantes : **noir laqué chaud, or, ivoire**. Plus **un seul accent saturé réservé au héros** (ou à l'objet que l'histoire suit) : c'est la seule grande surface de couleur, l'œil le trouve dans n'importe quel plan large. Un ton « pierre précieuse » plus froid peut porter des surfaces secondaires, sans jamais rivaliser en surface.

| Rôle | Exemple |
|---|---|
| Fond | noir chaud `#0d0b09`, laque `#060504` (jamais un gris-noir neutre) ; ciel de nuit `#0a0e16` vers un horizon émeraude `#10231f` |
| Or (dégradé en bandes : sombre, clair, brûlant, clair, sombre) | ombre `#6f5220`, base `#c9a24b`, clair `#f3d98b`, reflet `#fff4d2` |
| Ivoire | `#f2e8d5` (papier, gants, lumière, texte) |
| Accent / pierre | bordeaux `#8e1b2e` et émeraude `#1d6b57` (démo) ; ou corail et saphir ; ou jade et prune |

(Valeurs de la démo d'origine, données en exemple : la règle est le trio, pas ces codes.) Toujours écrire les couleurs sur six chiffres.

- **Le trait signature** : un sous-trait sombre gravé (environ 1,6 px plus large), le trait en dégradé d'or, puis un filet de lumière très fin dessus. Rien n'a de contour noir de dessin animé.
- **Volumes** : bord net + aérographe (dégradé de l'ombre vers la lumière dans la forme), une seule direction de lumière (en haut à gauche), fin liseré d'or du côté éclairé.
- **Motifs** (soleil rayonnant, arche à gradins, écailles, chevrons, éventail, étoile à quatre branches, lignes de vitesse, cadran) : toujours structurels (un fond, un cadre, une transition), jamais des autocollants.
- **Polices** (libres) : Limelight (titres), Poiret One (chiffres, enseignes, plaques), Josefin Sans (sous-titres, étiquettes), Italiana (numéros).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Limelight et d'Italiana ; Outfit à la place de Poiret One et de Josefin Sans. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/limelight`, `@fontsource/poiret-one`, `@fontsource/josefin-sans`, `@fontsource/italiana` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers, sauf mention ci-après) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. Attention : Italiana : sans « œ » : écrire « oe » ou changer de police pour ce mot.
- **Personnages** : eux aussi déco, environ 7 têtes, corps fuselés, plans laqués à facettes, yeux en amande ou en arc, nez d'un seul trait.

## 3. Composition 9:16

- Le vertical convient très bien : tours, ascenseurs, portes, arches. **L'axe central est sacré** : il passe à x 540 pour le décor ; garder les éléments importants à gauche de x 945.
- Une composition asymétrique doit se résoudre sur l'axe avant la fin du plan.
- Au moment fort, le héros occupe au moins un tiers de la hauteur (640 px), sinon son visage se lit comme un accessoire de l'ornement.
- **Titres** : barre de titre dorée à gradins sur une arche ou un soleil, largeur 800 px au plus, lettres de 90 à 150 px, entre y 300 et y 700.
- **Sous-titres** : une plaque laquée (noir à environ 88 %) à bouts en gradins, double filet d'or, Josefin Sans SemiBold 46 à 52 px ivoire, posée entre y 1380 et y 1540. Elle **se déplie depuis le centre**, comme tous les titres.
- Les nombres portent l'histoire sans narration : cadrans, horloges, médaillons d'étage, plaques.

## 4. Ce qui bouge

- **Action principale** : tout se déplie depuis le centre (un point, un filet, des barres qui s'ouvrent symétriquement, le texte qui monte, puis ailes et étincelle) ; les scènes changent par des portes qui se fendent sur l'axe.
- **Boucles de fond** : (1) un reflet de lumière qui traverse l'or ; (2) des ampoules qui s'allument une à une dans un ordre comptable, puis un chenillard une fois l'enseigne allumée.
- **Autorisés** : tracé de ligne `#004` (l'or se grave à la vitesse de la phrase musicale et arrive sur le coup), reflet de lumière `#022`, kaléidoscope `#135`, raccord de forme `#042` (cercle sur cercle, rayon sur rayon), contre-plongée `#177`, travelling avant sur un cadran `#027`, vue du dessus `#181`, anticipation `#121` pour le jeu des personnages, compteur `#007`.
- **Interdits** : fondu enchaîné `#044`, glissement générique `#137`, flottement `#096`, tremblement `#124`, caméra à l'épaule `#034`, courbes organiques.
- Les ampoules ont un dépassement à l'allumage (éclat à environ 1,6 fois, stabilisé en 0,18 s). Les portes, cadrans et aiguilles ont une accélération-décélération ferme et un petit tassement, comme une machine.
- Ce qui ne bouge jamais : l'axe central.

## 5. Rythme et montage

- Personnages à 15 dessins par seconde (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; caméra, lumière, ampoules, tracé de l'or et reflets fluides.
- Un coup de musique par unité de lumière comptée (une lettre, un étage, une voix). On accélère en divisant le temps, pas en changeant de tempo.
- Plans de 3 à 6 s ; les gags montent par trois (une fois, deux fois, puis la rafale).
- Transitions : portes fendues, porte tambour, ouverture d'arche, raccord de forme. Le son de la pièce suivante entre une mesure avant que sa porte s'ouvre.
- **Version courte (8 à 12 s)** : deux plans : le dépliage depuis le centre (4 s), puis le titre en ampoules tenu 2 s ; un seul gag, pas la montée par trois. Accroche : le point d'or part à l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`. Pour un vrai décor en perspective avec lumière (hall, tour, salle de bal), passer par `blender` et garder les titres, cadrans et sous-titres en HyperFrames par-dessus.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `deco.js` (dégradé d'or, trait signature, aérographe, motifs), `titres.js` (barre de titre, chiffres, cadran, horloge, plaque de sous-titre), `ampoules.js` (texte → enseigne, ordre d'allumage), `camera.js` (caméra à sténopé pour un vrai point de fuite).

```js
function traitOr(ctx, chemin, l, reflet = 0) {
  ctx.lineWidth = l + 1.6; ctx.strokeStyle = "#060504"; ctx.stroke(chemin);       // gravure
  ctx.lineWidth = l;       ctx.strokeStyle = degradeOr(ctx, reflet); ctx.stroke(chemin);
  ctx.lineWidth = 0.8;     ctx.strokeStyle = "rgba(255,244,200,.8)"; ctx.stroke(chemin); // filet de lumière
}
const eclat = d => d < 0 ? 0 : 1 + 0.6 * Math.exp(-d / 0.06);   // ampoule : 1,6× puis 1 en ≈0,18 s
```

- **Techniques clés** : la perspective est réelle (un ou deux points de fuite), donc un travelling change la perspective au lieu de grossir des aplats ; animer le décalage du dégradé d'or donne le reflet ; « l'exception d'une couleur » passe par le même remplissage + filet + lueur que l'or.
- **Pièges** : les enseignes à ampoules tirées du squelette des lettres cassent sur les courbes (G, S, R), il faut souder les bouts de chaîne à moins de 14 px ; les écailles se lisent comme des briques si on ne recouvre pas rangée par rangée ; un point d'or sur noir pur déclenche le détecteur d'image noire, il faut relever légèrement le fond ; un personnage de dessin animé générique a l'air collé.

## 7. Son

- **Musique** : jazz symphonique des années 1920-1930 (pas un big band des années 60) : piano stride, clarinette (trille, glissando), cordes, trompette bouchée, contrebasse en pizzicato, balais, cloches tubulaires, harpe, célesta. Familles de rythme : fox-trot, charleston, tango, ballade lente, fanfare d'actualités.
- **Bruitages par matière** : clic de laiton, grille de bronze et chaîne, talons sur le marbre, plateau d'argent, porte en bois, interrupteur à couteau et bourdonnement de filament, tic de relais, sonnette d'ascenseur.
- **Silence** : avant le son le plus important, ne garder qu'un petit son de la scène (un tic d'horloge, du vent), puis repartir avec ce seul son.
- **Voix** : possible en annonceur d'époque ; une distorsion de haut-parleur trop forte devient incompréhensible sous la musique.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le fond est un noir chaud, jamais gris neutre ni noir pur.
- [ ] Chaque composition a un axe central, et y revient avant la fin du plan.
- [ ] Un seul accent saturé, porté par le héros ou l'objet suivi.
- [ ] Aucun contour noir : tout trait est le trait d'or en trois couches.
- [ ] Les volumes sont à l'aérographe avec une seule direction de lumière.
- [ ] Titres, sous-titres et transitions s'ouvrent tous depuis le centre.
- [ ] Les ampoules s'allument dans un ordre qu'on peut compter, chacune sur un coup de musique.
- [ ] Aucun fondu ni glissement générique.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine, *Midnight at the Starlight Hotel* (58 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/art-deco.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/art-deco.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/art-deco/STYLE.md`, `DEMO.md`, `demo/engine/deco.js`, `type.js`, `bulbs.js`, `cam.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Limelight, Poiret One, Josefin Sans, Italiana : OFL 1.1.
- Adaptation Flot Web : traduction, composition verticale, portage vers HyperFrames (Blender en option), numéros de mouvements, règles de son du plugin.
