# Table lumineuse d'archives

## 1. Identité
- **Nom** : Table lumineuse d'archives. Identifiant : `table-lumineuse-archives`.
- **Inspiration** : les documentaires d'archives qui entrent dans les photos fixes ; les enquêtes visuelles qui annotent de vraies images (une ligne, un relevé, une source par écran) ; les films macro de produit (arêtes de verre, lumière transmise). Grammaire seulement, aucun nom cité.
- **Principe** : de vrais objets d'archives (négatifs sur verre, diapositives, lettres, télégrammes, coupures, dessins) reposent sur une table lumineuse froide, éclairée par dessous. Une loupe descend sur l'un d'eux et, **dans le verre, l'objet s'anime** : un négatif devient positif, une ligne de texte s'allume, un nombre se détache de la page, une photo s'ouvre en profondeur. Numéros de catalogue, dates et relevés précis sont épinglés aux objets. Net, moderne et calme, **sans filtre vintage**.
- **Cinq règles** : les objets sont réels (scans à leurs vraies proportions, avec leurs vrais dégâts : coins cassés, plis, marques de crayon) ; la lumière vient d'en dessous ; **la loupe est la porte de la caméra** (toute plongée dans un objet passe par une loupe qui se pose dessus) ; vérité de catalogue (chaque objet porte son vrai identifiant, sa date et son titre) ; une seule couleur signal.
- **Pour quels sujets** : histoire d'une marque ou d'une famille à partir de ses archives, chronologie de documents, album, moment fondateur, « deux versions d'une même histoire », hommage.
- **Ne marche pas pour** : un sujet sans archives numérisées en bonne définition, une actualité, un sujet qui demande des graphiques. Ce n'est pas un dossier « papier journal tramé », ni un film de données (les nombres vivent sur les objets).

## 2. Palette, typographie, matières
- **Fond neutre** : la table (presque blanche, froide, `#F7F9FB`) et les tons propres des archives (gris d'argent, bruns de papier). **Ne pas réétalonner l'archive** dans une charte de couleurs.
- **Une couleur signal** (orange `#FF5A1F`) pour marques, relevés, ancres et verdict ; jamais en fond derrière une image, jamais en décoration.
- **Texte** : encre `#15171A` sur les zones claires, blanc papier sur plaques sombres `rgba(14,15,17,0.74)` ; choisir le contraste selon le fond, jamais couleur sur couleur.
- **Polices libres** : mono (IBM Plex Mono) pour identifiants, dates et relevés ; sans pour les libellés ; serif seulement pour les titres et le nom que porte une photo.
- **Police de repli** : aucune à prévoir, IBM Plex Mono est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/ibm-plex-mono` (vérifié par `npm view` le 11/11/2026).
- **Matières** : la table est une surface émissive avec léger grain de diffuseur, cadre d'aluminium, bureau sombre au-delà ; elle peut s'éteindre et se rallumer en vacillant. **Négatifs sur verre** : ils transmettent la lumière, teinte chaude d'argent ; les coins cassés laissent voir la table. **Papier** : rétroéclairé, il rayonne chaud sur ses bords. Ce qui est opaque se lit plus sombre que la table.
- **Loupe** : bague noire avec reflet de biseau, jupe d'acrylique clair qui réfracte la table et brille à son pied ; à l'intérieur, grossissement ≈ 2,5× avec légère déformation en coussinet au bord et fines franges colorées.
- **Finition** : légère vignette, grain fin (plus marqué dans les photos). Aucun dégât de pellicule, aucun sépia, aucune trame.

## 3. Composition 9:16
- **Disposer les objets en colonne ou en quinconce vertical** sur la table, serrés (la caméra glisse sur des objets, pas sur du vide).
- **Loupe** : diamètre ≈ 620 à 760 px à l'écran, posée entre y 420 et y 1150 ; au moment de lecture, le sujet occupe au moins un tiers de la hauteur.
- **Étiquettes attachées aux objets** : point et anneau d'ancrage, trait vertical, puis le texte (identifiant 28 px minimum en mono, libellé 30 à 38 px).
- **Relevé** : plaque sombre avec petit libellé au-dessus, valeur 90 à 120 px, et la source dessous (numéro de catalogue ou formulation d'origine). À gauche de x 945, au-dessus de y 1360.
- **Sous-titres** : bande centrée, y 1400 à y 1540, plaque sombre à bord signal de 3 px.
- **Deux fiches côte à côte** deviennent en vertical deux fiches l'une sur l'autre, chacune avec un recadrage de sa source.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : relevés et étiquettes hors des 140 px du bas.

## 4. Ce qui bouge
- **Action principale** : la loupe se pose et la caméra pousse dans le verre. Pose en décélération rapide (≈ 0,4 s), la loupe grossit d'environ 1,35× en se posant et projette une ombre douce ; elle se lève de la même façon. La caméra glisse sur la table, ralentit pour laisser la loupe se poser, puis pousse.
- **Boucles de fond** : (1) glissé lent de la caméra (déplacement et légère rotation) ; (2) infime vacillement de la table et grain qui vit.
- **Gestes** : **négatif en positif sous la loupe** (un front de « développement » part du centre de la lentille avec un mince bord chaud, seulement à l'intérieur du verre) ; **la ligne s'allume** (sur le papier, une ligne s'éclaircit pendant que le reste s'assombrit, un soulignement se trace, un mot ou un nombre se détache vers une carte de relevé) ; **dans la photographie** (le bord de la lentille grandit au-delà du cadre, la photo gagne une profondeur en couches et un sujet dérive) ; mesurer sur la photo (une règle posée en perspective sur le sol, graduations qui se resserrent vers l'horizon, marquée « schéma » quand c'en est un) ; deux fiches tenues côte à côte jusqu'à lecture avant d'en barrer une ; **la table devient l'index** (recul sur toute la table, l'étiquette de chaque objet s'envole dans une liste avec son identifiant et son relevé).
- **Autorisés** : #025 panoramique de table, #027 poussée, #016 parallaxe (dans la photo seulement, petite), #004 tracé, #080 ligne surlignée, #007 compteur, #162 agrandissement en visionneuse, #029 suivi le long d'une ligne, #172 plan-séquence.
- **Interdits** : coupes, fondus au noir, #140 pages qui tournent entre les objets ; contenu de l'archive qui bouge hors d'un espace photo ; table qui bouge ; voile vintage ; loupe qui balaie de la table vide (elle tombe droit sur l'objet).

## 5. Rythme et montage
- 30 i/s (la source était à 24 i/s ; rien dans le style n'en dépend) ; chaque paramètre de caméra sur des courbes lisses sans dépassement.
- **La vitesse vit dans les glissés et les poussées ; les tenues sont pour lire.**
- Transitions faites par la loupe (poser, pousser, remonter, lever) et par le glissé.
- Lignes tracées en 0,3 à 0,6 s ; texte révélé depuis le côté de son trait de rappel ; nombres qui comptent et se posent avec la voix.
- Vrais silences avant une révélation ou un verdict ; le premier son après est la loupe, le lieu ou le verdict.
- **Citer la source quand c'est possible** : un recadrage de la vraie ligne, ou la formulation de la notice entre guillemets, vaut mieux qu'une paraphrase.
- **Version courte (8 à 12 s)** : une photo, une pose de loupe (avant 3 s), une étiquette, une valeur.

## 6. Recette technique
- **Moteur** : HyperFrames en 2.5D. Un monde = la table ; chaque objet est une image posée avec centre, rotation et échelle (pixels du scan → unités du monde à taille réelle) ; la caméra est un centre 2D, un zoom et une rotation ; table et marques passent par la même fonction monde → écran. La loupe est un élément rond à `overflow: hidden` qui contient **une seconde copie de la scène**, agrandie 2,5× autour du point visé : c'est dans cette copie que l'objet change d'état. **Blender** par le connecteur `blender` pour une vraie réfraction de la jupe et de vrais reflets.
```js
// l'intérieur de la loupe : même monde, grossi autour du point p (en coordonnées écran)
const G = 2.5;
interieur.style.transform = `translate(${R - p.x * G}px, ${R - p.y * G}px) scale(${G})`;
// négatif → positif : un masque radial qui grandit depuis le centre de la lentille, sur la copie intérieure seulement
tl.fromTo(positif, {clipPath: "circle(0% at 50% 50%)"}, {clipPath: "circle(75% at 50% 50%)", duration: 1.2, ease: "power2.out"}, T);
```
- **Négatif** : préparer le positif par inversion du scan (les positifs peuvent être légèrement redressés en niveaux ; les négatifs restent tels que le verre les donne) ; masque d'émulsion tiré du scan pour que les coins cassés montrent la table.
- **Espace photo** : découper les sujets debout en couches (voir `detourage-sujet`), combler derrière eux, garder des mouvements 2.5D assez petits pour que le comblement se voie à peine. Une seule carte de profondeur pour une photo avec des personnes les déchire.
- **Où trouver des archives** : collections ouvertes avec fichiers maîtres et notices (grandes bibliothèques nationales, musées en accès ouvert CC0, archives nationales, portails européens : vérifier la mention de droits de chaque objet). CC0, domaine public et CC BY (crédité) conviennent. Pour l'histoire d'une marque : demander au client ses scans, ses numéros d'archive et son droit de les utiliser.
- **Pièges** : scan faible trop grossi (rester sous ~1,5 pixel écran par pixel de scan dans la lentille ; choisir les objets par taille de scan) ; étiquette sur une table en mouvement qui sort du cadre avant d'être lue (tenir la caméra ou fixer la légende à l'écran) ; **dérive vintage** : l'âge est dans les objets, pas dans l'étalonnage.

## 7. Son
- **Ambiance** : ronflement du ballast de la table lumineuse, clics d'amorçage, bruit de pièce. Dans une photographie, le ronflement cède la place à l'air du lieu.
- **Bruitages** (budget du skill `son`) : la loupe sur le verre (claquement avec tintement aigu), froissement de papier pour les glissés et les lignes allumées, tics pour échelles et compteurs, trait de plume pour un verdict.
- **Musique** retenue et petite : piano feutré, quelques cordes, verre ou métal frotté pour les moments où l'on « voit ». Construire par subdivision et registre, pas par des percussions.
- Voix calme, phrases courtes qui disent ce que dit l'objet ; musique ≈ 10 dB dessous ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Chaque objet est un vrai scan, avec identifiant, date et titre de son détenteur, de licence claire, listé dans `CREDITS`.
- [ ] Aucun sépia, trame ni vieillissement ajouté ; l'archive n'est pas réétalonnée.
- [ ] Toute plongée dans un objet passe par la loupe ; aucune coupe ni fondu entre objets.
- [ ] Une seule couleur signal, jamais en aplat derrière une image.
- [ ] Intérieur de la loupe sous 1,5 pixel écran par pixel de scan (mesuré).
- [ ] Les nombres à l'écran viennent de la notice ; une mesure estimée sur photo porte « schéma » ; `FAITS.md` à jour.
- [ ] Dans l'espace photo, les personnes ne sont pas cisaillées (contrôle image par image sur le mouvement le plus ample).
- [ ] Étiquettes lisibles le temps de leur tenue ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/archive-lighttable.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/archive-lighttable.jpg
- Crédit : « Two Seconds Short », LemoLab, CC BY 4.0 ; objets d'archives de tiers (domaine public et licences propres) : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/archive-lighttable/STYLE.md`, `style.json`, `demo/film.js` (`IT`, `toW()`, `w2s()`, `dive()`, `annot`, `measure`, `compare`, `indexPanel`), `demo/tools/prep.py`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, table en colonne pour le 9:16, HyperFrames 2.5D (la démo d'origine utilise un shader), Blender en option.
