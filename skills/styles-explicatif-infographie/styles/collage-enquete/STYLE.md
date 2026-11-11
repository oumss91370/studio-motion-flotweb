# Collage d'enquête (style Vox)

## 1. Identité

- **Nom** : Collage d'enquête. « Style Vox » désigne une inspiration (les vidéos explicatives de la presse en ligne faites de papiers, de coupures et de photos) ; ce n'est ni un contenu officiel, ni une affiliation.
- **Fiche fusionnée** de deux sources : la grammaire « collage » de huashu (mesurée sur cinq vidéos : couleurs, cadences, mouvements de caméra) et l'explicatif documentaire de Charlie Hills (types de plans, règles de relecture, faits sourcés).
- **La règle en une phrase** : on pose le raisonnement **sur une table couverte de vrais documents** (coupures de presse, photos, pièces) ; la caméra s'y déplace comme l'œil d'un journaliste d'enquête ; les traits et le surligneur se posent **par à-coups** ; l'impression de preuve vient du fait que **ces choses ont vraiment été posées là**.
- **Marche pour** : « comment c'est arrivé », « qui a dit quoi et quand » : actualité, histoire, portrait, carte ; une question en « pourquoi » qu'un inconnu comprend à moitié ; tout moment où le spectateur doit **voir la source de ses yeux** (une citation, un chiffre, une date).
- **Ne marche pas pour** : un pur mécanisme ou un concept sans aucun document à montrer (on fabriquerait de « fausses archives » : voir `science-a-plat`) ; une démonstration pas à pas (voir `tableau-blanc-a-la-main`) ; beaucoup de jeu de personnages.
- **Ce style n'invente rien** : ni fait, ni date, ni citation. Il ne redessine pas de mémoire le logo d'une marque réelle (on utilise les fichiers du client, ou le nom écrit en lettres simples). Il dit « **une** raison », jamais « **la** raison », et « ressemble à » quand la recherche ne montre qu'une ressemblance.

## 2. Palette, typographie, matières

**Trois familles de couleurs ; ni blanc pur, ni noir pur.**

| Rôle | Couleur (mesurée sur les originaux) | Variante « papier clair » (Charlie Hills) |
|---|---|---|
| Fond presque noir / carton noir | `#171716`, `#1b1b1a` | bleu nuit `#14213D` |
| Table en papier | `#e4ddcf` | papier `#FBF7EE`, crème `#F1E6D0` |
| Blanc de papier | `#E0DCDA` à `#EEEDED` | |
| Rouge, deux valeurs | vif `#B65255` (traits ; `#b8433f` pour mieux lire à l'écran), sombre `#93403C` (aplats) | `#B8312A` |
| Surligneur | jaune olive `#DACF08`, en mode multiplication, à 90 % | accent jaune `#F2C230` |
| Vieux papier de carte / parchemin | `#E4DCCF` / `#CFB195` | |

- **Matières** : les photos sont **en niveaux de gris, tramées à 45°**, avec un bord blanc et deux bouts d'adhésif translucide ; les coupures de presse ont un **bord déchiré**, un papier jauni, un titre en caractères à empattement ; les étiquettes sont des **bandes noires à texte blanc gras** (« 2012 · NOM ») ; les fiches sont en papier ligné. Le grain du papier est **fixe** : il ne grouille pas d'image en image.
- **Ombres très faibles** : flou 10, décalage (3 ; 6), opacité 0,28.
- **Imparfait exprès** : trop propre, cela ressemble à une publicité plutôt qu'à un travail de rédaction.
- **Personnes** : une vraie photo détourée, traitée comme un autocollant (bord de papier blanc de 12 px, ombre). Seulement des photos dont le client a les droits.
- **Polices** (libres) : une condensée grasse pour les étiquettes et les phrases chocs (Oswald, Bebas Neue, Anton) ; une police à empattement pour les coupures (Libre Baskerville, Playfair Display) ; une police de machine à écrire pour les annotations (Special Elite, Courier Prime).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : League Gothic à la place de Bebas Neue et d'Anton ; EB Garamond à la place de Libre Baskerville ; Oswald, Playfair Display : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/bebas-neue`, `@fontsource/anton`, `@fontsource/libre-baskerville` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Finition à l'export** : grain fin, léger assombrissement des bords, franges de couleur **sur les bords du cadre seulement**. Pas de dégradé sur le texte, pas de lueur.

## 3. Composition 9:16

- **Le vrai document est le plan principal** : capture, texte original ou photo **remplit le cadre ou presque**, et l'on pousse jusqu'à la phrase à lire. La table est le monde que la caméra traverse, pas un fond pour de petites images. Test : plus de **2 plans de suite** où le document fait moins de 60 % de la largeur, c'est une mise en page « cadre photo ».
- En vertical, un document en portrait (une page, une coupure, une photo) remplit naturellement : le présenter à 90 % de la largeur ; la table se parcourt de haut en bas.
- **Le texte à lire est sur la couche du dessus, dessiné en dernier** : une photo, une pince ou une carte posée ensuite qui recouvre le texte est la faute la plus fréquente de ce style.
- **Le point d'arrivée de la caméra se calcule d'après ce qu'il faut lire à cet instant** (on encadre la cible, on laisse une marge). Une étiquette voisine à moitié dans le cadre est poussée dehors.
- **Sur une table qui s'accumule**, à chaque nouvelle carte, **relire à la suite tous les textes visibles** : deux cartes voisines peuvent former une phrase fausse.
- **Tailles** : phrase choc en trois lignes courtes, 110 à 150 px, sur une bande de papier déchiré ; étiquettes 44 à 56 px ; texte de coupure à lire 40 px au moins après zoom ; annotations 36 px au moins.
- **Grilles** : cartes de même taille, mêmes écarts. Une grille de travers se lit comme une erreur. En vertical : 2 colonnes sur 3 ou 4 rangées.
- **Un logo remplit sa carte** ; un petit logo qui flotte dans une grande boîte a l'air faux.
- Zone utile : x 60 à 945, y 160 à 1560.

**Les types de plans** (un par phrase du script) :

| Plan | Sert à |
|---|---|
| Phrase choc | une phrase qu'on veut qu'on retienne : trois lignes courtes en condensée grasse sur une bande déchirée |
| Cartes de papier | montrer plusieurs choses à la fois (logos, produits, citations) : des cartes à bord déchiré tombent avec de petites ombres |
| Avant / après | un changement dans le temps : même carte, la pastille de date bascule |
| Étiquette pointée | nommer une chose dans une image : un cercle au marqueur se trace, puis une étiquette |
| Compteur | un nombre qui grandit, construit en code, jamais deviné |
| Grille | « ils se ressemblent tous » : beaucoup de tuiles identiques, puis une seule rompt le motif |

## 4. Ce qui bouge

- **Action principale** : la caméra trouve un document, s'approche de la phrase, et un trait la souligne.
- **Deux cadences (le cœur du style)** : la **caméra est fluide** ; les **éléments avancent par à-coups, 15 fois par seconde** (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) (croissance d'une zone sur une carte, tracé d'un trait rouge, texte tapé, cercle à la main, arrivée d'une carte).
- **Boucles de fond** : (1) à l'intérieur d'une carte, un tracé, un surlignage ou un texte tapé qui avance par à-coups ; (2) sinon rien : **à l'arrêt, la table est vraiment à l'arrêt**. Pas de dérive lente.
- **Autorisés** : style image par image `#128`, surligneur `#080` (1,5 à 3 s par ligne, au rythme des mots de la voix), soulignement `#086` (0,5 à 1 s), tracé de ligne `#004` (cercle rouge en 1 s environ, d'un seul geste, **non fermé**, les bouts se croisent un peu), machine à écrire `#006` (13 caractères par seconde, par à-coups), compteur `#007`, coupe sèche `#046`, travelling de suivi `#029` le long d'un trait rouge, travelling avant `#027`, zoom arrière `#028`, raccord de forme `#042`, plan d'insert `#185`, très gros plan `#184`, bichromie `#116`.
- **Interdits** : transition « papier qui se déchire » (elle vient des banques de modèles, pas des originaux), **texte tapé comme seul effet partout**, dégradés sur le texte, lueur `#022`, rebond `#123`, mouvement lisse « d'entreprise » sur les éléments, dérive continue de caméra, grain qui grouille, objets qui tombent et rebondissent.
- **Entrées** : une photo d'archive ou une coupure **est là dès la coupe** : elle ne surgit pas, ne tombe pas. Seule exception : quand on suit une chronologie, la carte suivante **glisse depuis le hors-champ**, penchée de 5 à 15°, et se redresse en 0,8 s environ.
- **Caméra** : durée médiane d'un mouvement 1,3 s (0,7 à 2 s), **jamais linéaire** ; accélération-décélération symétrique pour « aller chercher la carte suivante » ; départ vif et longue fin pour « reculer et révéler » et « suivre un fil ».
- **Alterner les révélations** : écrire la liste (déjà là à la coupe, poussée, glissement vers la carte suivante, surligneur, trait rouge qui relie, tampon, carte qu'on retire) et ne pas enchaîner la même séquence plus de **3 fois**.
- **Une action officielle ne se joue qu'une fois** : rejouée après une poussée, elle se lit comme « c'est arrivé de nouveau ».

## 5. Rythme et montage

- **30 à 60 s, 8 à 14 plans, une phrase par plan.** Le plan 1 est la question elle-même, dite en grand ; la première surprise arrive **avant 5 s** ; le dernier plan est la conclusion, en cinq mots au plus.
- Chaque plan répond à quelque chose que la phrase précédente a dit. Si l'on ne peut pas dire ce qu'un plan prouve, on le coupe.
- **La coupe sèche domine**, placée sur la ponctuation de la voix.
- **Transitions** : (1) coupe sèche ; (2) **glissement le long d'un trait rouge** (1,3 à 1,8 s), la carte suivante entre en biais et se redresse ; (3) **poussée dans un papier ou une photo, puis coupe vers le même document en grand** (1 à 1,4 s) ; (4) **recul depuis une photo jusqu'à tout le collage** (environ 1 s) ; (5) croissance d'une zone ou tracé d'un itinéraire sur une carte (2,5 à 3,5 s, par à-coups, tête du trait marquée d'un point rouge) ; (6) une feuille qui glisse en arc avec son ombre.
- Chaque plan tient assez longtemps pour être lu à voix haute.
- **Version courte (8 à 12 s)** : trois plans : la question en grand (2 s), un document dont la phrase est soulignée (4 s), la conclusion (3 s) ; coupes sèches seulement (les glissements de 1,3 à 1,8 s ne tiennent pas). La première surprise arrive avant 3 s, et non 5.

## 6. Recette technique

- **Moteur** : HyperFrames. Les documents en `<img>` ou dessinés sur canvas ; la table est un grand conteneur que la caméra parcourt ; canvas 2D pour la trame des photos et les traits.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `FAITS.md` (chaque nom, date et nombre, avec son lien ; **rien ne va à l'écran qui n'y soit pas**), `table.js` (position de chaque document dans le monde), `materiaux.js` (trame, bord déchiré, adhésif, bande d'étiquette, fiche), `traits.js` (surligneur, soulignement, cercle, trait de liaison), `camera.js`, `film.js`.

```js
const pas15 = t => Math.floor(t * 15) / 15;                 // les ÉLÉMENTS par à-coups ; la caméra reste continue
// surligneur : avance au rythme des mots de la voix, par à-coups, en mode multiplication
ctx.globalCompositeOperation = "multiply"; ctx.fillStyle = "rgba(218,207,8,.9)";
ctx.fillRect(ligne.x, ligne.y, ligne.l * borner((pas15(t) - t0) / duree), ligne.h);
// caméra : départ vif, longue fin, pour suivre un fil ou reculer
gsap.registerEase("longueFin", CustomEase.create("longueFin", ".33,0,.2,1"));
tl.to("#table", { x: -cible.x, y: -cible.y, scale: cible.zoom, duration: 1.3, ease: "longueFin" }, tPonctuation);
```

- **Pièges** : le texte recouvert par un élément posé après lui ; deux étiquettes voisines qui forment une phrase fausse ; une photo qui passe en fondu ; un zoom sur une image en basse définition (couper vers une version haute définition du même document : la trame qui grossit se lit comme « une meilleure copie ») ; flou de mouvement ailleurs que pendant un glissement rapide.
- **Relecture d'éditeur avant l'export** : une image du milieu de chaque plan ; chaque date et chaque nom identique à la liste de faits, au caractère près ; aucune carte sur le texte d'une autre ; rien de lisse qui devrait être saccadé ; la question visible dans les 3 premières secondes.

## 7. Son

- **Le son n'est pas facultatif** : un explicatif muet paraît inachevé. Un lit grave, un accent sur chaque nouveau plan, une levée sur la dernière phrase.
- **La voix est au-dessus de tout** : si l'on n'entend pas la narration par-dessus les effets, on baisse la musique.
- **Bruitages** (papier et bureau, vrais enregistrements) : feuille qu'on pose ou qu'on fait glisser, marqueur et surligneur qui frottent, adhésif, tampon, machine à écrire, déclic d'appareil photo, trombone. Un accent par plan, pas un son par à-coup.
- **Silence** : une courte pause avant la conclusion.
- **Voix** : ton de journaliste : citation, preuve, cause. « Regardez cette phrase », « notez ce chiffre » : l'image va alors surligner cette phrase.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque fait à l'écran a sa source dans la liste de faits ; rien n'est inventé.
- [ ] Les vrais documents remplissent le cadre ; pas plus de 2 plans de suite en « petit cadre ».
- [ ] Les éléments bougent par à-coups (15 par seconde) ; la caméra est fluide ; à l'arrêt, tout est à l'arrêt.
- [ ] Le texte à lire n'est jamais recouvert, et les textes voisins ne forment pas une phrase fausse.
- [ ] Ni blanc pur ni noir pur ; un seul rouge (deux valeurs) et un surligneur.
- [ ] La même séquence de révélation ne revient pas plus de 3 fois ; aucune « déchirure de papier ».
- [ ] La question est visible dans les 3 premières secondes, la première surprise avant 5 s.
- [ ] Aucun logo redessiné de mémoire ; photos de personnes avec droits.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 16
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Grammaire « collage », planche de la démo (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y2_vox_总览.jpg — crédit : 花叔 Huashu (alchaincyf). La démo contient le personnage de son auteur (exclu de la licence) : lien seulement.
- Explicatif documentaire : présentation de l'auteur sur https://github.com/charlie947/motion-graphics-skills — crédit : Charlie Hills.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/y2_vox.md`, `scripts/engine/demos/y2_vox/`, `scripts/engine/lib/collage.js`. Licence MIT (© 2026 alchaincyf, 花叔), hors personnage de l'auteur.
- Dépôt `charlie947/motion-graphics-skills`, commit `229022e`, fichier `skills/vox-explainer/SKILL.md`. Licence MIT (© 2026 Charlie Hills).
- Adaptation Flot Web : fusion des deux sources (là où elles divergent, les mesures de huashu priment : par exemple pas de grain qui bouge), traduction, composition verticale, polices libres, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
