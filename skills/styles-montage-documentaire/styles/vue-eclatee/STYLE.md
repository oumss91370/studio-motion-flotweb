# Vue éclatée (démontage d'un produit)

## 1. Identité
- **Nom** : Vue éclatée. Identifiant : `vue-eclatee`.
- **Inspiration** : les films de lancement de matériel en vue éclatée (décalage des couches, rythme de l'orbite), les démontages des guides de réparation (ordre d'ouverture, macro sur la pièce qui compte), le dessin technique (traits de rappel, cotes). Grammaire seulement : aucun produit, mise en page, police ou musique repris, aucun nom cité.
- **Principe** : un vrai produit, construit à partir de **ses propres fichiers d'ingénierie** (CAO, circuit imprimé, nomenclature), éclairé comme une photo de studio et démonté devant la caméra : les couches se soulèvent sur un seul axe, la caméra voyage entre elles, chaque pièce est nommée avec les nombres que ses fichiers contiennent, puis l'objet se referme.
- **Cinq règles** : l'objet est réel et exact (géométrie, positions et comptes viennent des fichiers ; rien n'est estimé à l'œil si un fichier peut le donner) ; il est montré séparé (couches sur un axe, écarts réguliers et lisibles, chacune orientée comme dans le produit) ; il est photographié, pas dessiné ; les nombres vivent sur l'objet (traits fins depuis un point sur la pièce, cotes en perspective, jamais un tableau à côté) ; la caméra ne s'arrête jamais de voyager.
- **Pour quels sujets** : présenter un produit matériel du client (objet, appareil, meuble modulaire, emballage), expliquer « ce qu'il y a dedans », un comparatif d'épaisseur, une réparation.
- **Ne marche pas pour** : un produit dont on n'a ni fichiers ni dimensions publiées, un logiciel, un service. Ce n'est pas un rendu « beau verre » (un objet, pas de démontage), ni un plan sur grille, ni une notice de montage (numéros d'étapes, flèches, mains).

## 2. Palette, typographie, matières
- **Le produit apporte ses couleurs** ; le cadre autour est neutre et sombre, pour que le produit soit toujours l'élément le plus clair et le plus saturé. Fond : dégradé radial graphite `#34363a` → `#0d0e10` ; le sol n'est visible que par une ombre de contact douce.
- **Encre d'interface** : un blanc chaud `#f1efe9` à deux forces (noms pleins, caractéristiques à ~60 %) + **un accent** `#ff6b3d` réservé aux choses mesurées : cotes, indices des étiquettes, et un détail assorti sur le produit lui-même.
- **Ordre des valeurs** : fond le plus sombre, produit de moyen à clair, étiquettes les plus claires. Jamais de texte sur une pièce claire et chargée sans fond sombre.
- **Polices libres** : noms en sans de graisse moyenne ; caractéristiques et nombres en mono (JetBrains Mono) pour que les chiffres s'alignent et se lisent comme une mesure.
- **Police de repli** : aucune à prévoir, JetBrains Mono est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/jetbrains-mono` (vérifié par `npm view` le 11/11/2026).
- **Matières** : chaque matériau garde son caractère : plastiques au reflet doux (rugosité 0,55 à 0,7), cartes électroniques avec vernis mince et pistes en léger relief, pastilles métalliques, reflets serrés sur le métal usiné, caoutchouc mat. Les plastiques noirs sont relevés en gris foncé pour ne pas disparaître.
- **Lumière** : principale chaude d'en haut et de face ; contre-jour froid rectangulaire derrière, **qui suit la caméra** pour détacher les arêtes ; lumière douce du dessus ; environnement faible pour les reflets ; un appoint seulement là où la caméra entre dans l'objet.

## 3. Composition 9:16
- **L'axe d'éclatement est vertical** : c'est le cas idéal en 9:16. Les couches s'étagent de y 300 à y 1250, écarts réguliers.
- Aux moments clés, le sujet occupe au moins un tiers de la hauteur.
- **Colonne d'étiquettes** du côté libre, à gauche (x 60 à 480) : décaler la projection (décalage de vue) plutôt que déplacer l'objet. La position horizontale de la colonne ne bouge jamais.
- **Structure d'étiquette fixe** : indice à deux chiffres en accent, nom (38 px), une ligne de caractéristique (28 px), unités toujours écrites (mm, Mo, ×n). Une étiquette porte au plus **un** fait que la voix ne dit pas.
- **Cotes** : tracées dans la perspective de la scène, texte sur petite plaque sombre, qui suit l'angle de la ligne et n'est jamais à l'envers.
- **Sous-titres** : bande centrée, y 1400 à y 1540, ombre douce, sans boîte.
- Zones d'interface : haut 160, bas 360, droite 135 (aucune étiquette à droite de x 945).
- **16:9** : colonne d'étiquettes d'un côté, sous-titres dans les 12 % du bas.

## 4. Ce qui bouge
- **Action principale** : la séparation. Départ doux, milieu rapide, longue stabilisation ; les couches partent **par le haut d'abord**, à 0,15 à 0,2 s d'écart ; les pièces répétées (touches, vis, cellules) se soulèvent en **vague** ordonnée par la distance à un coin.
- **Boucles de fond** : (1) la caméra voyage en continu (orbite dehors, macro dedans) ; (2) tenues écartées, les couches peuvent flotter d'un millimètre ou deux en phases décalées, sauf pendant les macros où elles sont parfaitement immobiles.
- **Fermeture** : par le bas d'abord, plus vite (~1 s par couche) ; la dernière couche se pose avec une vraie réponse mécanique (une touche fait sa course et revient ; rien ne rebondit comme du caoutchouc, sauf le caoutchouc).
- **Gestes** : dans l'interstice (la caméra entre entre deux couches pour voir une face cachée) ; le trait qui se pose sur la pièce (étiquette macro dont la ligne finit sur le composant) ; cotes dessinées sur l'objet après la fermeture ; **un seul vrai mouvement** (une pièce fait une fois son vrai geste mécanique : pression, charnière, loquet) ; lumières allumées à l'intérieur pendant que l'objet est ouvert.
- **Étiquettes** : elles se tracent (point d'ancrage, trait qui pousse, texte qui glisse de 10 px) et s'effacent avant que les pièces rebougent.
- **Mouvements de caméra** : orbite pendant la séparation ; travelling macro rasant (toucher, matière) ; plongée entre les couches ; poussée lente sur une pièce immobile ; montée à travers la pile ; recul rapide (synthèse) ; dérive haute en trois quarts (tailles, pas, épaisseur).
- **Autorisés** : #143 vue éclatée, #030 orbite, #027 travelling macro, #176 traversée, #184 très gros plan, #033 bascule de mise au point, #002 décalage en cascade, #004 tracé (traits et cotes), #172 plan-séquence.
- **Interdits** : coupes au noir, transitions de diapositives, #144 écran partagé, #123 rebond élastique, sol ou rapport lumière/caméra qui changent, tableau de caractéristiques à côté de l'objet.

## 5. Rythme et montage
- 30 i/s (la source était à 24 i/s ; rien dans le style n'en dépend), tout est fluide ; un ou quelques mouvements continus, transitions = mouvements de caméra à travers l'objet.
- Déroulé type : macro d'ouverture (matière) → orbite et séparation → 3 à 5 arrêts macro d'environ 3 s, un fait chacun → recul → fermeture → cotes sur l'objet fermé.
- Une étiquette s'ouvre **avant** que la caméra se pose (un arrêt macro dure environ trois secondes).
- Au moins deux quasi-silences (bruit de pièce seul) avant les grandes séparations ou le retour ; le premier son après est le coup le plus important autour.
- Étiquette entièrement dans le cadre (lettres ÷ 15 + 1,5) s ; sous-titre ≥ max(1,8 s ; parole + 0,6 s).
- **Version courte (8 à 12 s)** : macro d'ouverture (1,5 s), séparation (3 s), **un seul** arrêt macro de 3 s avec son fait, fermeture (1,5 s).

## 6. Recette technique
- **Moteur** : **Blender** par le connecteur `blender` (recommandé : import direct des fichiers CAO, matériaux physiques, profondeur de champ). Chaque couche est une collection ; l'éclatement est un décalage sur un axe piloté par une seule valeur ; caméra en clés dans le repère du produit. Rendu en séquence d'images ; étiquettes, cotes et sous-titres ajoutés dans HyperFrames depuis les points d'ancrage projetés et exportés image par image. Three.js possible pour un objet simple.
```python
# une seule valeur d'éclatement e(t) entre 0 et 1 ; chaque couche a son rang et son écart
for rang, couche in enumerate(couches_du_haut_vers_le_bas):
    depart = t0 + rang * 0.18                          # le haut part d'abord
    u = clamp((t - depart) / duree, 0, 1)
    couche.location.z = z_assemble[rang] + ecart[rang] * (u * u * u * (u * (6 * u - 15) + 10))
# caméra : interpolation monotone entre les clés (pas de dépassement), sinon un arrêt macro « glisse »
```
- **D'où vient la géométrie** : pour le produit du client, demander **avant tout** ses exports CAO (STEP, IGES), ses fichiers de carte, sa nomenclature et sa fiche technique. Pour un produit public : matériel ouvert et fiches des fabricants. Licences acceptées avec crédit : CC0, domaine public, CC BY, MIT ; les licences de matériel à partage à l'identique ne sont pas équivalentes : dire les conditions au client et demander. **Sans fichiers** : construire seulement à partir des dimensions publiées, dire à l'écran ou à la voix que c'est une maquette, et ne montrer aucun nombre non sourcé.
- **Cartes électroniques** : peintes depuis leurs fichiers de conception (cuivre, pistes, pastilles, sérigraphie) à 14 à 20 px par millimètre, avec cartes de rugosité, de métal et de relief tirées du même dessin.
- **Profondeur de champ** : une seule ouverture pour le large et le macro (le flou grandit quand la caméra s'approche).
- **Pièges** : nombres inventés (mesurer dans la CAO et écrire « mesuré » dans les faits, ou s'abstenir) ; révisions mélangées (les trous et hauteurs doivent coïncider entre fichiers ; noter la version) ; carrés noirs d'une image (géométrie dégénérée : balayer les images) ; lumières de zone qui brûlent les plastiques ; **marques sur les pièces** (dessus de puces et connecteurs portent des logos : dessus neutres, sauf si le produit est celui du client).

## 7. Son
- **Instruments** : maillets accordés (marimba, vibraphone, verre), basse ronde, petit coup synthétique court, percussions sèches. Précis et sec hors de l'objet ; tenu et aérien dedans.
- **Le bruitage est la matière** : claquements creux pour les capots en plastique, clic d'interrupteur, petits coups secs pour les cartes, tintements pour le métal usiné, souffles aériens pour les couches qui se soulèvent et les plongées de caméra, fin sifflement de plume quand une cote se trace. Chaque séparation et chaque pose a son son, placé là où est la pièce (une vague de pièces répétées compte pour un seul événement dans le budget du skill `son`).
- Voix calme, proche, posée ; nombres dits en mots, écrits en chiffres ; musique ≈ 10 dB dessous ; basses très graves contenues ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La géométrie vient des fichiers du produit (ou de dimensions publiées, et alors le film dit « maquette »).
- [ ] Un seul axe d'éclatement, écarts réguliers, chaque couche orientée comme dans le produit.
- [ ] Chaque nombre à l'écran est dans `FAITS.md` avec sa source ou sa méthode de mesure.
- [ ] Les étiquettes suivent la structure indice / nom / une caractéristique, avec unité ; une seule couleur d'accent, réservée au mesuré.
- [ ] Aucune coupe au noir ; un arrêt macro tient vraiment (pas de glissement de caméra).
- [ ] Aucune image avec carré noir ou plastique brûlé (balayage des images).
- [ ] Aucune marque de tiers visible sur les pièces.
- [ ] Étiquettes à gauche de x 945, sous-titres hors zones d'interface.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/teardown.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/teardown.jpg
- Crédit : « 21 Keys, Opened », LemoLab, CC BY 4.0 ; le produit montré vient de fichiers de matériel ouvert de tiers (CC BY 4.0 / MIT) : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/teardown/STYLE.md`, `style.json`, `demo/src/` (`parts.js`, `pcbtex.js`, `comps.js`, `overlay.js`, `main.js`), `demo/src/tools/` (`extract_pcb.py`, `step2mesh.mjs`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, axe vertical pour le 9:16, Blender en moteur principal (la démo d'origine est en Three.js), assemblage HyperFrames.
