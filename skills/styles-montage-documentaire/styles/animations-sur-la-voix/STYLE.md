# Animations pendant qu'on parle (la forme qui ne coupe jamais)

## 1. Identité
- **Nom** : Animations sur la voix. Identifiant : `animations-sur-la-voix`.
- **Inspiration** : les inserts de motion design des vidéos « face caméra » de créateurs tech : une petite interface qui se transforme sous un curseur, calée sur chaque mot.
- **Principe** : à partir de la vidéo du client et de sa transcription, fabriquer des inserts animés calés sur ses mots. Chaque insert est **une seule forme qui ne coupe jamais** : elle change de taille, de coins et de couleur d'un état à l'autre pendant que son contenu se remplace par un court flou. **Un curseur pilote les changements** par de vrais clics et de vrais glissés, et chaque changement tombe sur un mot prononcé.
- **Pour quels sujets** : tutoriel, démonstration d'outil, conseil d'expert, avis sur un produit, toute phrase qui décrit quelque chose **à voir** (un produit, un procédé, une comparaison, un nombre, un changement de chapitre).
- **Ne marche pas pour** : les phrases personnelles, émotionnelles ou d'opinion (on laisse le visage) ; un sujet sans objets concrets à montrer ; une vidéo sans transcription horodatée.
- **Prérequis** : la vidéo dérushée (fiche `derushage-silences-rates`) et sa transcription mot à mot. Avec un simple fichier de sous-titres, les temps des mots sont des estimations (±0,2 s) : poser les changements importants sur le premier ou le dernier mot d'une réplique.

## 2. Palette, typographie, matières
- **Par défaut** (la fiche « ma chaîne » du client passe devant) : fond gris chaud `#E9E7E2`, encre `#0B0B0B`, composants blancs, **un seul accent** orange `#FF5A1F`. Les inserts posés sur une image sombre utilisent des formes claires `#F4F2EE`.
- **Polices libres (OFL)** : Geist pour le texte d'interface, Geist Mono pour le code, les noms de fichiers et les terminaux. **Embarquer les polices** dans la page (sinon substitution silencieuse au rendu).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Geist ; JetBrains Mono à la place de Geist Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/geist`, `@fontsource/geist-mono` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Icônes** : un seul jeu, une seule épaisseur de trait.
- **Matières** : aplats nets, coins arrondis (rayon 28 à 36 px), ombres douces et courtes. Ni lueur, ni dégradé sur les éléments d'interface, ni particules.
- **Vocabulaire d'interactions** (chaque idée se traduit par l'une d'elles) : pastille + clic, barre de progression, coche, îlot d'état, carte qu'on glisse, curseur de réglage, interrupteur, onglets, graphique + info-bulle, recherche et filtre, fichier glissé-déposé, frappe dans un terminal, comparaison côte à côte, carton de chapitre.

## 3. Composition 9:16
**La décision la plus importante, prise insert par insert et justifiée : quelle part du cadre prend-il ?**
- **Plein cadre** (on quitte le visage) : quand l'image est tout le visage et que la phrase décrit quelque chose à voir. Durée de l'idée (3 à 10 s), puis on rend le visage. Jamais dans la première seconde de l'accroche. Au moins ~2 s de visage entre deux pleins cadres. La forme occupe 60 à 80 % de la largeur, centrée vers y 800.
- **Panneau dans l'espace vide** : quand le montage laisse déjà de la place. En 9:16, c'est la **moitié haute** d'un écran partagé (y 170 à y 880) ou la bande au-dessus de la tête du client. Insert **transparent**, centré dans la zone vide, dimensionné pour ne jamais toucher le visage. Il peut durer longtemps (15 s et plus) en une seule transformation continue, puisque le client reste à l'écran.
- **Rien** : la phrase parle du client lui-même, ou elle est trop proche d'un autre insert.
- La caméra zoome pour que chaque état remplisse la zone ; le curseur reste dans le cadre à chaque zoom, y compris pendant les transformations.
- Texte : libellés ≥ 34 px, mot ou nombre héros ≥ 110 px, 5 mots au plus par état.
- Zones d'interface : rien d'important au-dessus de y 160, sous y 1560, à droite de x 945. Les sous-titres du reel gardent leur place (jointure ou torse) : l'insert ne les couvre jamais.
- **16:9** : mêmes règles ; le panneau se place dans la zone vide à côté du cadre du client.

## 4. Ce qui bouge
- **Action principale** : la transformation de la forme (largeur, hauteur, rayon, couleur) sur ressort, déclenchée par un clic ou un glissé du curseur. Ressorts avec un **minuscule dépassement au plus**.
- **Boucles de fond** : (1) le curseur, qui se déplace entre deux actions sur une trajectoire légèrement courbe, « humaine » ; (2) un petit élément qui reste vivant dans l'état tenu (barre qui progresse, point d'état qui pulse doucement).
- **Échange de contenu** : le contenu sortant part vite avec un flou court ; le contenu entrant attend un instant puis arrive en se défloutant. Sans ce décalage, ancien et nouveau texte se superposent.
- **Indicateur liquide** : les bords avant et arrière d'un indicateur (onglet actif, interrupteur) suivent **deux ressorts différents** : le bord qui avance est rapide, celui qui suit est lent, donc l'indicateur s'étire.
- **Manipulation directe** : tant que le curseur tient une poignée, la valeur vient de sa position ; au relâchement elle repart en ressort de là où elle était.
- **Autorisés** : #012 morphing de forme, #083 curseur, #085 onde de clic, #057 onglets, #059 interrupteur, #062 curseur de réglage, #056 notification, #007 compteur (valeurs réelles seulement), #161 élément partagé entre deux états, #028 zoom de caméra vers l'état.
- **Interdits** : amortis rebondissants (#123), #015 particules, lueurs, dégradés sur l'interface, icônes d'épaisseurs mêlées, temps mort, tout ce qui ressemble à un modèle tout fait, **données inventées**, coupe ou fondu entre deux états (la forme se transforme, elle ne coupe pas).

## 5. Rythme et montage
- **On suit la parole, pas la musique** : un changement par temps de parole, espacés d'environ 0,4 à 1,2 s. Temps local de l'insert = temps du mot − point d'entrée de l'insert.
- **Densité** (à demander au client) : légère = 2 à 4 inserts par minute, seulement les moments les plus forts ; moyenne (par défaut) = 4 à 7 par minute ; forte = la plupart des phrases couvertes, avec de courts retours au visage.
- **Une idée par insert.** Un long passage (tout un écran partagé) peut être un seul long insert à plusieurs états.
- Un insert finit en tenant son dernier état ; coupes franches à l'entrée et à la sortie du plein cadre.
- **Plan à faire valider avant tout code** : un tableau, une ligne par insert : n°, entrée-sortie, la phrase couverte, ce que fait la forme et sur quels mots, plein cadre ou panneau, pourquoi.

## 6. Recette technique
- **Moteur** : HyperFrames. Chaque insert est une sous-composition (un fichier par insert) placée sur la ligne de temps du reel par `data-start` ; le panneau transparent est simplement un clip sans fond au-dessus de la vidéo (pas besoin de fichier vidéo avec transparence, sauf si le client veut les inserts pour son propre logiciel de montage : rendre alors en format avec couche alpha).
- **Ressorts** : en GSAP, des amortis à faible dépassement ; ou une fonction de ressort en forme fermée appelée depuis `hf-seek` si l'on veut exactement « une valeur à plusieurs cibles = somme d'un ressort par changement ».
```js
const etats = { pastille: {width: 420, height: 96, borderRadius: 48},
                carte:    {width: 780, height: 560, borderRadius: 36} };
tl.to("#forme", {...etats.carte, duration: 0.6, ease: "back.out(1.15)"}, mot("dossier").debut);
// échange de contenu : sortie rapide et floue, entrée retardée qui se défloute
tl.to("#contenuA", {opacity: 0, filter: "blur(10px)", y: -10, duration: 0.12}, mot("dossier").debut)
  .fromTo("#contenuB", {opacity: 0, filter: "blur(10px)", y: 16},
          {opacity: 1, filter: "blur(0px)", y: 0, duration: 0.35}, mot("dossier").debut + 0.18);
// clic : le curseur s'écrase, une onde part
tl.to("#curseur", {scale: 0.84, duration: 0.045, yoyo: true, repeat: 1}, tClic)
  .fromTo("#onde", {scale: 0.4, opacity: 0.5}, {scale: 1.6, opacity: 0, duration: 0.4}, tClic);
```
- **Caméra** : une seule transformation sur un conteneur « monde » ; choisir le zoom de chaque état pour qu'il remplisse la zone.
- **Contrôle** : une planche d'images fixes aux instants où chaque état est posé, plus deux instants en pleine transformation ; corriger tout ce qui est serré, rogné, illisible, hors mot, ou un curseur qui sort du cadre.
- **Pièges** : jamais `will-change` sur ce que la caméra agrandit (texte flou) ; un texte à `mix-blend-mode` doit être dans le calque qui porte le mode de fusion (un parent filtré l'isole) ; les éléments qui glissent sous un surlignage ont besoin d'un ressort rapide, sinon la ligne surlignée reste vide un instant ; ne pas tweener `display` ou `visibility` d'un clip.
- **Règle de contenu** : montrer les vrais objets du sujet (le dossier, le terminal, le fichier, le produit, le résultat), tirés des mots. **Ne jamais inventer de nombres, de citations, de prix ni de résultats** : barres relatives, lignes de texte en squelette, libellés pris dans la transcription ; lister au client ce qui est illustratif. Les vrais chiffres n'entrent que si le client les donne.

## 7. Son
- La voix du client reste la piste principale ; les inserts ne la couvrent jamais.
- Bruitages discrets liés aux actions du curseur (budget du skill `son`, vrais enregistrements d'abord) : clic sec, petite tape quand une carte se pose, glissement léger pour un déplacement. Pas de carillon sur un clic, pas de souffle à chaque transformation.
- Panoramique léger selon la position à l'écran. Master −14 LUFS avec le reste du reel.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Chaque changement d'état tombe sur son mot (écart ≤ 2 images, contrôlé sur chaque insert).
- [ ] Une seule forme par insert, aucune coupe ni fondu à l'intérieur.
- [ ] Chaque changement est provoqué par le curseur (clic ou glissé visible) ; le curseur ne sort jamais du cadre.
- [ ] Aucun nombre, prix, citation ou résultat inventé ; la liste de ce qui est illustratif est remise au client.
- [ ] Pas de plein cadre dans la première seconde ni sur une phrase personnelle ; ≥ 2 s de visage entre deux pleins cadres.
- [ ] Un panneau ne touche jamais le visage, à aucun instant.
- [ ] Un seul accent, une seule épaisseur d'icône, polices embarquées.
- [ ] Texte lisible à 360 px de large ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu
- GIF de démonstration du dépôt d'origine : https://github.com/Barty-Bart/motion-graphics/blob/main/docs/demo-cutaway.gif (plein cadre) et https://github.com/Barty-Bart/motion-graphics/blob/main/docs/demo-panel.gif (panneau). Crédit : Bart, dépôt sous licence MIT. Lien seulement ; aperçu Flot Web en 9:16 à produire.

## 10. Origine
- Dépôt : Barty-Bart/motion-graphics, commit `3d83d98`. Fichiers : `skills/motion-broll/SKILL.md`, `skills/motion-broll/reference/engine-api.md`.
- Licence : MIT (© 2026 Bart) ; polices Geist sous SIL OFL ; tracés d'icônes adaptés de Lucide (ISC).
- Adaptations Flot Web : français, **réécrit pour HyperFrames** (la source a son propre moteur de rendu, non repris), section 9:16, liens avec `reel-face-cam`.
