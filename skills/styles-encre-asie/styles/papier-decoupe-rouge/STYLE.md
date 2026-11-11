# Papier découpé rouge

## 1. Identité

- **Nom** : Papier découpé rouge (« fleurs de fenêtre », art populaire chinois).
- **Inspiration** : les découpages de fenêtre des campagnes du nord de la Chine (dents de scie, croissants, nuages, volutes, rosaces symétriques par pliage) et les courts métrages en papier découpé articulé de la fin des années 1950. Aucun personnage de studio, aucune œuvre d'artiste nommé, aucune planche de motifs réelle : **chaque motif est généré par le code**.
- **Ce que c'est** : tout ce qu'on voit est **une feuille de papier coupée aux ciseaux** et posée à plat sur une autre. Ni peinture, ni dégradé d'ombre, ni trait de contour : détail, volume et expression viennent uniquement de **ce qui a été enlevé**. Le papier rouge est le matériau héros ; les fonds sont du papier aussi (clair le jour, teint foncé la nuit). Les personnages sont des **découpages articulés** animés par paliers secs.
- **Marche pour** : Nouvel An lunaire, fête, tradition, famille, « un geste qui se multiplie » (franchise, classe, récolte), ouverture d'un commerce, vœux.
- **Ne marche pas pour** : sujet triste (sauf à changer la famille de papier), technique, données, photo de produit.
- **À ne pas confondre** : pas des ombres chinoises (papier **opaque éclairé de face**, ni cuir, ni tiges ; le contre-jour est un événement rare) ; pas du vectoriel plat ; pas un film de silhouettes (l'intérieur de chaque forme est découpé). Le papier découpé de collage et les papiers de style Matisse sont dans `styles-papier-impression`.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Rouge de Chine (héros) | `#d2201f` (plage `#c8102e` à `#d7261e`) |
| Rouge un ton plus clair (proche) / plus sombre (loin, lourd) | `#e23a32` / `#a81a1c` |
| Fond jour : papier de riz, collines rouge pâle | `#f3e9d2`, `#e9b8ae` |
| Fond nuit : papiers indigo (loin plus clair, près plus sombre) | `#3c4f86`, `#27345f`, `#161d3a` |
| Feuille d'or (un seul moment tardif) | `#e3b04b` |

- **Profondeur et rôle par tons de papier voisins**, pas par ombrage : pièces proches un ton plus clair, lointaines un ton plus sombre, l'antagoniste ou l'objet lourd un ton plus profond.
- **Fond et héros doivent être de deux familles de papier différentes** : rouge sur rouge = une seule tache.
- **L'or** est réservé à un moment (un soleil, un titre, une pièce) ; jamais une seconde couleur principale.
- Sujet non festif : papier vert jade ou noir à la place du rouge.
- **Typographie** : serif robuste (**Fraunces SemiBold**, OFL). Sous-titres sur une **bande de papier dans le monde** : bannière rouge plus sombre que les rouges de l'image, bords dentelés, bouts en queue d'hirondelle, texte crème, ombre de papier. Titres en **lettres découpées** (les contreformes sont de vrais trous), bordures en dents de scie, sceau découpé par le code (abstrait).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Fraunces. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fraunces` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Grain* : texture gris neutre en lumière douce dans chaque pièce (marbrure de teinture, fibres), puis découpes rétablies : les trous restent des trous.
  - *Bord coupé* : silhouette en polyligne légèrement tremblée ; liseré clair de 1 px en haut à gauche, sombre en bas à droite (la tranche). Architecture et machines : segments droits + tremblé, jamais lissés.
  - *Épaisseur* : chaque pièce porte une ombre douce et serrée sur la couche du dessous ; du papier plié empilé montre 2 à 6 bords décalés.
  - *Double contour* : chaque pièce de personnage a une **fente intérieure** à quelques unités du bord ; elle sépare aussi rouge sur rouge (un bras sur un manteau).
  - *Vocabulaire de coupe* : rangées de dents de scie (fourrure, herbe, tuiles, franges), croissants (écailles), volutes (articulations), nuages, rosaces, fleur de prunier, pièce de monnaie, fentes effilées.
  - **Pas d'îles flottantes** : un anneau fermé ferait tomber son centre. Les yeux sont deux croissants qui laissent des ponts, plus une pupille en *trou*.
  - *Rosace* : dessinée sur un secteur de 45° et répétée 8 fois en miroir ; anneaux alternés « lignes rouges gardées » / « lignes découpées dans un champ rouge ». Garde les faibles plis du pliage.

## 3. Composition 9:16

- Les couches restent **parallèles à l'écran** ; la profondeur vient de la parallaxe et des tons de papier, jamais de la perspective.
- En vertical : 4 à 5 couches empilées (ciel, collines lointaines, village ou décor, sol, premier plan), personnage sur la couche du milieu, ≥ 1/3 de la hauteur. Vue de face frontale pour un emblème ou un titre ; vue du dessus (table) pour plier, couper, assembler.
- Une rosace plein cadre fait ≈ 900 px de diamètre, centrée vers y 800.
- **Bannière de sous-titres** : basse (y ≈ 1400 à 1520), texte ≈ 48 px ; elle tombe en deux paliers, comme un papier qu'on colle. Tenue ≥ max(1,8 s ; réplique + 0,7 s), jamais deux à la fois.
- De profil, un bras proche levé croise le visage : garde les mains en avant du visage ou laisse un accessoire les couvrir. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : **plier, couper, déplier** : on plie une feuille 2, 4 ou 8 fois, une coupe devient plusieurs ; le dépliage tombe sur un temps fort.
- **Boucle de fond 1** : couches de papier en parallaxe lente ; pièces volantes (chutes de découpe, flocons, confettis) fluides.
- **Boucle de fond 2** : la nuit : flammes et lumière chaude qui respirent, motifs projetés au sol par les trous.
- **Gestes natifs** : **les trous sont de la lumière** (une découpe éclairée par derrière brille rouge profond, chaque trou s'allume, le motif se projette sur le monde) ; la symétrie se multiplie (rosace → fleurs de fenêtre → feux d'artifice) ; **les chutes ont un avenir** (ce qui tombe pendant la coupe revient en neige, confettis, étoiles) ; tout est une seule feuille (une crête se lève et devient une créature) ; la paire en miroir.
- **Détail des gestes** : *pli* ≈ 0,5 s, chacun sur un coup ; *coupe* : le motif se révèle le long du trajet des ciseaux, la chute tombe quand le bord est franchi, les lames s'ouvrent et se ferment sur une subdivision du temps ; *dépliage* : volets successifs qui claquent à plat, puis petit gonflement d'échelle et éclair chaud.
- **Autorisés** : `#128` saccadé (15 poses par seconde), `#001` apparition en rebond d'un palier (« pop » à 1,15 × pendant une pose), `#016` parallaxe de couches, `#140` page tournée ou feuille pelée, `#021` volet qui se rabat (pli), `#184` très gros plan qui suit la pointe des ciseaux, `#181` vue du dessus, `#134` répétition en rosace, `#024` secousse pour le poids.
- **Interdits** : `#044` fondu, dégradés, traits de contour, `#012` métamorphose de visage (les expressions sont des **pièces de visage échangées** : sourire, surprise, peur, résolu, endormi), perspective, grain de film.

## 5. Rythme et montage

- Personnages à **15 poses par seconde** (pose prise à `floor(t × 15) / 15` ; à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; caméra, lumière, météo, flammes et pièces volantes fluides.
- Poses dures, accélérations minuscules, dépassement d'une seule pose. Le **poids** vient de la taille et de la secousse de caméra.
- Plans de 3 à 6 s. Transitions = **actions de papier** : pli, page tournée, feuille pelée, feuille qui s'envole, coupe à travers le cadre. Superpose l'action sortante et l'entrante : pas d'image vide entre deux plans.
- Un coup de ciseaux = une subdivision du temps ; un seul grand gong pour un seul accent ; silence total pour un souffle retenu.
- **Version courte (8 à 12 s)** : deux plans : plier et couper (3 s), puis déplier sur le temps fort et tenir la figure ; une seule transition de papier. Accroche avant 3 s : le premier coup de ciseaux.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (textures, constructeur de pièce : aplat, coupe, fente intérieure, bord, grain, ombre, transmission), `motifs.js` (bibliothèque de coupes), `rig.js` (pièces épinglées par rivets), `rosace.js` (un secteur × 8), `lumiere.js` (carte de lumière de nuit, pièces en contre-jour, halo, rayons, motif projeté), `pli.js` (plier, couper, déplier), `texte.js` (bannière, lettres découpées).
- **Techniques clés** :
  ```js
  const tq = Math.floor(t * 15) / 15;                       // poses des personnages
  // grain dans la pièce sans boucher les trous
  p.globalCompositeOperation = "soft-light"; p.drawImage(GRAIN, 0, 0);
  p.globalCompositeOperation = "destination-in"; p.drawImage(masquePiece, 0, 0);
  // pli : ~16 bandelettes, chacune comprimée par cos(theta) et agrandie le long du pli
  const echelle = 1 + 0.28 * hauteur;                       // fausse perspective ; assombrir en se levant
  // nuit : image × carte de lumière, puis pièces en contre-jour (lumière × transmission du papier)
  ```
- **Pièges** :
  - **Rouge sur rouge** : une seule tache. Autre famille de fond, tons proche et loin, fentes intérieures.
  - Assombrir une couche par la carte de lumière assombrit aussi ce qui la recouvre : teinte la couche elle-même.
  - **Un volet simplement écrasé par un cosinus se lit comme une carte qui glisse**, pas comme un pli : bandelettes à fausse perspective, assombries, couleur du verso passé 90°.
  - Pendant la coupe, la pile non coupée se voit par les trous : l'épaisseur de pile ne vaut que dans la zone « non coupée ».
  - Ciseaux qui pointent en arrière : l'axe des lames suit la direction du trajet.
  - Halo trop fort en contre-jour : le motif ne se lit plus au centre.

## 7. Son

- **Musique** : un ensemble de chambre chinois **clair**, ni piano et cordes, ni les percussions d'opéra des ombres chinoises : luth en poire (trémolo sur les notes longues), cithare (accords brisés, glissandos), vièle à deux cordes (glissés), flûte traversière de bambou, woodblock, petit et grand gong, tambour sur cadre. Modes pentatoniques.
- **Bruitages** (≈ 5 par 10 s) : ciseaux = cisaillement métallique + petit tintement + craquement de fibre ; pli = souffle + tape sur le pli ; dépliage = claquement sec ; pas lourds = **carton**, pas chair ; papier qu'on pèle ; collage = paume qui tapote ; allumette ; pétards = clics denses avec des graves.
- **Voix** : conteur chaleureux, peu de phrases. Musique baissée d'environ 9 dB sous la voix ; garde les impacts hors des phrases. Mix −14 LUFS, **aucun grain de film**.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : rouge sur rouge ; dégradés ; contours tracés ; formes pleines sans découpe ; animation lissée ; plis qui glissent.

- [ ] Aucune forme n'a de trait de contour ni de dégradé : seul le découpage dessine.
- [ ] Chaque pièce a un liseré clair / sombre et une ombre serrée sur la couche du dessous.
- [ ] Le fond et le héros sont de deux familles de papier différentes.
- [ ] Chaque pièce de personnage a sa fente intérieure ; aucun « îlot » flottant.
- [ ] Personnages à 15 poses par seconde, caméra fluide.
- [ ] Au moins une action de papier comme transition ; aucun fondu.
- [ ] L'or n'apparaît qu'une fois.
- [ ] Bannière de sous-titres lisible, hors y > 1560 et x > 945 ; aucun caractère inventé.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 11
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Film de démo d'origine (49 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/papercut-red.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/papercut-red.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/papercut-red.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#east-asian-traditions
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre le conte, les personnages ni les plans.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/papercut-red/STYLE.md`, `DEMO.md`, `demo/paper.js`, `motifs.js`, `rig.js`, `tuanhua.js`, `light.js`, `fold.js`, `hud.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, section 9:16, valeurs hex des tons voisins et des fonds proposées par Flot Web (la source donne le rouge héros et décrit les familles), numéros du dictionnaire de mouvements.
