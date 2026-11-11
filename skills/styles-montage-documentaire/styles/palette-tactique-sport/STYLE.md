# Palette tactique sport

## 1. Identité
- **Nom** : Palette tactique sport. Identifiant : `palette-tactique-sport`.
- **Inspiration** : la séquence d'analyse des émissions de sport, où le consultant fige l'image et dessine dessus, et les chaînes d'explication qui annotent de vraies images de match. Grammaire seulement : aucun logo, police, couleur, jingle ou graphisme d'un diffuseur, aucun nom cité.
- **Principe** : on montre l'action à vitesse réelle, on rembobine, on fige, et on **dessine sur l'image réelle** : anneaux sous les pieds des joueurs, flèches au marqueur pour la balle, tache rouge sur l'espace que personne ne couvrait ; puis on relance, on change d'angle, on compte les images, et on aplatit le terrain en tableau. Un habillage d'émission (jingle, pastille de coin, barre de score, volet jaune) tient le tout.
- **Cinq règles** : on regarde avant d'expliquer (un arrêt suit toujours du jeu) ; un arrêt = un constat ; tout est dessiné sur la vraie image et bouge avec elle ; les données sont comptées dans les images (temps = nombre d'images, distances = lignes du terrain) ; énergie de plateau.
- **Pour quels sujets** : analyse d'une action de match, résumé commenté, vidéo d'entraîneur ou de club amateur, décryptage d'un geste technique (tout sport filmé en plan large), et par extension toute séquence filmée qu'on veut décortiquer (danse, cuisine, geste d'artisan).
- **Ne marche pas pour** : un best-of de buts sur de la musique (chaque extrait doit être analysé), un sujet sans images du client ou sans droits sur les images. Ce n'est pas une enquête (ici : enthousiasme et habillage), ni une infographie (le tableau vu du dessus n'apparaît qu'une fois, en résumé).

## 2. Palette, typographie, matières
| Rôle | Couleur |
|---|---|
| L'équipe ou le joueur qu'on suit, la balle, les traits principaux | `#FFD400` jaune fluo |
| Adversaires (anneaux, flèches de blocage, lignes de liaison) | `#3FD8FF` cyan |
| L'espace (zone que personne ne couvre) | `#FF3B30` rouge, remplissage 0,34 à 0,38 + bord en tirets |
| Lignes du terrain retracées, marques neutres, tampons | `#F4F1E8` craie |
| Tableau de l'émission | `#0C1411` noir vert, grille discrète de 60 px |
| Fond des étiquettes et pastilles | `rgba(8,12,14,0.9)` |

**Une couleur = une identité** pendant tout le film : la barre gauche d'une étiquette prend la couleur de ce qu'elle nomme. On peut changer les teintes (couleurs de la fiche « ma chaîne »), jamais les trois rôles.
- **Polices libres** : étiquettes en sans ultra-gras ; chiffres d'habillage (score, minute, chronomètre) en Barlow Condensed 800 Italic ; horloge et numéros d'image en IBM Plex Mono. **Aucune police manuscrite** (elle fait cahier d'écolier).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Trait au marqueur** : contour sombre (largeur + 6, noir à 0,55) + cœur coloré avec halo + fin reflet blanc ; tirets pour une trajectoire voulue ou future, trait plein pour ce qui s'est passé.
- **Étalonnage** unique : `hqdn3d=1.2:1.2:2.5:2.5` → `lanczos` (≤ 1,5×) → `unsharp=5:5:0.55` → `eq=saturation=0.9:contrast=1.04:gamma=0.97`.

## 3. Composition 9:16
- **Image de match** : le plan large d'un match est horizontal. Deux mises en page : (a) **bande 16:9 pleine largeur** (1080×608) vers y 420 à y 1030, tableau d'émission au-dessus et en dessous ; (b) **recadrage vertical** sur la zone de l'action (≤ 1,5× d'agrandissement), le recadrage suit le jeu.
- **Pastille de coin** : en haut à gauche, sous y 170 : nom de l'émission sur pavé jaune + ligne de mode (DIRECT point rouge / ANALYSE jaune / RALENTI cyan). Présente dès l'image 1.
- **Horloge de source** : sous la pastille, sur chaque plan d'analyse : `❚❚ 04,20 s  i106` (secondes et numéro d'image de la source).
- **Barre de score** : sous l'image, vers y 1060 à y 1130, à gauche de x 945 ; le chiffre bascule sur l'image où la balle franchit la ligne.
- **Étiquette de constat** (carte noire, barre colorée à gauche, 44 px minimum) : dans de l'herbe ou de la tribune vide, jamais sur l'action décrite.
- **Sous-titres** : y 1300 à y 1520, barre noire à 0,64 avec liseré jaune de 4 px.
- **Double angle** : deux fenêtres empilées (haut / bas) au lieu de côte à côte, séparateur jaune de 6 px, libellé de caméra en haut à gauche de chacune.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : image plein cadre, pastille en haut à droite, barre de score en bas à droite, horloge en haut à gauche, sous-titres centrés en bas.

## 4. Ce qui bouge
- **Action principale** : l'entrée dans l'arrêt sur image. Flash blanc 0,1 s (0,55) + coup de zoom 1,035 → 1,0 en 0,35 s + désaturation 42 % + dominante froide + vignette plus forte ; puis une dérive lente de 1,2 %. Ordre de dessin dans l'arrêt : anneau (qui) → zone ou liaison (ce qui s'est passé) → étiquette (le constat en une ligne), espacés de 0,3 à 0,6 s.
- **Boucles de fond** : (1) l'anneau extérieur en tirets qui tourne à 60 px/s sous le joueur ; (2) l'horloge de source qui compte les images.
- **Gestes** : rembobinage (extrait inversé en 0,6 s, tremblement horizontal de ±13 px, quatre barres blanches de pistage, gros ◀◀) ; projecteur (tout ce qui est hors d'une ellipse s'assombrit à 0,42 en 0,3 s) ; chronomètre qui compte les images depuis la réception jusqu'à la frappe, puis s'arrête en jaune ; traînée de comète sur la balle (0,24 s seulement) ; aplatissement du terrain en carte de tirs ; tampon (une seule fois par film, tombe de 1,7× à 1× avec dépassement).
- **Autorisés** : #040 arrêt sur image, #004 tracé de ligne, #037 ralenti (0,6 à 0,85×, images voisines fondues), #014 traînée, #144 écran partagé, #164 chronomètre, #045 volet d'habillage (bande jaune inclinée en 0,34 s, seulement entre deux segments), #046 coupe sèche dans un segment, #010 dépassement (tampon).
- **Interdits** : #044 fondu, #140 page qui tourne, traînées longues (la caméra panote, elles tombent au mauvais endroit), dessin qui flotte hors de l'image avant l'aplatissement, pastille qui apparaît en fondu.

## 5. Rythme et montage
- **Ordre dans une action** : direct à 1× (son d'origine) → rembobinage 0,6 s → arrêt ① → ralenti → arrêt ② → ralenti avec chronomètre → arrêt ③ → vol de la balle → autre angle.
- Variantes légères pour les actions secondaires : **arrêt en plein jeu** (pas de rembobinage) ; **arrêt double angle** (les deux angles arrivent au même instant et se figent ensemble, le même joueur est entouré dans les deux).
- **Durée d'un arrêt** : 1,8 à 2,4 s ; au-delà de ~2,5 s il faut une seconde action dedans. Deux à quatre arrêts par action.
- Les mêmes secondes d'images sont réutilisées, chaque passage allant une couche plus profond.
- Cartes de comparaison (carte de tirs, fiche de chiffres) entièrement dessinées tôt et tenues ≥ 2,5 s. Une étiquette d'arrêt redit le sous-titre et ne vit qu'~1 s.
- **Version courte (8 à 12 s)** : une action et deux arrêts de 1,8 s : direct (1,5 s), rembobinage (0,6 s), arrêt ①, ralenti, arrêt ② ; couper le chronomètre.

## 6. Recette technique
- **Moteur** : HyperFrames. L'extrait est préparé en séquence d'images (un dossier par extrait) et dessiné sur un `<canvas>` depuis un écouteur `hf-seek` : c'est ce qui permet l'arrêt, le rembobinage et le ralenti exacts à l'image. Les dessins sont dans le même repère que l'image.
```js
// segments : {t0, t1, clip, f0, f1, mode: "direct" | "arret" | "ralenti" | "retour"}
window.addEventListener("hf-seek", (e) => {
  const s = segmentA(e.detail.time), u = (e.detail.time - s.t0) / (s.t1 - s.t0);
  const f = s.mode === "arret" ? s.f0 : s.f0 + (s.f1 - s.f0) * u;   // f1 < f0 pour le retour
  ctx.save(); appliquerCoupDeZoom(ctx, s, u);       // même transformation pour l'image ET les dessins
  dessinerImage(s.clip, f); dessinerAnnotations(s, u); ctx.restore();
});
```
- **Anneau suivi** : points clés posés à la main sur les pieds, en pixels de la source, toutes les 3 à 6 images, interpolés. Les lire sur des recadrages en pleine résolution, puis contrôler avec un mode de débogage qui peint tous les points suivis.
- **Chronomètre** : nombre d'images de la source ÷ cadence. Ne jamais écrire ce que l'image ne peut pas mesurer (vitesse de balle, distance parcourue).
- **Aplatissement** : pour chaque tir, marquer 6 à 8 points connus du terrain dans sa propre image (coins de surface, dimensions officielles) et ajuster une homographie du plan du sol (résidus ≤ 6 px) ; dessiner l'image de frappe comme un maillage de triangles dont chaque sommet glisse de sa position image à sa position tableau. Version exigeante : à faire en Three.js ou Blender (plan texturé qui bascule en vue du dessus).
- **Habillage sur les filigranes** : pastille et barre de score posées exactement sur le logo et l'adresse du diffuseur, dès l'image 1. Voir la section droits ci-dessous.
- **Pièges** : dessins hors de la transformation du coup de zoom = ils glissent des joueurs ; l'état du score doit correspondre à l'instant ; fenêtres de double angle rognées en coordonnées de la source, pas seulement à l'écran.

## 7. Son
- **Couches** : voix (une phrase par arrêt, 2,5 à 3 s) → son du match (commentaire et foule à plein niveau en direct ; sous un arrêt, seulement un lit de foule filtré ; clameur sur l'image du but) → musique → bruitages.
- **Musique** ~120 BPM. **Sur un arrêt, la batterie s'arrête** : un accent de cuivres + coup sourd + obturateur, puis seulement le charleston : la musique se fige avec l'image.
- **Bruitages** (budget du skill `son`) : crissement de marqueur par trait, petit « pop » par anneau, souffle sur chaque volet, moteur de bande sur un rembobinage, tic de chronomètre.
- −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] **Droits sur les images** : le client possède les images (son propre match filmé) ou une licence écrite ; les images de diffuseurs sont protégées. Couvrir un logo n'autorise pas l'usage.
- [ ] Chaque arrêt suit du jeu vu à vitesse réelle et ne dit qu'une chose (une étiquette, deux groupes de traits au plus).
- [ ] Trois rôles de couleur constants du début à la fin.
- [ ] Les anneaux restent sous les pieds pendant tout le plan (contrôle en mode débogage, image par image sur 1 s).
- [ ] Tous les chiffres viennent d'un comptage d'images ou des lignes du terrain ; un « ≈ » quand la balle est invisible.
- [ ] Pastille présente dès l'image 1 ; score juste à chaque instant.
- [ ] Noms propres : orthographe phonétique pour la voix, vraie orthographe dans les sous-titres.
- [ ] Ce qui doit être lu (scores, lignes du tableau) tient ≥ 2,5 s et reste hors zones d'interface.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/telestrator.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/telestrator.jpg
- Crédit : « Freeze Frame », LemoLab, CC BY 4.0. Le film contient des images de match d'un diffuseur et une photo de tiers sous leurs propres licences (CC BY 3.0 / 2.0), ainsi que des noms de clubs : **lien seulement**, jamais comme visuel de vente. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/telestrator/STYLE.md`, `style.json`, `demo/index.html` (`overlayAnalysis()`, `TRK`, `stopwatch()`, `splitView()`, `shotMap()`, `drawTri()`), `demo/tools/homography.py`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, deux mises en page 9:16, HyperFrames, mise en garde sur les droits des images de match.
