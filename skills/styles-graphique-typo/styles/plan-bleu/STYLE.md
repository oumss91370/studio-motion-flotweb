# Plan bleu (dessin technique)

## 1. Identité

- **Nom** : Plan bleu (dessin d'ingénieur sur papier cyanotype).
- **Inspiration** : les dessins techniques animés de certains génériques de fin de film, les pages de carnets d'inventeurs de la Renaissance, les dessins de brevets du XIXᵉ siècle (Fig. 1 / Fig. 2, bulles de repère numérotées, hachures fines). On n'en recopie rien : pas de vrai brevet, pas de machine ni de signature d'un inventeur réel.
- **Ce qui le fait reconnaître** : **tout le film se passe sur une seule feuille** posée sur une table à dessin sombre ; des traits blancs sur un bleu de Prusse inégal ; un langage de dessin au trait en 2D (vues de face, de côté, perspective cavalière), **jamais de rendu 3D** ; le dessin est sec et exact, ce sont les notes qui portent l'humour, la chaleur ou la gravité. La chose dessinée est le personnage.
- **Marche pour** : expliquer comment un objet est fait ou fonctionne, lancement de matériel, projet d'architecture ou de rénovation, invention, versions successives d'un produit, recette vue comme une notice. Films de 30 à 60 s.
- **Ne marche pas pour** : un sujet avec des personnes et des visages (on ne voit qu'une ombre de main et une signature), un produit de mode ou de beauté, un sujet sans objet concret. Ce n'est pas un hologramme (pas de fil de fer lumineux, pas de rotation 3D), ni un tableau blanc.

## 2. Palette, typographie, matières

**Bleu et blanc seulement.** Le bleu varie en valeur (couche sensible, taches, plis) ; le blanc varie en épaisseur et en douceur, jamais en teinte.

| Rôle | Exemple |
|---|---|
| Feuille (du sombre au clair) | `#18336B` → `#2A58A6` |
| Traits | `#E7F0F9` |
| Table à dessin | `#0D1116` |
| Variante feuille passée au soleil | `#3A6DA8` → `#5B8CC4` |
| Variante feuille surexposée | `#0F2350` → `#1D3F80` |

- **Une seule couleur non bleue, utilisée exactement une fois** : l'encre d'un tampon (rouge classique, vert APPROUVÉ, noir ANNULÉ). Elle porte le verdict.
- **Polices** (libres) : Architects Daughter (lettrage à la main : en-tête, étiquettes, notes, sous-titres), B612 (cases du cartouche), Allura (signature seulement).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place d'Architects Daughter ; Inter à la place de B612 ; Playfair Display à la place d'Allura. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/architects-daughter`, `@fontsource/b612`, `@fontsource/allura` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Feuille** : cyanotype procédural (bruit entre deux bleus, coulures de la couche, fibres, plis avec un bord clair et un bord sombre, bords décolorés, piqûres). Autour : toile sombre et ombre portée.
- **Traits** : quatre épaisseurs (contour, détail, fin, cheveu : 3,2 / 2,0 / 1,25 / 0,9 unités de feuille), légèrement doux, avec de petits manques d'encre guidés par le grain du papier.
- **Conventions de tirets** : axe (long-court), arête cachée (tirets courts), plan de coupe (long-court-court). Hachures à 45°, espacées de 8 à 14 unités, pour les coupes et les masses.
- **L'eau** : une goutte fait une auréole d'un bleu plus profond avec un liseré pâle ; les traits y deviennent flous.

## 3. Composition 9:16

- La feuille est dessinée **en portrait** : en-tête en haut (c'est le titre du film), cartouche et nomenclature en bas, colonne « NOTES GÉNÉRALES » le long du bord gauche ou sous la figure.
- Plans de récit rapprochés : la figure occupe environ 80 % de la largeur utile, avec du « ciel » vide au-dessus. Les plans larges sur toute la feuille sont rares.
- Garder la figure principale loin des bords de la feuille, sinon les plans larges montrent la table.
- **Sous-titres = notes de dessin** : un cadre clair translucide à double filet blanc, une case « NOTE / n », le texte lettré en 0,35 s environ, un petit trait de rappel. **Placés plan par plan dans le ciel vide**, jamais collés en bas (le bas d'un dessin, c'est la ligne de sol et le cartouche). Largeur 800 px au plus, lettres de 44 à 52 px, entre y 200 et y 1500.
- Chaque sous-titre est aussi recopié dans la colonne de notes : le plan large final montre toute la voix off sous forme de notes.
- Étiquettes et cotes : 30 px au moins à l'écran.

## 4. Ce qui bouge

- **Action principale** : l'objet se dessine tout seul dans l'ordre du dessinateur (axes, contours, détails, hachures, cotes, bulles, étiquettes), une couche par temps, avec une pointe lumineuse en tête de trait.
- **Boucles de fond** : (1) les mécanismes qui avancent cran par cran comme un échappement (une dent par subdivision, les dents s'engrènent vraiment) ; (2) les annotations vivantes : les cotes mesurent les pièces qui bougent et les chiffres changent.
- **Autorisés** : tracé de ligne `#004`, machine à écrire `#006` (le texte s'écrit de gauche à droite), vue éclatée `#143`, compteur `#007`, panoramique `#025` d'une figure à l'autre, travelling avant lent `#027`, plan fixe `#175`, gros plan en coupe sèche sur un temps fort `#184`, secousse d'impact `#024` (très légère, pour un tampon ou une feuille qui claque).
- **Interdits** : fondu enchaîné `#044`, orbite 3D `#030`, lueur et néon, particules `#015`, rebond `#123` sur le dessin, dégradés de couleur.
- **Vue éclatée** : les pièces partent l'une après l'autre sur des subdivisions du temps, et reviennent une par groupe de temps avec un clic.
- **Jeu de la machine** : les angles, les affaissements et les aiguilles de jauge sont son visage. Échec = ralentir et s'affaisser en 1,5 s environ ; joie = se redresser d'un coup, aiguille qui dépasse.
- **Une seule fois, au plus** : un symbole du dessin devient réel (une flèche de cote s'envole, une hachure devient pluie). Il prend du volume, une lueur blanche, une ombre qui tombe sur les traits, et laisse une empreinte pâle là où il était dessiné.

## 5. Rythme et montage

- Caméra et tracés fluides. Mouvements continus à l'intérieur d'une partie, **coupes sèches sur les temps forts** entre les parties.
- Plans de 3 à 7 s ; un tracé long peut tenir 8 s si une couche nouvelle arrive à chaque temps.
- Transitions propres au style : la coupe sur un temps fort, ou le numéro de figure barré et réécrit (« FIG. 1 » devient « FIG. 2 · VUE ÉCLATÉE »). Jamais de fondu.
- Laisser le moment le plus émouvant sans voix.
- **Version courte (8 à 12 s)** : un seul objet : axes et contours (3 s), cotes et étiquettes (3 s), cartouche tenu 2 s ; couper la vue éclatée. Accroche : le premier trait à l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames. Canvas 2D pour le dessin, et de préférence un shader WebGL pour la feuille (elle reste nette à tout niveau de zoom). Un papier en image fixe haute définition convient pour un premier essai.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (feuille, taches, ombres, tampon), `trace.js` (caméra, perspective cavalière, tracés progressifs, solides remplis de « papier », hachures, cotes, bulles, texte), `feuille.js` (cadre, en-tête, cartouche, notes), `film.js` (timeline sur une grille de temps). Chaque nouvelle machine a son propre module.

```js
// épaisseur à l'écran : ni saucisse en gros plan, ni trait invisible en plan large
const epaisseur = (unites, zoom) => unites * Math.pow(zoom, 0.65);
// tracé progressif : on coupe le chemin à la longueur d'arc voulue, pointe lumineuse en tête
function tracer(ctx, pts, p) { const L = longueur(pts) * p; dessinerJusqua(ctx, pts, L); pointe(ctx, pointA(pts, L)); }
```

- **Techniques clés** : masquage par ordre de peinture (chaque solide est rempli de « papier » avant que son contour soit tracé) ; extrusion cavalière en traçant le contour à N pas de profondeur ; composition en trois calques (encre, effets, sous-titres en dernier) ; les ombres assombrissent aussi les traits, c'est ce qui prouve qu'un objet a quitté le papier.
- **Pièges** : épaisseurs non adaptées au zoom ; une vue éclatée vers le haut percute l'en-tête (éclater sur les côtés) ; des sous-titres dessinés dans le calque d'encre disparaissent hors de la feuille ; une forme faite de plusieurs boules ombrées une à une ressemble à une grappe de raisin (un seul dégradé sur l'union) ; un objet final trop petit gâche le retour (un tiers de la hauteur, centré).

## 7. Son

- **Musique** : contrepoint mécanique : clavecin, basson, cordes en spiccato, harpe, célesta, boîte à musique. Des lignes en imitation (invention, canon) sonnent comme des pièces qui s'engrènent.
- **Bruitages** : papier (rouleau qui craque, feuille qui claque, té en bois qui glisse, plume technique qui gratte sur la durée du trait, compas, gomme) ; laiton et bois (clics de pièces, tic d'échappement, chaîne, ressort) ; eau (gouttes sourdes) ; tampon ; capuchon de stylo.
- **Silence** : il ne contient que des bruits de papier.
- **Voix** : sèche, discrète, comme on lit des notes de conception ; quelques phrases courtes.
- Les souffles de transition sont filtrés dans l'aigu pour ne pas masquer les consonnes.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Bleu et blanc seulement, plus une couleur de tampon utilisée une seule fois.
- [ ] Aucun rendu 3D, aucune lueur de néon : uniquement du trait.
- [ ] L'ordre de tracé est celui du dessinateur (axes d'abord, étiquettes en dernier).
- [ ] Quatre épaisseurs de trait, qui restent lisibles en gros plan et en plan large.
- [ ] Les sous-titres sont des notes placées dans le vide de chaque plan, jamais sur la figure ni en bas.
- [ ] Les engrenages s'engrènent vraiment et avancent cran par cran.
- [ ] Le « symbole devenu réel » apparaît une fois au plus.
- [ ] En plan large, on ne voit pas le bord de la table couper la figure.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 30

## 9. Aperçu

- Film de démo d'origine, *Patent Pending: The Cloud Catcher* (47 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/blueprint.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/blueprint.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/blueprint/STYLE.md`, `DEMO.md`, `demo/paper.js`, `demo/draw.js`, `demo/sheet.js`, `demo/film.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Architects Daughter, B612, Allura : OFL 1.1.
- Adaptation Flot Web : traduction, feuille en portrait, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
