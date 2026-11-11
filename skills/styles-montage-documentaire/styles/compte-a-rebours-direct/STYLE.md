# Compte à rebours en direct (écran qui se divise)

## 1. Identité
- **Nom** : Compte à rebours en direct. Identifiant : `compte-a-rebours-direct`.
- **Inspiration** : l'horloge en temps réel et les écrans divisés des séries d'action des années 2000 ; les panneaux multi-caméras et les codes de temps des documentaires spatiaux récents. Grammaire seulement : ni leur typo, ni leurs couleurs, ni leurs sons, et jamais leur nom dans la vidéo.
- **Principe** : un style de montage, pas un look. De vraies images d'un événement qui a un **zéro connu** (lancement, verdict, coup de sifflet final, fermeture des votes, ouverture d'une boutique), montrées en temps réel : une seconde d'écran = une seconde d'événement. Une horloge bat chaque seconde ; l'écran se divise en cases de plus en plus nombreuses à l'approche du zéro, toutes sur la même seconde ; à zéro, les cases fusionnent en une image et l'horloge s'inverse.
- **Pour quels sujets** : lancement d'un produit ou d'une fusée, dernière minute d'un match, ouverture des portes, mise en ligne, résultat d'un concours.
- **Ne marche pas pour** : un événement sans instant zéro, un sujet où l'on n'a qu'une seule caméra et aucun document, un récit qui doit revenir en arrière. Ce n'est pas un montage (pas de saut de temps), pas un mur de vidéosurveillance (la mise en page bouge), pas un diaporama.

## 2. Palette, typographie, matières
| Rôle | Valeur |
|---|---|
| Fond | `#06080A` ; panneaux `#0B0E11` |
| Texte principal / secondaire | `#F2F5F7` / `#7C878D` |
| Accent : signe T−, pastille « synchronisé », coche faite, drapeau d'événement | `#FF5B1F` |
| Voyant « parole en cours » | `#FF3B30` |
| Après zéro, bloc horloge inversé | fond `#FF5B1F`, texte `#0A0B0C` |

Orange = « maintenant / synchronisé / fait ». Gris = « en attente / non synchronisé ». Rien d'autre n'est coloré : la couleur appartient aux images.
- **Polices libres** : chiffres d'horloge en sans condensée demi-grasse (Barlow Condensed SemiBold) dessinée chiffre par chiffre dans des **cases de largeur égale** ; textes en Barlow ; codes et étiquettes en IBM Plex Mono.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; Inter à la place de Barlow ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed`, `@fontsource/barlow` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Cases** : rectangles durs, bordure 1 px `rgba(222,232,238,.16)`, gouttières de 8 à 9 px, légère vignette sur les cases vidéo. Ni coins arrondis, ni ombres, ni 3D.
- **Étiquette de caméra** en haut à gauche de chaque case : plaque sombre, point carré (orange = synchronisé, gris = non synchronisé ou image fixe), code (`CAM 4`, `DOC`, `LISTE`), nom.
- **Un seul étalonnage** pour toutes les sources (ombres froides, hautes lumières un peu chaudes) : `eq=contrast=1.07:saturation=0.9:gamma=0.97:brightness=-0.01,colorbalance=rs=-0.02:bs=0.03:rh=0.03:bh=-0.02`.

## 3. Composition 9:16
- Les cases s'empilent **verticalement** : 1 → 2 (une sur l'autre) → 3 → grille 2×3 ou 2×4 près du zéro. Zone des cases : y 170 à y 1250, x 30 à x 940 ; les étiquettes et les chiffres posés dans les cases commencent à x 60 au moins.
- **Horloge** : bloc fixe entre y 1270 et y 1420, chiffres 120 à 132 px, signe T−/T+ à 0,85×, dixièmes à 0,41× en gris, barre de dix segments dessous (elle se vide d'un segment par 0,1 s, se remplit après zéro).
- **Transcription en direct** (elle sert de sous-titre) : boîte fixe entre y 1430 et y 1550, voyant de parole + type de locuteur, une ou deux lignes de 40 px minimum. Le narrateur maison est marqué en orange pour ne jamais être confondu avec le son de l'événement.
- Moment plein écran (à zéro) : l'image occupe y 170 à y 1250 en plein cadre ; horloge et transcription restent sur leurs plaques.
- Rien d'important au-dessus de y 160, sous y 1560, ni à droite de x 945.
- **16:9** : marge extérieure 24 px, grille jusqu'à 3×3, horloge et transcription en bas à droite ou dans des cases de la grille.

## 4. Ce qui bouge
- **Action principale** : le changement de mise en page. 0,34 s en accélération-décélération ; les cases qui restent interpolent leur rectangle, les nouvelles s'ouvrent depuis leur bord gauche, celles qui partent se ferment vers la gauche ; une nouvelle case fait clignoter une bordure orange de 3 px pendant ~0,2 s.
- **Boucles de fond** : (1) l'horloge : à chaque seconde entière les nouveaux chiffres tombent de 14 px en 0,12 s ; (2) la barre des dixièmes de seconde.
- **Geste signature, « plusieurs en un »** : à zéro, chaque case rejoint sa tuile du plein cadre pendant que toutes fondent vers le même plan plein écran ; étiquettes et bordures disparaissent dans la première moitié ; flash blanc chaud `rgba(255,248,236,.7)` ; 0,42 s au total.
- **Autorisés** : #144 écran partagé, #164 compte à rebours, #045 volet (remplacement d'une source dans la même case, depuis la gauche), #046 coupe sèche (entre sources plein écran seulement), #080 surligneur sur un document, coup de zoom numérique sec sur le détail que le commentaire nomme.
- **Interdits** : #038 rampe de vitesse, #037 ralenti (une source au ralenti est remise à vitesse réelle), #041 saut de temps, poussée lente sur une vidéo pour simuler du mouvement, #140 page qui tourne, mots qui surgissent au centre.

## 5. Rythme et montage
- **Temps d'écran = temps de l'événement.** Une seule correspondance pour tout le film : `M = t − T0`. Chaque caméra a son propre décalage, mesuré une fois.
- **Les points de coupe sont des appels** : chaque changement de mise en page démarre sur le premier mot d'une vraie annonce du son d'origine (« dix », « allumage », un nom) ou sur un événement visible. La musique suit, elle ne décide jamais d'une coupe.
- **Le nombre de cases est la courbe de tension** : 1 → 2 → 3 ou 4 → beaucoup (6 à 9) → **une** à zéro → quelques-unes après (les conséquences) → une sous le titre. Les mises en page les plus courtes sont les plus proches du zéro.
- À l'intérieur d'une case, la source peut se couper elle-même (une régie qui change de caméra) : on la garde.
- **Silence avant zéro** : la musique s'arrête un quart de seconde avant ; il ne reste que le son d'origine et l'horloge.
- Toutes les 1 à 2 s, un élément nouveau (une case, une coche, un drapeau, un coup de zoom), jamais un faux mouvement de caméra.
- **Version courte (8 à 12 s)** : les dix dernières secondes du compte, avec deux changements de mise en page au plus.

## 6. Recette technique
- **Moteur** : HyperFrames. Chaque caméra est une `<video class="clip">` muette (une piste audio séparée porte le son d'origine), placée en CSS absolu ; une table de mises en page clés pilote les rectangles.
```js
const MEP = [ {t: 0, cases: {cam1: [30,170,910,1080]}},
              {t: 18.4, cases: {cam1: [30,170,910,535], cam2: [30,715,910,535]}} ];
MEP.forEach((k, i) => i && Object.entries(k.cases).forEach(([id, [x,y,w,h]]) =>
  tl.to("#" + id, {left: x, top: y, width: w, height: h, duration: 0.34, ease: "power2.inOut"}, k.t)));
```
- **Synchronisation** : ne jamais se fier aux métadonnées. Mesurer le zéro avec deux repères indépendants (un événement visible et un mot prononcé) et le remesurer sur le fichier réellement coupé (`ffmpeg -ss … -c copy` démarre sur l'image clé précédente). Régler `data-media-start` de chaque vidéo d'après son décalage. Synchroniser chaque caméra sur son image, pas sur son son.
- **Horloge** : chiffres en cases fixes, texte calculé depuis `M` dans un écouteur `hf-seek`, jamais par un minuteur.
- **Ralenti d'origine** : mesurer le facteur entre deux événements d'écart connu, puis `setpts=PTS/k`.
- **Texte incrusté dans les sources** (logos de régie, minuteurs, numéros de caméra) : définir une zone utile par plan ou flouter avec `delogo`.
- **Punch-in** : extraire le passage dans une résolution supérieure de la source au lieu d'agrandir une image 1080p (≤ 1,5×).
- **Pièges** : une ligne de sous-titre complète révèle la fin d'un décompte avant l'heure, découper le décompte en répliques séparées ; pics audio trop forts, pré-limiter le mix vers −4 dBFS.

## 7. Son
1. **Son d'origine** de l'événement (commentaire, radio, foule) : toujours au-dessus, jamais baissé.
2. **Narrateur** : rare, seulement dans les trous du son d'origine, voix différente de celles de l'événement.
3. **Horloge** : un tic par seconde (deux hauteurs alternées), plus fort dans les dix dernières secondes.
4. **Bruitages d'interface** (budget du skill `son`) : souffle + claquement métallique au changement de mise en page, tac de coche, coup sourd à la coupe plein écran.
5. **Musique à 60 BPM** (un temps = une seconde = un tic) : bourdon grave qui s'ouvre vers le zéro, roulement de timbales, silence, puis accord majeur de cuivres graves à zéro. Musique 8 à 10 dB sous le son d'origine. Si le client fournit une musique, choisir un passage dont un temps fort tombe pile sur zéro ; ne jamais déplacer l'horloge ni les coupes.
- Master −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] À n'importe quelle image, l'horloge et l'image se recoupent (contrôle sur 5 instants).
- [ ] Aucune coupe dans le temps, aucun ralenti, aucune accélération.
- [ ] Chaque case porte son badge : « synchronisé », « même période, non synchronisé image par image » ou « ralenti remis à vitesse réelle ». Une source non synchronisable n'est jamais présentée comme synchrone.
- [ ] Chaque changement de mise en page tombe sur un appel réel (écart < 2 images).
- [ ] Les chiffres de l'horloge ne tremblent pas (cases fixes).
- [ ] Un quart de seconde de silence musical avant zéro.
- [ ] `FAITS.md` : heures prévues et heures réellement entendues tenues séparément, sources officielles.
- [ ] Aucun insigne officiel utilisé comme graphisme ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : fixe
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 40

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/countdown.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/countdown.jpg
- Crédit : « Counting Itself Down », LemoLab, CC BY 4.0. Images d'agence publique dans le film : **lien seulement**, à ne pas utiliser comme visuel de vente. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/countdown/STYLE.md`, `style.json`, `demo/index.html` (`LAY`, `drawClock()`, `drawTx()`, `drawCheck()`), `demo/tools/prep.sh`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, empilement vertical des cases, HyperFrames. Sources et droits : `references/materiel-et-droits.md`.
