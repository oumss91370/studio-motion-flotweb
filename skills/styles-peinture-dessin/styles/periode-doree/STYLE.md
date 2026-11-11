# Période dorée (style Klimt)

## 1. Identité

- **Nom** : Période dorée (style Klimt, Vienne vers 1907). Inspiration seulement : aucune toile recopiée, jamais présenté comme officiel.
- **Inspiration** : la peinture à la feuille d'or du début du XXᵉ siècle : un fond d'or mat et tacheté, des vêtements couverts de motifs plats (spirales, cercles, yeux, carrés noirs et blancs), et au milieu un **visage et des mains peints de façon réaliste**.
- **Ce que c'est** : un **contraste** : décor et vêtement = ornement plat et doré ; chair = volume doux, presque sans contour. C'est ce contraste qui fait le style ; sans lui, on obtient du papier cadeau.
- **Marche pour** : bijouterie, parfum, cosmétique, mariage, fêtes de fin d'année, annonce d'un prix, portrait de fondatrice, édition limitée.
- **Ne marche pas pour** : sujet technique, humour, texte dense, marque « simple et pas chère », enfant.
- **À ne pas confondre** : `enluminure-doree` est une page de manuscrit médiéval (parchemin, vignes, lettres gothiques) ; l'affiche Art nouveau (catégorie « Papier et impression ») est en trait et en aplats pastel, sans or épais.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Or sombre → or → or clair | `#784e12` → `#c49434` → `#f6d880` |
| Chair : lumière → base → ombre → bord | `#fbe8da` → `#f0cfb8` → `#d8a88c` → `#b88068` |
| Motifs : cercles concentriques | rouge `#b8322a`, blanc `#f6efe0`, bleu `#2f4f9a`, violet `#6a3b8a`, or |
| Motifs : spirales | or sur brun profond `#3a2412` |
| Carrés du bas de vêtement | noir `#141210` et blanc, cernés d'or |

- **Typographie** : capitales élégantes à empattements fins (**Cinzel** ou **Marcellus**, OFL), en or clair sur brun profond ou en brun sur or. Interlettrage large.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Cinzel et de Marcellus. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cinzel`, `@fontsource/marcellus` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Feuille d'or* : calculée pixel par pixel à partir d'un bruit large et d'un bruit étiré, entre les trois ors ; **un trait de jointure très pâle tous les ≈ 96 px** (les feuilles collées une à une) ; par-dessus, une tache brune en multiplication et ≈ 9 000 grains de poudre d'or et de poudre sombre.
  - *Motifs du vêtement* : ≈ 150 motifs répartis en quatre familles : cercles concentriques tricolores (30 %), spirales d'or sur brun (32 %), **yeux stylisés** (22 %), grappes de points blancs à cœur rouge (16 %). En bas, ≈ 60 rectangles noirs et blancs cernés d'or. Contour sombre de 3 px autour du vêtement.
  - *Chair* : dégradé radial pour le volume, joues et creux des yeux floutés, contour pâle de 1,2 px seulement.

## 3. Composition 9:16

- Format idéal : une **figure en pied ou en buste** dans une longue forme dorée verticale, sur fond d'or. Le vêtement occupe la colonne centrale (x 180 à 860), le visage dans le tiers haut (y 380 à 760), tête ≥ 240 px.
- Le fond d'or laisse des plages calmes en haut (titre) et en bas (texte).
- Sol éventuel : un tapis de fleurs rondes qui grossissent en descendant (6 à 20 px de rayon).
- Sous-titres : capitales ou serif 46 à 52 px, or clair sur une bande brun profond, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.
- 16:9 : deux figures, ou une figure et un objet, dans une même masse dorée.

## 4. Ce qui bouge

- **Action principale** : un geste lent du visage ou des mains (regard qui se lève, main qui présente l'objet). Le corps ne bouge presque pas : le vêtement est une surface.
- **Boucle de fond 1** : **le vêtement vit** : les spirales tournent (±3 rad/s), les yeux clignent chacun leur tour (fermés quand `sin(2,2·t + φ) > 0,86`).
- **Boucle de fond 2** : **l'or scintille** : ≈ 420 grains qui deviennent des étoiles à quatre branches quand `sin(t·v + φ) > 0,55`, poudre qui monte (≈ 26 px/s), ≈ 34 paillettes de feuille d'or qui tombent en tournant (≈ 150 px/s), fleurs du tapis qui hochent.
- **Reflet** : une bande de lumière oblique (≈ 300 px de large en vertical, opacité 0,24, mode additif) traverse l'image **à vitesse constante** en ≈ 1,2 s, dessinée **avant** le sujet pour qu'il la masque naturellement.
- **Autorisés** : `#022` balayage de lumière (sur l'or seulement), `#015` particules (poudre d'or, lente), `#134` répétition de motifs tournants, `#027` avancée lente, `#184` très gros plan sur un motif, `#175` plan fixe.
- **Interdits** : `#024` secousse, `#043` panoramique filé, `#011` écrasement et étirement, motifs sur le visage ou les mains, contour épais sur la chair, étoiles trop grosses (effet décoration de Noël).
- **Transition signature** : l'or se répand **en spirale** depuis un point (la tête, l'objet) jusqu'à couvrir le cadre.

## 5. Rythme et montage

- Lent et solennel : plans de 5 à 8 s, une avancée continue.
- La bande de reflet passe **une fois par plan**, sur un temps fort ; pas en boucle.
- Sans les paillettes, la poudre et les fleurs, un tiers des images consécutives sont presque identiques (clignements intermittents, reflet trop doux) : garde ces trois mouvements continus.
- **Version courte (8 à 12 s)** : une seule avancée continue de 8 à 10 s ; un motif d'or s'allume avant 3 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Ordre des couches** : mur d'or (en cache) → étoiles de poudre (additif) → lointain éventuel → sol fleuri → mobilier → **bande de reflet** → sujet secondaire → vêtement doré (motifs découpés selon sa silhouette) → visage et mains réalistes → coiffure, objets dorés → vapeur ou poudre au premier plan.
- **Techniques clés** :
  ```js
  // feuille d'or : bruit large + bruit étiré, entre trois ors
  const f = 0.5 + fbm(x * 0.004, y * 0.004) * 0.55 + bruit(x * 0.003, y * 0.08) * 0.5;
  // motifs : dessiner TOUS les motifs sur un calque, puis découper ce calque par la silhouette
  calque.globalCompositeOperation = "source-in";  // une seule fois, sur le calque entier
  // étoile de poudre : rayon r * (0.6 + 1.1 * a), pas plus
  ```
- **Pièges** :
  - Découper **chaque motif** par la silhouette efface les précédents : découpe le calque entier, une fois.
  - Reflet à 0,38 d'opacité = éblouissement d'objectif : reste à 0,24.
  - Reflet avec accélération et freinage : il sort de la zone dorée avant d'avoir croisé le sujet. Vitesse constante.
  - Des spirales d'or sur un visage (ou la tête d'un animal) « ressemblent à une éruption » : motifs sur le corps seulement, et moins nombreux (≈ 46 sur une petite figure).
  - Étoiles trop grandes : décoration de Noël.

## 7. Son

- **Ambiance** : grande pièce feutrée, léger écho.
- **Musique** : valse lente ou cordes de chambre, harpe, célesta ; une montée douce vers le passage du reflet.
- **Bruitages** (≈ 5 par 10 s) : scintillements fins (carillon, verre), froissement de feuille d'or, tintement à chaque clignement groupé, frottement de tissu lourd.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (trois étoiles) : la main mal reliée à la manche ; soigne le raccord chair / vêtement. Erreurs : tout plat (visage compris) ; or uniforme sans jointures ; motifs partout ; images figées.

- [ ] Visage et mains en volume doux, contour ≤ 1,5 px ; vêtement plat, contour 3 px.
- [ ] L'or montre des taches et des jointures de feuilles.
- [ ] Quatre familles de motifs visibles, dont des yeux qui clignent.
- [ ] Aucun motif sur la chair.
- [ ] Le reflet traverse à vitesse constante et passe derrière le sujet.
- [ ] Trois mouvements continus en même temps (paillettes, poudre, fleurs ou spirales).
- [ ] Texte en or clair sur brun, hors y > 1560 et x > 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 13
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 18_klimt --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/18_klimt.md` (trois étoiles), `scripts/engine/scenes/18_klimt.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée, valeurs hex des motifs proposées par Flot Web quand la carte ne donnait que des noms de couleurs, section 9:16, son.
