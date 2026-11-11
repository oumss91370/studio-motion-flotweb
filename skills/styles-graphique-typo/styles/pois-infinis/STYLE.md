# Pois infinis (style Kusama)

## 1. Identité

- **Nom** : Pois infinis. « Style Kusama » désigne une inspiration : l'art contemporain à pois et les salles de miroirs « à l'infini ». Ce n'est ni une œuvre de cette artiste, ni un produit officiel ou affilié.
- **Inspiration** : tout est recouvert de pois, les objets comme les murs, jusqu'à ce que le sujet se fonde dans son décor ; des lumières répétées à l'infini dans des miroirs. On reprend l'idée (le pois comme matière unique, la répétition) ; **on ne reproduit aucune œuvre** (pas de citrouille jaune à pois noirs, pas de copie d'une installation existante) et on ne nomme pas l'artiste dans la vidéo.
- **Ce qui le fait reconnaître** : **des pois partout**, sur une grille en nid d'abeilles un peu irrégulière ; deux ou trois couleurs très franches ; des pois qui **gonflent et dégonflent en ondes** parties d'un point ; un sujet qui a presque le même motif que le fond.
- **Marche pour** : visuel hypnotique, boucle de fond, ouverture ou fin de clip, mode, musique, exposition, message court sur une image très forte, transition entre deux parties.
- **Ne marche pas pour** : explication, lecture de texte, produit à détailler, sujet calme et sérieux. Le style fatigue vite l'œil : **15 s au plus** sans pause. Usage prudent en commercial (artiste vivante) : garder le nom descriptif « Pois infinis ».

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Fond principal | rouge `#d81f26` |
| Pois | blanc `#ffffff` |
| Second couple | jaune `#f6c915` et noir `#111111` |
| Contour du sujet | noir, 4,5 px (6 px en 1080×1920) |
| Lumières de la salle de miroirs | 6 couleurs vives sur fond noir |

(La source ne donne pas de codes de couleur : valeurs d'exemple.) Un couple fond/pois par plan ; l'inversion du couple (pois rouges sur blanc) sert à détacher une zone.

- **Pois** : jamais des cercles parfaits : de légères ellipses avec un angle au hasard, comme peints à la main. Deux grilles en nid d'abeilles superposées : de **gros pois** (rayon 30 px, pas de 104 px) et de **petits pois** (rayon 10 px, décalés), chacune avec un décalage au hasard de 25 à 50 % (avec une graine).
- **Sol en perspective** : 9 rangées de pois, plus grands (de 6 à 28 px) et plus espacés en s'approchant, écrasés en ellipses (rapport 0,42).
- **Police** : une grotesque très grasse et ronde (Poppins 800, libre), en blanc, posée dans un grand pois ou un bandeau plein.
- **Police de repli** : aucune à prévoir, Poppins est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/poppins` (vérifié par `npm view` le 11/11/2026).
- **Matières** : aucune texture. La matière, c'est le pois.

## 3. Composition 9:16

- Le motif couvre tout le cadre. Le sujet (personnage, objet, mot) est au centre, entre y 450 et y 1350.
- **Le risque du style est sa signature** : le sujet a le même motif que le mur et se dissout. Pour le garder lisible : **contour noir épais** autour du sujet, et une zone du sujet **sans pois** ou au couple inversé.
- Le **point d'origine des ondes** est un vrai choix de mise en scène : le placer sur ce que l'on veut que le spectateur regarde.
- **Texte** : un mot ou un chiffre, lettres de 160 à 260 px, dans un pois géant (rayon 300 à 400 px) ou sur un bandeau plein sans pois, entre y 250 et y 700. Jamais de texte directement sur le motif. Sous-titres : bandeau noir plein, texte blanc de 50 px, entre y 1400 et y 1540.
- **Salle de miroirs** (variante sombre) : sur fond noir, une grille régulière de petites lumières en profondeur qui vient vers la caméra. En vertical, grille de 7 colonnes sur 13 rangées et 3 plans de profondeur.

## 4. Ce qui bouge

- **Action principale** : **une seule fonction anime tout l'écran**. Le rayon de chaque pois est multiplié par une onde qui part d'un point : `0,82 + 0,28 × sin(distance × 0,012 − 6 × t)`. Toute la pièce respire, anneau après anneau.
- **Boucles de fond** : (1) les pois d'un vêtement ou d'un objet **glissent vers le bas** le long de sa surface (46 px par seconde), découpés par sa silhouette ; (2) dans la salle de miroirs, les lumières avancent vers la caméra en boucle (0,3 unité de profondeur par seconde).
- **Autorisés** : pulsation `#125`, répéteur `#134`, kaléidoscope `#135`, transition par masque `#017` (les pois s'ouvrent sur l'image suivante), zoom à travers `#020`, boucle aller-retour `#127`, plan fixe `#175`, travelling avant lent `#027`.
- **Interdits** : flou de lumières `#105` (voir les pièges), mouvement saccadé, secousse `#024`, glitch `#023`, pois qui se déplacent au hasard, dégradés, caméra à l'épaule `#034`, texte animé lettre par lettre sur le motif.
- Un objet couvert de pois respire tout entier (échelle de ±2,5 %, autour de sa base).

## 5. Rythme et montage

- Lent et continu : plans de 3 à 6 s ; la vitesse de l'onde donne le pouls (environ une vague par seconde).
- Caler une vague sur chaque temps de la musique.
- **Transition signature** : les pois grossissent en anneaux depuis le point d'origine jusqu'à **presque** se toucher, et la nouvelle image apparaît dans les pois.
- **Fin signature, « se dissoudre »** : un voile de couleur monte ; une grande trame de pois (pas de 120 px) gonfle en anneaux jusqu'à 0,47 fois le pas, puis respire doucement 0,15 s. **La dernière image est une trame de pois, jamais une couleur unie.**
- **Version courte (8 à 12 s)** : deux plans : l'onde (4 s), la transition par les pois, puis la fin « se dissoudre » ramenée à 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`. Très léger.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `grille.js` (positions en nid d'abeilles, décalages à graine, calculés une fois), `onde.js`, `motifs.js` (sol, vêtement, objet), `miroirs.js` (projection en perspective).

```js
// positions calculées une fois ; seul le rayon dépend du temps
const onde = (x, y, t, o) => 0.82 + 0.28 * Math.sin(Math.hypot(x - o.x, y - o.y) * 0.012 - 6 * t);
function pois(ctx, grille, t, origine) {
  for (const p of grille) { const r = p.r * onde(p.x, p.y, t, origine);
    ctx.beginPath(); ctx.ellipse(p.x, p.y, r, r * p.aplat, p.angle, 0, 6.2832); ctx.fill(); }
}
// pois qui glissent sur un vêtement : on découpe à la silhouette, on décale en y modulo le pas
ctx.save(); ctx.clip(silhouette); ctx.translate(0, (46 * t) % 52); semis(ctx, 13, 52); ctx.restore();
// fin : le rayon est PLAFONNÉ
const rFin = p => Math.min(0.47 * 120, 120 * 0.47 * avancement(p, t));
```

- **Technique clé** : ne jamais déplacer les pois ; ne faire varier que leur rayon selon la distance au point d'origine. Pour la salle de miroirs : une **grille régulière** de lumières, chacune avec un petit cœur plein et un halo de 3,2 fois son rayon, en mode additif.
- **Pièges** : des lumières placées au hasard avec de gros halos donnent un flou de lumières banal, pas une répétition à l'infini (grille régulière, petits cœurs nets) ; des pois qui grossissent sans plafond finissent en écran blanc ; une fin sans image tenue ne « retombe » pas ; un sujet et un mur au même motif sans contour épais : le sujet disparaît.

## 7. Son

- **Musique** : nappe hypnotique, motif répété (marimba, cloches, synthétiseur doux), pulsation régulière au rythme de l'onde. Peu de changements ; une note qui monte lentement.
- **Bruitages** : très peu : « pop » doux et bulles pour les pois qui gonflent, verre ou cristal pour la salle de miroirs, un souffle long pour la dissolution.
- **Silence** : la musique se retire juste avant la dernière vague, puis une seule note tenue sur la trame finale.
- **Voix** : rare ; une phrase, pas plus.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Des pois sur toutes les grandes surfaces, sur une grille en nid d'abeilles un peu irrégulière.
- [ ] Les pois sont de légères ellipses, pas des cercles parfaits.
- [ ] Deux ou trois couleurs franches ; aucun dégradé.
- [ ] Les rayons varient en ondes depuis un point choisi ; les pois ne se déplacent pas.
- [ ] Le sujet reste lisible (contour épais, zone sans pois ou couple inversé).
- [ ] Aucun texte posé directement sur le motif.
- [ ] La dernière image est une trame de pois tenue, pas une couleur unie.
- [ ] Aucune œuvre existante n'est reproduite ; le nom de l'artiste n'apparaît pas dans la vidéo.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Pas d'aperçu séparé pour ce style. La planche contient des motifs proches de ceux de l'artiste : à donner en lien seulement, jamais comme visuel de vente.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/21_kusama.md` et `scripts/engine/scenes/21_kusama.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔). Police Poppins : OFL 1.1.
- Adaptation Flot Web : traduction du chinois, retrait de la scène, des personnages de la démo et des motifs propres à l'artiste, couleurs d'exemple, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
