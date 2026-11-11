# Export en reel vertical (d'une vidéo large à un 9:16 propre)

Format de sortie (pas un look) : il transforme une vidéo de produit faite en large en un fichier vertical avec une accroche au-dessus, que les applications acceptent sans délaver les couleurs.

## 1. Identité
- **Nom** : Export en reel vertical. Identifiant : `export-reel-vertical`.
- **Inspiration** : les reels « vidéo dans un cadre » : un titre de deux lignes en haut, la vidéo large au milieu, un fond uni.
- **Principe** : la plupart des démonstrations de produit se construisent en 16:9 (un écran d'ordinateur est large). Plutôt que de recadrer et de perdre l'interface, on **pose la vidéo entière dans un cadre vertical**, sous une accroche que les gens lisent sans le son, puis on encode exactement comme les applications l'attendent.
- **Pour quels sujets** : décliner sur Instagram, TikTok et YouTube Shorts une démo, un lancement ou un enregistrement d'écran faits en large ; republier une vidéo existante du client.
- **Ne marche pas pour** : une vidéo qu'on peut recomposer en vertical (toujours préférable : les autres fiches de la catégorie donnent leur mise en page 9:16 native) ; une vidéo large dont le texte serait illisible à 1080 px de large (recadrer sur la zone utile ou recomposer).
- **Règle de choix** : recomposer d'abord ; cet export est la solution rapide et propre quand on n'a que le fichier large.

## 2. Palette, typographie, matières
- **Fond** autour de la vidéo : presque noir `#0B0B0F` par défaut, ou la couleur de fond de la fiche « ma chaîne ».
- **Accroche** : la police de titre de la marque, très grasse, blanche (ou encre sur fond clair), un mot en accent au plus.
- **Logos** : uniquement depuis les fichiers fournis. **Chaque logo (et son libellé) sur sa propre tuile sombre arrondie** : un logo posé sur l'image disparaît sur les plans clairs.
- **Texte stylé en HTML, pas incrusté par ffmpeg** : on fabrique une image de surimpression transparente.
- **Police de repli** : Montserrat (800 ou 900) ou Archivo Black quand la police de titre de la marque manque. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : la police de la marque : fichier fourni par le client, copié dans `assets/fonts/` ; à vérifier (licence et accents).

## 3. Composition 9:16
- **Zone sûre de ce format** (plus stricte que la règle générale, car l'accroche doit rester lisible sous toutes les interfaces) : chaque mot et chaque logo **entre y 360 et y 1420**, et **hors des 135 px de droite** (la source dit 120 ; le plugin prend 135).
- **Accroche** : en haut de cette zone, entre y 360 et y 620 : **deux lignes courtes**, mot pour mot celles du client, 84 à 110 px, lisibles en une seconde.
- **Vidéo** : une vidéo 16:9 mise à 1080 px de large fait **608 px de haut** ; elle se pose bien à **y 660** (donc de y 660 à y 1268).
- **Sous la vidéo** (y 1290 à y 1420) : tuiles de logos ou une ligne d'appel à l'action.
- Sous y 1420 : rien. À droite de x 945 : rien d'important.
- **Variante « zoom utile »** : si l'interface est illisible, recadrer la vidéo source sur sa zone d'action (jusqu'à 4:3 ou 1:1), ce qui donne une vidéo de 810 à 1080 px de haut ; l'accroche remonte alors à y 200-340 et la vidéo commence à y 380.

## 4. Ce qui bouge
- **Action principale** : la vidéo d'origine elle-même.
- **Boucles de fond** : aucune obligatoire. En option, si l'on assemble dans HyperFrames plutôt qu'en ffmpeg : l'accroche qui se pose dans la première demi-seconde et un soulignement d'accent qui se trace.
- **Autorisés** : #005 révélation par masque de l'accroche (0,4 s), #086 soulignement animé, #028 poussée lente de 3 à 5 % sur la vidéo si elle est très statique.
- **Interdits** : fond dupliqué et flouté de la vidéo (se lit comme un remplissage paresseux), accroche qui bouge pendant qu'on la lit, plus de deux lignes d'accroche, texte dans le bas du cadre.

## 5. Rythme et montage
- L'accroche est présente **dès l'image 0** (c'est la vignette) et reste toute la durée, ou au moins les 3 premières secondes.
- La vidéo démarre immédiatement : pas de carton d'introduction.
- Si la vidéo large commence lentement, couper son début pour que l'action démarre dans la première seconde.
- Durée : celle de la source, idéalement 15 à 45 s pour un reel.
- **Version courte (8 à 12 s)** : couper la source sur sa meilleure action (8 à 10 s) ; l'accroche de deux lignes est là dès l'image 0 et l'action démarre dans la première seconde.

## 6. Recette technique
- **Moteur** : ffmpeg pour l'export direct ; HyperFrames si l'on veut animer l'accroche ou ajouter des sous-titres.
- **Étapes (export direct)** :
  1. Fabriquer `surimpression.png`, transparent, 1080×1920, en HTML (accroche + tuiles de logos), et le capturer.
  2. Composer et encoder :
```bash
ffmpeg -y -i entree.mp4 -loop 1 -i surimpression.png -f lavfi -i anullsrc=r=48000:cl=stereo \
 -filter_complex "color=c=0x0B0B0F:s=1080x1920:r=30[fond];[0:v]fps=30,scale=1080:-2,setsar=1[v];\
[fond][v]overlay=0:660:shortest=1[o];[o][1:v]overlay=0:0:shortest=1,\
scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[sortie]" \
 -map "[sortie]" -map 2:a -shortest -c:v libx264 -profile:v high -crf 18 -pix_fmt yuv420p \
 -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
 -c:a aac -b:a 128k -movflags +faststart reel.mp4
```
  Cette commande ajoute une piste audio **muette**. Si la vidéo a son propre son, remplacer `-map 2:a` par `-map 0:a`.
  3. Contrôler avant l'envoi :
```bash
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,pix_fmt,color_range,color_space -of compact reel.mp4
```
  **Réussi** = vidéo `h264`, `1080` × `1920`, `yuv420p`, `color_range=tv`, `bt709`, **et** une piste audio `aac`. Si l'on voit `hevc` ou `color_range=pc` : réencoder. Puis extraire une image du milieu et la regarder à la taille d'un téléphone.
- **Version HyperFrames** : la vidéo en `<video class="clip">` à `top: 660px; width: 1080px`, l'accroche en HTML ; rendu avec le préréglage portrait du skill `rendu`, puis le même contrôle `ffprobe`.
- **Pièges** (appris à la dure par l'auteur de la source) :
  - **Un enregistrement de téléphone est souvent en HEVC et en pleine plage** : envoyé tel quel, il ressort délavé ou mal réencodé. Toujours exporter un H.264 neuf en plage limitée, **y compris après la moindre retouche**.
  - **`+faststart` compte** : sans lui, le fichier ne peut pas commencer à jouer avant d'être entièrement chargé.
  - **Garder l'accroche à deux lignes.**
  - Une vidéo sans aucune piste audio est parfois refusée ou mal traitée : toujours une piste AAC, même muette.

## 7. Son
- Garder le son d'origine s'il existe ; sinon la piste muette. Si l'on ajoute une musique, appliquer les règles du skill `son` et viser −14 LUFS.
- Ne pas renormaliser un son déjà masterisé à −14 LUFS : vérifier d'abord la mesure.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] `ffprobe` : `h264`, 1080×1920, `yuv420p`, `color_range=tv`, `bt709`, une piste `aac`.
- [ ] Aucun mot ni logo hors de y 360 à y 1420, ni à droite de x 945.
- [ ] Accroche en deux lignes, lisible en une seconde, présente dès l'image 0.
- [ ] Une image du milieu regardée à la taille d'un téléphone : l'interface de la vidéo se lit (sinon, variante « zoom utile » ou recomposition).
- [ ] Chaque logo sur sa tuile sombre, depuis son fichier d'origine.
- [ ] Couleurs non délavées par rapport à la source (comparaison côte à côte d'une image).
- [ ] Le fichier démarre tout de suite en lecture (`+faststart`).
- [ ] L'accroche est mot pour mot celle du client.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Aucun aperçu fourni dans le dépôt d'origine pour ce format. Aperçu Flot Web à produire (avant / après).

## 10. Origine
- Dépôt : charlie947/motion-graphics-skills, commit `229022e`. Fichier : `skills/reel-export/SKILL.md`.
- Licence : MIT (© 2026 Charlie Hills).
- Adaptations Flot Web : français, marge droite portée à 135 px, variante « zoom utile », version HyperFrames, renvoi vers la recomposition native quand elle est possible. Voir aussi `references/exports.md` du skill `rendu`.
