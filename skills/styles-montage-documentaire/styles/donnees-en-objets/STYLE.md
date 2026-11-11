# Données en objets

## 1. Identité
- **Nom** : Données en objets. Identifiant : `donnees-en-objets`.
- **Inspiration** : la sculpture de données (une unité = un objet, l'objet est l'axe), la photo de produit et de nature morte (lumière principale chaude et basse, contre-jour froid, fond continu), la mise en page des rapports annuels (un relevé par écran, une ligne de source, une grotesque discrète). Grammaire seulement, aucun nom cité.
- **Principe** : de vraies statistiques construites en vrais objets. Chaque unité est une pièce de matière qu'on peut compter (plaque, bloc, pièce, barre), empilée **à l'échelle exacte** sur un socle soigné, et filmée comme un produit en studio. La caméra lit un nombre sur la tranche d'une plaque, suit la donnée qui grandit, puis recule jusqu'à ce que le graphique soit une installation.
- **Six règles** : l'unité est un objet, et la règle est dite une fois à l'écran (« 1 plaque = 10 GW ») ; une matière plus lourde marque chaque dixième unité, la pile est sa propre règle graduée ; l'échelle est exacte (arrondi d'une unité au plus, écrit dans les faits) ; lumière de studio et vraie matière (rien ne brille, rien n'est détouré, pas de fausse interface) ; la croissance est un assemblage (des pièces posées une à une, avec poids et son ; jamais une mise à l'échelle ni un morphing) ; au moins un recul qui révèle le graphique comme un objet fabriqué ; chaque nombre a sa source à l'écran.
- **Pour quels sujets** : comparer deux séries (renouvelable contre fossile, import contre export, deux chiffres d'affaires), les ventes d'un trimestre, des tonnes de CO₂, un budget, une population, douze mois en cadran.
- **Ne marche pas pour** : des données non comptables en unités (pourcentages flous, ressentis), plus de deux ou trois séries, des chiffres sans source. Ce n'est pas une infographie isométrique (ni icônes ni codes de couleurs plats), ni un graphique sur papier, ni une présentation sombre aux néons.

## 2. Palette, typographie, matières
- **Plateau chaud et neutre** : fond continu grège, socle en matière naturelle, séries en couleurs de matière. **C'est la matière, pas la peinture, qui sépare les séries** : métal brossé contre acrylique teinté, bois clair contre pierre sombre, pièces de cuivre contre papier. Une troisième matière (laiton) seulement pour les pièces « règle », commune à toutes les séries.
- Exemple de la démo : fond `#C4BEB4`, socle en noyer, aluminium `#C8CCD1`, acrylique `#9FD3D6` (teinte sarcelle), laiton `#D2B07A`, encre `#1C1D20`, accent `#D4521C`.
- **Un seul accent** (orange signal) pour le relevé ou le verdict qui compte sur cet écran. Encre presque noire à deux forces (valeur, puis libellés à ~60 %).
- Pas de palette arc-en-ciel, pas de dégradé de couleur sur les objets, pas de mode sombre.
- **Polices libres** : chiffres en grotesque légère (Inter 200 à 300) ; libellés et verdicts en sans ; unités, années et lignes de source en mono ; serif seulement pour le titre.
- **Police de repli** : aucune à prévoir, Inter est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/inter` (vérifié par `npm view` le 11/11/2026).
- **Pièces** : boîtes ou cylindres fins, par milliers, chacune avec un décalage aléatoire de quelques millimètres, une légère rotation, une variation de valeur de ±7 % et un interstice très fin : c'est ce qui fait lire une pile comme empilée, et non comme une barre.
- **Socle** : plaque de matière réelle avec marques incrustées (anneau de graduations, noms de catégories ou années gravés à l'échelle du socle), éclairée avec la scène.

## 3. Composition 9:16
- **Le vertical aime les piles** : cadrer une ou deux piles en trois quarts, leur sommet vers y 400, le socle vers y 1150. Une comparaison garde les deux sujets entièrement dans le cadre.
- Aux moments clés, le sujet occupe au moins un tiers de la hauteur.
- **Relevé** = un point sur l'objet, un trait de rappel de 1,4 px, un petit échantillon de la matière de la série, la ligne de catégorie, puis valeur et unité, sur une plaque papier translucide (~84 %). Relevé de pile 56 à 64 px ; relevé héros 150 à 180 px. Deux relevés d'une paire s'empilent dans une colonne, la plus grande valeur au-dessus. Ils vivent dans le fond vide, jamais sur la bande de sous-titres, jamais à droite de x 945.
- **Verdict** : dans le tiers haut-gauche (y 200 à y 420), sur sa propre plaque en couleur d'accent, souligné par un filet qui pousse ; il n'apparaît qu'après que les relevés qu'il juge sont restés immobiles ≥ 2,5 s.
- **Ligne de source** (jeu de données, éditeur, année, licence) : dans le cadre avec la donnée, 28 px, encre à ~60 %, en bas à gauche au-dessus de y 1540 mais à l'écart des sous-titres ; présente du premier relevé au résumé et sur le carton titre.
- **Sous-titres** : y 1400 à y 1530, filet d'encre de 2 px et plaque papier qui s'estompe à droite, alignés à gauche.
- Zones d'interface : haut 160, bas 360, droite 135.

## 4. Ce qui bouge
- **Action principale** : l'alimentation. L'augmentation d'une période arrive pièce par pièce depuis le hors-champ, sur le niveau de la période précédente : forte décélération, une rotation qui se déroule (« posée », pas « lâchée »), 8 à 16 pièces par seconde, **le compteur roule avec les pièces posées**.
- **Boucles de fond** : (1) la caméra ne s'arrête jamais (dérive de 2 à 5 % pendant les tenues) ; (2) bascule de mise au point lente entre l'avant et l'arrière des piles.
- **Gestes** : la cascade (une pile s'assemble de bas en haut en 0,5 à 1 s, chaque pièce tombant de quelques centimètres) ; le gros plan sur l'unité (pousser dans le flanc d'une pile jusqu'à ce qu'une pièce remplisse le cadre, puis encadrer une pièce « = 10 » et une pièce règle « = 100 ») ; la montée en paire (deux séries sur un socle, construites année par année pendant que la caméra suit ; le croisement est tenu immobile avec les deux relevés avant le verdict) ; du graphique à l'installation (reculer jusqu'à ce que les barres soient un cadran, une silhouette de ville, une pièce de table) ; **le dernier objet** (une seule pièce plus lourde tombe avec gravité, atterrit avec un seul petit rebond amorti, l'ombre se resserre : elle porte le nombre final gravé).
- **Mouvements de caméra** : travelling macro le long de la tranche d'une pile ; travelling latéral bas le long de la série (le temps qui passe) ; cadre trois quarts verrouillé sur deux sujets (comparaison) ; grue qui monte avec le sommet (accumulation) ; recul vers une vue presque à la verticale ; orbite lente autour du socle.
- **Autorisés** : #027 travelling avant macro, #033 bascule de mise au point, #029 travelling latéral, #031 grue, #030 orbite, #002 décalage en cascade, #007 compteur (lié aux pièces), #105 flou d'arrière-plan, #172 plan-séquence.
- **Interdits** : barre qui s'étire ou se met à l'échelle, #012 morphing, pièce qui bouge une fois posée, socle qui bouge, coupe vers un graphique plat, #045 volets, #140 pages, reflets d'objectif, aberration chromatique, relevés qui glissent pour sortir (ils s'effacent).

## 5. Rythme et montage
- 30 i/s (la source était à 24 i/s ; rien dans le style n'en dépend), animation à chaque image ; une seule prise continue dans un seul plateau quand c'est possible : les transitions sont des mouvements de caméra.
- Déroulé type : la règle « 1 pièce = X » en macro → la construction (cascade ou alimentation) → le cadre de comparaison tenu ≥ 2,5 s → le verdict → le recul → le dernier objet.
- Accélérer par subdivision de la musique (croches → doubles croches), pas par le tempo.
- Un creux de 0,3 à 0,6 s avant chaque impact dessiné (deux ou trois par film).
- Relevés : ils apparaissent en fondu avec une montée de 16 px et tracent leur trait ; libellé tenu (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : la règle « 1 pièce = X » (2 s), une seule alimentation (4 s), le cadre de comparaison tenu 2,5 s ; couper la seconde série.

## 6. Recette technique
- **Moteur** : **Blender** par le connecteur `blender` (recommandé : métal, acrylique en transmission, ombres longues, profondeur de champ). Pièces en instances, calendrier de pose calculé depuis les données, rendu en séquence d'images ; relevés, verdict, source et sous-titres ajoutés dans HyperFrames à partir des positions écran exportées. Three.js possible pour une version légère (maillages instanciés, matériaux physiques).
```python
# calendrier de pose : la donnée décide du nombre de pièces et de l'instant où chacune se pose
pieces = round(valeur / unite)                 # arrondi d'une unité au plus, noté dans FAITS.md
for i in range(pieces):
    t_pose = t_debut + i / cadence             # cadence : 8 à 16 pièces par seconde
    matiere = "laiton" if (i + 1) % 10 == 0 else serie.matiere    # la pièce règle
# compteur à l'écran = nombre de pièces posées à l'instant t × unite (jamais un compteur au temps)
```
- **Lumière** : environnement de studio faible pour les reflets seulement ; lumière principale chaude à 20-35° avec longues ombres douces ; un ou deux contre-jours froids pour détacher métal et acrylique du bois ; occlusion ambiante ; socle plus sombre que les pièces.
- **Relevé accroché** : même fonction monde → écran que la caméra ; le borner à une boîte sûre pour qu'il ne sorte pas du cadre avec un objet en mouvement.
- **Sources de statistiques** : Our World in Data (créditer aussi la source d'origine, CC BY 4.0), Banque mondiale, Eurostat (CC BY 4.0), instituts nationaux de statistique (vérifier les conditions de chaque jeu). Garder le fichier téléchargé et ses métadonnées dans `data/`. Chiffres du client : demander aussi le document d'où ils viennent ; ne jamais les arrondir « pour une meilleure histoire ».
- **Pièges** : deux matières trop proches se lisent comme une seule série (teinter l'une, vérifier en vignette) ; métal qui brunit de loin (contre-jour froid) ; moiré sur des pièces de 2 à 3 px (variation par pièce, suréchantillonnage) ; arrondi à la pièce qui inverse deux valeurs proches (le dire à l'écran ou choisir une unité plus fine) ; acrylique strié à angle rasant (rugosité ≥ 0,2).

## 7. Son
- **Le son propre de la matière est le bruitage** : les plaques de métal tintent clair et court, l'acrylique « toque » plus sourd, le bois cogne, les pièces sonnent. Une cascade est une rafale de ces sons aux instants de pose, atténuée quand la densité monte (c'est une texture, elle compte pour un seul événement dans le budget du skill `son`).
- **La règle chante** : chaque pièce règle (chaque dixième) fait sonner une note de maillet accordée, un timbre par série, en montant une gamme pentatonique avec le compte : le graphique devient un arpège.
- **Musique** : maillets et air (ostinato de marimba, vibraphone, harpe, verre, nappe douce) ; cors pour un retournement.
- **Impacts** : un retournement ou le dernier objet se pose sur un coup grave + grosse caisse + cloche ; ce sont les moments les plus forts.
- Voix calme et précise, ≈ 10 dB au-dessus de la musique ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La règle « 1 pièce = X » est écrite une fois à l'écran ; chaque dixième pièce est d'une autre matière.
- [ ] Le nombre de pièces de chaque pile correspond à la donnée (compte vérifié par script).
- [ ] Deux séries comparées utilisent la même unité et se distinguent en vignette de 200 px.
- [ ] La croissance se fait par pose de pièces ; aucune pièce ne bouge après s'être posée.
- [ ] Le compteur est lié au nombre de pièces posées.
- [ ] Ligne de source visible avec la donnée du premier relevé au résumé ; `FAITS.md` donne adresse, ligne citée et calculs dérivés.
- [ ] Un seul élément en couleur d'accent par écran ; verdict après 2,5 s d'immobilité des relevés.
- [ ] Au moins un recul « installation » ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/data-physical.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/data-physical.jpg
- Crédit : « Two Spirals », LemoLab, CC BY 4.0 ; données de tiers (CC BY 4.0) créditées dans le film : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/data-physical/STYLE.md`, `style.json`, `demo/set.js` (`buildSet()`, `landed()`), `demo/film.js` (`pairLabels`, `verdict`), `demo/mix.py`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, cadrage 9:16, Blender en moteur principal (la démo d'origine est en Three.js), assemblage HyperFrames.
