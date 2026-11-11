# Les 16 effets premium

Seize petites animations « une chose devient une autre chose » : un bouton devient un lecteur, des barres deviennent une courbe, une carte devient une fenêtre. Elles servent de **briques** à l'intérieur d'un style de cette catégorie (surtout `keynote-produit`, `keynote-sombre`, `graphique-anime`, `nombre-jalon` et `typo-cinetique`), ou seules, comme une boucle de 8 secondes à publier.

Origine : Charlie Hills, dépôt `charlie947/motion-graphics-skills`, commit `229022e`, fichiers `skills/motion-effects/SKILL.md` et `skills/motion-effects/references/effects.md`, licence MIT (© 2026 Charlie Hills). Traduit et adapté par Flot Web : format vertical, moteur HyperFrames, règles de son. Aperçu de l'auteur : https://github.com/charlie947/motion-graphics-skills (images animées du fichier README).

## Choisir un effet

| N° | Effet | À utiliser quand on veut… |
|---|---|---|
| 01 | Bouton → lecteur | glisser un moment « regardez la démo » |
| 02 | Recherche → résultats | montrer ce qu'on trouve dans une aide en ligne ou un catalogue |
| 03 | Carte → espace de travail | annoncer une fonction : une petite carte devient tout l'éditeur |
| 04 | Onglets → panneaux | comparer des offres, des formules ou des canaux sans mur de texte |
| 05 | Barres → courbe | poser un résultat de la semaine dans un bilan |
| 06 | Zoom sur le tableau de bord | sortir d'un tableau de bord le seul indicateur qui compte |
| 07 | Pile à ressort | montrer trois offres, trois cas clients ou trois avis, l'un après l'autre |
| 08 | Barre d'icônes aimantée | montrer ses outils ou les intégrations d'un produit |
| 09 | Lettres masquées | révéler un nom de campagne, un numéro, un titre de lancement |
| 10 | Lettres élastiques | ouvrir un événement, un webinaire, un podcast par un carton-titre |
| 11 | Texte → mise en page | changer un titre en couverture de carrousel ou en amorce d'article |
| 12 | Volets d'image | faire monter l'attente avant un produit, puis découvrir la photo |
| 13 | Couches en perspective | expliquer les couches d'un service, d'une marque ou d'une technique |
| 14 | Loupe de verre | faire lire la seule ligne d'un rapport qui compte |
| 15 | Chemins de lumière | montrer un contenu qui alimente plusieurs canaux, ou un tunnel simple |
| 16 | Logo en particules | finir une vidéo sur sa marque |

Si le client décrit un besoin plutôt qu'un effet (« montrer nos tarifs », « révéler le nom »), propose les deux effets qui conviennent le mieux et laisse-le choisir.

## L'horloge commune

Toutes les recettes tiennent sur 8 secondes. Les temps sont en secondes depuis le début de la boucle.

| Phase | Secondes | Ce qui se passe |
|---|---|---|
| Départ | 0,0 | l'état de départ, tenu une image |
| Mouvement | 0,0 à 2,2 | le seul changement, avec accélération et décélération |
| Tenue | 2,2 à 6,6 | l'état final ; **quelque chose de petit continue de vivre**, pour que la tenue ne paraisse jamais figée |
| Retour | 6,6 à 8,0 | tout revient en douceur à l'état de départ |
| Boucle | 8,0 | identique à 0,0, au pixel près |

Dans le mouvement : « tôt » = les 0,8 premières secondes ; « milieu » = de 0,8 à 1,4 ; « tard » = de 1,4 à 2,2.

**Deux modes** : *boucle* (publication, image animée) ou *tenue* (sous une voix off : le mouvement se joue une fois et l'image reste sur l'état final, pour ne jamais repartir au milieu d'une phrase). **Dans une vidéo verticale au rythme rapide, 8 secondes c'est trop lent** : ne garder que la partie active (environ 1,4 s) et le mode tenue.

Rôles de couleur dans les recettes : **fond**, **surface**, **encre**, **atténué**, **accent**, **second accent**. Ils viennent de la fiche « ma chaîne » du client (skill `marque`). Les mots des recettes montrent la forme du contenu : on les remplace par les vrais mots du client.

## Règles de fabrication

1. **Une seule horloge.** Chaque image se calcule à partir du temps seul : en HyperFrames, une timeline GSAP en pause, enregistrée, sans minuterie ni animation CSS autonome ni hasard sans graine.
2. **Retour à la case départ** : le retour ramène chaque élément exactement où il était. Rien ne saute.
3. **Du vrai contenu** : les mots et les chiffres du client. Des chiffres d'exemple portent la mention « exemple » sur chaque image.
4. **Autonome** : polices chargées depuis le projet, images locales, aucun appel réseau.
5. **Remplir le cadre** : l'effet occupe la zone utile (x 60 à 945, y 160 à 1560 en 1080×1920). Ce n'est pas une petite tuile dans un grand vide. On **met à l'échelle** le dessin entier ; on ne le redessine pas avec d'autres coordonnées.
6. **Un fantôme du départ** : un contour très pâle reste là où le bouton ou la carte a commencé. Sans lui, l'état final semble sortir de nulle part.
7. **Décaler d'un temps** : rangées, lames, lettres et points partent chacun un peu après le précédent. Tout ce qui part ensemble ressemble à un changement de diapositive.

## Contrôle avant de montrer

Capturer les images à 0, 1, 2,2, 4,4, 6,6, 7,9 et 8 secondes et les regarder toutes.

- **La boucle** : les images 0 et 8 sont identiques.
- **Le mouvement** : les images 0, 1 et 2,2 sont toutes différentes. Si deux sont pareilles, une partie de l'effet ne tourne pas.
- **L'ajustement** : aucun texte ne sort de sa boîte, rien n'est coupé.
- **L'image fixe** : à 4,4 s, on comprend l'effet sur cette seule image.
- **La marque** : chaque couleur et chaque police vient de la fiche du client.

Pièges relevés par l'auteur : la première image peut se peindre avec une police de secours (charger chaque police avant la première image) ; une page blanche vient souvent d'un nom déclaré deux fois ; choisir une seule unité de temps (les secondes) et s'y tenir.

---

## Interfaces : montrer un produit qui fait quelque chose

### 01 Bouton → lecteur

Un petit bouton « Aperçu » grandit jusqu'à devenir un lecteur vidéo.

- **Départ** : un bouton en pilule avec un triangle de lecture et le mot « Aperçu », en haut à gauche, sur fond sombre.
- **Fin** : un grand lecteur qui remplit la tuile : une vignette, un titre (« Lancement de printemps »), un minutage (« 0:17 / 0:42 ») et une barre de progression à poignée ronde.
- **Minutage** : de 0,0 à 2,2, la coque même du bouton s'étire jusqu'à la forme du lecteur. Son libellé s'efface dans le premier quart. Le contenu du lecteur apparaît dans la seconde moitié. L'icône de lecture voyage du bouton au centre du lecteur, gagne un disque sombre derrière elle et change de couleur. Vers 2,6, elle se transforme en icône de pause. Pendant la tenue, la barre de progression avance et le minutage compte. À partir de 6,6, la pause redevient lecture et la coque rétrécit.
- **Ce qui le rend premium** : c'est un seul objet qui change de forme, jamais un fondu d'une chose à une autre. Un fantôme pâle du bouton reste à son point de départ. Le passage lecture-pause est un morphing de deux formes, pas un remplacement.

### 02 Recherche → résultats

Un champ de recherche s'ouvre, une requête se tape toute seule, les résultats s'empilent.

- **Départ** : une courte pilule avec une loupe et le mot gris « Rechercher ».
- **Fin** : une barre pleine largeur où l'on lit « campagne de printemps », et trois cartes de résultat dessous, chacune avec une tuile colorée, un titre et une ligne de mesure (« E-mail · 48 % d'ouverture »).
- **Minutage** : tôt, la pilule s'élargit et un curseur apparaît. De 0,75 à 1,2 environ, la requête se tape lettre par lettre. À partir de 1,1, les trois résultats montent de 14 px, l'un après l'autre. Le retour inverse le tout, résultats d'abord.
- **Ce qui le rend premium** : la pilule s'ouvre **avant** que la frappe commence, les deux mouvements ne se gênent jamais. Les résultats s'installent un à un. Chaque résultat porte un vrai chiffre, pas des barres de remplissage.

### 03 Carte → espace de travail

Une petite carte s'ouvre sur l'éditeur complet auquel elle appartient.

- **Départ** : une carte repliée en bas à gauche, en contour, titrée « Brief T3 », avec deux barres de texte grises.
- **Fin** : une fenêtre d'éditeur : barre de titre, colonne latérale avec un élément actif dans la couleur d'accent, un titre de document (« Plan de lancement »), des barres de texte, une image et deux pastilles d'état (« Brouillon », « 3 modifications »).
- **Minutage** : de 0,0 à 1,4 environ, la coque de la carte grandit depuis son propre coin. De fins guides en pointillés relient les coins de la carte à ceux de la fenêtre. Les barres de texte de la carte s'effacent dans le premier cinquième. Le contenu de la fenêtre n'apparaît qu'une fois la coque à plus de la moitié. Le titre voyage de la carte à la barre de titre.
- **Ce qui le rend premium** : le titre est un **élément partagé** : il se déplace, il n'est jamais dupliqué. Un fantôme en pointillés de la carte fermée reste à l'origine. Le contenu attend qu'il y ait de la place : rien n'est écrasé.

### 04 Onglets → panneaux

L'onglet sélectionné glisse vers le suivant et le panneau change avec lui.

- **Départ** : trois onglets (Reels, Posts, E-mail), « Reels » sélectionné dans une pilule sombre. Le panneau montre « Reels de la semaine », une pastille de total et trois lignes classées.
- **Fin** : « Posts » sélectionné, avec son panneau.
- **Minutage** : tôt, la pilule de sélection **s'étire** : son bord avant part le premier, son bord arrière suit un temps après ; elle s'allonge, puis reprend sa taille en arrivant. Deux courts traits de vitesse la suivent. Chaque libellé s'éclaircit quand la pilule le recouvre. À partir de 0,9 environ, l'en-tête et les trois lignes du panneau s'échangent, chacun glissant de 14 à 16 px de côté en s'effaçant, la ligne du haut d'abord.
- **Ce qui le rend premium** : l'étirement. Une pilule qui glisse à largeur fixe a l'air mécanique. La couleur du libellé suit la part de pilule qui le recouvre : le texte ne « bascule » jamais d'un coup.

---

## Données et listes : faire passer un message

### 05 Barres → courbe

Six barres deviennent une courbe qui passe par leurs sommets.

- **Départ** : un graphique en barres titré « Portée de la semaine », six barres (du lundi au samedi), un quadrillage léger. La mention « exemple » en haut à droite si les chiffres sont des exemples.
- **Fin** : une courbe lisse par les six mêmes valeurs, un remplissage doux dessous, un point sur chaque valeur, le dernier dans la couleur d'accent avec une petite étiquette (« 92 »).
- **Minutage** : dès le début, chaque barre s'amincit jusqu'à un fil, de gauche à droite, chacune un temps après la précédente. À partir de 0,84 environ, la courbe se trace de gauche à droite et le remplissage apparaît dessous. Chaque point surgit quand la courbe l'atteint. Vers 1,5, l'étiquette monte sur le dernier point.
- **Ce qui le rend premium** : **les valeurs ne changent jamais**. Les six mêmes nombres sont des barres puis une courbe, donc le spectateur fait confiance. La courbe est tracée, elle n'apparaît pas en fondu.

### 06 Zoom sur le tableau de bord

Une tuile d'indicateur se détache d'un tableau de bord et remplit le cadre.

- **Départ** : un tableau de bord discret : trois tuiles, une courbe de tendance, deux barres de texte grises.
- **Fin** : le tableau de bord assombri derrière une grande carte : « Inscriptions », une pastille d'évolution (« +18 % »), le grand nombre (« 12 480 ») et une mini-courbe.
- **Minutage** : dans les 0,9 premières secondes, quatre équerres d'angle dans la couleur d'accent se referment autour de la tuile choisie. Le reste s'assombrit. À partir de 0,7 environ, la tuile avance depuis sa position exacte jusqu'à la grande carte, avec des guides en pointillés entre leurs coins. Le contenu de la carte apparaît dans la seconde moitié.
- **Ce qui le rend premium** : la carte grandit depuis la position et la taille réelles de la tuile : c'est le même objet qui s'approche. Les équerres disent « celle-ci » avant que rien ne bouge.

### 07 Pile à ressort

Une pile de cartes bien rangée s'ouvre en éventail ; la carte du dessus dépasse, puis se pose.

- **Départ** : trois cartes produit empilées au même angle. Celle du dessus montre une image, un nom, un prix, un bouton de validation.
- **Fin** : les trois cartes en éventail, à trois angles différents.
- **Minutage** : chaque carte suit un **vrai ressort** avec son propre amortissement : la carte du fond très amortie, celle du milieu moins, celle du dessus le moins (elle dépasse son angle de repos et oscille). La carte du dessus part la première, les autres 0,05 et 0,1 s après. Le ressort est posé vers 1,8. Un fantôme en pointillés montre l'angle de repos. Le retour ramène les trois cartes sans ressort.
- **Ce qui le rend premium** : des ressorts, pas des courbes d'accélération, et un amortissement différent par carte.

### 08 Barre d'icônes aimantée

Une barre d'icônes sombre dont les icônes gonflent au passage d'un curseur.

- **Départ** : sept petites icônes carrées dans une barre translucide, toutes de la même taille, le curseur à droite.
- **Fin** : le curseur au milieu de la barre, les icônes proches agrandies, une étiquette au-dessus de la plus grande.
- **Minutage** : pendant le mouvement, le curseur glisse et les icônes grandissent. La taille de chaque icône suit une **courbe en cloche** de sa distance au curseur. La barre se recentre en s'élargissant. Pendant la tenue, le curseur balaie une fois à gauche et à droite ; le gonflement et l'étiquette le suivent.
- **Ce qui le rend premium** : la taille décroît en douceur ; ce n'est pas « cette icône grande, les autres petites ». L'étiquette est toujours au-dessus de la plus grande icône.

---

## Typographie : faire bouger les mots

### 09 Lettres masquées

Une image monte à travers les lettres d'un grand mot en contour.

- **Départ** : le mot en fin contour, une mention de numéro en haut à gauche, une saison en haut à droite, une ligne vide dessous.
- **Fin** : les lettres remplies par l'image, et une seconde ligne posée sous le mot.
- **Minutage** : pendant les 1,35 premières secondes, le bord du remplissage monte du bas des lettres jusqu'en haut. Un filet d'accent avec une petite poignée carrée marque ce bord. À partir de 0,95 environ, la seconde ligne monte de derrière une ligne de coupe nette. Le filet s'efface quand le remplissage est complet.
- **Ce qui le rend premium** : l'image ne se voit **que dans les lettres**. La seconde ligne est révélée par un masque, pas par un fondu. Le filet montre au spectateur ce que fait le mouvement.

### 10 Lettres élastiques

Chaque lettre d'un mot s'étire sur une ligne de base verrouillée.

- **Départ** : le mot au repos sur une ligne de base marquée, un petit fantôme du mot dessous.
- **Fin** : les lettres étirées en pic. Celle du milieu est la plus haute et la plus étroite ; les autres décroissent régulièrement des deux côtés.
- **Minutage** : l'étirement part de la lettre du milieu et gagne l'extérieur, chaque paire un temps plus tard. La lettre du milieu atteint son pic vers 1,3 ; les lettres extérieures finissent à 2,2. Un affichage compte la largeur (« largeur 100 » à « largeur 62 »). Le retour détend toutes les lettres ensemble.
- **Ce qui le rend premium** : la ligne de base ne bouge jamais. Les lettres changent de largeur autant que de hauteur : le mot reste un mot. Seule la lettre du milieu est dans la couleur d'accent.
- **À savoir** : demande une police variable à axe de largeur (par exemple Archivo ou Anybody, libres).

### 11 Texte → mise en page

Un simple titre se recompose en page d'article.

- **Départ** : une ligne de petit texte dans une bande en pointillés.
- **Fin** : une page éditoriale : un surtitre, le titre sur deux grandes lignes, quatre lignes de texte, une image et une carte de citation.
- **Minutage** : dès le début, le titre se coupe en deux moitiés qui voyagent séparément et grandissent en chemin. La seconde moitié descend d'abord, puis glisse à gauche : les deux moitiés ne partagent jamais une ligne. À partir de 0,8 environ, des guides en pointillés montrent leur trajet. Le surtitre apparaît vers 1,0 ; l'image s'ouvre de gauche à droite vers 1,05 ; les lignes de texte se tracent vers 1,1 ; la carte de citation monte en dernier vers 1,2.
- **Ce qui le rend premium** : le titre est **le même texte qui se déplace**, jamais retapé. Tout le reste arrive dans l'ordre de lecture.

### 12 Volets d'image

Des lames sombres se retirent et découvrent une image.

- **Départ** : le cadre couvert par sept lames verticales sombres.
- **Fin** : l'image entière, avec une petite étiquette en pilule (« Nouveauté ») en haut à gauche.
- **Minutage** : chaque lame s'amincit jusqu'à disparaître vers sa propre ligne centrale, de gauche à droite, chacune un temps après la précédente. La dernière a disparu vers 1,7. L'étiquette apparaît à partir de 1,05.
- **Ce qui le rend premium** : chaque lame a un fin bord clair qui en fait un objet physique, et les lames partent en séquence.

---

## Systèmes : expliquer comment les choses se relient

### 13 Couches en perspective

Les couches plates d'une page s'écartent en profondeur.

- **Départ** : trois couches empilées presque à plat, comme une seule page : un graphique au fond, une liste au milieu, une mise en page dessus.
- **Fin** : les trois couches écartées et tournées vers un même point de fuite à droite, chacune avec son contenu.
- **Minutage** : les couches se séparent du fond vers l'avant, chacune un temps après la précédente. À partir de 0,9 environ, des guides de perspective en pointillés apparaissent vers le point de fuite. Pendant la tenue, le point de fuite dérive doucement de haut en bas : toute la pile respire.
- **Ce qui le rend premium** : toutes les couches partagent **un seul point de fuite**, donc la profondeur est juste. Chaque couche garde un vrai contenu : on lit « les couches de cette chose », pas trois cartes grises.

### 14 Loupe de verre

Une loupe descend sur un rapport flou et rend nette la ligne qu'elle survole.

- **Départ** : une carte de rapport avec cinq lignes (libellé et valeur), toutes légèrement floues, la loupe sur la première.
- **Fin** : la loupe posée sur une ligne, nette et un peu agrandie.
- **Minutage** : pendant le mouvement, la loupe passe à la deuxième ligne. Pendant la tenue, elle descend jusqu'à la dernière et remonte à la deuxième, sur une courbe adoucie.
- **Ce qui le rend premium** : seul le texte dans la loupe est net, à 1,1 fois sa taille. Deux copies teintées très pâles de ce texte sont décalées d'une fraction de pixel de chaque côté, comme dans du vrai verre. La loupe a un reflet en haut et un double bord.
- **À savoir** : dans une vidéo, ne jamais flouter un texte que le spectateur doit lire ailleurs que sous la loupe.

### 15 Chemins de lumière

Des impulsions de lumière partent d'une source, traversent trois canaux et arrivent à un résultat.

- **Départ** : cinq pilules libellées sur fond sombre : « Brief » à gauche ; « E-mail », « Reel », « Post » au milieu ; « Bilan » à droite ; reliées par de fines courbes pâles. (En vertical : la source en haut, le résultat en bas.)
- **Fin** : toutes les lignes allumées, tous les nœuds lumineux.
- **Minutage** : à partir de 0,25, trois impulsions quittent la source, à 0,14 s d'intervalle, et allument les liaisons en les parcourant (environ une seconde chacune). À l'arrivée, le nœud répond par un anneau qui s'élargit et un point plus vif. À partir de 1,75 environ, une seconde série va des trois canaux au résultat ; ces lignes passent de la couleur froide à la couleur d'accent. Vers 3,6, une seconde vague refait le trajet.
- **Ce qui le rend premium** : les nœuds **répondent à l'arrivée**, donc la cause et l'effet se voient. La ligne est tracée par l'impulsion, elle ne s'allume pas d'un coup. La seconde vague garde la tenue vivante.

### 16 Logo en particules

Des points épars volent et forment un logo.

- **Départ** : un nuage de petits points d'un côté et un contour en pointillés très pâle de la marque de l'autre.
- **Fin** : les points rangés dans la marque, une partie dans la couleur d'accent.
- **Minutage** : chaque point part à un moment un peu différent, les plus éloignés d'abord, avec un peu de hasard (à graine), sur les 1,1 premières secondes. Chacun vole sur un arc doux avec une courte traînée. Les derniers se posent à la fin du mouvement. Le retour les disperse jusqu'à leur point de départ exact.
- **Ce qui le rend premium** : les points sont sur une **grille à l'intérieur de la vraie forme** de la marque, donc le logo fini est net. La dispersion a une graine : chaque boucle est identique. Les traînées montrent la direction sans flou.
- **À savoir** : n'utiliser que le fichier de logo fourni par le client, jamais un logo redessiné de mémoire.

---

## Les brancher dans une vidéo

```js
// l'horloge commune, en HyperFrames : un effet = une timeline de 8 s (ou sa partie active)
const tl = gsap.timeline({ paused: true });
tl.to("#coque", { width: 900, height: 560, borderRadius: 28, duration: 2.2, ease: "power3.inOut" }, 0)   // le mouvement
  .to("#libelle", { opacity: 0, duration: 0.55 }, 0)                                                     // premier quart
  .to("#contenu", { opacity: 1, duration: 1.1 }, 1.1)                                                    // seconde moitié
  .to("#barre", { scaleX: 0.6, duration: 4.4, ease: "none" }, 2.2)                                       // la tenue vit
  .to("#coque", { width: 220, height: 72, borderRadius: 36, duration: 1.4, ease: "power2.inOut" }, 6.6); // le retour
window.__timelines["effet"] = tl;
```

- **Son** : un bruitage discret sur le début du mouvement et un sur l'arrivée suffisent (voir `son`). Pas de son sur chaque rangée décalée.
- **Mouvements du dictionnaire** les plus utilisés ici : morphing de forme `#012`, révélation par masque `#005`, machine à écrire `#006`, tracé de ligne `#004`, décalage en cascade `#002`, dépassement `#010`, vue éclatée `#143`, particules `#015`, compteur `#007`.
