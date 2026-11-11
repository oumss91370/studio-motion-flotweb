---
name: styles-explicatif-infographie
description: "Catégorie de styles « Explicatif et infographie » (17 styles : données au crayon, infographie isométrique, keynote sombre, keynote produit, screencast vivant, hologramme, plan de métro, livre d'images isométrique, circuit imprimé, maths animées, graphique animé, tableau blanc à la main, collage d'enquête, science à plat, récit dessiné, présentateur, nombre-jalon) et 16 effets premium. À utiliser quand le client veut expliquer quelque chose, montrer des chiffres, présenter un produit ou un fonctionnement."
---

# Styles « Explicatif et infographie »

Cette catégorie regroupe les styles dont le métier est de **faire comprendre** : un mécanisme, des données, un produit, une règle, une histoire vraie. La plupart se construisent autour d'une voix off : c'est elle qui fixe le minutage, et l'image **pose chaque nom et chaque chiffre à l'instant où il est dit**.

Ce skill ne pilote pas la vidéo. Le parcours (questions, histoire, look, storyboard, construction, revue, livraison) est dans `studio-coeur`. Les règles de mouvement et le dictionnaire des 192 mouvements (numéros `#001` à `#192` cités dans les fiches) sont dans `principes-mouvement`. L'export est dans `rendu`, le son dans `son`, la 3D dans `blender`, les personnages dans `personnages`, les couleurs et polices du client dans `marque`. Ici on trouve seulement **le look et sa recette**.

## Les 17 styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `donnees-crayon` | Données au crayon | De vraies données tracées marque par marque au crayon rouge et bleu, avec des notes manuscrites | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/dataviz.mp4) |
| `graphique-anime` | Graphique animé | Graphique de presse : le repère, puis les données qui poussent, puis une seule annotation | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t3_finance_chart_总览.jpg) |
| `nombre-jalon` | Nombre-jalon | Des milliers de points se rassemblent en un vrai nombre | hyperframes | facile | [image animée](https://github.com/charlie947/motion-graphics-skills/blob/main/assets/readme/demo-milestone.gif) |
| `maths-animees` | Maths animées (style 3Blue1Brown) | Fond noir, une couleur par concept, une forme se transforme en la suivante | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t1_3b1b_总览.jpg) |
| `tableau-blanc-a-la-main` | Tableau blanc à la main | Une main écrit et dessine pendant que la voix parle ; à la fin on voit tout le tableau | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y3_whiteboard_总览.jpg) |
| `collage-enquete` | Collage d'enquête (style Vox) | De vrais documents sur une table, surlignés et reliés de rouge | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y2_vox_总览.jpg) |
| `science-a-plat` | Science à plat (style Kurzgesagt) | Une idée devient un objet rond et lumineux ; la caméra voyage entre les échelles | hyperframes | élevée | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y1_kurzgesagt_总览.jpg) |
| `recit-dessine` | Récit dessiné (heure du conte) | Un personnage rond raconte une anecdote : poses rapides, arrêts, gros plan de réaction | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y4_storytime_总览.jpg) |
| `presentateur` | Présentateur | Un personnage dessiné explique entre documents, graphiques et grands nombres | hyperframes | élevée | aucun (à produire) |
| `keynote-produit` | Keynote produit (style Apple keynote) | Un écran, une chose ; la vraie capture du produit en grand ; le chiffre tombe quand on le dit | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t2_keynote_ui_总览.jpg) |
| `keynote-sombre` | Keynote sombre | Scène noire, interface dessinée, un seul accent, tout s'accroche à la grille | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/dark-keynote.mp4) |
| `screencast-vivant` | Screencast vivant | Faux enregistrement d'écran redessiné, habité par une mascotte en pixels | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/living-screencast.mp4) |
| `hologramme-hud` | Hologramme de science-fiction | L'objet en fil de fer lumineux ; des cadres se verrouillent sur ses pièces | three (dans hyperframes) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/hologram-hud.mp4) |
| `infographie-isometrique` | Infographie isométrique | Un diorama de blocs à trois tons qui s'ouvre ; nombres faits d'icônes | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/iso-infographic.mp4) |
| `livre-isometrique` | Livre d'images isométrique | Une règle du quotidien : des gens de dos font la chose dans l'ordre, mots peints au sol | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/isometric-picture-book.mp4) |
| `plan-de-metro` | Plan de métro | Un réseau tracé par des pointes lumineuses sur une feuille filmée en perspective | hyperframes (blender conseillé) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/transit-map.mp4) |
| `circuit-imprime` | Circuit imprimé | Le sujet en carte électronique vue du dessus ; ce qui circule est de la lumière | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/circuit-board.mp4) |

**Voir aussi (fiches portées par une autre catégorie)** : deux styles de la même famille sont rangés ailleurs (une seule fiche par style dans tout le plugin) :
- la **typo cinétique** (le mot comme acteur : listes, chiffres, phrases chocs, cartes de chapitre) : `styles-graphique-typo/styles/typo-cinetique/STYLE.md` ;
- l'**isométrique au trait fin** (un objet blanc au trait gris très fin, un seul point sombre ; produit, matériel, infrastructure) : `styles-matieres-3d/styles/isometrique-trait-fin/STYLE.md`.

Les aperçus sont ceux des auteurs d'origine (crédits dans chaque fiche, section 9, et dans `licenses/styles-explicatif-infographie.md`). Ils sont presque tous en 16:9 : ils montrent le look, pas le cadrage vertical. Les noms « style 3Blue1Brown », « style Vox », « style Kurzgesagt », « style Apple keynote » désignent une inspiration, jamais un contenu officiel ni une affiliation. Deux films d'aperçu (`livre-isometrique`, `circuit-imprime`) ont une voix exclue de leur licence : à donner en lien, ou à montrer sans le son. Un autre (`screencast-vivant`) met en scène une marque tierce : lien seulement.

## Comment choisir

D'abord : **qu'est-ce que le client veut faire comprendre ?**

| Le sujet est… | Propose d'abord | Puis |
|---|---|---|
| Un seul chiffre à fêter | `nombre-jalon` | `keynote-produit` |
| Quelques chiffres, une évolution, un classement | `graphique-anime` | `donnees-crayon` (si les données racontent une histoire humaine) |
| Une liste, une phrase choc, des cartes de chapitre | `typo-cinetique` (catégorie « Graphique et typo ») | `keynote-produit` |
| Un mécanisme abstrait, des maths, un algorithme | `maths-animees` | `science-a-plat` |
| Un phénomène de science, une question d'échelle, « ce qu'il y a dedans » | `science-a-plat` | `infographie-isometrique` |
| Un raisonnement, une opinion, une chaîne de causes | `tableau-blanc-a-la-main` | `collage-enquete` |
| Une histoire vraie avec des documents, de l'actualité, « pourquoi… » | `collage-enquete` | `presentateur` |
| Une anecdote personnelle, drôle | `recit-dessine` | |
| Un produit dont on a des captures d'écran | `keynote-produit` | `screencast-vivant` |
| Un logiciel à lancer, sans captures à montrer | `keynote-sombre` | `keynote-produit` |
| Un tutoriel de logiciel, pas à pas | `screencast-vivant` | `keynote-produit` |
| Un objet physique et ses caractéristiques | `hologramme-hud` | `isometrique-trait-fin` (catégorie « Matières et 3D ») |
| Un système avec des étapes et des flux (chaîne, trajet, fabrication) | `infographie-isometrique` | `circuit-imprime`, `plan-de-metro` |
| Une règle de la vie courante, une file d'attente, une consigne | `livre-isometrique` | |
| Un réseau, une croissance dans le temps, une feuille de route | `plan-de-metro` | `graphique-anime` |
| De l'énergie, des signaux, des paiements, un trajet technique | `circuit-imprime` | `infographie-isometrique` |
| Du matériel ou une architecture technique, sobrement | `isometrique-trait-fin` (catégorie « Matières et 3D ») | `hologramme-hud` |

Puis trois filtres :

1. **Débutant ou délai court** : `graphique-anime`, `nombre-jalon`, `keynote-produit`, et `typo-cinetique`. Les styles de difficulté « élevée » demandent un moteur de dessin à écrire et plusieurs tours de contrôle.
2. **Ce que le client possède** :
   - de **vraies données sourcées** : obligatoires pour `donnees-crayon`, `graphique-anime`, `nombre-jalon`, `plan-de-metro` ;
   - de **vrais documents ou photos** : obligatoires pour `collage-enquete` ;
   - des **captures ou la documentation du produit** : pour `keynote-produit`, `screencast-vivant` ;
   - un **personnage** (skill `personnages`) : obligatoire pour `recit-dessine`, `presentateur`, `screencast-vivant` (mascotte) ;
   - une **voix off** : presque tous ; seuls `nombre-jalon`, `isometrique-trait-fin` (catégorie « Matières et 3D »), `hologramme-hud` (écran en boucle) et `keynote-sombre` vivent bien sans.
3. **Le ton** : sérieux et crédible (`graphique-anime`, `collage-enquete`, `maths-animees`, `donnees-crayon`) ; chaleureux (`science-a-plat`, `livre-isometrique`, `recit-dessine`, `tableau-blanc-a-la-main`) ; technologique (`keynote-sombre`, `hologramme-hud`, `circuit-imprime`, `isometrique-trait-fin` (catégorie « Matières et 3D »)).

**Trois styles isométriques, à ne pas confondre** : `infographie-isometrique` = un système en blocs colorés sur un plateau flottant, avec étiquettes et nombres ; `livre-isometrique` = un vrai lieu plein cadre, avec des gens et des mots au sol ; `isometrique-trait-fin` (catégorie « Matières et 3D ») = un objet blanc au trait, sans couleur.

**Deux keynotes** : avec de vraies captures du produit, `keynote-produit` ; sans capture, tout en interface dessinée, `keynote-sombre`.

**Voisins dans d'autres catégories** : le tableau blanc sans main, aux feutres de couleur, est `tableau-blanc` dans `styles-peinture-dessin` (`styles-peinture-dessin/styles/tableau-blanc/STYLE.md`) ; les films faits de vraies images et de vraies pièces (enquête visuelle, tableau de briefing, habillage de journal télévisé, animations posées sur une personne qui parle) sont dans `styles-montage-documentaire` ; les films de lancement complets (structure en plusieurs temps, caméra, étalonnage) sont dans `styles-lancement-produit` : les deux keynotes d'ici donnent un look, pas un déroulé de lancement.

## Ce qui vaut pour toute la catégorie

- **Format** : 1080×1920, 30 images par seconde. Zone utile : x de 60 à 945, y de 160 à 1560 (rien d'important dans les 160 px du haut, les 360 px du bas ni les 135 px de droite). Les sources sont en 16:9 : chaque fiche donne la mise en page verticale, qui est une **nouvelle composition**, jamais un recadrage.
- **Moteur** : HyperFrames. Les styles dessinés sur canvas suivent un seul schéma : une fonction `dessiner(t)` qui ne dépend que du temps, appelée par la timeline.

```html
<canvas id="toile" width="1080" height="1920"></canvas>
<script>
  const etat = { t: 0 }, DUREE = 30;
  const tl = gsap.timeline({ paused: true });
  tl.to(etat, { t: DUREE, duration: DUREE, ease: "none", onUpdate: () => dessiner(etat.t) });
  window.__timelines["scene"] = tl;   // même t = même image, au pixel près
</script>
```

- **Déterminisme** : aucun `Math.random()` sans graine, aucun `Date.now()`, aucun état gardé d'une image à l'autre.
- **La vérité d'abord.** Tout fait, nombre, date ou citation à l'écran vient du client ou d'une source vérifiée, notée dans un fichier `FAITS.md` du projet (ce qui est affirmé, la valeur, le lien, la date de vérification). On n'arrondit pas, on n'extrapole pas, on n'invente pas. Des données d'exemple portent la mention « Données d'exemple » sur chaque image. Les barres partent de zéro.
- **La voix commande.** On enregistre ou on génère la voix d'abord ; chaque nom et chaque chiffre se pose à l'instant où il est dit (le début d'une animation = l'instant du mot − la durée de l'animation). Le texte à l'écran reprend **le mot clé ou le nombre**, jamais la phrase entière.
- **Une chose par écran**, et après l'arrivée, l'image s'arrête : pas de flottement ni de poussée lente pour meubler. Le mouvement vient de l'événement suivant.
- **Pas trois fois la même mise en page d'affilée** : au-delà, la vidéo se lit comme un diaporama.
- **Temps de lecture** : règle commune de la porte de livraison (`studio-coeur/references/controles.md`, section 2). Ces styles posent du texte à lire : lance le contrôle avec `--strict` (caractères ÷ 15 + 1,5 s, jamais moins de 1,5 s, texte entier et immobile). Un sous-titre **en phrase entière** tient en plus la durée de la phrase dite + 0,6 s ; des sous-titres au mot suivent la règle de la porte (0,7 s au moins, 17 caractères par seconde au plus) ; un nombre à retenir, 2,5 s.
- **Couleurs** : pas plus de 30 % d'images dominées par un bleu-violet saturé (c'est le look « fait par une machine ») ; un accent = une seule chose par plan.
- **Son** : mixage à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages pour 10 secondes, voix nettement au-dessus de tout. Quand une fiche décrit « un son par élément », lire : un son continu pour la série et un accent sur l'élément principal. Les exceptions où la synthèse est le bon choix (sons d'interface, électricité) sont dites dans les fiches.
- **Droits** : aucun logo redessiné de mémoire, aucune mascotte ni interface d'une marque tierce, aucune photo sans droits. Les références citées servent à comprendre la grammaire.

## Les 16 effets premium

`references/effets.md` décrit seize petites animations de 8 secondes où **une chose devient une autre** (bouton → lecteur, barres → courbe, carte → espace de travail, logo en particules…). Ce ne sont pas des styles : ce sont des briques à placer **dans** un style de cette catégorie, surtout `keynote-produit`, `keynote-sombre`, `graphique-anime` et `nombre-jalon`, ou à publier seules en boucle. Lis ce fichier quand le client demande « un effet » précis ou quand un plan de produit a besoin d'un moment fort.

## Lire une fiche

Chaque style est dans `styles/<identifiant>/STYLE.md`, avec dix sections fixes : identité, palette et matières, composition 9:16, ce qui bouge, rythme, recette technique, son, liste de contrôle, aperçu, origine. Lis la fiche en entier avant d'écrire le storyboard, puis rends **une image de style** (une seule image fixe au vrai format) et vérifie-la avec la liste de contrôle de la section 8 avant d'animer.
