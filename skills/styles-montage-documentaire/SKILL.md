---
name: styles-montage-documentaire
description: "Catégorie de styles « Montage et documentaire » du studio motion : monter ses propres rushes (couper silences et ratés, reel face caméra, animations pendant qu'on parle, détourage), huit styles de montage documentaire (info sous-titres, actualités 1920, compte à rebours, time-lapse, enquête, constructiviste, palette sport, habillage de JT) et huit « films de preuves » (satellite, tableau de briefing, nuage de points, maquette projetée, données en objets, vue éclatée, microscope, table lumineuse). À utiliser quand le client fournit une vidéo de lui à monter, ou veut une vidéo bâtie sur du matériel réel : archives, documents, données, images, produit."
---

# Styles Montage et documentaire (catégorie 10)

Vingt fiches. Leur point commun : **le matériel est réel**. Le look ne vient pas d'un dessin mais de la façon dont on coupe, range, légende, mesure et fait sonner des rushes, des archives, des documents, des données ou un vrai objet.

Le skill `studio-coeur` pilote le parcours (questions, histoire, storyboard, revue, livraison). `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, transcription, sous-titres, export), `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s), `marque` (fiche « ma chaîne ») et `blender` (3D par le connecteur `blender`) s'appliquent. Les noms, couleurs et logos d'émission viennent toujours de la fiche « ma chaîne » du client.

**À lire avant toute fiche de cette catégorie : `references/materiel-et-droits.md`** (demander le matériel du client, sources libres, licences, `SOURCES.md` / `FAITS.md` / `CREDITS`, personnes à l'écran, limites d'agrandissement).

## Famille A : monter ses propres rushes

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `derushage-silences-rates` | Dérushage : silences et ratés | Retire l'air mort en gardant les respirations, puis bégaiements, faux départs et reprises après relecture | ffmpeg + outils de `rendu` | facile | à produire |
| `reel-face-cam` | Reel face caméra | Accroche en 3 s, écran partagé / illustration / gros plan, sous-titres mot à mot dans une boîte unique, musique 11 dB sous la voix | hyperframes | moyenne | à produire |
| `animations-sur-la-voix` | Animations pendant qu'on parle | Une forme qui ne coupe jamais, pilotée par un curseur, chaque changement sur un mot prononcé | hyperframes | moyenne | [GIF](https://github.com/Barty-Bart/motion-graphics/blob/main/docs/demo-cutaway.gif) (Bart, MIT) |
| `detourage-sujet` | Détourage du sujet | Isoler le client ou un objet pour passer un mot ou une forme derrière lui | outil de détourage + hyperframes | moyenne | [GIF](https://github.com/Barty-Bart/motion-graphics/blob/main/docs/object-separation.gif) (Bart, MIT) |

Ordre normal : `derushage-silences-rates` → `reel-face-cam` → (au choix) `animations-sur-la-voix`, `detourage-sujet`.

## Famille B : montage documentaire (8 styles)

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `info-sous-titres` | Info sous-titres | Actu lisible sans le son : énormes sous-titres claqués par blocs, mot-clé sur pavé jaune, source et document surlignés | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/caption-news.mp4) (LemoLab, CC BY 4.0) |
| `actualites-1920` | Actualités filmées 1920 | Vraies archives dans une fenêtre de projection, journal qui tournoie, speaker enjoué, orchestre qui s'arrête pour la chute | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/newsreel.mp4) (LemoLab, CC BY 4.0) |
| `compte-a-rebours-direct` | Compte à rebours en direct | Temps réel d'un événement : l'écran se divise de 1 à 9 cases sur la même seconde, fusion à zéro | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/countdown.mp4) (LemoLab, CC BY 4.0) |
| `symphonie-time-lapse` | Symphonie en time-lapse | Film de lieu monté comme une musique répétitive, sans narrateur, coupe au noir sur un temps fort | ffmpeg + hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/city-symphony.mp4) (LemoLab, CC BY 4.0) |
| `enquete-visuelle` | Enquête visuelle | Vidéos, photos, documents et cartes d'un événement réel sur une seule horloge qui les recoupe | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/visual-investigation.mp4) (LemoLab, CC BY 4.0) |
| `montage-constructiviste` | Montage constructiviste | Archives tirées encre et papier + un seul rouge, bandes diagonales, chocs d'images, rythme de machine | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/kino-montage.mp4) (LemoLab, CC BY 4.0) |
| `palette-tactique-sport` | Palette tactique sport | On fige, on rembobine et on dessine sur l'image réelle : anneaux, flèches, zones, puis carte tactique | hyperframes (canvas) | élevée | lien dans la fiche (démo avec images de diffuseur et noms de clubs : pas en vitrine) |
| `habillage-jt` | Habillage de journal télévisé | Jingle qui devient pastille, sommaire, bandeau permanent, graphiques plein cadre : tout en code | hyperframes | moyenne | affiche dans la fiche (voix du film exclue de la licence, marques citées : pas en vitrine) |

## Famille C : films de preuves (8 styles)

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `briefing-satellite` | Briefing satellite | Imagerie satellite réelle en gris d'analyste, lignes de mesure blanches, un zoom continu orbite → sol | hyperframes + three (blender pour l'orbite) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/satellite-briefing.mp4) (LemoLab, CC BY 4.0) |
| `tableau-de-briefing` | Tableau de briefing | Vrai tableau blanc filmé : photos détourées, aimants, tampons, feutre en trois couleurs au sens fixe, recul final | hyperframes 2.5D (blender en option) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/briefing-board.mp4) (LemoLab, CC BY 4.0) |
| `releve-lidar` | Relevé LiDAR | Vrai nuage de points d'un lieu ; un plan de coupe le condense en relief éclairé rasant, mesuré au trait fin | three dans hyperframes (blender en option) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/lidar-survey.mp4) (LemoLab, CC BY 4.0) |
| `maquette-blanche-projetee` | Maquette blanche projetée | Maquette blanche d'un vrai lieu ; un projecteur y peint les données couche par couche, seule la lumière change | blender + hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/white-model.mp4) (LemoLab, CC BY 4.0) |
| `donnees-en-objets` | Données en objets | Statistiques construites en plaques, blocs ou pièces à l'échelle exacte, filmées comme un produit en studio | blender + hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/data-physical.mp4) (LemoLab, CC BY 4.0) |
| `vue-eclatee` | Vue éclatée | Vrai produit démonté sur un axe depuis ses fichiers techniques, pièces nommées et chiffrées | blender + hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/teardown.mp4) (LemoLab, CC BY 4.0) |
| `recit-au-microscope` | Récit au microscope | Vraie microscopie, un seul changement d'échelle de la lame à la cellule, barres d'échelle tirées des métadonnées | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/microscope.mp4) (LemoLab, CC BY 4.0) |
| `table-lumineuse-archives` | Table lumineuse d'archives | Objets d'archives sur table lumineuse ; une loupe descend et l'objet s'anime dans le verre | hyperframes 2.5D (blender en option) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/archive-lighttable.mp4) (LemoLab, CC BY 4.0) |

Tous les films d'aperçu LemoLab sont en 16:9 et contiennent du matériel de tiers sous sa propre licence : on les montre par un lien, crédités « LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 », sans en extraire de plans.

**Voir aussi (fiches portées par une autre catégorie)**, quand le client n'a pas de matériel réel ou veut un passage dessiné :

- `typo-cinetique` (le mot comme acteur : accroche, liste, chiffre, carte de chapitre entre deux plans) : `styles-graphique-typo/styles/typo-cinetique/STYLE.md` ;
- `constructivisme` (l'affiche dessinée ; ici, `montage-constructiviste` monte de vraies images) : `styles-graphique-typo/styles/constructivisme/STYLE.md` ;
- `tableau-blanc` et `tableau-blanc-a-la-main` (tableaux dessinés ; ici, `tableau-de-briefing` est un vrai tableau filmé) : `styles-peinture-dessin/styles/tableau-blanc/STYLE.md`, `styles-explicatif-infographie/styles/tableau-blanc-a-la-main/STYLE.md` ;
- `collage-enquete` (de vrais documents sur une table, surlignés et reliés de rouge ; voisin de `enquete-visuelle`) : `styles-explicatif-infographie/styles/collage-enquete/STYLE.md`.

## Comment choisir

Pose une seule question : **« Qu'as-tu comme matériel réel ? »**

| Le client a… | Styles à proposer (le premier est le conseillé) |
|---|---|
| Une vidéo de lui qui parle | `derushage-silences-rates` puis `reel-face-cam` ; ajouter `animations-sur-la-voix` s'il explique un outil ; `detourage-sujet` pour 1 à 3 moments forts |
| Un rapport, une étude, un chiffre qui surprend | `info-sous-titres` ; `donnees-en-objets` si deux séries à comparer |
| Plusieurs actus de la semaine, aucune image | `habillage-jt` |
| Des archives filmées ou imprimées d'une époque | `actualites-1920` (ton léger) ; `montage-constructiviste` (effort collectif, chantier) ; `table-lumineuse-archives` (histoire d'une marque, d'une famille) |
| Plusieurs caméras d'un même instant | `compte-a-rebours-direct` (un zéro connu) ; `enquete-visuelle` (comprendre ce qui s'est passé) |
| Des time-lapses d'un lieu | `symphonie-time-lapse` |
| Des images d'un match ou d'un geste filmé, avec les droits | `palette-tactique-sport` |
| Un lieu vu du ciel, un changement dans le temps | `briefing-satellite` ; `releve-lidar` s'il existe un relevé laser ; `maquette-blanche-projetee` pour un quartier |
| Des objets à comparer, un plan, un budget | `tableau-de-briefing` |
| Un produit matériel et ses fichiers | `vue-eclatee` |
| Un échantillon, un matériau, de la biologie | `recit-au-microscope` |

Débutant : commence par `derushage-silences-rates` + `reel-face-cam`, ou par `habillage-jt` (aucun rush nécessaire). Les styles marqués « blender » demandent Blender installé (skill `blender`).

## Règles communes à la catégorie

1. **Le matériel avant l'histoire.** Dans cette catégorie seulement, on rassemble et on vérifie le matériel **avant** d'écrire le traitement : c'est lui qui dit quelle histoire est possible.
2. **Rien de généré ne remplace du réel.** Ni archive, ni preuve, ni lieu, ni objet, ni personne. Faute de matériel libre : changer de style, dessiner un schéma annoncé comme tel, ou étiqueter « ILLUSTRATION ».
3. **Chaque nombre a une source**, écrite dans `FAITS.md` avec la formulation citée, et visible à l'écran quand la fiche le demande. Les mots ne sont jamais plus forts que la source.
4. **Une seule couleur d'accent, qui veut dire quelque chose** (le mesuré, le point clé, la décision). Le reste appartient au matériel.
5. **Un constat par écran**, puis le temps de le lire : sous-titre ≥ 1,8 s ; texte (lettres ÷ 15 + 1,5) s ; comparaison et verdict ≥ 2,5 s.
6. **Les marques restent collées au matériel** : même transformation pour l'image et pour ce qu'on dessine dessus (anneaux, cotes, étiquettes), sinon elles glissent au premier mouvement de caméra.
7. **Zone sûre 9:16** : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Les démos d'origine sont en 16:9 : la section 3 de chaque fiche donne la mise en page verticale, qui est **une autre mise en page, pas un recadrage**.
8. **Retenue** : pas de ralenti sur un drame, pas de bruitage sur des victimes, pas d'anonyme en héros de gros plan.
9. **Anti-copie de la démo** : la démo d'origine sert à comprendre une technique, jamais son sujet, ses plans ni sa structure. Aucun nom de média, de chaîne, de club ou de marque des démos ne passe dans la vidéo d'un client.
10. **Son** : plusieurs fiches décrivent « un son pour chaque action ». On garde l'idée (le son de la matière) mais on applique le budget du skill `son` : choisir les actions qui comptent. Exception assumée : `symphonie-time-lapse` (musique seule).

## Du moteur d'origine à HyperFrames

Les démos d'origine sont des pages « une image = une fonction du temps ». Dans HyperFrames, la même fonction se branche sur l'évènement de déplacement dans le temps :

```js
window.addEventListener("hf-seek", (e) => dessiner(e.detail.time));   // canvas, Three.js
```

**Timeline à enregistrer.** Un film dessiné par `hf-seek` doit quand même enregistrer une timeline, même vide, après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire le contrôle qui détecte un film figé. Recette complète : skill `rendu`, section « Film en canvas piloté par `hf-seek` » (vérifiée en rendu réel le 11/11/2026).

Tout ce qui est texte, carte, bandeau, sous-titre ou trait passe de préférence en HTML/SVG animé par une timeline GSAP en pause (plus simple à contrôler par `npx hyperframes check`). Aléatoire toujours à graine fixe ; aucune horloge réelle. Les styles 3D lourds se rendent dans Blender en séquence d'images, puis s'assemblent dans HyperFrames avec les relevés et sous-titres.

## Fiches

`styles/<identifiant>/STYLE.md`, dix sections fixes (identité, palette, composition 9:16, ce qui bouge, rythme, recette technique, son, liste de contrôle, aperçu, origine). Crédits et licences : `licenses/styles-montage-documentaire.md` à la racine du plugin.
