# Décor peint : trois passes, matières procédurales, fusion par matière

Pour un décor **peint** dont la lumière se règle par ambiance (style `tete-ronde-trait-plein-delie` de la catégorie `styles-2-5d`). Ces règles viennent d'un essai réel du studio du 12/11/2026 : un intérieur et un extérieur, 3 656 objets, 258 images en 1080 × 1920 sur une carte graphique intégrée, Blender 5.3 (EEVEE). La bibliothèque qui les applique est `bl_decor.py`, dans le kit de cette catégorie (`skills/styles-2-5d/kit/LISEZMOI.md`).

Unité : **D = diamètre de la tête d'un personnage** dans la scène (0,52 m dans l'essai). Toutes les tailles de texture se donnent en D.

## 1. Séparer la couleur et la lumière : trois passes par image

Ne cuis pas la lumière dans le rendu. Rends trois images par image de film et compose ensuite.

| Passe | Contenu | Format |
|---|---|---|
| Couleur | la couleur peinte de chaque surface, sans aucune lumière | 8 bits, vue « Standard » |
| Lumière | rouge = part de soleil reçue (ombres portées comprises) ; vert = lumière des lampes ; bleu = occlusion | 16 bits, vue « Raw » |
| Données | rouge et vert = normale dans le repère de la caméra ; bleu = profondeur divisée par une profondeur maximale | 16 bits, vue « Raw » |

Comment : chaque matière se termine par trois émissions (couleur, lumière, données) et un aiguillage commandé par **une seule valeur partagée** (un groupe de nœuds qui ne contient qu'un nœud « Valeur »). La boucle de rendu passe cette valeur à 0, 1, 2 et rend trois fois.

Pourquoi : l'ambiance (couleur et force des ombres, teinte de la lumière, pénombre, brume, ciel, contours, flou de profondeur) se règle alors **en quelques secondes à l'assemblage**, au lieu de relancer 40 minutes de rendu. Dans l'essai, quatre tours de correction chiffrée et un tour de critique n'ont demandé aucun rendu Blender.

Ce que la composition fait de ces passes (ombres en mélange vers une teinte, contours tirés des ruptures de profondeur et de normale, ciel peint, flou selon la profondeur) est décrit dans le prompt maître de la catégorie : `skills/styles-2-5d/references/prompt-maitre.md`.

## 2. Calculer la part de soleil dans la matière

La part de soleil reçue se calcule **dans la matière**, avec la vraie normale : la lumière diffuse reçue (nœud diffus, puis « Shader vers RVB »), divisée par le produit de la normale et de la direction du soleil, bornée entre 0 et 1.

- Une face tournée vers le soleil sort alors en aplat, et la pénombre des ombres portées reste douce.
- **Ne reconstruis jamais cette part après coup** à partir de la normale de la passe de données : le signe se perd dès que la caméra lève le nez.
- La direction du soleil est inscrite dans les matières : si elle change d'un plan à l'autre, reconstruis les matières ou passe-la par une valeur partagée.

Réglage des lumières pour ces passes : le soleil en rouge pur, les lampes en vert pur, fond du monde noir. **Seul le soleil porte des ombres** (les lampes non) : en intérieur, le style n'a pas d'ombre nette, et le rendu est trois fois plus rapide. Diamètre apparent du soleil : 3°, pour une pénombre de 0,05 fois la distance à l'objet.

## 3. Textures peintes procédurales, en D

Aucune image téléchargée : des nœuds. Les briques utiles, avec leurs réglages mesurés :

| Brique | Réglage | Remarque |
|---|---|---|
| Planches et lames à joints | un joint tous les **0,32 D**, épais de **0,02 D**, dans une version sombre et violacée de la teinte ; une teinte tirée au hasard par planche | viser un contraste de 12 à 18 niveaux sur l'image finale |
| Fil du bois | traînées longues et fines dans le sens du plus grand côté de l'objet | un bruit étiré ne suffit pas sur une grande surface : il se lit comme un rideau de fils ; dessiner des veines et des nœuds |
| Taches douces | bruit large à bord adouci, deux échelles | enduits, sable, tissus : 3 à 8 niveaux |
| Tuiles, pierre appareillée | deux familles de bandes croisées | |
| Patine | taches rares d'une teinte opposée | métal |
| Matières qui brillent | émission pure, marquée dans la passe de lumière (rouge à 1) | flammes, lampes, fenêtres éclairées : elles reçoivent un halo à l'assemblage |

Coordonnées : « monde » pour les motifs qui doivent se suivre d'un objet à l'autre (plancher, murs), « objet » pour ce qui bouge. Une matière à fil se décline en trois variantes (une par axe) ; chaque objet prend celle de son plus grand côté.

## 4. Réunir les objets fixes par matière

Avant le rendu, réunis en un seul maillage tous les objets fixes qui partagent une matière (et le même réglage d'ombre). Laisse à part ce qui est animé, parenté ou porteur d'un modificateur.

Mesuré : **3 656 objets réunis en 535 ; le rendu est passé de 30 s à 9 s par image** pour les trois passes (avec les ombres portées réservées au soleil).

## 5. Petits détails posés au sol

Cailloux, touffes, petits débris : 5 à 11 par D² autour du sujet, diamètre médian de 0,03 D.

- **Éclairés comme le sol qui les porte** : normale forcée vers le haut dans la passe de lumière.
- **Marqués** dans la passe de lumière (bleu à 0) pour échapper à l'occlusion et aux contours de l'assemblage.
- **Liseré peint dans la matière** (sur le pourtour, d'après l'angle de vue), puisqu'ils n'ont pas de contour à l'assemblage.
- Pas d'ombre portée.

## 6. Une seule boucle de rendu, avec reprise et arrêt propre

- Une image dont les trois passes existent est sautée : après un plantage du pilote, on relance la même commande.
- **Un seul Blender rend à la fois.**
- **Note le numéro du processus qui rend et arrête-le par ce numéro.** Arrêter la tâche qui a lancé la boucle ne suffit pas : dans l'essai, une boucle crue arrêtée a tourné une minute en parallèle d'une autre, et ses images ont dû être écartées.
- Ferme la scène par une grande sphère de fond, pour que chaque pixel ait une profondeur (au-delà de la profondeur maximale = ciel).
- Une matière non compilée sort en magenta : fais-le vérifier par l'assemblage et re-rends l'image.
- Le reste (profilage, réglages par carte, boucle fantôme) : `rendu-long-et-fiable.md`.

## 7. Temps mesurés

| Étape | Temps |
|---|---|
| Construction de la scène | 16 s |
| Trois passes, par image, 1080 × 1920 | 9,2 s (couleur 5 s, lumière 3 à 4 s, données 1 à 2 s) |
| 258 images | 39 min 40 s |

## 8. Ce qui n'est pas au niveau

- Le fil du bois en bruit étiré (contraste de 10,9 niveaux contre 20,8 visés).
- Les ombres longues ne s'adoucissent pas assez avec la distance (−48 % en plan large) : régler la pénombre du soleil ou adoucir d'après la distance à l'objet.
- Les contours tirés de la profondeur sont légèrement tremblés, et les arêtes intérieures trop discrètes.
- Plein jour et nuit : non essayés.
