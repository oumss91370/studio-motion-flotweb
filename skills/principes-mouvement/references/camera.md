# Caméra : vocabulaire, usages et valeurs

La caméra est une **ponctuation**. Elle sert à dire « regarde ici », « voici où nous sommes », « ça y est ». Si elle bouge sur chaque plan, elle ne dit plus rien — et la vidéo ressemble à un diaporama qui zoome.

Sommaire : 1. trois questions avant de bouger — 2. vocabulaire français — 3. valeurs typiques — 4. dosage — 5. images fixes plein cadre — 6. fabriquer la caméra en HyperFrames — 7. caméra dans Blender — 8. spécificités du 9:16 — 9. contrôle.

Les numéros (#027…) renvoient au `dictionnaire-mouvements.md`.

---

## 1. Trois questions avant de bouger la caméra

1. **Que doit regarder le spectateur maintenant, et le voit-il bien à cette distance ?** S'il le voit, on ne bouge pas. Si l'image bouge déjà toute seule (vidéo réelle, courbe qui se trace, liquide qui coule, texte en cours de lecture), on bouge encore moins : la caméra volerait la vedette.
2. **Est-ce une liaison ou un accent ?** Emmener le regard vers le détail suivant, situer, installer une émotion : c'est une **liaison**, lente. Révélation, retournement, chiffre clé, chute d'une blague : c'est un **accent**, rapide — et rare.
3. **Qu'a fait le plan précédent ?** Après une avancée, cherche un recul ou un déplacement latéral. Le même geste trois fois de suite, et le spectateur entend un métronome.

---

## 2. Vocabulaire français

### Mouvements

| Terme français | Terme d'origine | Ce que c'est | Pourquoi l'utiliser | # |
|---|---|---|---|---|
| **Plan fixe** | Locked-off | La caméra ne bouge pas | Laisser lire, laisser l'action jouer, silence après une chute | 175 |
| **Avancée lente** (travelling avant) | Dolly in, push | La caméra s'approche ; le premier plan grossit plus vite que le fond | Emmener vers un détail, faire monter l'émotion d'un cran | 027 |
| **Avancée rapide** (coup de zoom) | Punch | Approche brève et sèche, puis arrêt | Accent : révélation, chiffre clé | 028 |
| **Recul** (travelling arrière) | Pull, dolly out | La caméra s'éloigne | Revenir à l'ensemble, situer, conclure une partie, finir | 027 inversé, 183 |
| **Zoom** | Zoom in / out | La caméra ne bouge pas, toute l'image grossit du même rapport (pas de parallaxe) | Désigner un point de façon plate, « observateur » | 028 |
| **Travelling latéral** (glissement) | Glide, tracking | La caméra se déplace de côté | Passer d'un élément au suivant sur un même mur, suivre un sujet | 029 |
| **Panoramique** | Pan | La caméra pivote sur place, gauche-droite | Révéler un lieu large, déplacer l'attention | 025 |
| **Panoramique vertical** | Tilt | La caméra pivote sur place, haut-bas | Montrer une hauteur — naturel en 9:16 | 026 |
| **Panoramique filé** | Whip pan | Pivot très rapide avec flou, la scène change dedans | Changer de lieu ou de sujet avec énergie | 043 |
| **Translation verticale** | Pedestal | Toute la caméra monte ou descend sans s'incliner | Parcourir de bas en haut — le geste roi du vertical | 169 |
| **Grue** | Crane up | La caméra monte en s'inclinant vers le bas | Quitter une scène, révéler l'échelle | 031 |
| **Travelling circulaire** | Orbit, arc | La caméra tourne autour du sujet | Montrer un objet en volume (3D) | 030 |
| **Travelling compensé** | Dolly zoom | Recul + zoom avant : le sujet ne change pas, le fond se resserre | Prise de conscience, malaise — une fois au plus | 032 |
| **Traversée** | Fly-through | La caméra passe par une ouverture | Entrer dans un lieu, passer d'un monde à l'autre | 176, 020 |
| **Plan de suivi** | Follow shot | La caméra suit le sujet de dos | Entrer quelque part avec un personnage | 174 |
| **Caméra à l'épaule** | Handheld | Léger tremblement irrégulier | Effet documentaire, présence | 034 |
| **Stabilisateur** | Steadicam | Glissement fluide avec lent balancement | Déplacement élégant | 173 |
| **Dérive lente** | Drift | Avancée ou glissement presque imperceptible et continu | Plan d'ambiance, image d'art « toujours vivante » | — |
| **Impact** (plaqué) | Slam | Un élément ou l'image s'écrase en place avec un léger dépassement | Gros titre, chiffre, tampon | 024 |
| **Secousse** | Shake | Tremblement amorti de tout le cadre | Accompagner un impact | 024 |
| **Bascule de point** | Rack focus | Le net passe d'un plan à un autre | Déplacer l'attention sans bouger ni couper | 033 |

### Angles et cadres

| Terme français | Terme d'origine | Effet | # |
|---|---|---|---|
| **Plongée** | High angle | Caméra en hauteur qui regarde vers le bas : le sujet paraît petit, on comprend la situation | 178 |
| **Contre-plongée** | Low angle | Caméra basse qui regarde vers le haut : puissance, hauteur | 177 |
| **Vue zénithale** | Bird's-eye | À la verticale : plan, trajets, disposition | 181 |
| **Cadre penché** | Dutch angle | Horizon en diagonale : tension, malaise | 036 |
| **Caméra subjective** | POV | Par les yeux du personnage | 179 |
| **Par-dessus l'épaule** | Over-the-shoulder | Un personnage en amorce floue, l'autre net | 180 |
| **Plan d'ensemble** | Establishing shot | Vue large qui situe | 183 |
| **Plan moyen**, **gros plan**, **très gros plan** | Medium, close-up, extreme close-up | De la silhouette au détail ; le très gros plan est un pic d'émotion | 184 |
| **Insert** | Insert shot | Très gros plan d'un détail de la scène, puis retour | 185 |

### Raccords (changer de plan)

| Terme français | Terme d'origine | Usage | # |
|---|---|---|---|
| **Coupe franche** | Cut | Le raccord par défaut : 0 image | — |
| **Saut de valeur** | Punch-in cut | Coupe vers un cadre plus serré du même sujet : réaction, chute comique | — |
| **Coupe sautée** | Jump cut | Même cadre, on saute dans le temps : resserrer, accélérer | 041 |
| **Raccord de forme** | Match cut | Deux scènes reliées par une forme ou un geste | 042 |
| **Coupe choc** | Smash cut | Contraste brutal calme / intense | 046 |
| **Fondu enchaîné** | Cross dissolve | Temps qui passe, souvenir | 044 |
| **Fondu au noir** | Fade to black | Fin de chapitre, fin | 187 |
| **Volet** | Wipe | Changement net, comparaison | 045 |
| **Fermeture à l'iris** | Iris out | Fin façon dessin animé | 188 |
| **Plan de coupe** | Cutaway | Montrer une réaction, cacher une ellipse | 189 |
| **Montage alterné** | Cross-cutting | Deux actions simultanées, tension | 190 |
| **Montage en J / en L** | J-cut / L-cut | Le son précède ou prolonge l'image | 047, 048 |

---

## 3. Valeurs typiques

Ce sont des points de départ mesurés sur des films jugés réussis, pas des quotas.

| Geste | Durée | Amplitude | Courbe (GSAP) | Remarque |
|---|---|---|---|---|
| Plan fixe | aussi longtemps que la voix le demande | — | — | Le geste le plus utilisé |
| Avancée lente | 0,6 à 1,5 s (jusqu'à 2 s si l'on double l'échelle) | 10 à 40 % : jusqu'à ce que la cible soit lisible | `sine.inOut` ou `power2.inOut` | La liaison par défaut |
| Recul | 0,8 à 2 s | retour à l'ensemble | départ vif, longue fin : `expo.out` ou `power3.out` | Ferme une partie |
| Travelling latéral | 0,5 à 0,9 s ; 1,3 à 1,8 s pour suivre un tracé | d'un élément au suivant | `sine.inOut` | Suit la vitesse de l'objet s'il y en a un |
| Avancée rapide | 0,25 à 0,35 s | 18 à 32 %, puis arrêt | `power3.out` | Accent ; variante : 6 images d'avancée + 2 images de retour |
| Panoramique filé | 0,26 à 0,30 s (0,8 s pour un raccord complet, #043) | — | `expo.inOut`, avec flou de mouvement | Regard qui saute, rythme comique |
| Impact | 0,17 s | échelle 1,55 → 0,94 → 1,0 | — | **Une fois par plan au plus** ; pas à chaque coupe |
| Coupe franche, saut de valeur | 0 image | — | — | La chute se joue à la coupe |
| Dérive lente | continue | 1 à 4 % par seconde | linéaire | Ambiance seulement ; **interdite sur chaque plan d'un film explicatif** |
| Panoramique, translation verticale, grue | ≈ 2,9 s en démonstration | — | `power2.inOut` | À raccourcir à 1 à 1,5 s dans un court |
| Travelling circulaire | ≈ 3 s | ≈ 100° | `power2.inOut` | 3D seulement |
| Bascule de point | 0,35 à 0,45 s (1,6 s en version contemplative) | flou 2,6 px + opacité 0,55 sur le plan abandonné | `power2.inOut` | |
| Pulsation sur le temps musical | — | +1,2 % par temps, +3 % par mesure après le temps fort, retombée exponentielle | — | Films calés sur la musique |

Règles liées :

- **Le zoom s'interpole en logarithme** (rapport constant), sinon il paraît accélérer puis traîner : anime l'exposant (`échelle = début × (fin / début) ^ p`) plutôt que l'échelle elle-même pour un grand écart.
- **Jamais deux gestes opposés collés** (avancée puis recul immédiat sans maintien entre les deux).
- **La caméra a un amortissement de 1** : pas de rebond de caméra, sauf l'impact.
- Pour **arriver** sur un temps musical, lance le mouvement environ 0,3 s avant.
- **Avance avant l'action, immobile pendant, relâche après** : une caméra encore en mouvement pendant un clic ou une révélation vole l'instant.

---

## 4. Dosage

**Principe** : les gestes d'accent sont comme le gras dans un texte. Tout en gras, plus rien n'est important. Et une avancée appelle un retour.

| Type de vidéo | Règle |
|---|---|
| Explicatif, vulgarisation, finance, tableau blanc | Accents (avancée rapide + impact + filé) sur **moins d'un tiers des plans** ; jamais trois avancées de suite ; au-delà de 8 avancées par minute, on revoit le film à vitesse normale |
| Accroche (3 premières secondes) | Densité libre ; retour au rythme normal ensuite |
| Typographie cinétique, passage calé sur la musique | Le nombre d'accents suit le rythme et les mots forts |
| Histoire, comédie | Surtout plan fixe + coupe franche + saut de valeur ; très peu d'avancées |
| Clip, film d'émotion | Couplet : avancée lente, dérive ; refrain : on accélère ; pont : recul ; le pic des transitions tombe sur les temps |
| Parcours d'images d'art | La dérive lente peut durer ; ce qui compte : une action principale et deux boucles de fond par plan |
| Démonstration d'écran, tutoriel | Capture plein cadre ; avancée lente seulement vers la zone qu'on ne lit pas ; une à deux fois par image ; puis recul ou glissement |
| Graphique animé | Pendant que la courbe pousse, **plan fixe** ; avancée lente sur une donnée citée ; avancée rapide pour les une ou deux valeurs clés du film |
| Enquête, « table de documents » | Une grande toile ; le travelling latéral entre les pièces est le geste principal ; à l'arrêt, la pièce occupe 80 à 90 % du cadre |

**Contre-exemple à garder en tête** : un court vertical de 102 s et 44 plans, avec environ 48 avancées (une toutes les 2 secondes), toutes vers l'intérieur, de 10 à 26 % en 0,28 s, presque aucun recul ni glissement. Verdict de son auteur : beaucoup trop de zooms avant, trop rapides, rien de fluide.

---

## 5. Images fixes ou vidéos plein cadre : le piège

Avec une photo ou une vidéo qui remplit le cadre, la seule chose que la caméra sait faire est d'avancer. Le film devient « une image, un zoom, une image, un zoom ».

- **La vidéo réelle bouge déjà : plan fixe.**
- **Une ou deux avancées par image au plus**, et seulement quand la zone est illisible en plan large. Avancer à chaque nom prononcé, c'est battre la mesure de la voix.
- **Change la façon d'entrer** : partir d'un détail et reculer ; arriver par le côté ; couper franc à la même valeur de plan.
- **Plusieurs documents à enchaîner : pose-les sur une même toile** et glisse de l'un à l'autre. Avancées et glissements alternent d'eux-mêmes.
- **Une coupe ne remet pas le compteur à zéro** : si chaque plan repart de l'échelle 1 pour avancer, on empile les zooms.
- **Image horizontale dans un cadre vertical : recadre d'abord.** Une image 16:9 posée entière dans du 9:16 ne laisse qu'une bande au milieu. Recadre en vertical sur la partie dont on parle ; l'image entière ne sert qu'au recul final.

---

## 6. Fabriquer la caméra en HyperFrames (2D)

Il n'y a pas de vraie caméra : on transforme **un conteneur qui contient toute la scène**.

### Structure

```html
<div id="cadre">            <!-- 1080 × 1920, overflow: hidden -->
  <div id="monde">          <!-- tout ce que la caméra regarde -->
    …
  </div>
  <div id="habillage">      <!-- sous-titres, logo : ne bougent pas avec la caméra -->
  </div>
</div>
```

```js
// Avancée lente vers un point (cx, cy) de la scène, sur l'étiquette "detail"
gsap.set("#monde", { transformOrigin: `${cx}px ${cy}px` });
tl.to("#monde", { scale: 1.25, duration: 1.0, ease: "sine.inOut" }, "detail");

// Recul : départ vif, longue fin
tl.to("#monde", { scale: 1, duration: 1.2, ease: "expo.out" }, "ensemble");
```

### Règles de fabrication

- **Tout ce que la caméra déplace est dans `#monde`** ; ce qui doit rester fixe (sous-titres, marque) est en dehors.
- **Point fixe** : place l'origine du zoom exactement sur l'élément visé. Il ne bouge pas pendant l'avancée, tout le reste grandit autour : le curseur, les ondes et les repères déjà calculés restent justes.
- **Deux nœuds pour deux gestes.** Ne mets jamais sur le même élément une rotation qui dure tout le plan et un zoom ponctuel : deux tweens sur la même transformation se battent. Conteneur extérieur = avancée et recul ; conteneur intérieur = rotation.
- **Légère rotation 3D pour sortir de l'aplat** (écran, carte, document) : `transformPerspective` 2200 à 2800 ; `rotationY` de −6 à −10° vers −1 à −2° sur toute la durée du plan (ne jamais finir à 0 pile) ; `rotationX` de 2° vers 0,5° ; `power1.inOut`. Le spectateur lit une caméra qui se pose, pas un objet qui tourne.
- **Profondeur sans moteur 3D** : avec `transform-style: preserve-3d`, donne 12 à 22 px de `z` aux éléments dont parle l'histoire.
- **Parallaxe** : deux plans, un mouvement lent chacun sur toute la durée du plan, en sens opposés (par exemple proche `x: 12 → −6`, lointain `x: −7 → 5`). Pas de dérive élément par élément : c'est l'effet économiseur d'écran. Facteurs de profondeur : premier plan ×1, moyen ×0,5, fond ×0,2.
- **Bascule de point** : flou et opacité réduite sur le plan qu'on abandonne. Donne un `filter: blur(0px)` explicite en CSS, sinon la première image saute.
- **Budget de cadre** : un zoom fait grandir la scène vers les bords. Avant de choisir l'échelle, calcule où arrive chaque bord : `bord_après = bord + (bord − origine) × (échelle − 1)`, et vérifie les zones d'interface (haut 160 px, bas 360 px, droite 135 px).
- **Un cadre vide est une faute** : après chaque geste, le sujet remplit l'image.
- **Texte net** : pas de `will-change` sur ce que la caméra agrandit ; prévois les images à la résolution de leur plus forte échelle.
- **Secousse** : somme de sinus amortie calculée à partir du temps (voir #024), jamais d'aléatoire sans graine.
- **Flou de mouvement** : seulement sur un à trois gestes rapides du film (filé, grande traversée) ; jamais à travers une coupe franche.

---

## 7. Caméra dans Blender (3D et 2.5D)

Quand la scène est en 3D, la caméra est réelle : préfère les vrais gestes aux zooms.

- **Avancée = déplacement de la caméra**, pas changement de focale : c'est la parallaxe entre premier plan et fond qui donne la profondeur (#027 contre #028).
- Place **un objet de premier plan** (bord de table, feuillage, montant) : sans lui, un travelling ressemble à un zoom.
- **Une caméra qui traverse l'objet vaut dix orbites** : le travelling circulaire est un geste de présentation, pas de récit.
- Courbes d'animation en Bézier avec accélération et ralenti (jamais linéaires), sauf pour une dérive ou un accompagnement à vitesse constante.
- Focales : large pour situer (plan d'ensemble), longue pour isoler (gros plan, fond flou). Le travelling compensé (#032) se fait en animant position et focale en sens inverse.
- Mêmes règles de dosage que plus haut : la 3D n'excuse pas une caméra qui tourne sans arrêt.
- Les plans rendus dans Blender sont assemblés dans HyperFrames : les gestes d'accent 2D (impact, secousse légère, avancée rapide sur l'image rendue) restent possibles au montage.

---

## 8. Spécificités du 9:16

- **L'axe naturel est vertical** : translation verticale (#169), panoramique vertical (#026), grue (#031), contre-plongée (#177) fonctionnent mieux qu'en horizontal. Le panoramique horizontal balaie peu de champ : préfère le travelling latéral entre deux éléments, ou la coupe.
- **Sujet au centre**, dans le carré 1080 × 1080 ; ne cadre rien d'important dans les zones d'interface.
- **Les filés horizontaux** (#043) sont courts (la largeur n'est que de 1080 px) : 6 à 9 images suffisent.
- **L'orbite** réduit le sujet en largeur : garde une marge, ou limite l'angle.
- **Avancée sur un texte** : vérifie le budget de cadre, un titre large sort vite des 1080 px.
- **Très gros plans** efficaces : l'écran du téléphone est petit, un détail plein cadre se lit mieux qu'un plan large chargé.

---

## 9. Contrôle

Au découpage :

- pas trois plans de suite avec le même geste (le plan fixe ne compte pas) ;
- pas trois avancées de suite ;
- accents sur moins d'un tiers des plans (hors accroche et passages musicaux) ;
- au moins un geste dans le film (un découpage sans aucun mouvement de cadre est un diaporama).

Sur le film rendu :

- **regarde le film entier à vitesse normale**, au moins les 30 secondes les plus denses : une planche d'images fixes montre la composition, jamais le rythme de la caméra ;
- chaque geste a une raison que tu peux dire en une phrase (« on avance parce que le prix devient lisible ») ;
- après chaque geste, le sujet est dans la zone sûre et le cadre n'est pas vide.

---

## Sources

- Table des gestes, durées mesurées, dosage par type de film, piège des images plein cadre, contrôles : **alchaincyf/huashu-art-motion** (MIT, © 2026 alchaincyf, commit `1468196`), référence « langage de la caméra ».
- Caméra à deux nœuds, point fixe, rotation 3D légère, profondeur, bascule de point, parallaxe, budget de cadre : **AbubakrChan/product-launch-motion** (MIT, © 2026 Abubakr Chan, commit `edbfb10`), référence caméra.
- Zoom en logarithme, pulsation sur le temps, flou ciblé : **howseen-ai/claude-motion-design** (MIT, commit `3d90d34`). « Une caméra qui traverse l'objet » : **whaleyxbt/claude-motion** (MIT, commit `6f80380`).
- Noms et numéros des gestes : **showheyohtaki/motion-prompt** (MIT, © 2026 Shohei Ohtaki, commit `7819d38`).
