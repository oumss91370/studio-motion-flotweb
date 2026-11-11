# Dessiner un personnage en pièces SVG

## Dossier

```
personnages/<nom>/
  pieces/        tete.svg  corps.svg  bras-g.svg  bras-d.svg  jambe-g.svg  jambe-d.svg  costume-<nom>.svg
  expressions/   yeux-neutre.svg  yeux-grands.svg  yeux-plisses.svg  yeux-fermes.svg  yeux-regard-cote.svg
                 bouche-fermee.svg  bouche-petite-ouverte.svg  bouche-grande-ouverte.svg  bouche-moue.svg  bouche-sourire.svg
                 extra-goutte.svg  extra-rouge-joues.svg
  png/           les mêmes fichiers exportés en PNG ×2
  fiche.md       couleurs, tailles, pivots, rôle, costume
  planche.png    planche de contrôle
```

## Gabarit commun

Toutes les pièces partagent **le même repère** : même `viewBox`, mêmes unités. Empilées sans déplacement, elles forment le personnage debout, de face.

- `viewBox="0 0 600 1000"`, origine en haut à gauche, pieds posés sur `y = 980`, axe du corps sur `x = 300`.
- Proportions de départ pour un personnage à tête ronde : tête de 300 à 340 de diamètre (environ un tiers de la hauteur), corps de 280 de haut, membres en bâtons épais.
- Fond transparent : aucun rectangle de fond.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 1000">
  <circle cx="300" cy="260" r="160" fill="#F2C9A0" stroke="#1B1410" stroke-width="14"/>
</svg>
```

## Règles de style

- **Aplats** : une couleur par forme. Pas de `linearGradient`, pas de filtre, pas de texture, pas d'ombre dessinée.
- **Un seul poids de contour** pour tout le personnage (12 à 16 unités dans ce gabarit, valeur par défaut), couleur d'encre sombre, `stroke-linejoin="round"` et `stroke-linecap="round"`. **La fiche de style l'emporte sur cette valeur** : si le `STYLE.md` du film donne l'épaisseur du trait (par exemple 3 à 5 px), sa couleur ou sa matière, on dessine les pièces avec ce trait-là, pour que le personnage soit de la même main que le décor.
- Ne pas contourer un bras **sur** le torse : le contour du bras s'arrête là où il rejoint le corps, sinon l'épaule a l'air collée.
- Yeux : deux points ou deux petits ovales. Bouche : un trait ou une forme simple. Le visage doit se lire à 60 px de large.
- 4 à 6 couleurs au total : peau, encre, deux couleurs de costume, un accent. L'accent est une couleur saturée que les décors n'utilisent pas, pour retrouver le personnage dans un plan large.
- Les membres dépassent un peu sous la pièce qui les recouvre (20 à 30 unités), pour qu'une rotation ne montre jamais de trou.

## Pivots

Noter dans `fiche.md` le pivot de chaque pièce, en unités du gabarit. C'est le point autour duquel la pièce tourne.

| Pièce | Pivot | Exemple |
|---|---|---|
| Racine du personnage | entre les pieds, au sol | (300, 980) |
| Corps | bassin | (300, 700) |
| Tête | cou | (300, 420) |
| Bras | épaule | (215, 470) et (385, 470) |
| Jambe | hanche | (265, 700) et (335, 700) |
| Yeux, bouche | centre du visage | (300, 260) |

Hiérarchie : racine → corps → tête → (yeux, bouche, extras, coiffe) ; corps → bras ; racine → jambes.

## Costume selon le rôle et l'époque

Le costume dit qui est le personnage en une forme : une coiffe, un col, un tablier, une cape, un outil. Une pièce par élément, pour pouvoir habiller le même corps autrement (figurants, autre épisode).

Pour une histoire vraie, vérifier le costume avec une source (époque, pays, rang) et le noter dans les sources de l'épisode. Rester simple : une forme juste vaut mieux que dix détails.

## Vues

Le personnage est dessiné de face. Deux variantes suffisent en général :

- **trois quarts** : décaler le visage (yeux et bouche) de 30 à 40 unités vers le côté du regard, raccourcir le bras du fond ;
- **profil** : seulement si un plan le demande (une marche latérale), comme un deuxième jeu de pièces.

Un personnage plat ne tourne **jamais** en perspective : on passe d'une vue dessinée à une autre.

**À savoir avant de compter sur une autre vue** (film réel du 11/11/2026) : le kit 2.5D ne fournit que la vue de face, et décaler le visage ne suffit pas à faire lire un trois quarts ; les regards du film sont restés un point faible après deux tours de critique. Une vue de plus est un second jeu de pièces à dessiner, à valider en planche et à échanger à une coupe : marche à suivre dans `limites-du-pantin.md`.

## Planche d'expressions

Chaque élément de la planche est un fichier séparé, dans le même gabarit, qui ne contient **que** cet élément (les yeux seuls, la bouche seule).

| Fichier | Dessin |
|---|---|
| `yeux-neutre` | deux points ronds |
| `yeux-grands` | deux cercles plus grands, pupille petite : surprise, peur |
| `yeux-plisses` | deux traits courts légèrement arqués : doute, malice, effort, anticipation |
| `yeux-fermes` | deux arcs vers le bas : clignement, soulagement, fierté |
| `yeux-regard-cote` | points décalés du même côté : méfiance, réflexion, gêne |
| `bouche-fermee` | petit trait |
| `bouche-petite-ouverte` | petit ovale : parole, étonnement léger |
| `bouche-grande-ouverte` | grand ovale : cri, rire, mot fort |
| `bouche-moue` | arc vers le bas |
| `bouche-sourire` | arc vers le haut, plus large |
| `extra-goutte` | goutte de sueur près de la tempe |
| `extra-rouge-joues` | deux ovales rosés |

Éléments souvent ajoutés ensuite : sourcils froncés, yeux en larmes, yeux brillants, bouche tremblante, marque de colère, point d'exclamation, point d'interrogation, ampoule. Les marques de réaction sont des **dessins**, jamais des lettres tapées dans une police.

## Pièces SVG dans un style au trait propre (ou dessiné en canvas)

Certaines fiches de style ont leur propre trait (fin, à manques, décalé de la couleur) et décrivent un moteur en canvas. Les pièces SVG restent utilisables de deux façons.

**Voie 1 : rester en SVG en ligne, et donner aux pièces le trait du style.** C'est la voie du film d'essai `cartoon-annees-50` rendu le 11/11/2026 (HyperFrames 0.9.33) : 7 pièces et 6 expressions, assemblées dans `index.html`, textes en vrai texte.

- Chaque forme d'une pièce est écrite **deux fois** : un aplat (classe `ap`, sans contour, avec son `fill`) puis un trait (classe `tr`, sans remplissage). Les formes pleines d'encre (cheveux, pupilles) ont une troisième classe `en`. Le fichier de pièce ne porte aucune épaisseur en dur : tout vient de trois règles CSS, celles de la fiche de style.
  ```html
  <style>
    .ap { stroke: none; transform: translate(var(--dx), var(--dy)); }   /* couleur décalée du trait, si le style le veut */
    .tr { fill: none; stroke: #2B2420; stroke-width: 4.5; stroke-linecap: round; stroke-linejoin: round;
          stroke-dasharray: 92 13 41 9 128 17 66 11; stroke-dashoffset: var(--do); }   /* manques du trait */
    .en { fill: #2B2420; }
  </style>
  <g id="bras-d"><rect class="ap" x="341" y="436" width="34" height="118" rx="15" fill="#B8452B"/><rect class="tr" x="341" y="436" width="34" height="118" rx="15"/></g>
  ```
- Un petit script d'assemblage (Python ou Node) écrit les fichiers de `pieces/` et `expressions/`, puis les recolle dans la page : un `<g>` par pièce, dans la hiérarchie des pivots ; tous les jeux d'yeux et de bouches sont présents, un seul est affiché à la fois.
- L'animation se fait dans l'écouteur `hf-seek` : `piece.setAttribute("transform", "rotate(angle px py)")` avec le pivot de la fiche, en unités du gabarit, et un temps de dessin tenu (`Math.floor(t * 15) / 15`). On enregistre une timeline vide (skill `rendu`, « Film en canvas piloté par `hf-seek` » : la recette vaut aussi pour du SVG).
- Ce qu'on perd : un trait dont la largeur varie le long du chemin (ruban d'encre). Les manques, le décalage et le saut « en deux » passent très bien.

**Voie 2 : dessiner les pièces dans le canvas du style.** À prendre quand le style exige un trait que SVG ne sait pas faire (ruban à largeur variable, craie, pinceau). Non essayée en rendu réel : à vérifier sur une capture avant de s'engager.

- Garder les pièces comme **données** : pour chaque pièce, ses chemins (`d`), sa couleur, son pivot. Un `<rect>`, un `<circle>` ou une `<ellipse>` se réécrit en chemin, ou se trace par `roundRect`, `arc`, `ellipse`.
- Dans le canvas : `const forme = new Path2D(d)` ; se placer dans le repère de la pièce (`translate` au pivot, `rotate`, `translate` inverse, dans l'ordre de la hiérarchie) ; `ctx.fill(forme)` pour l'aplat ; puis passer **les points du chemin** à la fonction de trait du style (son ruban, sa craie), au lieu de `ctx.stroke`.
- Le gabarit ne change pas (`viewBox` 0 0 600 1000) : une seule mise à l'échelle place le personnage dans le cadre. Ne jamais agrandir le personnage par un zoom du monde : l'épaisseur du trait grossirait avec lui ; on redessine à l'échelle.
- Les textes restent en HTML par-dessus le canvas, pour être relevés et contrôlés.

Dans les deux voies, la `fiche.md` du personnage note le trait employé (« Contour : 4,5 px, manques, selon la fiche cartoon-annees-50 ») à la place du contour par défaut.

## Export

- Exporter chaque SVG en **PNG à 2×** (1200 × 2000 px pour ce gabarit), fond transparent, avec l'outil disponible sur la machine (`rsvg-convert -z 2`, Inkscape en ligne de commande, ou une capture de la page par le navigateur de HyperFrames).
- Toutes les images ont **la même taille** : c'est ce qui permet de les superposer sans calcul.
- Vérifier une image exportée : bords nets, fond vraiment transparent, contour non rogné sur les bords du cadre.
- HyperFrames peut utiliser directement les SVG ; Blender a besoin des PNG.

## Planche de contrôle

Une image qui montre, sur fond neutre : le personnage complet en pose neutre, puis 8 à 12 combinaisons d'yeux et de bouche avec leur nom. La lire à petite taille : chaque expression se distingue-t-elle des autres ? La faire valider par le client.

## Fiche du personnage (`fiche.md`)

```
Nom, rôle, époque
Hauteur dans le décor : 1,60 m   (taille du plan dans Blender)
Couleurs : peau #…, encre #…, costume #…, #…, accent #…
Contour : 14 unités
Pivots : (tableau)
Expressions disponibles : (liste)
Costumes : (liste)
Ce qu'il ne fait jamais : (par exemple : ne sourit pas avant la dernière phrase)
```
