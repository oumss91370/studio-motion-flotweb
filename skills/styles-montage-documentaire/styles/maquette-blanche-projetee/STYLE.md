# Maquette blanche projetée

## 1. Identité
- **Nom** : Maquette blanche projetée. Identifiant : `maquette-blanche-projetee`.
- **Inspiration** : les maquettes d'urbanisme éclairées par projection dans les galeries de ville (la salle sombre, le faisceau doux, la couleur seulement sur des surfaces blanches), la photo macro de maquette (peu de profondeur de champ à hauteur de toit), les graphiques éditoriaux (un chiffre, un libellé, une source par couche). Grammaire seulement, aucun nom cité.
- **Principe** : une maquette de volumes **blanc pur** d'un vrai lieu, posée sur un socle dans une salle sombre ; un projecteur y peint les données **en lumière**, une couche à la fois : la lumière tombe sur les surfaces qui lui font face, s'estompe sur les murs détournés, s'arrête au bord du faisceau et déborde un peu sur le socle. **La maquette ne change jamais ; seule la lumière change.**
- **Cinq règles** : la maquette est la vraie géométrie d'un vrai lieu (emprises et hauteurs issues de données ouvertes, à une échelle annoncée) ; blanc = matière, donnée = lumière (la couleur n'est jamais peinte dans le matériau) ; les couches arrivent une à une, chacune répond à la question laissée par la précédente ; une salle physique (lumières de salle, projecteur qui s'allume, socle) ; chaque nombre à l'écran est calculé à partir des mêmes bâtiments que ceux de la table.
- **Pour quels sujets** : croissance d'un quartier par décennie, hauteurs d'une ville, ombre d'une tour sur un parc, zone inondable, ce que possède un acteur, bâtiment classé, parcelle à vendre, plan d'évacuation.
- **Ne marche pas pour** : un lieu sans données de bâtiments ouvertes, un objet (voir `vue-eclatee`), un sujet sans géographie. Ce n'est pas une infographie isométrique (ni diorama ni icônes), ni un hologramme (la lumière se pose sur de la matière), ni un nuage de points (pas de lignes de balayage).

## 2. Palette, typographie, matières
- **Maquette** : blanc mat `#F3F3F1`, rugosité ≈ 0,9, arêtes nettes ; l'eau est une incrustation satinée plus sombre dans la plaque ; ponts en dalles blanches basses ; plaque mince sur un socle satiné sombre ; salle presque noire.
- **Une famille de teintes par couche**, choisie pour la donnée : un accent unique pour « l'ancien / l'exception » (ambre chaud) ; un dégradé séquentiel pour une donnée continue (bleu → cyan → blanc pour le temps ; violet → magenta → pêche pour la hauteur). Une couleur ne revient qu'avec le même sens. Jamais plus de deux palettes de couches à l'écran.
- **Le soleil est chaud, son ombre est un bleu profond projeté** ; les couleurs de données sont rangées quand le soleil arrive. Jamais de couleur sur la maquette sous la lumière de salle.
- **Polices libres** : chiffre en grotesque très légère (Inter Tight 200) ; libellés en sans ; instruments, années et coordonnées en IBM Plex Mono.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Finition** : vraie profondeur de champ (plus forte en gros plan), halo seulement au-dessus des hautes lumières de projection, vignette, grain léger à l'encodage. Environnement de studio **neutre** (un environnement chaud rend la maquette beige).

## 3. Composition 9:16
- **La table en hauteur** : cadrer en plongée oblique, le grand axe du quartier dans le sens vertical ; aux moments clés, le sujet occupe un tiers de la hauteur, entre y 450 et y 1150.
- **Relevé** (un par couche) : en bas à gauche de la zone utile (x 70, y 1150 à y 1400) : indice + nom de la couche (30 px), un chiffre (130 à 150 px), un libellé (34 px), une ligne de source (28 px), une barre de légende.
- **Épingles** : un trait fin qui monte d'un toit vers une étiquette sur plaque sombre (titre 34 px + une ligne 28 px) ; ancrées sur la partie la plus haute du bâtiment ; jamais sur le relevé, jamais à droite de x 945.
- **Étiquette d'identité**, discrète, en haut à gauche sous y 170 : lieu, échelle, sources des données.
- **Sous-titres** : centrés, y 1420 à y 1540, sur un dégradé sombre doux, sans boîte.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : relevé dans le tiers gauche, sous-titres en bas au centre.

## 4. Ce qui bouge
- **Action principale** : **la lumière est l'acteur.** Chaque couche arrive par un geste de lumière à bord doux : une nappe qui s'étend depuis l'axe du projecteur, des bâtiments qui s'allument un à un avec un bref éclair, un niveau qui grimpe sur toutes les façades, l'horloge du soleil qui tourne. Jamais une ligne dure qui balaie la table (elle se lit comme un scanner laser).
- **Boucles de fond** : (1) la caméra bouge en continu et lentement, change de vitesse avec les couches, ne s'arrête jamais net ; (2) léger souffle du faisceau (poussières discrètes) et compteur qui roule pendant que la lumière avance.
- **Gestes** : lumières éteintes, lampe allumée (relais, noir, la lampe s'amorce avec un bref scintillement, la première couche arrive) ; **le trou** (n'éclairer que l'ensemble qui répond à la question, et laisser l'absence dessiner la forme) ; couches par époque (les bâtiments s'allument dans la décennie de leur construction, chaque couche plus vite que la précédente) ; **le niveau qui monte** (les bâtiments bas finissent en premier, le plus haut en dernier, le relevé monte avec) ; **l'horloge du soleil** (un vrai soleil à une vraie date balaie les ombres, puis le projecteur trace une ombre et la mesure) ; la mise en évidence d'un seul bâtiment ; lumières rallumées (la donnée s'arrête, l'objet reste).
- **Mouvements de caméra** : glissé macro à hauteur de toit avec faible profondeur de champ ; grue en arrière et vers le haut ; orbite lente avec montée ; descente à angle bas contre le noir (hauteur, silhouette) ; travelling de côté le long d'une ligne mesurée ; recul quand la salle se rallume.
- **Autorisés** : #030 orbite, #031 grue, #033 bascule de mise au point, #029 travelling, #177 contre-plongée, #105 flou d'arrière-plan, #172 plan-séquence, #007 compteur, #004 ligne mesurée qui pousse de A à B avec graduations.
- **Interdits** : coupes, #044 fondus et #045 volets (les transitions sont des changements de lumière dans une seule prise), maquette ou socle qui bougent, ombre truquée, ligne de balayage fine.

## 5. Rythme et montage
- **Une seule prise**, rythmée par les changements de lumière : salle allumée → noir → couche 1 → couche 2 (qui répond à la question de la 1) → soleil → salle rallumée.
- Lumières de salle coupées vite (relais, 0,25 s), rallumées lentement (1 s).
- Les compteurs roulent pendant que la lumière avance et se posent quand elle se pose.
- Silence : le projecteur s'éteint, tout s'arrête sauf un mince ronron de ventilateur, avant le retournement.
- Sous-titre ≥ max(1,8 s ; parole + 0,6 s) ; libellé (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : deux couches de lumière de 4 s et un seul relevé ; couper l'extinction et le rallumage de la salle.

## 6. Recette technique
- **Moteur** : **Blender** par le connecteur `blender` (recommandé : c'est un film de lumière, de matière et de profondeur de champ). Emprises extrudées à leur hauteur, matériau blanc mat unique, une lumière de zone « salle », un projecteur dont la couleur dépend d'attributs par bâtiment, un soleil directionnel. Rendu en séquence d'images, puis assemblage, relevés, épingles et sous-titres dans HyperFrames. Three.js possible pour une version légère (matériau standard + terme de projection ajouté dans le shader).
- **Une couche est un état, pas une image** : les attributs de chaque bâtiment (année, hauteur, rang, drapeaux) vivent dans les données des sommets ; le matériau décide à chaque image quelle couleur le projecteur leur donne.
```glsl
// terme de projection ajouté à la surface éclairée : jamais une texture collée sur le maillage
couleur += teinteCouche * (0.42 + 0.58 * max(dot(N, versProjecteur), 0.0)) * masqueFaisceau * albedo;
```
- **Soleil réel** : direction calculée depuis la latitude du lieu, une vraie date et une vraie heure ; ombres portées réelles. Le projecteur peut retracer ce que fait le soleil (l'emprise d'une ombre), jamais truquer une ombre.
- **Relevés et épingles** : exporter de Blender la position écran des points d'ancrage image par image (ou la caméra) pour que la couche 2D reste accrochée à la maquette.
- **Données de bâtiments** : chercher d'abord les données 3D ou emprises-avec-hauteurs ouvertes du lieu (portails de données ouvertes des villes, référentiels nationaux du bâti). Licences acceptées : CC0, domaine public, CC BY (crédit dans `CREDITS` et à l'écran). OpenStreetMap et jeux sous licence de partage à l'identique : dire les conditions au client et demander avant. Pour son propre site, demander au client son plan ou sa maquette numérique.
- **Les couches dépendent de ce qui existe** : l'année de construction par bâtiment est rare. Sinon, projeter ce que la donnée contient : hauteurs, nombre d'étages, surface d'emprise, zonage, périmètre, **soleil et ombre (toujours calculables)**. Ne jamais inventer une couche d'années.
- **Pièges** : normales de murs à l'envers (murs « creux ») ; murs mitoyens qui scintillent ; occlusion ambiante en vue large rasante (bandes sombres : la garder pour les gros plans) ; soleil bas qui éclaire les façades, pas les toits (filmer du côté éclairé) ; ombres étroites perdues parmi les autres (tracer celle qui compte) ; nombres de sources mêlées (dire lequel : « toit », « mesuré »).

## 7. Son
- **La salle** : bruit de pièce, ventilateur du projecteur qui monte quand la lampe s'amorce, relais des lumières, amorçage de lampe, souffle d'une nappe de lumière.
- **La lumière en son** : maillets et verre pour ce qui s'allume, vibraphone frotté pour une lumière tenue, ligne de maillets montante pour un niveau qui grimpe, une note de verre par bâtiment mis en évidence.
- **Poids** : timbales, gong, cuivres graves pour un fait lourd. Pas de mélodie piano-cordes générique.
- Budget de bruitages du skill `son` (les notes de verre comptent comme musique). Voix calme, ≈ 10 dB au-dessus ; les deux impacts dessinés sont les moments les plus forts ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La maquette vient de données réelles et ouvertes ; échelle et sources affichées ; rien d'inventé ni de « représentatif ».
- [ ] La couleur n'apparaît que comme lumière projetée : elle faiblit sur les faces détournées et déborde un peu sur le socle.
- [ ] Une couche à la fois ; au plus deux palettes à l'écran ; une couleur garde son sens.
- [ ] Aucune coupe : une seule prise, transitions par la lumière.
- [ ] Ombres du soleil calculées pour une date et une heure réelles, écrites à l'écran.
- [ ] Chaque nombre est calculé par un script à partir des mêmes bâtiments (`FAITS.md` + méthode).
- [ ] La maquette reste blanche (pas de dérive beige) sous la lumière de salle.
- [ ] Épingles ancrées au point haut ; rien sous 28 px ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/white-model.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/white-model.jpg
- Crédit : « How a Flattened City Grew Back », LemoLab, CC BY 4.0 ; données de bâtiments de tiers (CC BY 4.0) : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/white-model/STYLE.md`, `style.json`, `demo/studio.js` (`makeStudio()`, `projMaterial()`, `buildCity`), `demo/overlay.js`, `demo/tools/` (`prep.py`, `sun.py`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mise en page 9:16, Blender en moteur principal (la démo d'origine est en Three.js), assemblage HyperFrames.
