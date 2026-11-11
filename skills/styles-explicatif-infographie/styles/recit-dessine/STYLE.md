# Récit dessiné (heure du conte)

## 1. Identité

- **Nom** : Récit dessiné, ou « heure du conte » (anecdote racontée à la première personne par un personnage simple).
- **Inspiration** : les chaînes d'anecdotes animées, où le créateur raconte une histoire personnelle et se dessine en petit personnage rond. On en reprend la grammaire de montage ; on ne reprend le personnage, le trait ni l'univers d'aucun créateur.
- **La règle en une phrase** : **la voix est le héros ; l'image est la « planche de réactions » de la voix**. Le personnage **passe d'une pose à l'autre en un dixième de seconde, puis se fige** ; le gag vient d'une coupe sur un **très gros plan de réaction**, pendant lequel **il se tait**.
- **Marche pour** : raconter une expérience, un raté, « ma première fois que… », à la première personne, avec un début, un retournement et **une chute sur laquelle on peut marquer une pause** ; une chaîne où le public vient pour « cette personne » ; un petit budget et un rythme de publication régulier (un personnage, cinq ou six poses, trois bouches suffisent pour un épisode).
- **Ne marche pas pour** : un tutoriel dense ou des chiffres (le spectateur guette le gag et ne retient pas les nombres : voir `typo-cinetique`) ; un contenu sans « je » (actualité, comparaison de produits : le personnage n'a rien à jouer) ; **une voix qui n'est pas drôle et n'a pas de pauses** : ce style amplifie la voix, il ne la sauve pas.
- **Personnage** : à construire avec le skill `personnages` (planche de poses et d'expressions dessinée, pas un bonhomme tracé à la va-vite en code : la source juge ces bonshommes génériques « reconnaissables au premier coup d'œil comme faits par une machine »). C'est **l'avatar du client** : un ou deux signes distinctifs (un chapeau, des lunettes, une coiffure) suffisent à le reconnaître.

## 2. Palette, typographie, matières

| Élément | Couleur (démo d'origine) | Règle |
|---|---|---|
| Peau | `#FFE2CC` | claire, presque blanche |
| Vêtement clair | `#FFFFFF`, détail `#E4E4E8` | le blanc tient grâce au contour noir |
| Vêtement secondaire | `#CDBB97` | |
| **Trait du personnage** | `#1B1B1F` | **le plus noir de tout le film** |
| Mur / table / sol | `#DCE9EC` / `#E2C29B` / `#E8DCC8` | peu saturés, très clairs : le décor est toujours plus « léger » que le personnage |
| Trait du décor | `#5B6470`, 3 px | plus clair, et au moins deux fois plus fin |
| Vide du plan de réaction | `#3D405B` + assombrissement radial | froid et sombre : toute l'attention sur le visage |
| Bouche / langue / joues | `#6E2430` / `#F07B7B` / rose à 35 % | la seule couleur saturée : la bouche qui s'ouvre se voit |
| Chiffre ou mot « frappé » | `#FFCB6B` | |

- **Trait du personnage = 5 % du rayon de la tête** (4 px au moins) : il grossit et s'affine avec le cadrage. **Trait du personnage au moins deux fois celui du décor** : c'est pourquoi « la personne ressort toujours ».
- **Formes** : tout est rond, rien n'est aigu. Tête : un rond un peu aplati. Corps : un haricot. **La tête fait environ 58 % de la hauteur totale.** Bras : un tube à bouts ronds, sans coude ni doigts ; la main est un rond. Aucun angle droit, sauf les accessoires.
- **Expressions** : surtout **les sourcils** (levés = surprise ; relevés à l'intérieur = peiné ; à plat = blasé). **Cinq bouches** : sourire en arc, trait droit, vague (inquiet), entrouverte, grande ouverte. Yeux : des points noirs avec un reflet blanc ; « yeux de poisson mort » : points rétrécis, sans reflet.
- **Décor** : il dit seulement « où » : un mur, une table, une fenêtre, **3 à 5 grands aplats**. Un fond blanc ou uni fonctionne aussi.
- **Polices** (libres) : une très grasse pour le mot ou le chiffre frappé (Poppins 900, Inter 900) ; sous-titres en blanc à contour noir.
- **Police de repli** : aucune à prévoir, Poppins et Inter sont fournies par HyperFrames et se chargent par leur nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/poppins`, `@fontsource/inter` (vérifié par `npm view` le 11/11/2026).

## 3. Composition 9:16

- **Plan moyen par défaut** : le personnage coupé à la taille, **la tête occupe 25 à 35 % de la hauteur** (480 à 670 px), centré un peu d'un côté ; l'autre côté est pour « ce dont il parle » (un écran, quelqu'un, un objet). En vertical : le personnage dans la moitié basse (y 800 à 1500), l'objet de son discours au-dessus ou à côté.
- **Plan de réaction** : le décor disparaît ; **le visage remplit le cadre** (en vertical, la tête fait environ 850 px de large, centrée vers y 850), fond uni sombre.
- **Plan du gag « à l'envers »** : un **très grand plan d'ensemble** où le personnage est tout petit (être minuscule et démuni est le gag).
- **Plan par-dessus l'épaule** : ce qu'il voit (un écran, un téléphone), avec **l'arrière de sa tête en amorce** au premier plan, détaillé (pas une silhouette noire, qui se lirait comme « un autre personnage »), bordé d'un liseré de lumière froide du côté de l'écran.
- **Les trois cadrages d'un même lieu sont un seul grand dessin du monde**, dans lequel seule la caméra change. Ce dessin doit **dépasser largement le plan le plus large**, sinon un bord noir apparaît.
- **Texte dans l'image** : seulement ce qui « doit être vu » : ce qui est sur l'écran du personnage, et **le chiffre clé**, frappé en très gros (200 à 260 px, dépassement de 23 %).
- **Sous-titres** : blancs, 50 à 54 px, contour noir de 10 px, entre y 1400 et y 1540 ; **la phrase entière entre et sort d'un coup, sans animation** (un sous-titre qui bouge vole le regard au personnage).
- Visage et chiffre à gauche de x 945.

## 4. Ce qui bouge

- **Action principale** : **changement de pose en 0,10 s, puis arrêt** de 0,4 à 0,7 s. Dans les originaux les plus typiques, **70 % des images sont strictement immobiles**. Au changement de pose, le corps se tasse de 7 % en hauteur et revient en ressort (0,35 s).
- **Boucles de fond** (minuscules, 1 à 2 % d'amplitude au plus) : (1) la **respiration** (le corps varie de ±1,2 % en hauteur, période de 1,6 s) et le **clignement** (2 images, toutes les 2,4 à 3,6 s, à des instants fixés d'avance) ; (2) la **bouche** qui suit le volume de la voix : trois formes (fermée, entrouverte, ouverte), **changée au plus 10 fois par seconde** (une image sur trois à 30 i/s) ; la tête s'abaisse un peu quand la bouche s'ouvre.
- **Autorisés** : coupe sèche `#046` (la grande majorité), coupe saccadée `#041` vers un cadrage deux fois plus serré, panoramique filé `#043` (0,26 s, avec flou de mouvement, vers ce qu'il regarde), très gros plan `#184`, par-dessus l'épaule `#180`, plan subjectif `#179`, plan d'ensemble `#183`, arrêt sur image `#040`, style image par image `#128` (personnage redessiné à chaque image du film, soit 30 par seconde ; la source tournait à 24 i/s ; caméra fluide), écrasement `#011` léger au changement de pose, apparition éclair `#001` avec dépassement `#010` (15 à 30 %) **pour les accessoires et les signes seulement** (« ? », « ! », goutte de sueur, chiffre), secousse d'impact `#024` (0,3 s) sur le chiffre frappé, plan fixe `#175`.
- **Interdits** : animation fluide de tout le corps, flottement `#096`, poussée lente et continue dans chaque plan, fondu `#044`, **entrée animée du personnage** (au premier plan d'une coupe, il est déjà en place et parle déjà), décor aussi contrasté que le personnage, sous-titres animés, bouche qui change à chaque image.
- **Le coup de poing visuel** : coupe sur le plan de réaction, qui arrive à 1,22 fois sa taille et revient à 1 en ressort, avec un éclair blanc à 55 % sur les 2 premières images.
- Le regard : les pupilles se déplacent vers ce qu'il désigne.

## 5. Rythme et montage

- **Les plans suivent les phrases de la voix, pas les temps d'une musique** : une phrase ≈ un plan. Durée moyenne d'un plan : **environ 2,4 s** (de 1 à 3 s) pour la variante la plus nerveuse, jusqu'à 5 ou 6 s pour une variante plus posée où le personnage bouge en continu à 15 dessins par seconde.
- **La transition se place dans la respiration entre deux phrases** ; sous-titre et coupe changent sur la même image. Jamais au milieu d'une phrase.
- **Le plan de réaction se place dans un silence** : après la phrase énorme, **ne pas enchaîner** : laisser **0,8 à 1,5 s** au visage, sans un mot (juste un petit détail : une goutte de sueur, un clignement lent, un sourcil qui tombe).
- **Après la chute, tenir au moins 0,9 s** : sinon « le temps du rire est coupé ».
- **Le chiffre dans l'image tombe sur la syllabe** où la voix le dit : même instant pour le chiffre, le coup sourd et la secousse.
- **Transitions** : coupe sèche ; coup de poing sur la réaction ; filé vers ce qu'il regarde ; saut vers un cadrage deux fois plus serré, sans changer de décor (« il vient de comprendre ») ; par-dessus l'épaule.

## 6. Recette technique

- **Moteur** : HyperFrames. Le personnage est une **bibliothèque d'images de poses** (du skill `personnages`) ou des pièces SVG ; le code règle la position, l'échelle, l'ancrage aux pieds et le changement d'image. Le décor : un grand dessin du monde mis en cache.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `monde.js` (le lieu, plus grand que le plan le plus large), `personnage.js` (poses, expressions, bouches, clignements), `histoire.js` (minutage des poses par phrase), `voix.json` (volume de la voix image par image, calculé hors ligne), `film.js`.

```js
const tPerso = t => Math.floor(t * 30) / 30;                              // personnage à chaque image (30 i/s ; 24 dans la source) ; caméra continue
// changement de pose : 0,10 s, puis un tassement de 7 % qui revient en ressort (volume conservé)
const tassement = dt => dt < 0 ? 0 : -0.07 * Math.cos(2 * Math.PI * 3.5 * dt) * Math.exp(-9 * dt);
perso.scaleY = 1 + tassement(t - tPose); perso.scaleX = 1 - tassement(t - tPose);
// bouche : trois formes selon le volume, changée au plus 10 fois par seconde
const v = VOLUME[Math.floor(Math.floor(t * 10) / 10 * 30)]; const bouche = v < 0.06 ? "fermee" : v < 0.22 ? "entrouverte" : "ouverte";
// clignement : instants fixés d'avance, 2 images
const cligne = CLIGNEMENTS.some(c => t >= c && t < c + 3 / 30);
```

- **Techniques clés** : une pose se remplace **d'un coup** avec un petit ressort ; on ne fond jamais deux silhouettes l'une dans l'autre (cela fait un double contour) ; aligner les poses par les pieds et par une taille médiane.
- **Pièges** : **tout faire bouger tout le temps** : le style vit de « coupe rapide puis arrêt », et tout ce qui flotte le rend « trop mou, trop lent » ; **un décor aussi travaillé que le personnage** : l'œil quitte le visage et le gag est perdu ; **pas de silence pour la réaction** ; un monde trop petit (bords noirs) ; une coupe au milieu d'une phrase ; une voix provisoire remplacée sans recalculer le volume (la bouche ne suit plus).

## 7. Son

- **La voix est tout** : enregistrée d'abord, avec ses pauses ; tout le montage s'y accroche.
- **Bruitages** : peu, et placés comme des blagues : un souffle sur un filé, un clavier, un « ploc », un **coup sourd sur le chiffre frappé**, une note grave « tadam » sur le coup de poing visuel, **des grillons pendant le silence de la réaction**, un « boing » sur un signe qui surgit.
- **Musique** : facultative, légère et discrète ; elle peut s'arrêter net sur la réaction.
- **Silence** : c'est l'outil principal du gag : 0,8 à 1,5 s sans voix sur le plan de réaction.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le personnage est un vrai personnage dessiné (planche de poses), reconnaissable à un ou deux signes.
- [ ] Les poses changent en 0,1 s puis se figent ; plus de la moitié des images sont immobiles.
- [ ] Le trait du personnage est au moins deux fois plus épais et plus noir que celui du décor.
- [ ] Le décor est clair, peu saturé, fait de 3 à 5 aplats.
- [ ] La bouche suit la voix, en trois formes, sans changer plus de 10 fois par seconde.
- [ ] Le plan de réaction est un gros plan silencieux de 0,8 à 1,5 s.
- [ ] Chaque coupe tombe entre deux phrases ; la chute est tenue au moins 0,9 s.
- [ ] Les sous-titres ne sont pas animés ; aucun bord noir à l'écran.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 13
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Planche de la démo d'origine (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y4_storytime_总览.jpg
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. La démo met en scène le personnage de son auteur, **exclu de la licence** : planche donnée en lien seulement, personnage non repris.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/y4_storytime.md`, `scripts/engine/demos/y4_storytime/`, `scripts/engine/lib/toon.js`. Licence MIT (© 2026 alchaincyf, 花叔), hors personnage de l'auteur.
- Adaptation Flot Web : traduction du chinois, personnage de la démo retiré (renvoi au skill `personnages`), cadrages verticaux, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
