---
name: principes-mouvement
description: "Socle commun du mouvement pour toutes les vidéos du studio — dictionnaire des 192 mouvements numérotés, principes d'animation adaptés au vertical, règles chiffrées, pièges GSAP et vocabulaire caméra. À utiliser dès qu'on choisit, écrit, corrige ou vérifie une animation, un mouvement de caméra ou une transition, et avant de rédiger ou d'appliquer la section « Ce qui bouge » d'une fiche de style."
---

# Principes de mouvement

Ce skill est la **référence commune à tous les styles**. Une fiche de style dit *de quoi c'est fait* (matière, palette, typographie) ; ce skill dit *comment ça bouge* et donne les mots pour en parler. Il s'applique à chaque vidéo, quel que soit le style choisi.

Cadre par défaut : vertical **1080 × 1920, 30 images par seconde**, moteur HyperFrames (HTML + GSAP) ; Blender pour la 3D et la 2.5D. Le parcours de production est piloté par le skill `studio-coeur` ; le moteur par `rendu` ; le son par `son`.

## Ce que contient ce skill

| Fichier | Contenu | Quand l'ouvrir |
|---|---|---|
| `references/dictionnaire-mouvements.md` | Les 192 mouvements numérotés (8 packs de 24) : nom français, ce qui bouge, durée et courbe, quand l'utiliser, chemin du code | Au découpage, pour choisir ; à la construction, pour porter |
| `references/motion-prompt/` | Copie locale figée des fiches et du code d'origine (`e/NNN.txt`, `kit/<pack>.js`) | Avant de porter un mouvement : lire sa fiche |
| `references/principes.md` | Règles chiffrées, courbes et ressorts, 12 principes adaptés au vertical, chorégraphie, composition 9:16, règles de goût, règles « anti-motion IA » | Avant d'écrire une timeline ; pendant la relecture |
| `references/gsap.md` | Pièges et bonnes pratiques GSAP pour un rendu image par image, tableau des pannes | Pendant l'écriture du code ; dès qu'une animation saute, disparaît ou saccade |
| `references/camera.md` | Vocabulaire caméra français, valeurs typiques, dosage, fabrication en HyperFrames et en Blender | Dès qu'un plan a un mouvement de cadre ou un raccord particulier |

**Ordre de priorité en cas de conflit** : la référence fournie par le client → la fiche de style → les règles du moteur (skill `rendu`) → ce skill.

## Comment choisir un mouvement

Fais-le **au découpage, avant tout code**. Pour chaque plan :

1. **Dis l'intention en un verbe précis.** « Le prix tombe », « la courbe se trace », « l'écran s'ouvre ». Si le seul verbe disponible est « apparaît » ou « s'affiche », l'idée du plan n'est pas encore trouvée.
2. **Classe le besoin** : entrée, mise en valeur, transformation, transition entre plans, geste de caméra, boucle de fond.
3. **Ouvre la fiche de style** (section 4, « Ce qui bouge ») : elle liste les numéros autorisés et interdits. Choisis d'abord parmi les autorisés.
4. **Cherche dans le dictionnaire** : l'« index par besoin » en fin de fichier, puis le tableau du pack. Retiens un numéro par besoin.
5. **Vérifie quatre choses** :
   - le mouvement **sert le sens** (un chiffre qui monte → #007 ; deux faces → #021 ; pas l'inverse) ;
   - il est **lisible en vertical** et tient dans la zone sûre ;
   - il n'est **pas interdit** par le style, et il reste dans le budget d'accents du film ;
   - il **diffère** du plan précédent (pas trois fois le même geste de suite).
6. **Note-le dans le découpage** : colonne « Mouvement » avec le numéro et le nom, par exemple `#005 Révélation par masque`. Une ligne par plan : action principale, éventuel geste de caméra, raccord de sortie.
7. **À la construction** : lis `motion-prompt/e/NNN.txt`, reprends durées, courbe et amplitudes relatives, change seulement le contenu et la matière. Si tu reprends du code ou des valeurs, **recopie la ligne de licence** de la fiche en commentaire (voir le dictionnaire).

Si le client a choisi un numéro lui-même, tu ne le remplaces pas en silence : s'il pose problème, dis pourquoi et propose le voisin le plus proche.

Si aucun numéro ne convient, tu peux composer un mouvement original, à condition de respecter les règles ci-dessous et de le noter « hors dictionnaire » dans le compte rendu.

## Les 10 règles d'or

1. **Aucune vitesse constante.** Tout déplacement, changement d'échelle ou d'opacité a une courbe. Le linéaire est réservé aux rotations continues, dérives, défilements et barres de progression.
2. **Une seule chose importante bouge à la fois.** Un point focal par image ; au plus un tiers des éléments en mouvement au même instant.
3. **Une entrée combine 2 à 3 propriétés, jamais l'opacité seule** — et les entrées varient au fil du film.
4. **Décalages de 3 à 6 images** entre éléments d'un groupe (mots 3, liste 4 à 5, gros blocs 6), total sous 0,5 s.
5. **Les sorties durent environ 10 images, les entrées environ 20.** Ce qui part ne mérite pas l'attention.
6. **Frappe, pause, construction.** Après un temps fort, 15 à 20 images sans rien de nouveau. Un texte ne bouge pas pendant qu'on le lit ; il tient au moins 1 s, plus 0,25 s par mot au-delà de trois (règle contrôlée par la porte de livraison : `studio-coeur/references/controles.md`, section 2, avec sa variante `--strict` pour l'explicatif posé).
7. **Quelque chose bouge avant l'image 15 de chaque scène, et rien ne reste figé plus de 90 images.** Chaque plan a une action principale et deux boucles de fond discrètes.
8. **Le texte important reste dans la zone utile**, hors des zones d'interface (haut 160 px, bas 360 px, droite 135 px ; table complète : `rendu/references/zones-interface.md`), et se lit sur une image réduite à 360 px de large.
9. **Le son tombe sur l'impact, jamais avant.** L'attaque d'un coup, d'un clic ou d'un pop se pose sur l'image du contact, avec 8 ms de retard visé (tolérance : de 45 ms avant à 75 ms après). Seuls les sons qui s'établissent lentement (souffle, montée) **commencent** avant, pour que leur pic ou leur fin tombe sur l'image. Règle et outils de calage : skill `son` (règle 8, `caler.py`).
10. **Une identité de mouvement par vidéo** : une famille de courbes, trois durées, un seul moment héros, une caméra qui ponctue — et uniquement des mouvements autorisés par la fiche de style, rendus de façon reproductible (aucun aléatoire sans graine, aucune horloge).

**Règle de sécurité (elle passe avant les dix autres, avant la fiche de style et avant la demande du client).** Pas plus de **3 éclairs ou changements brusques de couleur ou de luminance par seconde sur une grande surface** : au-delà, l'image peut déclencher une crise chez une personne photosensible. Grande surface : plus d'un quart de l'image. Brusque : fait en moins de 3 images. En pratique, au moins 10 images (0,33 s) entre deux éclairs, et chaque aplat plein cadre tient au moins 10 images. Les effets rapides restent permis sur de **petites surfaces** (moins d'un dixième de l'image : un voyant, une étincelle, le grain, un trait qui vibre) et à **faible contraste** (scintillement discret d'un fond). Détail et cas limites : `references/principes.md`, section 1.

Le détail, les conversions en secondes et les exceptions sont dans `references/principes.md`.

## Les fiches de style déclarent leurs mouvements par numéro

**Principe : chaque fiche de style déclare ses mouvements autorisés et interdits par numéro du dictionnaire.** C'est ce qui garantit qu'un style reste reconnaissable d'une vidéo à l'autre, et qu'un contrôle est possible.

Dans la section 4 d'un `STYLE.md` (« Ce qui bouge »), on doit trouver :

```markdown
### Mouvements
- Action principale type : …
- Boucles de fond (2) : …
- Identité de mouvement : courbe signature `…`, durées … / … / … s, motif d'entrée …, dépassement … %
- Cadence : 30 i/s lissé | « en 2 » (15 poses par seconde à 30 i/s, `steps`) | …
- **Autorisés (natifs du style)** : #004 Tracé de ligne, #012 Morphing de forme, #136 Trait vibrant
- **Autorisés avec réserve** : #024 Secousse d'impact (une fois par vidéo)
- **Interdits** : #023 Glitch, #015 Particules, #021 Retournement
- Caméra : gestes autorisés (voir `camera.md`) et dosage
- Raccords : coupe franche par défaut ; transition signature : #…
```

Règles d'usage :

- **Tout numéro absent des trois listes est neutre** : utilisable s'il respecte l'identité de mouvement du style (courbe, durées, cadence). En cas de doute, préfère un mouvement natif.
- **Un numéro interdit ne s'utilise jamais**, même si le client le demande : explique pourquoi il casse le style (par exemple un glitch dans un lavis d'encre) et propose un équivalent autorisé.
- **Le dictionnaire fixe le timing, le style fixe la matière.** Le même #012 est rendu en papier déchiré dans un style papier découpé, en blocs dans un style pixel, en encre dans un style dessiné. La fiche du dictionnaire donne les durées et la courbe ; la fiche de style peut les remplacer par sa courbe signature et sa cadence, en gardant les proportions.
- **Cadence « en 2 » ou image par image** : on ne change pas les durées, seulement l'échantillonnage (`steps`).
- **Cadence saccadée à 30 i/s (règle unique du plugin)** : un film à 30 i/s ne tient des poses régulières qu'à **15, 10 ou 6 par seconde** (une image sur 2, 3 ou 5). Les sources ont été réglées à 24 i/s, où « en deux » = 12 et « en trois » = 8. Quand une fiche de style ou un extrait de code dit **12**, joue **15** ; quand il dit **8**, joue **10** (`Math.floor(t * 15) / 15`). 12 ou 8 poses par seconde à 30 i/s donnent un rythme irrégulier (2 images, puis 3). Seuls les personnages, les objets et le trait sont saccadés ; la caméra, la lumière et les fluides restent à 30 i/s. Si le client accepte un film à 24 i/s, garde les valeurs d'origine.
- **Quand tu rédiges une fiche de style**, remplis ces listes à partir des vraies sources du style ; cite au moins 3 mouvements natifs et les interdits évidents. Quand un geste du style n'existe pas dans le dictionnaire, décris-le en clair, sans inventer de numéro.
- **Le compte rendu de fin de production** liste, plan par plan, le numéro et le nom de chaque mouvement utilisé, ce qui a été modifié, et tout mouvement hors dictionnaire.

## Liste de contrôle du mouvement

À passer sur le découpage, puis sur le rendu (images extraites **et** film regardé à vitesse normale).

**Choix**
- [ ] Chaque plan a une action principale dite par un verbe précis, et un numéro du dictionnaire (ou la mention « hors dictionnaire »).
- [ ] Aucun numéro interdit par la fiche de style ; les « avec réserve » respectent leur limite.
- [ ] Pas trois plans de suite avec le même mouvement ni le même geste de caméra ; accents de caméra sur moins d'un tiers des plans.
- [ ] Un seul moment héros, pas gaspillé (sauf s'il est l'accroche).

**Rythme**
- [ ] Aucun déplacement, échelle ou opacité à vitesse constante.
- [ ] Quelque chose bouge avant l'image 15 de chaque scène ; rien de figé plus de 90 images ; l'image 0 n'est pas vide.
- [ ] Décalages de 3 à 6 images, total d'un groupe sous 0,5 s.
- [ ] Sorties d'environ 10 images, entrées d'environ 20 ; les scènes se chevauchent, pas de trou.
- [ ] Une pause de 15 à 20 images après chaque temps fort ; au moins 3 moments d'immobilité dans la vidéo.
- [ ] Chaque texte tient son temps de lecture (1 s + 0,25 s par mot au-delà de trois ; 2 s pour le dernier) et ne bouge pas pendant sa lecture.

**Qualité**
- [ ] Une seule chose importante bouge à la fois ; un point focal par image.
- [ ] Entrées à 2 ou 3 propriétés, variées ; jamais l'opacité seule.
- [ ] Une famille de courbes, trois durées : celles de la fiche de style.
- [ ] Trois couches présentes : action principale, accompagnement, deux boucles de fond.
- [ ] Rien de la liste « anti-motion IA » : arc-en-ciel, lueurs, particules gratuites, rebonds partout, retournements 3D sans raison, zoom avant sur chaque plan.

**Cadre**
- [ ] Texte important dans la zone utile, hors zones d'interface ; lisible à 360 px de large.
- [ ] Après chaque geste de caméra, le sujet est dans la zone sûre et le cadre n'est pas vide.

**Sécurité**
- [ ] Jamais plus de 3 éclairs ou changements brusques de couleur ou de luminance par seconde sur plus d'un quart de l'image (compter sur les images extraites, à 30 i/s : au moins 10 images entre deux éclairs).

**Technique**
- [ ] Rendu reproductible : aucun aléatoire sans graine, aucune horloge, aucune répétition infinie.
- [ ] Aucun élément n'est animé sur la même propriété par deux timelines ; les éléments animés plusieurs fois utilisent `fromTo`.
- [ ] Chaque bruitage d'impact a son attaque sur l'image de l'impact (+8 ms visés, jamais avant) ; seuls les souffles et les montées commencent avant (skill `son`).
- [ ] La ligne de licence d'origine est présente partout où du code ou des valeurs du dictionnaire ont été repris.

**Test final** : montre le film sans le son à un relecteur qui ne l'a pas fabriqué. S'il résume le message en une phrase, le mouvement fait son travail. Sinon, retire du mouvement avant d'en ajouter.

## Crédits

Ce skill adapte des sources libres (MIT) : Motion Prompt (Shohei Ohtaki), motion-design-skill (LottieFiles), claude-remotion-skill (haidrrrry, règles seulement), gsap-skills (GreenSock), claude-motion (whaleyxbt), claude-motion-design (Howseen AI), huashu-art-motion (alchaincyf), product-launch-motion (Abubakr Chan). Détail, commits et textes de licence : `licenses/principes-mouvement.md` à la racine du plugin.
