# Bauhaus

## 1. Identité

- **Nom** : Bauhaus (affiche d'école de design des années 1920).
- **Inspiration** : les affiches et le théâtre de l'école du Bauhaus : géométrie pure, trois couleurs primaires, lettrage géométrique, mobilier en tube d'acier, personnages-pantins faits de volumes simples. On s'inspire du vocabulaire ; on ne recopie aucune affiche ni aucun logo de l'école.
- **Ce qui le fait reconnaître** : **cercle, carré, triangle et barres épaisses**, rien d'autre ; rouge, bleu, jaune et noir sur un papier crème vieilli ; un mot en très grandes lettres posé à la verticale ; **aucune courbe tracée à main levée, aucun contour**. Les personnages eux-mêmes sont des assemblages de formes.
- **Marche pour** : sujet de design, d'architecture, d'école ou de formation, idée abstraite à rendre simple (trois principes, trois étapes), ouverture graphique, marque qui veut un air « moderne classique ».
- **Ne marche pas pour** : émotion, récit avec des visages expressifs, sujet organique (nature, cuisine, soin), beaucoup de texte courant. À ne pas confondre avec `typo-suisse` (grille stricte, une seule couleur) ni avec `constructivisme` (diagonales, rouge et noir, photo tramée).

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Papier vieilli | `#ebe3cf` |
| Noir | `#161514` |
| Rouge | `#d3262b` |
| Bleu | `#2a58b4` |
| Jaune | `#efc12f` |
| Bleus clairs (touches) | `#b9cee0`, `#a6c0da` |
| Gris / crème | `#c6c3bb` / `#f2ecdf` |
| Orange (un seul élément vivant) | `#ee8a2a`, ombre `#c25a14` |
| Chrome (tube d'acier) | `#c9c9c6` |

- **Police** : Poppins 800 pour les grands mots, Poppins 600 pour les petites lignes (libre). Tout en minuscules.
- **Police de repli** : aucune à prévoir, Poppins est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/poppins` (vérifié par `npm view` le 11/11/2026).
- **Matières** : papier crème marbré (un petit bruit agrandi, à 50 % d'opacité), deux couches de piqûres sombres comme une vieille impression. Le grand disque rouge porte des taches plus claires, pour imiter l'encre inégale d'une sérigraphie. Les tubes chromés sont un même tracé repassé trois fois (gris sombre épais, chrome, filet de lumière décalé de 2 px).
- Aucun dégradé décoratif, aucune ombre portée.

## 3. Composition 9:16

- Une **affiche en hauteur** : une grande forme dominante (disque rouge d'environ 500 px de diamètre) dans le tiers haut ou central ; une longue barre noire en diagonale ; un mot géant posé à la verticale le long du bord gauche (lu de bas en haut, lettres de 200 px environ, x 80 à 260) ; un second mot plus petit en rouge (150 px) ; deux lignes de petit texte en bas à droite, à gauche de x 945 et au-dessus de y 1560.
- Une **grille-fenêtre** de 4 × 4 cases (cases d'environ 100 px, joints de 9 à 10 px) sert de « tableau » qui change de couleurs.
- Une ligne de sol fine traverse l'image vers y 1450 ; un petit carré gris et un triangle jaune servent de contrepoids.
- Composition asymétrique mais équilibrée : une masse lourde en haut d'un côté, une masse légère en bas de l'autre.
- Texte : au plus un grand mot et une ou deux lignes courtes par plan. Petites lignes à 36 px au moins.

## 4. Ce qui bouge

- **Action principale** : une forme agit comme une pièce de machine. Exemple type : la longue barre noire tourne comme une aiguille autour de son moyeu (de 28° à 50° en 0,2 s, avec une décélération), le moyeu ne bouge pas.
- **Boucles de fond** : (1) la grille-fenêtre change de couleurs, par à-coups à 13 changements par seconde au plus, chaque case avec sa phase, et pas toutes à chaque coup (le rythme ne doit pas être mécanique) ; (2) des arcs concentriques à côté du disque rouge « respirent » (rayon ±3 px) et s'étendent comme une onde sonore.
- **Autorisés** : rotation autour d'un pivot fixe, courbes d'accélération `#009`, tracé de ligne `#004`, répéteur `#134` (arcs), pulsation `#125`, transition par forme `#018` (carré bleu, disque rouge, triangle jaune qui tournent et grossissent jusqu'à remplir l'écran), zoom à travers `#020`, plan fixe `#175`.
- **Interdits** : morphing organique `#013`, tremblement du trait `#136`, rebond mou `#123`, particules `#015`, lueur `#022`, caméra à l'épaule `#034`, toute courbe libre.
- **Une balle roule vraiment** : angle de rotation = distance parcourue ÷ rayon (un diamètre blanc et un point montrent qu'elle roule), avec deux lignes de vitesse derrière.
- La vapeur ou la fumée est une fine ligne sinusoïdale qui monte, pas un nuage.
- **Personnages-pantins** : tête en disque, tronc en trapèze, jupe en éventail, membres en grosses barres à bouts ronds, articulations en disques crème cerclés de noir avec un point central. Yeux : barres verticales noires (clignement = barre horizontale). Les animaux aussi : corps en disque, tête en carré, oreilles en triangles.

## 5. Rythme et montage

- Plans de 2 à 5 s. Mouvements nets, comme des mécanismes : départ franc, arrêt franc avec décélération, pas de flottement.
- Les changements de couleur de la grille sont calés sur le tempo.
- **Transition signature** : les trois formes primaires tournent et grossissent ; le centre du zoom est le centre du disque rouge.
- Animation fluide (30 images par seconde), sauf la grille qui change par à-coups.

## 6. Recette technique

- **Moteur** : HyperFrames. Le plus simple : éléments SVG ou HTML animés par GSAP (formes nettes, modifiables une par une). Canvas 2D si l'on veut les textures de papier et d'encre.
- **Structure** : un fond mis en cache une fois (papier, barres fixes, lettres, sol, mobilier, piqûres), puis les éléments mobiles par-dessus.

```js
// l'aiguille : pivot au moyeu, 28° → 49,5° avec décélération
tl.fromTo("#barre", { rotation: 28, transformOrigin: "74% 50%" }, { rotation: 49.5, duration: 0.22, ease: "power2.out" }, 0.26);
// la grille : par à-coups, chaque case sa phase, pas à chaque coup
const coup = Math.floor(t * 13);
cases.forEach((c, i) => { if ((coup + 2 * i) % 9 < 6) c.couleur = PRIMAIRES[(coup + i) % PRIMAIRES.length]; });
// la balle roule : angle = distance / rayon
balle.rotation = (balle.x - x0) / RAYON;
```

- **Techniques clés** : le mot vertical est tourné de −90° puis étiré à la longueur exacte voulue ; la texture du disque rouge est appliquée seulement dans la forme (`source-atop`).
- **Pièges** : calculer la taille des cases à partir du cadre intérieur moins les joints, sinon la grille déborde ; **ne pas mettre de noir dans les couleurs qui tournent** (une case noire fait croire à une case cassée) ; une bouche dessinée en longue barre sortant du visage ressemble à une cigarette (une courte barre à l'intérieur).

## 7. Son

- **Musique** : piano mécanique ou piano préparé, percussions sèches (wood-block, claves, caisse claire aux balais), clarinette ou saxophone en notes détachées ; une écriture en motifs courts et répétés, comme des pièces qui s'emboîtent.
- **Bruitages** : clic de mécanisme, bois contre bois, balle qui roule sur une table, métal de tube, feuille de papier, tic de métronome pour les changements de la grille.
- **Silence** : un temps d'arrêt complet avant la transition aux trois formes.
- **Voix** : claire, posée, phrases courtes.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Uniquement des cercles, carrés, triangles et barres : aucune courbe libre, aucun contour.
- [ ] Rouge, bleu, jaune, noir sur papier crème ; l'orange ou le chrome restent de petites touches.
- [ ] Le papier est vieilli (marbrure, piqûres) : pas un fond blanc pur.
- [ ] Au moins trois éléments bougent à tout moment (une forme principale + deux boucles).
- [ ] Ce qui tourne tourne autour d'un pivot fixe ; ce qui roule roule de la bonne quantité.
- [ ] Les couleurs qui changent ne contiennent pas de noir.
- [ ] Un seul grand mot par plan, lisible, et rien d'important hors de la zone utile.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9, le style y figure parmi 35) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : page des versions du dépôt, https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Il n'existe pas d'aperçu séparé pour ce style. La composition de la planche (une jeune fille, un chat, une table) appartient à un film tiers dont elle s'inspire : on la donne à voir en lien, on ne s'en sert pas comme visuel de vente.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/12_bauhaus.md` et `scripts/engine/scenes/12_bauhaus.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔). Police Poppins : OFL 1.1.
- Adaptation Flot Web : traduction du chinois, retrait de la scène et des personnages de la démo, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
