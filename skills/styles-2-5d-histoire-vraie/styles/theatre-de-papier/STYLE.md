# Théâtre de papier

## 1. Identité

- **Nom** : Théâtre de papier.
- **Inspiration** : les théâtres-jouets en carton imprimé du XIXe siècle (feuilles à découper lithographiées et coloriées à la main, décors en plans glissés sur des tringles, cadre de scène doré, rampe de bougies) et la caricature gravée de la même époque. On reprend la grammaire de l'objet, pas une feuille ou un personnage existants.
- **Pour quels sujets** : une histoire vraie ancienne (du XVIIe au début du XXe siècle), un fait divers d'époque, une anecdote de cour, de théâtre ou de justice, la vie d'un inventeur, une scène à plusieurs personnages face à face. Le ton pince-sans-rire lui va très bien.
- **Ne marche pas pour** : un sujet contemporain ou technique, une histoire qui demande un vrai volume (un mécanisme à faire tourner), un grand espace extérieur traversé par la caméra, un ton grave et réaliste.

C'est le style le plus simple de la catégorie : tout est plat, y compris le décor, et toute la lumière vient d'un seul endroit. L'objet héros reste en volume (voir section 6).

## 2. Palette, typographie, matières

Valeurs reprises du prompt d'origine.

| Rôle | Couleur |
|---|---|
| Carton crème (fond de toutes les pièces, peau, ciel, eau) | `#F4ECD6` |
| Rouge profond (cadre de scène, rideaux) | `#C8262C` |
| Or terne (cadre de scène ; jamais de jaune vif) | `#E0AB36` |
| Bleu (costumes) | `#2F5A9A` |
| Décors | bruns grisés, gris, crème |
| Trait | noir lithographique |

- **Tout est du carton imprimé** : contours noirs fins d'environ 1/400 de la largeur du cadre (2 à 3 px en 1080), **hachures de crayon gras clairsemées d'un seul côté** de chaque pièce, coloriage à la main, délavé et ancien.
- **Chaque découpe garde une marge blanche de ciseaux** d'environ 1/200 de la largeur du cadre (5 à 6 px). C'est la signature : une figurine sans marge casse le style.
- **Décors** : des plans de carton parallèles, plats chacun, étagés en profondeur.
- **Cadre de scène** doré, tentures rouges, loges de spectateurs peintes sur les côtés.
- **Hors scène** (plan d'ouverture ou de fin) : une table en bois sombre dans une pièce obscure.
- **Typographie** (polices libres) : titres en capitales à empattements d'affiche ancienne (Playfair Display, IM Fell English) ; sous-titres en Montserrat ExtraBold blanc à contour sombre pour rester lisibles.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place d'IM Fell English ; Playfair Display, Montserrat : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/im-fell-english` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.

## 3. Composition 9:16

- 1080×1920. Zones sans rien d'important : 160 px en haut, 360 px en bas, 135 px à droite.
- Dans le prompt d'origine (image large), l'ouverture de scène occupe 80 à 90 % de la largeur. En vertical, **le théâtre est plus haut que large** : ouverture de scène d'environ 900 px de large sur 1100 à 1200 px de haut, centrée un peu au-dessus du milieu ; fronton et rideaux dans le haut ; rampe de bougies et bord de table dans le bas (dans la zone des 360 px, où rien d'important ne se joue).
- Les décors gagnent de la hauteur : frises, cintres, ciel peint, balcon.
- Figurines : un quart à un tiers de la hauteur de l'ouverture en plan de scène ; en gros plan, deux figurines face à face remplissent la largeur.
- **Sous-titres** : 1 à 2 mots, 96 à 112 px, sur la bande sombre entre la rampe et la zone du bas (ligne de base vers 1400–1500 px du haut), jamais sur une figurine.
- 16:9 : format d'origine ; ouverture de scène à 80–90 % de la largeur.

## 4. Ce qui bouge

- **Action principale** : une figurine **glisse** sur sa tringle (entrée, pas en avant, recul), pivote légèrement autour de sa base, ou lève un accessoire. Un geste par plan, calé sur un mot.
- **Deux boucles de fond** : (1) **le vacillement de la rampe de bougies**, qui fait bouger toutes les ombres portées sur le décor ; (2) une micro-dérive de la caméra ou un léger tremblement des cartons sur leurs tringles (1 à 2 px).
- **Les ombres sont le spectacle** : la rampe, placée en bas devant la scène, projette l'ombre de chaque découpe sur le plan de derrière, **agrandie d'environ 1,5 fois**, douce, vacillante.
- Mouvement de carton : translations et petites rotations rigides. Pas de déformation, pas d'écrasement, pas de membres articulés fluides.

| Autorisés (dictionnaire `principes-mouvement`) | Interdits |
|---|---|
| `#016` parallaxe entre les plans de décor | `#011` écrasement-étirement |
| `#027` avancée lente vers la scène | `#012` métamorphose de forme |
| `#029` travelling latéral le long de la scène | `#030` orbite (révélerait la tranche des cartons) |
| `#024` secousse d'impact, courte, sur un cri ou un choc | `#032` travelling compensé |
| `#010` léger dépassement à l'arrêt d'une figurine sur sa tringle | `#023` effet de parasite, `#043` panoramique filé |

Le jeu d'acteur passe par la **pose**, la **distance** entre figurines et l'**ombre**, pas par le visage : prévoir 2 ou 3 découpes par personnage (neutre, bras levé, recul) et les échanger sur un mot.

## 5. Rythme et montage

- Trois tailles de plan nettement différentes : la table (large), la scène (moyen), le gros plan. Les enchaîner dans cet ordre construit une montée.
- Plans de 2 à 3 s ; coupes franches sur un début de mot.
- Changement de lieu : un plan de décor glisse sur le côté et un autre arrive, ou le rideau se ferme et se rouvre (une ou deux fois par vidéo, pas plus).
- Fin possible : recul de la caméra qui découvre la pièce sombre et le théâtre posé sur la table.
- **Version courte (8 à 12 s)** : garder les trois tailles de plan une fois chacune (table, scène, gros plan), un geste de figurine par plan ; couper le changement de lieu, le rideau et le recul final. Accroche avant 3 s : une figurine entre sur sa tringle dans le premier plan.

## 6. Recette technique

- **Moteur** : Blender (skill `blender`) ; assemblage dans HyperFrames.
- **Structure** : un théâtre construit une fois (cadre de scène, tentures, plancher, tringles, table), réutilisé pour tous les lieux en changeant les plans de décor.
  - 4 à 6 plans de décor parallèles, espacés de 8 à 15 cm, du ciel peint au premier plan ;
  - figurines sur des plans intercalés, chacune sur sa tringle (un objet vide qu'on fait glisser) ;
  - toutes les pièces sont des images à fond transparent **avec leur marge blanche dessinée** (contour blanc ajouté autour de la découpe à l'export).
- **Matériau** : ici les cartons **reçoivent la lumière** (matériau mat ordinaire, rugosité élevée, transparence par découpe), parce que le style repose sur les ombres portées d'un plan sur l'autre. C'est l'exception à la règle « personnages émissifs » de la catégorie : le personnage reste plat, sans modelé, mais il vit dans la lumière de la rampe.

```python
# rampe : une rangée de lumières ponctuelles chaudes, en bas devant la scène (théâtre de 60 cm de large)
for i, x in enumerate((-0.30, -0.15, 0.0, 0.15, 0.30)):
    d = bpy.data.lights.new(f"Rampe_{i}", "POINT")
    centrale = (i == 2)
    d.energy = 1.0 if centrale else 0.2          # en watts : à cette échelle, quelques watts brûlent tout
    d.use_shadow = centrale                      # une seule lampe projette l'ombre
    d.color, d.shadow_soft_size = (1.0, 0.72, 0.42), 0.012
    o = bpy.data.objects.new(d.name, d); bpy.data.collections["LUMIERES"].objects.link(o)
    o.location = (x, -0.25, 0.03)
```

- Essai fait en Blender 5.3 (Cycles) : avec cinq lampes qui projettent toutes une ombre, on obtient cinq ombres pâles et illisibles ; avec **une seule lampe à ombre** (les autres ne font que déboucher), l'ombre de la figurine se lit nettement sur le décor, agrandie et douce. Une puissance de 6 W par lampe brûle la scène ; rester autour de 1 W pour la lampe principale et monter par petites touches.
- Cacher les lampes derrière le rebord de la rampe : le plancher juste devant elles est très clair.
- L'agrandissement des ombres (environ 1,5 fois) se règle par la distance : rampe proche des figurines, plan de décor plus loin derrière.
- Les figurines projettent leur ombre : `obj.visible_shadow = True`, transparence en méthode « dithered » pour que l'ombre suive la découpe.
- Profondeur de champ légère (f/4 à f/5,6) : la scène nette, la table et la pièce floues.
- **Objet héros** : construit en volume, à l'échelle du théâtre (un accessoire de quelques centimètres), posé sur le plancher de scène et éclairé par la rampe ; il a son gros plan.
- **Pièges** : couleurs vectorielles vives (délaver, griser) ; vraie profondeur dans un plan de décor (chaque plan reste plat) ; lumière douce de studio (toute la lumière vient de la rampe, par en dessous) ; figurines sans marge blanche ; caméra trop de côté qui montre la tranche des cartons.

## 7. Son

- **Ambiance** : une petite salle, le bois qui craque, le frottement léger du carton sur les tringles.
- **Bruitages** : glissement de carton à chaque entrée, petit choc de bois à l'arrêt, froissement du rideau, souffle de bougie ; un coup de grosse caisse ou de cymbale de théâtre sur l'événement central.
- **Musique** : piano droit, orgue de Barbarie, petit ensemble de fosse ; un thème, sous la voix, résolu sur la dernière image.
- Une seule voix ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque découpe a sa marge blanche de ciseaux.
- [ ] Aucun jaune vif, aucune couleur saturée moderne ; rouge, or terne et bleu seulement en accents.
- [ ] Toute la lumière vient de la rampe ; les ombres des figurines se voient sur le décor, plus grandes qu'elles, et vacillent.
- [ ] Chaque plan de décor est plat ; aucun plan ne montre la tranche d'un carton.
- [ ] Les figurines glissent et pivotent, sans déformation.
- [ ] Trois tailles de plan différentes dans la vidéo (table, scène, gros plan).
- [ ] L'objet héros est en volume et a son gros plan.
- [ ] Sous-titres hors des figurines et au-dessus des 360 px du bas.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Extrait d'origine (2,5 s, de 2:08 à 2:11) dans le film collectif de LemoLab : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/opuscar98.mp4 · page des styles : https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles
- Crédit : **LemoLab**, CC BY 4.0, https://github.com/lemomo-ai/lemo-opuscar.
- **À consulter seulement, ne pas afficher sur une page de vente** : l'extrait met en scène une mascotte tierce et l'adaptation d'une œuvre protégée. Aperçu à produire avec le plugin.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichier `styleboard/opuscar98_styles.json`, entrée n° 41 (« Victorian Toy Theatre », rendu 2.5D), champs `prompt_en`, `desc_en`, `blend_en`, `shots`.
- Licence : MIT (prompt et documents), CC BY 4.0 (film et images).
- Repris : couleurs, épaisseur du trait, marge de ciseaux, ombres de rampe agrandies, cadre de scène, mouvements de caméra, liste « à éviter ». Retirés : le titre et les personnages de l'œuvre adaptée, la mascotte, les noms de fabricants.
- Ajouts du studio : composition 9:16, recette Blender, son, numéros du dictionnaire de mouvements, liste de contrôle. Ce style n'a pas de code de démo d'origine : **recette à valider par un rendu réel.**
