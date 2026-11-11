# Fresques de Dunhuang

## 1. Identité

- **Nom** : Fresques de Dunhuang (peintures murales des grottes de la route de la soie).
- **Inspiration** : les peintures murales bouddhiques de l'ouest de la Chine, du Vᵉ au VIIIᵉ siècle : un mur de terre, des couleurs minérales, des figures qui volent à l'horizontale en traînant de longs rubans, des montagnes en dents de scie, et quinze siècles d'usure. On en apprend la grammaire ; on ne recopie ni une figure, ni une scène, ni la composition d'une paroi précise.
- **Ce que c'est** : une image **sèche, ancienne, craquelée**. Fond de terre rouge (ou crème), aplats de pigments minéraux (bleu de pierre, vert de pierre, blanc, or), **trait de fer** brun-rouge d'épaisseur constante. Ce qui vit : **les rubans** qui ondulent, les fleurs qui tombent du ciel, la flamme d'une lampe ; et le mur lui-même, qui s'écaille.
- **Choisis une époque et tiens-la**, sans mélanger :
  - **Période ancienne** (Vᵉ-VIᵉ siècles) : fond rouge uni, animaux d'un seul bloc blanc, montagnes en triangles étroits de couleurs alternées, feuilles en virgule emportées par le vent, figures volantes très horizontales. Plus graphique, plus simple à réussir.
  - **Période classique** (VIIIᵉ siècle) : bordures de rinceaux, nuages, figures plus rondes aux vêtements à bandes, tapis de fleurs de lotus. Plus riche, plus délicate.
- **Marche pour** : histoire et patrimoine, route de la soie, musique et danse, spiritualité, épices et thé, jeu ou récit d'aventure ancien, « ce qui traverse le temps ».
- **Ne marche pas pour** : sujet moderne, humour, interface, texte dense, produit technologique.
- **À ne pas confondre** : pas une miniature persane (pleine, précise, fils d'or) ; pas une fresque italienne (enduit blanc voilé) ; pas une illustration « style chinois » lisse à dégradés. Ici, la matière est **sèche, vieille, fendue**, et la couleur est du minéral.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Terre rouge du mur / plus sombre | `#a5452f` (ou `#92342d`) / `#7a3020` |
| Fond crème (variante) | `#e8dcc5` |
| Vert de pierre | `#3f8f6e`, `#6ab08e` (période ancienne : `#577f7a`) |
| Bleu de pierre | `#2f5f8f`, `#5a86b0` (période ancienne : `#3e919c`) |
| Blanc minéral | `#ecdfc4` |
| Or | `#d8b05a` |
| Trait de fer / trait des visages | `#5a2414` / `#8a3a24` |
| Enduit mis à nu par l'écaillage | `#d8c6a2` |

- **Typographie** : serif classique sobre (**Cormorant Garamond** ou **EB Garamond**, OFL), en blanc minéral ou en trait de fer, dans un **cartouche rectangulaire** peint (bande claire cernée de brun), comme les étiquettes des fresques. Pas de caractères inventés.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond ; EB Garamond : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Mur* : texture de terre (grain, taches), bandeau décoratif en haut (losanges ou rinceaux, triangles pendants de couleurs alternées avec perles d'or), bande de sol en bas.
  - *Trait de fer* : épaisseur **constante** (≈ 2,6 px en 16:9, 3,5 à 4 px en vertical), jamais de pleins et déliés.
  - *Aplats minéraux* un peu inégaux ; vêtements à bandes obliques alternées.
  - *Voile d'usure*, posé **par-dessus** la peinture : décoloration générale (≈ 30 %), couche de poussière claire en multiplication, **écaillage par plaques** (là où un bruit large dépasse un seuil, l'enduit clair apparaît, avec un liseré sombre au bord), ≈ 500 craquelures en marche aléatoire, suie en dégradé dans le haut.

## 3. Composition 9:16

- Le mur remplit le cadre. En vertical, découpe en **registres** : bandeau décoratif (y 160 à 300), ciel où volent les figures (y 300 à 800), scène principale (y 800 à 1380), bande de sol ou cartouche (y 1380 à 1560).
- **Les figures volantes sont horizontales** : tête en avant, corps allongé, rubans vers l'arrière. En vertical, donne-leur toute la largeur (700 à 900 px) et fais-les traverser.
- Montagnes de la période ancienne : rangées de triangles étroits au bas de la scène, le rouge du fond visible entre eux.
- Sujet principal ≥ 1/3 de la hauteur de son registre ; visages petits, yeux et sourcils fins.
- **Zones protégées** : l'écaillage et les craquelures épargnent les visages et le sujet principal ; ils ne touchent que le fond.
- Sous-titres dans le cartouche du bas, 46 à 52 px. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : une figure traverse le ciel (≈ 300 px/s en 16:9) en montant et descendant doucement, ou un animal court (deux temps : envol, regroupement).
- **Boucle de fond 1** : **les rubans** : une onde qui descend le long du tissu ; l'amplitude grandit vers le bout, le dernier tiers se relève. Un ruban part de l'épaule, passe **en grand arc au-dessus de la tête** et retombe derrière : c'est la forme la plus reconnaissable.
- **Boucle de fond 2** : **la pluie de fleurs** (≈ 30 fleurs à quatre pétales qui tournent et se retournent en tombant), les nuages à queue effilée qui dérivent (40 à 76 px/s), les feuilles en virgule emportées vers l'arrière, la flamme d'une lampe (`1 + 0,12·sin(17·t) + 0,08·sin(29·t)`).
- **Le mur vit aussi** : une dizaine d'éclats de peinture se détachent du bord d'une plaque écaillée et tombent en tournant.
- **Autorisés** : `#126` trajet de mouvement (vol), `#131` ruban le long d'un tracé, `#096` flottement, `#015` particules lentes (fleurs, poussière), `#025` panoramique le long du mur, `#027` avancée lente, `#175` plan fixe, `#004` tracé du trait de fer.
- **Interdits** : perspective, ombres portées, dégradés lisses, `#011` écrasement, `#024` secousse, traits d'épaisseur variable, usure sur les visages, néon.
- **Transition signature** : un ruban balaie le cadre ; ou la peinture s'écaille et la scène suivante apparaît dessous.

## 5. Rythme et montage

- Lent et processionnel : plans de 5 à 8 s, un long panoramique le long du mur vaut mieux que des coupes.
- Trois vitesses superposées : rubans (rapides), figures (moyennes), nuages (lents).
- Entrée possible « à la lampe » : mur sombre, la flamme révèle la peinture.
- Musique au tempo d'une danse lente ; un geste par phrase.
- **Version courte (8 à 12 s)** : un seul panoramique de 8 à 10 s le long du mur, avec une figure volante qui traverse ; ramener l'entrée « à la lampe » à 1,5 s. Accroche avant 3 s : la figure entre dans le cadre, ou la flamme révèle un visage.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Ordre des couches** : mur de terre (cache) → registres, bandeaux, triangles pendants (cache) → montagnes (cache) → dynamique : feuilles, figures volantes, fleurs, animaux, poussière → lampe et lueur → **voile d'usure par-dessus** (craquelures, écaillage, sel) → grain de terre en multiplication.
- **Techniques clés** :
  ```js
  // ruban : points en onde, puis bande de largeur variable ; le bout se relève
  const x = dos + 230 * q + 64 * q * Math.sin(4.2 * q - 5.5 * t);
  // écaillage par plaques : bruit LARGE + seuil ; liseré sombre juste sous le seuil
  const n = fbm(x * 0.0032, y * 0.0032) + 0.12 * bruit(x * 0.03, y * 0.03);
  if (n > 0.30 && !zoneProtegee(x, y)) pixel = ENDUIT; else if (n > 0.28) pixel = sombre(pixel);
  ```
- **Pièges** :
  - **Ruban trop timide** (18 à 34 px d'amplitude, presque vertical) : il se lit comme un montant de chaise. Il faut ≥ 200 px de déplacement latéral et le bout relevé.
  - **Bruit d'écaillage trop fin** (fréquence 0,006) : des grains de sésame partout, comme des taches. Fréquence ≈ 0,0032 et seuil plus haut : de vraies plaques.
  - Maquillage de joue trop opaque : une cicatrice. Opacité ≈ 0,3.
  - Auréole en disque plein : une bouée. Disque à ≈ 28 % d'opacité + filet.
  - Une couleur chaude du sujet vire au brun sous le voile de décoloration : pars d'un ton plus vif (`#e08a3a` plutôt que `#c8843a`).
  - Montagnes trop géométriques : il manque les rangées qui se chevauchent.

## 7. Son

- **Musique** : luth en poire, flûte de bambou, cithare, petit tambour sur cadre, grelots ; ou une voix seule très réverbérée. Modes pentatoniques, tempo de danse lente.
- **Ambiance** : grotte : air immobile, écho long, sable et vent dehors.
- **Bruitages** (≈ 3 à 5 par 10 s) : froissement de soie pour un ruban, clochette, grésillement de lampe, petit éclat sec quand la peinture s'écaille, sabots étouffés.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défauts connus des cartes (deux étoiles pour la période classique ; recette de recherche notée ≈ 72/100 pour la période ancienne) : **figures volantes grossières**, torse trop plat, montagnes trop géométriques. Erreurs : époques mélangées ; image lisse et neuve ; rubans raides ; usure sur les visages.

- [ ] Une seule période choisie et tenue.
- [ ] Trait de fer d'épaisseur constante ; aplats minéraux ; aucune ombre portée.
- [ ] Au moins un ruban qui ondule sur plus de 200 px, bout relevé.
- [ ] L'écaillage forme des plaques, avec un liseré sombre ; il épargne visages et sujet.
- [ ] Trois vitesses de mouvement visibles (rubans, figures, nuages ou fleurs).
- [ ] Bandeau décoratif en haut, registres lisibles.
- [ ] Aucune figure ni scène recopiée d'une paroi réelle ; aucun caractère inventé.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 15
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Images fixes possibles avec le moteur d'origine (`render.py --solo 20_dunhuang --stills` ; pour la période ancienne, `--film style_studies --solo 55_dunhuang` ; non exécutés ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/20_dunhuang.md` (période classique, deux étoiles) et `55_dunhuang.md` (période ancienne, recette de recherche v1, non validée par son auteur) ; `scripts/engine/scenes/20_dunhuang.js`, `55_dunhuang.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : deux cartes fusionnées et traduites, section 9:16 en registres, numéros du dictionnaire de mouvements, son. La période ancienne reste à valider par un rendu réel avant d'être vendue.
