# Hologramme de science-fiction

## 1. Identité

- **Nom** : Hologramme de science-fiction (objet scanné en fil de fer lumineux).
- **Inspiration** : les interfaces holographiques du cinéma de science-fiction (cadres de visée, étiquettes à trait de rappel, chiffres qui défilent, couches de profondeur ; ou bien une seule couleur, des filets très fins et de l'espace) et les vues éclatées des logiciels de conception. On n'en recopie ni mise en page, ni icône, ni police, ni couleur.
- **Ce qui le fait reconnaître** : le sujet est toujours un **fil de fer fait de lumière**, au-dessus d'un socle de projection rond, sur une scène presque noire ; jamais un objet rendu en plein. Tout se lit comme des **données scannées** : un plan de balayage fait pousser le modèle, des **cadres de visée se verrouillent sur les pièces**, chaque pièce s'ouvre en vue éclatée locale, un trait de rappel sort, et son nombre **défile depuis des caractères au hasard jusqu'à la vraie valeur**.
- **Trois couches de profondeur toujours présentes** : une trame de points au fond (parallaxe lente), le sujet avec son socle, et l'affichage de premier plan (équerres d'angle, règles graduées qui glissent plus vite, texte d'état).
- **Style « de scène »** : il fait un travail pratique pour tout objet qui a des pièces (voir la section 5).
- **Marche pour** : présentation des caractéristiques d'un produit, démontage commenté, écran en boucle pour un salon, comparaison ancienne/nouvelle version, ordre de montage.
- **Ne marche pas pour** : un objet sans pièces distinctes, un service, une histoire avec des personnes, un sujet chaleureux. Ce n'est pas une `keynote-sombre` (qui repose sur la typo et l'interface), ni un plan bleu, ni un rendu de produit.

## 2. Palette, typographie, matières

- **Une teinte froide + un accent chaud**, tous deux à choisir d'après le sujet.

| Couple | Teinte (lignes, affichage, faces) | Accent (valeurs verrouillées) |
|---|---|---|
| Menthe / orange | `#5ef2c8` | `#ff8a3c` |
| Violet / citron vert | `#9a8cff` | `#c6f24a` |
| Bleu glacier / rouge | `#7fd4ff` | `#ff4a4a` |
| Scène | presque noir teinté par la teinte, par exemple `#04090b` | |

(Les couples sont ceux de la source ; les codes sont des exemples.) Préférer menthe ou bleu glacier : le violet tombe vite sous la règle commune « pas plus de 30 % d'images bleu-violet ».

- **L'accent ne sert qu'aux valeurs verrouillées** : un nombre prend la couleur d'accent à l'image où il devient vrai. Rien d'autre ne l'utilise.
- **Le blanc, c'est la chaleur** : des arêtes presque blanches et des éclairs d'une image marquent ce qui est actif (le front du scan, les pièces internes d'un élément ouvert, une pièce pointée). Tout ce qui est au repos reste dans les niveaux d'opacité de la teinte.
- Un seul objet peut garder sa propre couleur : une marque, jamais une décoration.
- **Polices** (libres) : Rajdhani en capitales (Light pour les grands nombres et le nom du produit, interlettrage large ; Medium ou SemiBold pour les étiquettes) ; Share Tech Mono pour les micro-données (coordonnées, compteurs, zoom).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Rajdhani ; Space Mono à la place de Share Tech Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/rajdhani`, `@fontsource/share-tech-mono` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Fil de fer** : traits additifs d'environ 1,3 px (1,8 px en 1080×1920), en quelques niveaux d'opacité fixés par un **brouillard de profondeur** (près = vif, loin = environ 25 %), plus deux passes de lueur en basse résolution.
- **Vraie structure d'objet** : les tubes sont des anneaux et des lignes longitudinales ; **chaque pièce est physiquement reliée** aux autres (une pièce qui flotte se remarque en premier) ; chaque pièce a sa silhouette caractéristique.
- **Le texte n'est jamais posé sur le fil de fer** : chaque bloc de texte a sa **plaque sombre** (presque noir translucide, bordure de 1 px, repères d'angle).
- **Hologramme plein** (une fois, au plus) : les faces se remplissent d'un reflet de bord et de lignes entrelacées qui défilent ; les lignes restent au-dessus.

## 3. Composition 9:16

- L'objet au centre, **au moins un tiers de la hauteur** à chaque moment clé (640 px), entre y 380 et y 1150. Un objet haut (bouteille, lampe, vélo vu de trois quarts) profite du format ; un objet long se présente en diagonale ou de trois quarts.
- **En vertical, les cartes ne vont pas sur le côté** : la carte de caractéristique se place **au-dessus ou au-dessous** de l'objet (y 200 à 360, ou y 1180 à 1360) ; le **rail de pastilles** (les valeurs déjà lues) s'empile le long du bord gauche ou en une rangée sous l'objet ; les sous-titres entre y 1400 et y 1540 ; la loupe au-dessus d'eux. Rien ne se touche.
- Raccourcir une vue éclatée plutôt que d'envoyer une pièce dans un texte.
- **Tailles** : nom du produit 80 à 110 px ; valeur 110 à 160 px, chiffres à largeur fixe ; étiquettes 32 à 38 px ; micro-données 22 à 26 px (décor, pas à lire : à marquer `data-passage` ; tout texte à lire fait 32 px ou plus). Le point décimal est un petit carré (un point lumineux se lit comme une virgule).
- **Sous-titres** : une plaque sombre à équerres d'angle, avec des barres d'« empreinte vocale » qui bougent avec la parole, texte presque blanc de 46 px.
- **Habillage** : équerres d'angle et règles dans la zone utile ; mention « sujet // mode » en haut à gauche et ligne d'état vivante à côté, sous y 160 ; rien d'utile à droite de x 945.
- Le titre fait partie de la scène : le nom défile comme une valeur, puis viennent le code, la catégorie et la phrase d'accroche.

## 4. Ce qui bouge

- **Action principale** : scan, verrouillage, ouverture, valeur. Le cadre de visée arrive trop grand, tourné de 45° et pâle ; il s'ajuste en 0,2 s environ et lance un éclair blanc de 3 images sur le temps fort.
- **Boucles de fond** : (1) le socle de projection qui tourne lentement (anneaux, graduations, rayons pâles) ; (2) la trame de points et les règles en parallaxe, la ligne d'état qui vit.
- **Autorisés** : orbite `#030` lente, plateau tournant, travelling avant `#027`, panoramique filé `#043` qui suit le cadre de visée, vue du dessus `#181`, contre-plongée `#177`, grue `#031`, vue éclatée `#143`, tracé de ligne `#004` (trait de rappel : anneau d'ancrage, diagonale, horizontale, en 0,5 s environ), brouillage de texte `#129` puis compteur `#007` (les caractères se verrouillent de droite à gauche), parallaxe `#016`, reflet de lumière `#022`, glitch `#023` (**trois images au plus, une seule fois**, sur le plus grand changement), points d'intérêt `#163`, iris `#188` de la loupe.
- **Interdits** : coupe et fondu `#044` à l'intérieur de la scène, objet rendu en plein et éclairé de façon réaliste, flou de mouvement sur l'affichage (il reste net), rebond `#123`, lueur généralisée sur le texte, deux couleurs d'accent.
- **Vue éclatée** : le capot glisse **le long de son propre axe de montage** ; le contenu reste en place et s'illumine. Ouvrir sur un ou deux temps, refermer vite.
- **Rail de pastilles** : une valeur lue glisse sur le côté et y reste jusqu'à la fin.
- La caméra part **avant** le verrouillage suivant ; le flou de mouvement n'existe que pendant le filé.

## 5. Rythme et montage

- 30 images par seconde, fluide ; seuls les caractères qui se brouillent changent à chaque image.
- **La musique d'abord**, sur une grille : une mesure = une information ; les verrouillages tombent sur les temps forts.
- Aucune coupe : seuls le plan de balayage (qui fait apparaître ou efface) et l'iris de la loupe servent de transitions.

**Les usages : l'ordre et la durée de l'information** (une grammaire, pas un gabarit à remplir) :

| Usage | Ordre de l'information | Tenue par couche | Durée |
|---|---|---|---|
| Présentation des caractéristiques | nom + accroche → une caractéristique par pièce (étiquette, valeur, unité, détail) → poids ou prix → appel à l'action | titre 5 s au moins ; valeur 2,5 s au moins, puis rangée ; fiche finale 3 s au moins | 30 à 40 s, 2 à 5 pièces |
| Écran en boucle | nom → 3 à 5 caractéristiques → appel à l'action, sans voix ; dernière image = première | 3 s par caractéristique, 5 s à la fin | boucle de 20 à 30 s |
| Démontage | pièce → ce qu'elle fait → un nombre ; l'intérieur seulement quand on ouvre | 4 à 6 s par pièce | 40 à 60 s |
| Mise à niveau | pièce → ancienne valeur (pâle) → nouvelle valeur (accent) ; l'ancienne pièce est effacée par le scan, la nouvelle scannée | 3 s par changement | 20 à 30 s |
| Ordre de montage | numéro d'étape → nom de la pièce ; les pièces se mettent en place une à une | une mesure par pièce | 20 à 40 s |

- **Version courte (8 à 12 s)** : le nom (1,5 s, et non 5), deux caractéristiques de 3 s (scan, verrouillage, valeur), l'appel à l'action tenu 2 s ; couper le démontage et les autres pièces. Accroche : le premier scan avant 2 s.

## 6. Recette technique

- **Moteur** : `three` (Three.js dans une composition HyperFrames) pour le fil de fer : c'est léger et suffisant. `blender` seulement pour préparer le modèle (simplifier un fichier 3D du client, extraire les arêtes par pièce). L'affichage (cadres, cartes, pastilles, sous-titres) reste en HTML ou canvas 2D par-dessus.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `modele.json` (pièces : arêtes, axe de montage, pièces internes, points d'ancrage ; normalisé au chargement pour que les caméras marchent avec n'importe quel objet), `holo.js` (projection, scan, vue éclatée, faces, lueur, socle), `affichage.js` (plaque, cadre de visée, trait de rappel, texte qui défile, carte, pastille, loupe, sous-titre), `contenu.json` (les faits du client), `film.js`.

```js
// brouillard de profondeur : opacité d'une arête selon sa distance
const alpha = z => 0.25 + 0.75 * (1 - borner((z - zProche) / (zLoin - zProche)));
// valeur qui défile : les caractères se verrouillent de droite à gauche ; hasard à graine, par image
function defiler(valeur, p, image) {
  const n = valeur.length, verrouilles = Math.floor(p * (n + 1));
  return [...valeur].map((c, i) => (n - i <= verrouilles || !/\d/.test(c)) ? c : GLYPHES[hasard(image * 31 + i) % GLYPHES.length]).join("");
}
// cadre de visée : trop grand, tourné, pâle → ajusté en 0,2 s, éclair de 3 images sur le temps
tl.fromTo("#cadre", { scale: 1.8, rotation: 45, opacity: .25 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.2, ease: "power3.out" }, temps(8) - 0.2);
```

- **Pièges** : des cadres de visée qui enflent (calculer sur la pose de repos, ignorer les pièces internes) ; un long trait de rappel en diagonale qui désigne la mauvaise pièce (poser l'anneau sur le corps de la pièce, la faire clignoter) ; deux boîtes parallèles qui s'écartent ne se lisent pas comme une ouverture ; une pièce faite de boîtes génériques ne se reconnaît pas ; un filé écrit dans le segment suivant se joue comme une coupe sèche (le démarrer dans le précédent) ; remplacer le contenu de la démo et reconstruire n'est qu'un test technique, pas une façon de faire un film.

## 7. Son

- **Musique** : synthétiseurs : arpège avec écho alterné (creusé dans les médiums pour laisser passer la voix), basse en croches, charleston et claps de synthèse, nappes. **La densité suit l'information.**
- Outils au choix (deux ou trois par film) : passer à mi-tempo pour laisser lire ; un temps de **vrai silence** (rien, pas même un bip d'interface) ; une grande chute pour le plus grand changement ; une couche ajoutée ou retirée par pièce ; une note tenue sous une longue tenue.
- **Bruitages par matière** : la lumière = sons purs et bips **dans la tonalité** (synthèse à sa place ici) ; les mécanismes = glissement de moteur, souffle pneumatique, tintement de métal (vrais enregistrements) ; un verrouillage = coup sourd + claquement + bip à deux tons ; le défilement d'une valeur = un seul tic continu.
- **Ambiance** : bourdonnement du projecteur et son de la pièce.
- **Voix** : calme, assurée. Baisser la musique **et** les bruitages sous la voix, avec une baisse tenue entre les mots (pas de pompage).
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le sujet est un fil de fer lumineux, jamais un objet plein (sauf le moment unique de l'hologramme plein).
- [ ] Une teinte froide, un accent chaud ; l'accent n'apparaît que sur les valeurs verrouillées.
- [ ] Les trois couches (trame du fond, sujet, affichage) sont présentes et glissent à des vitesses différentes.
- [ ] Chaque pièce est reliée au reste et se reconnaît à sa silhouette.
- [ ] Aucun texte sur le fil de fer : chaque texte a sa plaque, et ne touche ni l'objet ni un autre texte.
- [ ] Chaque valeur reste lisible au moins 2,5 s avant d'être rangée.
- [ ] Aucune coupe ni fondu dans la scène ; un glitch au plus.
- [ ] Le sujet fait au moins un tiers de la hauteur aux moments clés.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 32

## 9. Aperçu

- Film de démo d'origine, *Volt · Spec Scan* (39 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/hologram-hud.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/hologram-hud.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/hologram-hud/STYLE.md`, `DEMO.md`, `demo/engine/holo.js`, `demo/engine/hud.js`, `demo/models/mkmodel.mjs`, `demo/content.json`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Rajdhani et Share Tech Mono : OFL 1.1.
- Adaptation Flot Web : traduction, disposition verticale des cartes et du rail, codes de couleur d'exemple, portage vers Three.js dans HyperFrames, numéros de mouvements, règles de son du plugin.
