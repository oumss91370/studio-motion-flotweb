# Vitrail

## 1. Identité

- **Nom** : Vitrail (verre coloré vu depuis une salle de pierre sombre).
- **Inspiration** : les prologues de contes racontés vitre par vitre, les effets de verre qui se fend et se recompose pièce par pièce, et les verrières des XIIᵉ et XIIIᵉ siècles (logique des couleurs, grisaille, mise en plomb). On n'en recopie ni personnage, ni composition, ni sujet, ni musique.
- **Ce qui le fait reconnaître** : des **pièces de verre coloré serties de plomb sombre**, visages et plis **peints en grisaille brune** ; le verre n'a pas de lumière propre, il **ne s'allume que quand le soleil est derrière** et projette une copie douce et colorée sur le sol de pierre ; les figures bougent pièce par pièce, rigides et saccadées ; la salle est toujours là (pierre, embrasure, barres de fer, dallage).
- **Laïque** : aucune croix, aucun saint, aucune auréole, aucune image religieuse. On emprunte le métier, pas les sujets.
- **Marche pour** : légende, conte, patrimoine, histoire en chapitres, récit de fêtes, étapes d'un processus vues comme les heures d'une journée, histoire d'une entreprise qui se réinvente (le verre se fend, le plomb répare).
- **Ne marche pas pour** : sujet technique ou chiffré, humour rapide, lancement de produit, contenu au rythme serré. Ce n'est pas du vectoriel à contours noirs, ni un filtre kaléidoscope ou Voronoï, ni de la mosaïque (la mosaïque réfléchit, le verre transmet).

## 2. Palette, typographie, matières

- **Deux teintes portent l'image** (une profonde, une chaude) ; trois ou quatre autres seulement en petites touches. Exemple : fond cobalt, rubis, touches d'or, de vert et de pourpre.

| Rôle | Exemple |
|---|---|
| Cobalt (fond) | `#1b3fa0` |
| Rubis | `#b3202a` |
| Or, vert, pourpre (touches) | `#e0a92e`, `#2f7d4f`, `#7a2a5a` |
| Verre blanc verdâtre (visages, filets, ciel) | `#dfe8d8` |
| Plomb / pierre | `#0d0d0f` / gris chaud `#8d8679` |

(Valeurs d'exemple à ajuster : la règle est « deux teintes dominantes, le reste en touches ».)

- **Les chairs plus sombres qu'on ne croit**, sinon les visages en contre-jour brûlent en blanc.
- **La couleur du soleil est l'horloge** : aube blanc-bleu, midi presque blanc, après-midi doré, crépuscule orange profond (monter l'intensité plutôt que le rouge), faible lune bleue. La longueur de la tache au sol suit la hauteur du soleil.
- Pierre et plomb ne prennent de couleur que par la lumière projetée. Une lumière de l'histoire (bougie, lampe, écran) peut avoir une couleur qu'aucun verre n'utilise.
- **Polices** (libres) : IM Fell English (sous-titres), Cinzel 600 (titres gravés dans la pierre).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place d'IM Fell English ; Playfair Display à la place de Cinzel. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/im-fell-english`, `@fontsource/cinzel` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Pièces** : découpes en courbes douces, sans coin rentrant profond. **Chaque pièce est texturée** : stries à un angle propre, dérive de teinte de ±10 %, bords plus sombres près du plomb, épaisseur variable de ±9 %, bulles et rayures.
- **Plomb** : presque noir, un seul réseau, plus fin sur les petites pièces, joints ronds, points de soudure ; seulement là où deux couleurs se touchent.
- **Grisaille** : traits effilés brun sombre translucide, lavis pointillé pour les ombres, et **rehauts grattés** (un trait fin à côté de chaque pli, de la couleur de la pièce : le seul reflet que la lumière transmise permet).
- **Visages** : yeux en amande, paupière lourde, grande pupille. L'expression vit dans les sourcils et la bouche ; on la change **en remplaçant la pièce du visage**, jamais en la déformant.
- **Fonds** : losanges taillés à la main (treillis irrégulier, un motif peint dans chacun), bordures à perles et rinceaux.

## 3. Composition 9:16

- Une **lancette** (fenêtre haute et étroite) est naturellement verticale : c'est le cadre idéal. On la lit de bas en haut ou de haut en bas, médaillon par médaillon ; ou bien deux lancettes côte à côte, une éclairée, une sombre.
- Les sujets sont grands : en gros plan, une vitre occupe 1,3 à 2,3 fois la largeur d'une lancette. Dans une lancette étroite, empiler les figures en diagonale.
- Une chose révélée se place près du centre et fait au moins un huitième de la largeur, avec sa lueur.
- **Le sol compte** : réserver le bas de l'image (y 1100 à 1560) au dallage qui reçoit la tache colorée, quand la scène s'y joue.
- **Sous-titres** : une **banderole de parchemin** (bouts enroulés, léger creux, filet fin), IM Fell English 48 à 54 px en encre sombre, entre y 1380 et y 1540. Elle se déroule depuis le centre ; le texte n'apparaît que lorsqu'elle est ouverte à 75 %.
- **Titres** : capitales romaines gravées dans la pierre, révélées par une bande de lumière ; 36 px au moins pour les petites lignes.

## 4. Ce qui bouge

- **Action principale** : la lumière se déplace, et seule la vitre éclairée vit. Quand la lumière la quitte, ses figures se figent.
- **Boucles de fond** : (1) les rais de lumière chargés de poussière qui dérivent ; (2) la tache colorée au sol, floue, qui glisse et s'allonge.
- **Autorisés** : style image par image `#128` (figures à 10 dessins par seconde), reflet de lumière `#022`, contre-jour `#097`, travelling latéral qui suit la bande de lumière `#029`, panoramique vertical `#026` des rais jusqu'au sol, travelling avant lent `#027`, plan fixe `#175`, éclatement `#142` (fissure), secousse d'impact `#024` (2 images), heure dorée `#103`.
- **Interdits** : fondu enchaîné `#044`, volet `#045`, retournement `#021`, morphing `#012` (le verre ne plie ni ne se déforme jamais), écrasement `#011`, lumière saccadée (elle se lit comme un scintillement).
- **Fissure** : des lignes brisées courent depuis l'impact en un quart de seconde, brillantes, avec un bref éclair blanc.
- **Remise en plomb** : des groupes de pièces glissent, un temps chacun, avec une petite bosse vers l'extérieur le long du plomb, chacun finissant par une étincelle de soudure ; les fissures deviennent des plombs de réparation.
- Les choses apparaissent **en étant éclairées**, jamais en fondu.

## 5. Rythme et montage

- Rythme de conteur : plans de 4 à 8 s, peu de coupes. Les actions tombent sur les temps.
- Figures à 10 dessins par seconde (à 30 i/s : une image sur trois ; 8 seulement dans un film livré à 24 i/s) ; lumière, caméra, rais et poussière fluides.
- Transitions : la lumière qui se déplace, les rais, une fissure, l'obscurité. Jamais de fondu, de volet ni de retournement.
- Revenir à un cadrage du début sous une autre lumière : la rime montre ce qui a changé.
- **Version courte (8 à 12 s)** : une seule vitre : la lumière arrive avant 2 s, une figure joue une action sur les temps, la lumière repart ; couper le travelling le long de la bande.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D pour les pièces et un compositeur WebGL pour la lumière. Pour un rendu photoréaliste de la salle, `blender` peut fournir la pierre et les rais ; le vitrail reste dessiné en code.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `verre.js` (pièces, textures, plomb, grisaille, losanges), `compo.js` (compositeur), `fenetre.js` (lancettes, rose, bordures, mur), `scene.js` (caméra, projection au sol, rais, poussière), `banderole.js`.

Une seule formule pour tout, afin que chaque élément soit dans la même lumière :

```
verre   = tons( contre-jour(x,y,t) × transmission × texture du verre ) + voile d'usure × lumière de la salle
surface = albédo × (ambiance + lueur des vitres éclairées + lumières ponctuelles)      // pierre, plomb, fer
sol     = dalles × (ambiance + carte des taches colorées, floutée + halo)
+ rais additifs avec poussière · éblouissement (le verre vif mord sur le plomb)
```

```js
const tFigure = (t, tLumierePartie) => Math.floor(Math.min(t, tLumierePartie) * 10) / 10;  // règle du gel
```

- **Techniques clés** : courbe de tons qui **préserve la teinte** (sinon le cobalt devient pastel) ; pièces rigides en cinématique directe ; projection au sol floutée, désaturée d'environ 20 %, modulée par la pierre, inversée (le haut de la fenêtre tombe le plus loin dans la salle).
- **Pièges** : les plombs cachés transparaissent si on n'efface pas la surface sous chaque pièce ; un crépuscule rouge sur du verre bleu donne de la boue ; un pavage Voronoï se lit comme un filtre et des aplats comme du clip-art ; une tache au sol nette ressemble à un autocollant ; des rais à pleine force près de la fenêtre lavent la vitre ; un texte gravé dans un plan large sombre est illisible (s'approcher, poser une lumière dessus).

## 7. Son

- **Musique** : orgue (bourdon de pédale, jeux doux, plein jeu), harpe, clochettes, cloches tubulaires, flûte à bec ou voix proche du plain-chant, verres chantants, timbales, vielle à roue. Modes anciens, quintes à vide, bourdons. Pas de piano ni de cordes génériques. Une note peut signifier « la lumière » à chaque vitre qui s'éveille.
- **Bruitages** : verre frappé (son cristallin, non harmonique), fissure (claquement + pluie de tintements), plomb qui grince, verre qui glisse dans sa rainure, grésillement de soudure, ambiance de salle de pierre, oiseaux sous la voûte.
- **Silence** : arrêt net, réverbération comprise ; seul reste le tintement du verre. Une cloche à longue résonance peut le refermer.
- **Voix** : conteuse ou conteur doux et régulier, peu de phrases, courtes. Mixage ample et réverbéré.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque pièce de verre est texturée ; aucun aplat pur.
- [ ] Deux teintes dominent ; les autres restent en touches.
- [ ] Une vitre non éclairée est sombre et laiteuse, ses figures figées.
- [ ] Les figures bougent par pièces rigides à 10 dessins par seconde ; la lumière est fluide.
- [ ] Les visages ne brûlent pas en blanc à contre-jour.
- [ ] La tache au sol est floue, désaturée et modulée par les dalles.
- [ ] Aucune image religieuse ; aucun fondu, volet ni morphing.
- [ ] La banderole et les titres gravés se lisent à taille téléphone.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Film de démo d'origine, *The Dragon of the East Window* (56 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/stained-glass.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/stained-glass.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/stained-glass/STYLE.md`, `DEMO.md`, `demo/glass.js`, `demo/comp.js`, `demo/scene.js`, `demo/subs.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices IM Fell English et Cinzel : OFL 1.1.
- Adaptation Flot Web : traduction, composition en lancette verticale, exemples de couleurs, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
