# Produit en verre

## 1. Identité

- **Nom** : Produit en verre.
- **Inspiration** : les films de lancement haut de gamme (un balayage de lumière qui dessine un contour dans le noir, orbites lentes, bascule de point en macro, coupes sur le temps, typographie très fine et très large), les publicités de matériel transparent (l'intérieur comme ornement, vues éclatées, noir et blanc plus un accent), et la photographie du verre sur fond noir. On n'en copie ni les silhouettes, ni les polices, ni les sons, ni les gabarits de couleur, et on ne les nomme pas.
- **Ce que c'est** : **un seul objet héros en verre, métal et lumière**, qui flotte dans un studio noir infini. De longues bandes lumineuses **derrière et à côté** de lui changent le verre clair en un fin contour blanc aux arêtes irisées ; l'intérieur se voit comme dans une vitrine. Tout bouge lentement et précisément ; chaque coupe, balayage et pulsation tombe sur le temps.
- **L'objet est toujours fictif ou celui du client.** Jamais la silhouette d'un produit réel d'une autre marque (le contour d'un téléphone ou d'un casque célèbres), ni un nom, un logo, une police ou une interface de marque tierce.
- **Marche pour** : lancement d'un produit physique, « ce qu'il y a dedans », rendre visible ce que le produit fait d'invisible (charge, données, chaleur, son), un ingrédient, une vue éclatée, une promesse en un chiffre.
- **Ne marche pas pour** : service sans objet, ton chaleureux ou familier, tutoriel, humour, petit budget de temps (rendu lourd).
- Ce n'est ni un packshot sur fond blanc, ni un affichage filaire, ni une diapositive : matière et lumière sont le sujet.

## 2. Palette, typographie, matières

- **Le monde est neutre** : noir, gris, le blanc des reflets de bandes, la teinte propre des métaux.
- **Une seule famille de couleur d'accent, réservée à la lumière** (émission, anneaux de caustique, filet sur les titres), qui peut glisser entre deux teintes voisines. Choisis-la d'après **ce que fait le produit**. La démo d'origine va du bleu glacier `#62DCFF` au violet doux `#A98BFF` : c'est précisément la zone que la porte de livraison surveille. **Préfère ambre → rose, ou vert → cyan** ; garde bleu → violet seulement si la marque du client l'impose, et mesure.

| Rôle | Valeur |
|---|---|
| Fond | dégradé radial `#34383D` → `#16181B` → `#000000` (sépare les arêtes du verre) |
| Verre clair | transmission 1, rugosité ≈ 0,015, indice ≈ 1,52, dispersion activée, teinte d'atténuation `#F3F8FB` |
| Verre dépoli | transmission ≈ 0,85, rugosité ≈ 0,4, teinte laiteuse `#EEF2F5`, épais |
| Guide de lumière | acrylique poli sombre `#15181B`, vernis |
| Métaux | bandeau satiné (rugosité 0,16), chrome (rugosité ≥ 0,14), acier brossé, circuit graphite à pistes dorées |

- Les émetteurs qui ne font qu'éclairer (dans le verre dépoli) restent blanc froid et faibles.
- Les arcs-en-ciel de dispersion ne sont permis **qu'aux arêtes épaisses du verre et dans la caustique**, jamais en dégradé sur une surface ou un texte.
- **Typographie** : une grotesque libre (**Inter Tight**, OFL). Titres en graisse ultra-fine (200), très grands, interlettrage très large ; un éclat diagonal balaie les lettres en même temps que le balayage sur l'objet. Petites capitales espacées pour les mentions.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Sous-titres = une plaque de verre dépoli** : barre arrondie centrée remplie de l'image vivante floutée, un peu de blanc froid, fin filet clair et ligne d'accent au-dessus.
- **Sol** : noir brillant, miroir flouté, fondu radial, caustiques (anneau de lentille aux rayons rouge, vert et bleu décalés ; anneaux qui se propagent depuis un évènement). **Aucune ligne d'horizon.**

## 3. Composition 9:16

- **Un héros, centré ou sur une forte diagonale**, jamais coupé par le bord dans un plan large. En vertical : objet au centre (y 600 à 1300), dressé ou incliné pour épouser la hauteur ; le sol-miroir et sa caustique en dessous (y 1300 à 1560).
- **Vue éclatée le long de l'axe vertical** : le format 9:16 lui convient parfaitement (pièces étalées sur ≈ 2 fois la taille du produit) ; axe à ≈ 40° du regard, jamais perpendiculaire (on ne verrait que des traits).
- **Titres** : 96 à 120 px, graisse 200, interlettrage large, centrés dans le tiers haut (y 240 à 520), sur l'espace noir laissé par un recul lent. Nom du produit et slogan sont des **cartons de titre**, pas des lignes de sous-titre.
- **Sous-titres** : 40 à 44 px, presque blanc, plaque de verre vers y 1440 à 1520.
- Les films de produit n'ont **pas besoin de continuité d'espace** : chaque plan est sa propre scène de présentation ; cache ce qui ne le sert pas.

## 4. Ce qui bouge

- **Action principale** : la **vue éclatée** : les pièces s'écartent le long de l'axe (longue décélération), flottent un instant, puis **se referment d'un claquement très bref sur un premier temps**.
- **Boucle de fond 1** : **la caméra dérive toujours** : orbite lente ou avancée ; jamais de cadre figé, jamais d'épaule (sauf 2 images de micro-secousse sur un impact).
- **Boucle de fond 2** : pulsations de lumière « en comète » qui courent dans les guides (tête vive, traîne qui s'éteint), et leur anneau de caustique au sol.
- **Autorisés** : `#022` balayage de lumière, `#030` orbite lente, `#027` avancée lente, `#033` bascule de point de la surface vers la pièce intérieure, `#143` vue éclatée, `#184` macro, `#181` vue du dessus, `#177` contre-plongée sous l'objet, `#125` pulsation, `#046` coupe sur le temps, `#105` flou d'arrière-plan.
- **Interdits** : `#044` fondu enchaîné, `#045` volet, `#034` caméra à l'épaule, `#175` plan totalement fixe, `#011` écrasement et étirement, `#001` rebonds joueurs, reflet peint en 2D (la lumière est une vraie géométrie), dégradé arc-en-ciel sur une surface, grain.
- Chaque pièce garde une petite inclinaison et une rotation proportionnelle à son écart. Les couvercles pivotent à l'arrière et se dressent derrière l'objet comme un halo à contre-jour.
- Pulsations et balayages sont des **évènements de la grille musicale**, pas une animation libre.

## 5. Rythme et montage

- **Écris d'abord la carte des repères musicaux** ; une seule liste d'impacts partagée entre la musique et le rendu.
- Coupes seulement sur les temps (barres de mesure si possible). Transitions : coupe, ou un balayage qui passe par le noir.
- Plans de 2 à 5 s. Durée conseillée : 15 à 35 s.
- **Silence comme outil** : un court silence total (queues de réverbération coupées) avant une libération.
- Adapter n'importe quel sujet : trouve **la chose invisible que fait le produit** et rends-la visible comme une lumière dans le verre.
- Geste possible au sommet : **du dépoli au clair** (rugosité et teinte s'animent vers zéro, l'intérieur apparaît).
- **Version courte (8 à 12 s)** : deux plans : l'objet en dérive (3 s), puis la vue éclatée qui s'ouvre et se referme d'un claquement (5 s), titre tenu 2 s ; couper le plan de détail.

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`, rendu Cycles) : c'est le style où le lancer de rayons change le plus le résultat. **Three.js** fonctionne (moteur d'origine) pour une version légère.

| | Blender / Cycles (conseillé) | Three.js (léger) |
|---|---|---|
| Verre | réfraction, épaisseur et reflets internes exacts ; dispersion par nœuds (trois indices légèrement différents) | `MeshPhysicalMaterial` : transmission, indice, épaisseur, dispersion ; **tout ce qui est dans le verre doit être opaque** |
| Studio | plans émissifs (bandes) modélisés autour de l'objet : ils se reflètent d'eux-mêmes | petite scène noire de plans émissifs **recuite en carte d'environnement à chaque image** |
| Caustiques | vraies (coûteuses) ou imitées par une texture animée au sol | toujours imitées : anneau et filaments procéduraux |
| Sol | miroir flouté réel | réflecteur + flou à écrire |
| Bruit d'image | à débruiter ; verre = beaucoup d'échantillons | aucun ; rendu 2× |
| Durée | long (minutes par image possibles) : valide sur images fixes | rapide |

- **Le studio est une scène de bandes lumineuses, pas un ciel photographié** : un ciel de studio photo contient des fenêtres et du désordre qui s'impriment en traînées sales sur le verre. Bandes hautes de côté derrière l'objet (silhouette), bande large au fond (liseré d'horizon), boîte douce au-dessus (volume du dépoli et du métal), carte faible de face, et **le balayage** : une bande haute qui se déplace sur un arc. Comme c'est de la vraie géométrie, son reflet, sa réfraction et sa dispersion bougent physiquement.
- **Techniques clés** :
  ```python
  # Blender : verre clair (Principled) et bande de balayage animée
  bsdf.inputs["Transmission Weight"].default_value = 1.0
  bsdf.inputs["Roughness"].default_value = 0.015
  bsdf.inputs["IOR"].default_value = 1.52
  bande.rotation_euler.z = angle_balayage(t)       # plan émissif sur un arc, clé par temps musical
  ```
  - **Verre dépoli sur fond noir = plastique gris sombre**, sauf s'il y a **quelque chose de lumineux derrière ou dedans** (une forme émissive opaque, floutée en lueur interne).
  - Modélise en millimètres. Faible profondeur de champ en macro, grande pour les vues éclatées. Lueur seulement sur les très hautes lumières. Courbe de tons **neutre** (certaines courbes filmiques blanchissent les accents).
- **Pièges** : émetteur coloré dans le dépoli qui teinte tout l'objet ; chrome miroir qui devient un disque blanc (rugosité ≥ 0,14) ; profils purs lus comme des formes simples (champignon, couvercle) : préfère les trois quarts ; verre concave face caméra qui imprime la carte de face en rectangle gris (éteins-la) ; pics de basse sans marge qui dérèglent la normalisation du volume.

## 7. Son

- **Électronique minimale, jamais piano-cordes.** Timbres possibles : verre frotté, nuages de cristal granulaires, cloches de verre, grille de tics filtrés pour la précision, nappe chaude, bourdon grave, kicks courts et doux, basse profonde à glissements, montées de bruit, « ding » de verre aigu. Couleurs mineures et modales.
- **Chaque pulsation, balayage et claquement est verrouillé sur la musique.**
- **Bruitages selon la matière** (≈ 5 par 10 s ; vrais enregistrements de verre et de métal quand ils existent) : scintillement de verre pour un balayage (placé en stéréo avec la bande), frottement verre-métal, clic magnétique, souffle d'air d'une pièce qui bouge, claquement de fermeture = grappe de clics + accord de verre, tintement verre contre verre.
- **Voix** : retenue, grave, très peu de phrases très courtes. Jamais un nom de produit seul : donne-lui un verbe.
- Musique baissée d'environ 12 dB sous la voix ; −14 LUFS ; aucun grain.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Fond noir sans ligne d'horizon ; un seul objet héros, jamais coupé en plan large.
- [ ] Le verre clair se lit par ses arêtes lumineuses (bandes derrière et sur les côtés).
- [ ] Le verre dépoli a une source lumineuse derrière ou dedans.
- [ ] Une seule famille d'accent, portée uniquement par de la lumière ; part de bleu-violet mesurée.
- [ ] La caméra dérive dans chaque plan ; aucune coupe hors temps.
- [ ] Au moins un balayage de lumière physique et une vue éclatée qui se referme sur un premier temps.
- [ ] Aucun arc-en-ciel hors des arêtes épaisses et de la caustique ; aucun grain.
- [ ] Aucune silhouette, marque, police ou interface d'un produit tiers.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 40

## 9. Aperçu

- Film de démo d'origine *Aura — Hear the Light* (32 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/glass-product.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/glass-product.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/glass-product/STYLE.md`, `DEMO.md`, `demo/studio.js`, `product.js`, `main.js`, `story.js` (moteur d'origine : three.js). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Police Inter Tight (SIL OFL 1.1).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, composition 9:16, voie Blender / Cycles et tableau comparatif (non testés par un rendu), mise en garde sur l'accent bleu-violet, numéros du dictionnaire.
