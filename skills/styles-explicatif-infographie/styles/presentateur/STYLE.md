# Présentateur

## 1. Identité

- **Nom** : Présentateur (un personnage dessiné explique, entre des documents, des graphiques et des mots clés).
- **Inspiration** : les vidéos de vulgarisation économique où un présentateur de dessin animé se tient à côté de ce qu'il explique, y entre, réagit.
- **La règle en une phrase** : **un personnage relie les informations** : il se tient de côté pour expliquer, laisse la place à un grand nombre, entre dans un graphique, réagit en gros plan. Les **nombres se posent quand la voix les dit** ; le personnage change de pose **d'un coup**.
- **Marche pour** : histoire d'une entreprise ou d'un marché, mécanisme d'un produit, explication qui a besoin d'**une réaction humaine** (étonnement, doute, satisfaction) à côté des chiffres ; une chaîne qui veut un visage récurrent sans se filmer.
- **Ne marche pas pour** : un sujet grave ou un contenu d'entreprise très sobre ; une vidéo sans voix ; un sujet sans chiffres ni documents (voir `recit-dessine`) ; un projet sans personnage disponible.
- **État de la source, à connaître** : c'est la plus mince des grammaires d'origine : une carte courte, **sans démo propre ni images de personnage**, et un code de référence situé dans un dossier que l'on ne reprend pas (il porte le nom d'une marque tierce). Cette fiche fixe donc la grammaire ; le reste s'appuie sur les fiches voisines : `graphique-anime` (graphiques), `collage-enquete` (documents), `typo-cinetique` (mots clés), `recit-dessine` (jeu du personnage). **À valider par un rendu réel avant de le proposer à un client.**
- **Personnage** : obligatoire, fourni par le skill `personnages` (planche de poses) ou par le client. Jamais un bonhomme générique tracé en code.

## 2. Palette, typographie, matières

La source ne fixe aucune palette. Règles reprises des fiches voisines et de la palette commune du plugin :

| Rôle | Jeu d'exemple « papier » |
|---|---|
| Fond | papier `#f4efe6` |
| Surface (cartes, graphiques) | `#ffffff` |
| Encre | `#1c1b19` |
| Texte secondaire | `#6b665e` |
| Accent (le chiffre, le héros du graphique) | une couleur de la marque, par exemple `#e3562b` |
| Second accent (comparaison) | bleu marine en aplat `#1f3a5f` |

- **Un accent = une seule chose par plan.** Pas de dégradé de fond, pas de lueur.
- **Le personnage est l'élément le plus contrasté** : trait plus noir et plus épais que tout le reste (au moins deux fois le trait du décor), couleurs un peu plus saturées que le fond.
- **Polices** (libres) : Inter ou Noto Sans (titres en 700, texte en 500) ; Roboto Condensed ou Inter Tight pour les grands nombres ; chiffres à largeur fixe pour les compteurs.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Noto Sans et d'Inter Tight ; Oswald à la place de Roboto Condensed ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/noto-sans`, `@fontsource/roboto-condensed`, `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Bandeau du haut** (facultatif) : l'année ou le chapitre en cours, sous y 160 à gauche. **Bandeau, sous-titres et titres de partie lisent la même horloge** (une seule source de temps).
- **Matières** : papier légèrement texturé, fixe. Les documents et graphiques sont posés comme sur une table ou un mur, pas flottants.

## 3. Composition 9:16

**Avant d'écrire le storyboard, attribuer une mise en page à chaque plan.** Cinq dispositions à faire tourner ; **ne jamais garder « le personnage d'un côté, le graphique de l'autre » pendant tout le film** :

| Disposition | En vertical |
|---|---|
| Explication de côté | le document ou le graphique occupe le haut (y 200 à 1050, 90 % de la largeur) ; le personnage en buste en bas à gauche (y 1000 à 1500), tourné vers lui |
| Nombre plein écran | le nombre seul, 300 à 420 px de haut, centré vers y 800 ; le personnage est absent, ou très petit dans un coin |
| Comparaison | deux blocs empilés (avant en haut, après en bas), le personnage entre les deux, désignant l'un |
| Le personnage dans l'image | il se tient **dans** le graphique : sur une barre, le long d'une courbe, à côté d'un point |
| Réaction en gros plan | le visage en buste remplit la moitié basse ou le cadre ; fond uni |

- **Deux cadrages du personnage au moins** : en pied et en buste, à partir de **vraies images à ces tailles**. Un gros plan obtenu en agrandissant fort une image en pied est flou et se coupe mal. Une pose assise ou appuyée demande sa propre image.
- **Le personnage ne masque jamais un texte ni un chiffre** ; vérifier aussi qu'une poussée de caméra ne le coupe pas. Ces deux défauts ne se détectent qu'à l'œil : regarder chaque plan.
- **Tailles** : titre de partie 70 à 90 px ; grand nombre 300 à 420 px ; étiquettes 36 à 44 px ; sous-titres 46 à 50 px, entre y 1400 et y 1540, jamais sur le personnage.
- Zone utile : x 60 à 945, y 160 à 1560.

## 4. Ce qui bouge

- **Action principale** : le personnage **change de pose d'un coup, avec un petit surgissement** (une légère mise à l'échelle qui se pose) ; on ne fond jamais deux silhouettes différentes l'une dans l'autre, cela donne un double contour.
- **Boucles de fond** : (1) **la bouche** : ouverte et fermée suivent le temps de la voix ; **pendant une pause, la bouche s'arrête** ; (2) clignement et respiration très légers ; dans l'image, ce qui vit dans le graphique (point de tête, annotation).
- **Autorisés** : style image par image `#128` (poses), apparition éclair `#001` avec un petit dépassement `#010` au changement de pose, compteur `#007`, tracé de ligne `#004`, surligneur `#080`, cercle d'insistance tracé **après** que le nombre s'est posé, coupe sèche `#046`, très gros plan `#184` de réaction, travelling avant `#027` par la caméra de la scène, plan fixe `#175`, poussée `#137` entre deux pages.
- **Interdits** : fondu `#044` entre deux poses, marche glissée (une marche demande **de vraies images de pas**), bouche qui continue pendant un silence, zoom dans une image aplatie de la scène (elle se coupe et devient floue : utiliser la caméra de la scène), flottement `#096` du personnage, deux accents de couleur dans un plan.
- **Les nombres** : ils se posent **à l'instant où la voix les dit**. Pendant qu'un compteur tourne, **ne pas afficher d'avance « plus de » ni « + »** : ce sont des affirmations qui n'arrivent qu'avec la valeur finale. Le cercle d'insistance vient après.
- Le personnage **regarde et désigne** ce dont il parle : c'est lui qui guide l'œil.

## 5. Rythme et montage

- **Une phrase de voix = un plan ou un changement de pose.** Plans de 2 à 6 s.
- **La pause après un moment fort se prévoit dès l'écriture du texte et l'enregistrement de la voix** : on ne peut pas l'ajouter au montage.
- **Transition propre au style** : **la page tourne ou glisse, mais le personnage et le bandeau du haut restent** : ils traversent la transition sans bouger, ce qui donne la continuité.
- Au début de chaque partie, **redonner explicitement la position et l'échelle du personnage** : une valeur héritée de la partie précédente provoque des retours en arrière.
- Alterner : explication de côté, nombre plein écran, réaction ; jamais trois fois de suite la même disposition.

## 6. Recette technique

- **Moteur** : HyperFrames. Le personnage en images (une par pose et par cadrage, fond transparent) dans un calque **au-dessus** des pages ; les pages (documents, graphiques, nombres) dans des scènes en dessous ; le bandeau du haut dans un calque fixe.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `personnage/` (images de poses, avec pour chacune le **point d'ancrage des pieds** et une hauteur de référence), `distribution.js` (qui, où, à quelle échelle, quelle pose, à quel instant), `pages/` (une scène par page), `horloge.js` (la source de temps unique : voix, sous-titres, année affichée), `film.js`.

```js
// le code règle l'ancrage aux pieds, la position, l'échelle et le changement d'image
function placer(perso, cle) {                                  // cle = { pose, x, y, echelle }  (x, y = position des PIEDS)
  const im = POSES[cle.pose]; perso.src = im.src;
  perso.style.transformOrigin = `${im.pieds.x}px ${im.pieds.y}px`;
  perso.style.transform = `translate(${cle.x - im.pieds.x}px, ${cle.y - im.pieds.y}px) scale(${cle.echelle * H_REF / im.hauteur})`;
}
// changement de pose : coupe franche + petit surgissement
const surgir = dt => dt < 0 ? 1 : 1 + 0.06 * Math.exp(-dt / 0.05);
// opacité imbriquée : MULTIPLIER, pour garder le fondu du parent
ctx.globalAlpha *= alphaLocal;
// bouche : seulement pendant que la voix parle
const parle = SEGMENTS_VOIX.some(s => t >= s.debut && t < s.fin);
```

- **Techniques clés** : aligner toutes les poses sur une **hauteur médiane** (sinon le personnage change de taille en changeant de pose) ; un buste pour les gros plans ; une seule source de temps.
- **Pièges** : une position héritée d'une partie précédente ; une opacité affectée au lieu d'être multipliée (l'élément échappe au fondu du parent) ; le personnage devant un texte ; le personnage coupé par une poussée ; une affirmation (« plus de ») affichée pendant que le compteur tourne ; prendre cette fiche pour un gabarit de film complet : personnage et voix sont à fournir.
- **Contrôles** : dès la première version, vérifier que chaque texte tient dans le cadre et que la zone des sous-titres est libre.

## 7. Son

- **Voix** : c'est le présentateur qui parle : ton vivant, un peu complice ; elle fixe tout le minutage.
- **Bruitages** : un « pop » léger sur un changement de pose important (pas sur tous), un coup feutré quand un nombre se pose, un frottement de papier quand la page change, un trait de marqueur pour le cercle d'insistance. Environ 5 pour 10 s.
- **Musique** : discrète, régulière, qui baisse sous la voix et remonte dans les pauses.
- **Silence** : la pause prévue après le moment fort, avec la réaction du personnage.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le personnage vient d'une vraie planche de poses, avec au moins un cadrage en pied et un en buste.
- [ ] La disposition change : jamais « personnage d'un côté, graphique de l'autre » pendant tout le film.
- [ ] Les poses changent d'un coup ; aucune silhouette en double contour.
- [ ] La bouche bouge pendant la voix et s'arrête pendant les pauses.
- [ ] Chaque nombre se pose quand la voix le dit ; aucune affirmation affichée avant la valeur finale.
- [ ] Le personnage ne masque aucun texte et n'est coupé par aucun mouvement de caméra.
- [ ] Le personnage et le bandeau du haut restent en place pendant les changements de page.
- [ ] Bandeau, sous-titres et titres suivent la même horloge.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Aucun aperçu d'origine : la source n'a ni démo ni planche pour cette grammaire. Carte d'origine : https://github.com/alchaincyf/huashu-art-motion/blob/main/references/动画语法/y6_presenter_explainer.md
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Un premier aperçu maison est à produire (voir le compte rendu de la catégorie).

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichier `references/动画语法/y6_presenter_explainer.md`. Le code de référence cité par la carte (`scripts/engine/reference_films/spacex/`) n'est **pas** repris : dossier au nom d'une marque tierce, contenant des données sous une autre licence.
- Licence : MIT (© 2026 alchaincyf, 花叔).
- Adaptation Flot Web : traduction du chinois ; composition verticale, palette, tailles, recette HyperFrames et section son ajoutées par Flot Web (absentes de la source) ; renvois aux fiches voisines et au skill `personnages`.
