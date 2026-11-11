# Enluminure dorée

## 1. Identité

- **Nom** : Enluminure dorée (manuscrit gothique, vers 1290).
- **Inspiration** : les manuscrits enluminés de la fin du XIIIᵉ siècle : parchemin, fond de feuille d'or gravé de losanges, architecture gothique dessinée à plat, grande lettrine, vignes et petites bêtes drôles dans les marges.
- **Ce que c'est** : **une page de livre**. Au centre, une scène dans un cadre d'architecture (arc brisé, pinacles) sur fond d'or ; autour, des marges de parchemin où poussent des tiges ; en bas, quelques lignes d'écriture gothique. L'or **accroche un reflet** qui traverse la page, et des étoiles à quatre branches s'allument sur son passage.
- **Marche pour** : conte, légende, « il était une fois », patrimoine, artisanat d'art, fête religieuse ou traditionnelle, bière d'abbaye, jeu médiéval, citation solennelle, humour décalé (les marges sont faites pour ça).
- **Ne marche pas pour** : sujet technique moderne, données, mouvement rapide, minimalisme.
- **À ne pas confondre** : `periode-doree` est moderne, sensuel, avec un visage réaliste ; ici tout est plat, cerné, médiéval.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Parchemin | `#ecdfc2` |
| Or sombre / or / or clair | `#9c6a1a` / `#d9a63a` / `#f8de86` |
| Bleu d'outremer, rouge vermillon | `#2b4a9a`, `#c0392b` |
| Vert, rose | `#3f7d4f`, `#e3a8a0` |
| Encre du trait et du texte | brun-noir `#2a1c12` |
| Rubriques (premiers mots) | vermillon |

- **Typographie** (OFL) : écriture gothique **UnifrakturMaguntia** pour 1 à 3 lignes décoratives courtes (≈ 44 px en 16:9, 50 à 56 px en vertical ; plus grand, le texte sort de la page). **Illisible pour un public francophone d'aujourd'hui au-delà de quelques mots** : les vraies informations vont dans une serif claire (**EB Garamond**) sur un bandeau de parchemin. Premiers mots en vermillon, lettrine dorée.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place d'UnifrakturMaguntia ; EB Garamond : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/unifrakturmaguntia` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Feuille d'or* : calculée pixel par pixel : bruit large + **stries de polissage horizontales** (bruit 20 fois plus serré en vertical qu'en horizontal) + lumière venant d'en haut à gauche + grain ±5 %, entre les trois ors.
  - *Losanges gravés* : pas de 46 px, deux familles de diagonales ; chaque ligne tracée deux fois (une sombre, une claire décalée de 1,2 px) pour paraître creusée ; 4 points poinçonnés au cœur de chaque losange.
  - *Jointures* : un trait très pâle tous les ≈ 120 px (les feuilles d'or posées une à une).
  - *Personnages* : aplats cernés d'encre, draperies à fines rayures d'or, auréoles ou couronnes à points poinçonnés, visages simples aux yeux en amande.

## 3. Composition 9:16

- La page verticale est le format **naturel** du manuscrit. Découpe : marge haute (y 160 à 300), **cadre d'architecture doré** (y 300 à 1180, x 120 à 860), bloc de texte (y 1220 à 1540), marges latérales de parchemin où courent les tiges (gauche 0 à 120 ; à droite, garde les tiges décoratives entre x 860 et 1080, rien d'important).
- Scène : un ou deux personnages plats sous l'arc, ≥ 1/3 de la hauteur du cadre doré.
- **Lettrine** : en haut à gauche du bloc de texte, 160 à 220 px, dorée.
- **Drôleries** dans les marges : un escargot, une souris, un petit chevalier ; minuscules (60 à 110 px), elles portent l'humour.
- Sous-titres : serif claire brun-noir 44 à 50 px sur le parchemin du bloc de texte. 16:9 : scène à gauche, texte à droite, comme une double page.

## 4. Ce qui bouge

- **Action principale** : un geste simple des personnages plats (lever une coupe, bénir, tendre un objet), par rotation des membres.
- **Boucle de fond 1** : **le reflet sur l'or** : une bande claire oblique (pente ≈ 0,45) traverse la page **à vitesse constante** ; elle n'éclaire **que ce qui est doré** ; sur son passage, des étoiles à quatre branches s'allument en des points fixes.
- **Boucle de fond 2** : **les marges vivent** : les tiges ondulent (`sin(t·2,1 + i·0,09)`), les feuilles de lierre pivotent sur leur attache (±0,28 à ±0,42 rad), l'escargot avance (≈ 60 px/s), une souris traverse en courant, le vitrail scintille (points blancs qui s'allument).
- **Autorisés** : `#022` balayage de lumière (sur l'or), `#004` tracé de ligne (tiges qui poussent, lettres qui s'écrivent), `#140` page tournée, `#027` avancée lente, `#175` plan fixe, `#096` flottement, `#127` va-et-vient (pendule).
- **Interdits** : perspective, ombres portées réalistes, `#016` parallaxe profonde, `#024` secousse, dégradés modernes, texte gothique long.
- **Transition signature** : la page de parchemin **se tourne**.

## 5. Rythme et montage

- Posé : plans de 5 à 8 s ; une page = un plan. Le reflet passe une fois par page, calé sur un temps fort.
- Les drôleries donnent le tempo comique : une par plan, à contretemps.
- Transition : page tournée (≈ 0,6 s) avec son de parchemin.
- **Version courte (8 à 12 s)** : une seule page : la lettrine se trace, le reflet passe sur l'or avant 3 s, une ligne de texte ; pas de page tournée.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; très léger (≈ 12 ms par image) une fois la page mise en cache.
- **Chaîne de rendu** :
  1. Calque fixe en cache : parchemin → or → losanges → architecture → vitrail → mobilier → bloc de texte → drôleries fixes.
  2. **Masque d'or automatique**, calculé une fois sur le calque fixe : pour chaque pixel, une mesure de « dorure » sert d'opacité.
  3. À chaque image : scintillement du vitrail → reflet → étoiles → tiges et feuilles → drôleries animées → personnages → grain.
- **Techniques clés** :
  ```js
  // « dorure » d'un pixel : pas besoin de redessiner les formes dorées pour le masque
  const or = clamp((r - b - 70) / 50) * clamp((g - b - 30) / 40) * clamp((r - 140) / 40);
  // reflet : bande en dégradé, limitée au masque d'or, ajoutée en clair
  bande.globalCompositeOperation = "destination-in"; bande.drawImage(MASQUE_OR, 0, 0);
  ctx.globalCompositeOperation = "lighter"; ctx.globalAlpha = 0.85; ctx.drawImage(bande.canvas, 0, 0);
  const x = lerp(xDebut, xFin, (t - t0) / duree);          // vitesse CONSTANTE
  ```
  - Le parchemin (rouge − bleu ≈ 42) et le rose (bleu élevé) sont exclus du masque d'eux-mêmes.
- **Pièges** :
  - Reflet avec accélération et freinage : il a quitté la zone dorée avant de croiser le personnage. Vitesse constante.
  - Feuilles des tiges trop petites et rares : la marge paraît vide. Échelle 1,05 à 1,45.
  - Un rig de personnage moderne impose ses accessoires (une tasse à anse) : dessine les pièces toi-même, dans l'ordre auréole → cheveux → robe → manteau → tête → objet.
  - Mesurer le mouvement en prenant la toute première image comme référence fausse le résultat si une transition d'entrée est en cours.

## 7. Son

- **Ambiance** : scriptorium : pierre, écho long, plume, feu lointain.
- **Musique** : voix a cappella en bourdon, vièle, harpe, flûte, petit tambour ; ou un chœur très doux.
- **Bruitages** (≈ 5 par 10 s) : carillon fin au passage du reflet, plume qui gratte, parchemin qui se tourne, petits pas de souris, clochette.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (trois étoiles) : coiffure lue comme une capuche ; simplifie les silhouettes. Erreurs : or plat et jaune ; perspective ; texte gothique long ; marges vides ; reflet sur le parchemin.

- [ ] L'or a des stries horizontales, des losanges gravés et des jointures.
- [ ] Le reflet n'éclaire que l'or et avance à vitesse constante.
- [ ] Des étoiles s'allument au passage du reflet.
- [ ] Les marges contiennent des tiges qui bougent et au moins une drôlerie.
- [ ] Aucune perspective, aucun dégradé moderne ; tout est cerné d'encre.
- [ ] Trois lignes gothiques au plus ; l'information utile est en serif lisible.
- [ ] Mise en page de livre respectée ; rien d'important sous y = 1560 ni à droite de x = 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 05_gothic --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/05_gothic.md` (trois étoiles), `scripts/engine/scenes/05_gothic.js`. Licence MIT, © 花叔 Huashu. Les polices du dépôt sont sous OFL : à reprendre depuis leur source d'origine, avec leur licence.
- Adaptation Flot Web : carte traduite et généralisée, mise en page verticale, règle de lisibilité du texte gothique, valeurs hex des pigments proposées par Flot Web quand la carte ne donnait que des noms. Son.
