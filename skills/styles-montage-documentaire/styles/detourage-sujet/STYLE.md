# Détourage du sujet (texte et animations derrière la personne)

Technique de montage (pas un look) : elle sépare un sujet de son fond dans une vidéo du client, pour glisser du texte ou des animations **derrière** lui, l'isoler, ou le détacher du décor.

## 1. Identité
- **Nom** : Détourage du sujet. Identifiant : `detourage-sujet`.
- **Inspiration** : les titres géants qui passent derrière la tête d'un créateur, les objets tenus en main qui s'illuminent, les sujets posés sur un fond redessiné.
- **Principe** : on isole **un** sujet (le client, sa main, un produit) image par image ; tout se passe sur l'ordinateur du client, rien n'est envoyé ailleurs. Le résultat est un **masque par image** (blanc = sujet), plus une vidéo de contrôle où le sujet est teinté en vert pour voir exactement ce qui a été séparé. Les masques restent sur le disque : tout ce qu'on fera ensuite part d'eux sans relancer la séparation.
- **Pour quels sujets** : mot-clé géant derrière le client, flèche ou forme qui passe derrière puis devant, produit mis en évidence, fond assombri ou remplacé, découpes de personnes pour les styles `montage-constructiviste`, `tableau-de-briefing` et `table-lumineuse-archives`.
- **Ne marche pas pour** : cheveux fins et flous (masques à bords durs : très propres sur les objets et les mains, moins sur une chevelure vaporeuse), fumée, verre, plusieurs personnes qui se croisent, de longues durées sans carte graphique.
- **Quand ne pas s'en servir** : si un simple recadrage, un écran partagé ou un fond uni filmé suffit. Le détourage coûte du temps de calcul ; on le réserve à 1 à 3 moments forts par vidéo.

## 2. Palette, typographie, matières
- **Texte derrière le sujet** : très gras, très grand (voir section 3), dans la police de titre de la fiche « ma chaîne » ; une seule couleur pleine (blanc, ou l'accent de la chaîne) avec une ombre portée courte vers le bas pour l'asseoir dans l'espace.
- **Liseré de découpe** (optionnel, selon le style) : un bord clair de 4 à 8 px dilaté hors du masque ; c'est le look « autocollant » et il cache les erreurs de bord.
- **Mise en évidence d'un objet** : teinte de remplissage à 35 %, lueur douce sur le bord, liseré clair d'un pixel ou deux. Le vert de la vidéo de contrôle (`rgb(57,255,20)`) n'est qu'un outil de vérification, jamais un look livré.
- **Fond** : assombri (luminosité 0,45 à 0,6) et légèrement désaturé derrière le sujet pour faire ressortir le texte ; pas de flou lourd généralisé.
- **Police de repli** : Montserrat (800 ou 900) ou Archivo Black quand la fiche « ma chaîne » ne donne pas de police de titre. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : la police de titre de la fiche « ma chaîne » : `@fontsource/<nom>` si elle est libre (vérifier par `npm view @fontsource/<nom> version`), sinon fichier du client ; à vérifier.

## 3. Composition 9:16
- **Mot derrière la tête** : un à trois mots, 260 à 420 px de haut, centré horizontalement, placé pour que **la tête en cache 15 à 35 %** : assez pour prouver la profondeur, pas assez pour gêner la lecture. Vérifier que chaque lettre reste devinable sur toute la durée (le client bouge).
- Le mot vit entre y 200 et y 900 (au-dessus des épaules) ; rien d'important au-dessus de y 160, sous y 1560, à droite de x 945.
- **Sous-titres** : ils restent **devant** le sujet, à leur place habituelle. Ne jamais faire passer derrière le sujet un texte que le spectateur doit lire en entier.
- **Objet tenu en main** : cadrer pour que l'objet occupe au moins un quart de la largeur ; l'étiquette se place à côté, reliée par un trait.
- **16:9** : le mot peut s'étaler sur toute la largeur derrière le buste.

## 4. Ce qui bouge
- **Action principale** : l'élément qui passe **derrière** le sujet (un mot qui glisse ou grossit, une forme qui traverse), calé sur le mot prononcé.
- **Boucles de fond** : (1) le sujet lui-même, qui bouge naturellement devant l'élément : c'est ce mouvement qui vend l'effet ; (2) une dérive lente du mot (2 à 4 % d'échelle) pour qu'il ne soit jamais figé.
- **Variantes** : passer derrière puis devant (l'élément change de calque à un instant où il ne touche pas le sujet) ; isoler (le fond s'assombrit, le sujet garde sa lumière) ; halo d'objet qui s'allume sur son nom.
- **Autorisés** : #133 masque de texte, #005 révélation par masque, #016 parallaxe légère entre sujet et fond, #008 typographie cinétique (un mot, un mouvement), #099 silhouette (sujet en aplat), #028 poussée lente.
- **Interdits** : texte long derrière le sujet ; élément qui change de calque pendant qu'il chevauche le sujet (saut visible) ; détourage sur toute la vidéo « parce qu'on peut » ; bord qui grouille (voir pièges).

## 5. Rythme et montage
- Un effet de profondeur dure 1,5 à 4 s, sur une phrase clé (accroche, pivot, chiffre). Un à trois par vidéo courte.
- Entrée et sortie de l'élément derrière le sujet en 0,3 à 0,5 s ; tenue au moins (lettres ÷ 15 + 1,5) s si le mot doit être lu.
- Essayer d'abord sur une courte plage (environ 20 images), vérifier, puis lancer toute la plage.

## 6. Recette technique
- **Moteur** : le détourage se fait hors page ; l'assemblage se fait dans HyperFrames avec **trois calques** : la vidéo d'origine (fond), l'élément animé (milieu), le sujet seul (dessus).
- **Voie simple** : l'outil de détourage du skill `rendu` (suppression de fond locale), qui livre directement le sujet en vidéo avec transparence. À essayer en premier pour une personne face caméra.
- **Voie précise (sujet désigné par clics)** : un modèle de segmentation vidéo local (SAM 2), dans un environnement Python isolé placé dans le dossier du projet (le supprimer retire tout). Choix du modèle selon la machine : carte graphique de 12 Go et plus = grand modèle (≈ 900 Mo) ; carte plus petite ou puce Apple = modèle moyen (≈ 320 Mo) ; sans carte graphique = petit modèle (≈ 160 Mo), **environ 5 secondes par image** (un extrait de 10 s à 30 i/s ≈ une demi-heure). L'annoncer au client avant de lancer.
  1. Convertir la vidéo en cadence constante si besoin (`ffmpeg -i in.mp4 -vsync cfr -r 30 out.mp4`).
  2. Enregistrer la première image de la plage avec une grille de coordonnées ; choisir **deux ou trois points sur le sujet** et des **points d'exclusion** sur ce qu'il faut laisser (les doigts qui tiennent l'objet, l'emballage, la table).
  3. Traiter par blocs de 60 images (mémoire basse), chaque bloc repartant du dernier masque du précédent.
  4. Écrire un PNG de masque par image.
  5. Produire la vidéo de contrôle teintée en vert et regarder le début, le milieu et chaque instant où une main ou un objet passe devant. Si le vert déborde : ajouter un point d'exclusion et relancer ; s'il manque une partie : ajouter un point sur le sujet.
- **Du masque au calque « sujet »** : fusionner la vidéo et ses masques en une vidéo avec transparence, par exemple :
```
ffmpeg -i source.mp4 -framerate 30 -start_number 0 -i masques/%05d.png \
  -filter_complex "[1:v]format=gray,gblur=sigma=1.2[m];[0:v][m]alphamerge" \
  -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 24 sujet.webm
```
- **Assemblage** :
```html
<video id="fond"  class="clip" data-start="0" data-duration="6" src="assets/source.mp4" muted></video>
<div   id="mot"   class="clip" data-start="1.2" data-duration="3">RÉSULTAT</div>
<video id="sujet" class="clip" data-start="0" data-duration="6" src="assets/sujet.webm" muted></video>
```
  Les deux vidéos partagent exactement la même cadence, le même point de départ et le même cadrage ; si l'on recadre ou zoome, appliquer la transformation à un conteneur qui contient les trois calques.
- **Pièges** : décalage d'une image entre fond et sujet (liseré fantôme : vérifier image par image sur un mouvement rapide) ; bord dur qui grouille (léger flou du masque, sigma 1 à 1,5, ou liseré assumé) ; tout ce qui est attaché au sujet compte comme le sujet (emballage, film) ; cadence variable ; compression de la couche alpha (rester en VP9 avec alpha ou en séquence PNG, pas de H.264) ; premier lancement seulement : téléchargement du modèle (connexion nécessaire une fois).

## 7. Son
- L'entrée de l'élément derrière le sujet peut porter **un** bruitage (souffle court ou coup sourd doux), compté dans le budget du skill `son`. La voix reste au premier plan.
- Pas de son pour le détourage lui-même : il doit passer pour de la mise en scène, pas pour un effet.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La vidéo de contrôle a été regardée au début, au milieu et à chaque passage d'une main ou d'un objet devant le sujet.
- [ ] Fond et calque « sujet » sont alignés à l'image près (contrôle image par image sur 1 s de mouvement rapide : aucun liseré fantôme).
- [ ] Le bord ne grouille pas à vitesse réelle ; s'il grouille, flou léger du masque ou liseré.
- [ ] Le mot derrière le sujet reste devinable à chaque image (la tête n'en cache jamais plus d'un tiers).
- [ ] Aucun texte à lire en entier n'est derrière le sujet ; les sous-titres sont devant.
- [ ] L'élément ne change jamais de calque pendant qu'il chevauche le sujet.
- [ ] Le client a été prévenu de la durée de calcul et de la taille du modèle avant le lancement.
- [ ] Zones d'interface respectées ; 1 à 3 effets par vidéo, pas plus.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- GIF de démonstration du dépôt d'origine : https://github.com/Barty-Bart/motion-graphics/blob/main/docs/object-separation.gif. Crédit : Bart, dépôt sous licence MIT. Lien seulement ; aperçu Flot Web à produire.

## 10. Origine
- Dépôt : Barty-Bart/motion-graphics, commit `3d83d98`. Fichier : `skills/object-separation/SKILL.md` (choix du modèle selon la machine, points de clic et d'exclusion, traitement par blocs, vidéo de contrôle, nettoyage).
- Licence : MIT (© 2026 Bart). Le modèle de segmentation est téléchargé à l'exécution sous sa propre licence ; il n'est pas embarqué dans le plugin.
- Adaptations Flot Web : français, usage décrit en HyperFrames (trois calques, vidéo avec transparence), composition 9:16, voie simple par l'outil du skill `rendu`. Le code Python d'origine n'est pas recopié : l'agent l'écrit au besoin d'après ces étapes.
