# Tableau de briefing

## 1. Identité
- **Nom** : Tableau de briefing (d'ingénieur). Identifiant : `tableau-de-briefing`.
- **Inspiration** : les explications filmées devant un mur de cartes, le long recul sur un mur couvert de travail, les conventions du dessin technique (plan au-dessus de l'élévation, cotes, hachures). Grammaire seulement, aucun nom cité.
- **Principe** : **un vrai tableau blanc, filmé**. Lumière de fenêtre sur l'émail, fantômes de feutre effacé, cadre et gouttière. Des photos détourées de vraies choses s'y posent avec du poids ; étiquettes, aimants, règle et tampons y sont fixés ; l'encre du feutre se trace seule, en **trois couleurs au sens fixe**. La caméra suit les lignes d'un fait à l'autre et ne recule qu'à la fin pour montrer tout le briefing.
- **Cinq règles** : un tableau physique dans une pièce ; de vraies choses dessus (jamais une image générée présentée comme l'objet réel) ; une encre qui veut dire quelque chose ; un seul mur continu, sans pages ; le mur entier, une seule fois, au dernier recul, comme une affiche.
- **Pour quels sujets** : comparaison chiffrée d'objets réels (autonomie de quatre voitures, tailles, coûts), plan d'action, feuille de route, budget d'un foyer, choix entre des options avec verdict, goulot d'étranglement d'un procédé.
- **Ne marche pas pour** : un sujet abstrait sans objets à photographier, une histoire à personnages, un sujet à moins de trois faits mesurables. Ce n'est pas l'explication « main qui dessine sur une page plate », ni un film de données, ni une présentation.

## 2. Palette, typographie, matières
- **Fond** : émail blanc cassé avec dégradé de fenêtre et reflet diagonal qui glisse ; mur gris chaud neutre autour.
- **Encre, trois sens fixes** : **graphite** = noms, règles, faits ; **bleu** = eau et mesure (cotes, lignes de projection, nombres mesurés) ; **rouge** = la décision seulement (un rejet, le mot clé d'un verdict, la seule marque à remarquer). Gris pour le dessin technique (lignes d'attache, hachures). Rouge rare : deux ou trois marques par image au plus, jamais sur un objet rouge. La couleur pleine appartient aux photos ; les accessoires restent neutres ; un aimant rouge est un verdict.
- **Encre** : aplat à ~90 % en `multiply`, cœur plus clair, bouts ronds, reflet humide sur le trait en cours. Effacer laisse un fantôme flou (~7 %).
- **Polices libres** : une police « feutre » à graisse unique pour l'écriture au tableau (révélée glyphe par glyphe avec inclinaison et ligne de base légèrement irrégulières, à graine fixe) ; sans robuste pour les étiquettes imprimées ; mono pour les crédits.
- **Police de repli** : aucune police « feutre » n'est fournie : Nunito pour l'écriture au tableau, Inter pour les étiquettes imprimées, IBM Plex Mono pour les codes. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/permanent-marker` ou `@fontsource/patrick-hand` pour le feutre (accents français présents, vérifié le 11/11/2026).
- **Hauteurs** (2.5D) : tableau z 0 ; photos z 6 à 14 ; accessoires (étiquettes aimantées, aimants, règle d'acier, cartes, tampon) z 8 à 26 ; gouttière z 70, au plus près de l'objectif.
- **Photos** : détourées en pleine résolution, bords nets, un seul étalonnage (moins saturé, un peu plus chaud, noirs relevés), ombre = silhouette floutée le long d'**un seul vecteur de lumière**, plus douce quand l'objet est plus haut.

## 3. Composition 9:16
- **Concevoir d'abord le mur entier comme une affiche verticale** (par exemple 2400×4000 unités de tableau : hiérarchie, chemin de lecture de haut en bas, cadre rempli), puis prévoir chaque plan comme un recadrage de cette affiche. Garder une zone (couche secondaire, verdict, carton titre) pour le recul final seulement.
- Cadrage : décentré, rogné, proche. La première image contient un sujet lisible ; la première action forte arrive dans la première demi-seconde.
- Avant le recul final : au plus ~60 % de la largeur du tableau, jamais les deux bords à la fois, jamais la zone réservée.
- **Écriture au tableau** : 60 à 90 px à l'écran pour le contenu ; verdict 130 à 220 px. Dans le mur final, tout texte fait pour être lu fait ≥ 28 px à l'écran.
- **Cadre de jugement** : l'objet entier, la limite et le verdict dans le même cadre, tenu ≥ 2,5 s ; en vertical, empiler objet au-dessus, cote et limite au milieu, verdict dessous.
- **Sous-titres** : bande d'acrylique dépoli centrée, y 1400 à y 1540, avec un petit trait de feutre bleu ; le contenu clé reste au-dessus de y 1360. C'est le seul élément en espace écran.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : mur horizontal (4000×2400), sous-titres dans les 15 % du bas.

## 4. Ce qui bouge
- **Action principale** : la caméra qui **chevauche une ligne** (avec la pointe du feutre ou d'une cote) : une quantité est tracée comme une vraie longueur à une seule échelle et la caméra suit la pointe.
- **Boucles de fond** : (1) respiration de caméra à la main (≤ 3 px) ; (2) le reflet diagonal qui glisse sur l'émail et la parallaxe par hauteur.
- **Poids** : les photos descendent du côté caméra, se posent, rebondissent et se calment pendant que l'ombre se resserre ; les aimants claquent pour les fixer ; les étiquettes se balancent ; un aimant retiré saute vers l'objectif ; ce qui est frappé sursaute et revient.
- **Gestes** : lignes de projection (des tirets portent une arête d'une vue à l'autre) ; aimants comme unités comptables (ils claquent en rythme, sautent quand une règle les retire) ; effacer jusqu'au fantôme (l'idée rejetée reste faiblement visible) ; le tampon (verdict, coup sourd et sursaut) ; la réponse physique (un vrai accessoire posé comme solution) ; trait de rappel du nombre décisif vers la conclusion ; cadrage en escalier (chaque nouvel élément avec le résultat précédent).
- **Mouvements de caméra** : poussée lente avec légère inclinaison (tension) ; recul de côté (énoncer une règle) ; filé le long de la ligne avec dépassement (un résultat qui dépasse) ; montée le long d'un trait de rappel (de la preuve au verdict) ; long recul final.
- **Autorisés** : #004 tracé de ligne, #029 suivi, #016 parallaxe, #034 caméra à la main (légère), #043 filé avec la ligne, #122 suivi d'élan, #123 rebond (photos qui se posent), #036 cadrage incliné léger, #172 plan-séquence.
- **Interdits** : coupes, #044 fondus, zoom « ajusté au contenu », texte qui grossit en pop ou apparaît en fondu tout seul, amortis rebondissants d'interface, pages.

## 5. Rythme et montage
- 30 i/s (la source était à 24 i/s ; rien dans le style n'en dépend), rien n'est saccadé. Tous les 1 à 2 temps, quelque chose se pose, se trace ou se balance ; seuls les silences et les tenues de jugement sont immobiles.
- L'encre se trace à la vitesse d'une main ; les cotes se posent avec un petit coup de pointe de flèche.
- **Déroulé d'un élément** : détail → cadre de jugement → tenue → verdict (après que la caméra s'est posée) → on avance.
- Trois structures : une mesure qui grandit jusqu'à casser une limite ; un avant/après où le premier plan effacé reste en fantôme sous le second ; une liste tamponnée élément par élément en descendant le mur.
- Flou en mouvement, net là où on lit. Texte du tableau entièrement dans le cadre (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : une seule ligne chevauchée par la caméra et deux éléments posés au tableau.

## 6. Recette technique
- **Moteur** : HyperFrames en 2.5D CSS (un conteneur « mur » en `transform-style: preserve-3d`, chaque élément avec son `translateZ`, la caméra = transformation inverse du mur). **Blender** par le connecteur `blender` si l'on veut de vraies ombres portées et un vrai reflet d'émail (plan, images en plans détourés, une lumière de zone « fenêtre »).
```js
// description du mur : chaque élément a une position sur le tableau, une hauteur et une arrivée
{ type: "etiquette", texte: "Parking souterrain", xy: [560, 800], z: 12, arrive: {t: 0.2, genre: "balance"} },
{ type: "encre", genre: "cote", de: [700, 900], a: [1300, 900], couleur: "bleu", t: 0.6, d: 0.6 },
{ type: "tampon", texte: "RETENU", xy: [1500, 700], rot: -8, t: 4.2 }
// caméra : mouvements qui se chevauchent, vitesse ∝ u^a (1−u)^b, a et b entre 1,5 et 4 (b > a = inertie)
```
- **Tracé de l'encre** : chemins SVG révélés par `stroke-dashoffset`, écriture glyphe par glyphe avec `clip-path`.
- **Détourage** : voir la fiche `detourage-sujet`. Les parties fines (câbles, mâts, rambardes) sont mesurées dans la photo et **redessinées en traits propres** d'une seule couleur.
- **Aucune image n'agrandit une photo** : ≥ 1 pixel source par pixel écran à sa plus grande taille (mesuré) ; sinon limiter le zoom ou trouver une source plus grande.
- **Contrôles propres** : part du mur visible à chaque image (le mur ne doit pas être vu trop tôt) ; présence d'un cadre de jugement par élément testé ; résolution des photos.
- **Pièges** : texte aperçu en passant (mettre les mots là où la caméra se pose) ; seulement des gros plans (on ne voit jamais l'objet entier contre la limite) ; photos qui ne vont pas ensemble (un étalonnage, un vecteur de lumière, une famille de points de vue) ; lettrage dans les photos (enseignes, noms, logos : retoucher, couper ou changer de photo) ; mur final clairsemé ou minuscule.

## 7. Son
- **Pièce** : climatisation et circulation derrière la fenêtre, ~20 dB sous la voix ; les silences ne gardent que ça.
- **Bruitages** (budget du skill `son`, vrais enregistrements d'abord) : crissement de feutre proportionnel à la longueur du trait, claquement d'aimant (une hauteur par aimant d'une rangée), photo qui se pose (coup sur le tableau, claque de papier), feutre d'effaceur, coup sourd du tampon.
- Le son propre du sujet arrive en avance (J-cut) ; le premier son après un silence est un impact ou le son du sujet.
- **Musique** : petit ensemble rythmique, de la marche à l'allure vive (basse, batterie légère, percussions en bois, accents de cuivres graves pour les verdicts) ; pas de nappe piano-cordes. Poses, tampons et flèches sur le temps. Voix calme et sûre, 8 à 10 dB au-dessus ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Le mur complet a été dessiné comme une affiche avant le premier plan, et n'est vu en entier qu'au dernier recul.
- [ ] Trois couleurs d'encre aux sens respectés ; pas plus de trois marques rouges par image.
- [ ] Toutes les photos sont de vrais objets, de licence claire, listées dans `CREDITS` ; faute de photo libre, l'objet est **dessiné au feutre**, jamais généré.
- [ ] Aucune photo agrandie au-delà de ses pixels (contrôle par image).
- [ ] Chaque élément testé contre une limite a son cadre de jugement tenu ≥ 2,5 s.
- [ ] Aucune coupe ni fondu : uniquement des mouvements.
- [ ] Une seule direction d'ombre pour tout le mur.
- [ ] Texte lisible ≥ 28 px dans le mur final ; sous-titres hors zones d'interface ; `FAITS.md` à jour.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/briefing-board.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/briefing-board.jpg
- Crédit : « The Ship Decides », LemoLab, CC BY 4.0 ; photos de tiers sous CC BY 2.0 : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/briefing-board/STYLE.md`, `style.json`, `demo/kit/board.js`, `demo/kit/README.md`, `demo/tools/` (`camcheck.mjs`, `rescheck.mjs`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mur vertical pour le 9:16, HyperFrames 2.5D, Blender en option.
