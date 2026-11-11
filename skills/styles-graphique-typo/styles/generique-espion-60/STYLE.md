# Générique d'espionnage années 60

## 1. Identité

- **Nom** : Générique d'espionnage années 60 (papier découpé, quatre encres).
- **Inspiration** : les génériques de film en papier découpé de la fin des années 1950 et des années 1960 (encres plates et opaques, personnages réduits à des silhouettes, le lettrage comme architecture) et leurs hommages des années 2000 (poursuite en papier découpé à travers des décors graphiques). On n'en recopie ni logo, ni lettrage, ni personnage, ni plan. Pas d'ouverture en canon de pistolet, pas de panthère de dessin animé.
- **Ce qui le fait reconnaître** : quatre couleurs plates sur papier ; des bords coupés aux ciseaux ; des silhouettes de profil qui jouent par leur contour et leur rythme ; **les textes sont le décor** (une ligne de mots devient un immeuble, un train, une serrure) ; chaque coup de cuivres est une coupe.
- **Marche pour** : ouverture de vidéo ou d'événement, bande-annonce, lancement où « ce que tout le monde poursuit » devient le titre final, liste de fonctions ou de noms à faire défiler avec panache.
- **Ne marche pas pour** : une explication détaillée, des données, un tutoriel, un sujet grave. Ce n'est pas du vectoriel plat (les bords sont coupés, le papier est physique), ni une grille suisse (ici tout est en diagonale et joueur).

## 2. Palette, typographie, matières

Quatre encres : un noir, une crème de papier, une couleur chaude, un second ton chaud. Des versions plus sombres de ces encres servent seulement à la profondeur.

| Jeu | Noir | Papier | Couleur chaude | Second ton |
|---|---|---|---|---|
| Classique | `#1b1714` | `#efe4c9` | rouge `#d23a22` | moutarde `#e2a52a` |
| Froid | `#161a22` | `#ece6d6` | sarcelle `#1f8a8a` | orange `#f07a28` |
| Pop | noir | rose pâle `#f3d6cc` | cobalt `#2a46b8` | citron `#f0d23a` |

- **Une couleur de fond dominante par lieu**, qui change avec le décor. La couleur chaude est réservée à un accent sur le héros (cravate, écharpe) et au danger. Le second ton marque l'objet poursuivi.
- Les accessoires de fond prennent une version plus sombre du fond, **jamais le noir**, sinon ils se lisent comme des lettres.
- **Polices** : League Gothic (condensée, pour les textes-décors), League Spartan 600 (sous-titres). Le titre final est fait de lettres géométriques découpées à la main (coupes droites et arcs, graisses inégales, lignes de base décalées), jamais le lettrage d'un vrai film.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place de League Spartan ; League Gothic : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/league-spartan` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : une texture de papier multipliée sur toute l'image (marbrures, fibres), quelques manques d'encre sur le noir, de légères traces de raclette. Chaque pièce est séparée de sa voisine par une fente d'environ 2,4 px de la couleur du fond et porte une petite ombre de papier (décalée de quelques pixels, flou d'environ 5, opacité d'environ 0,3).

## 3. Composition 9:16

- Diagonales fortes (environ 30°), grands aplats, **personnages petits face aux lettres**.
- En vertical, la ligne de texte-décor devient une **colonne** : les mots s'empilent, les lettres deviennent des étages, et le travelling latéral devient un panoramique vertical le long de la colonne. Garder aussi des plans de poursuite latérale sur une bande centrale (y 500 à 1300).
- Toujours ouvrir large sur le texte entier, lisible à un moment, avant de s'approcher : un texte qu'on ne voit jamais en entier met mal à l'aise.
- **Tailles** : lettres-décors de 300 à 900 px de haut ; silhouettes d'environ 7 têtes, 300 à 500 px de haut ; sous-titres 44 à 52 px sur une bandelette de papier légèrement penchée, coupée aux ciseaux, en bas à gauche au-dessus de y 1560 (claire sur scène sombre, sombre sur scène claire).
- L'objet poursuivi repose sur une doublure noire pour se lire sur n'importe quel fond ; c'est la chose la plus claire de l'image.
- Zone utile : y de 160 à 1560, x de 60 à 945.

## 4. Ce qui bouge

- **Action principale** : une poursuite (ou un compte à rebours, un casse à l'envers) à travers des lieux faits de lettres, jusqu'à ce que les morceaux s'assemblent en titre.
- **Boucles de fond** : (1) l'accent coloré du héros (cravate, écharpe) qui flotte en arrière, ruban à plusieurs segments parcouru par une onde ; (2) les textes qui glissent le long des lignes de la grille et s'arrêtent net sur le temps.
- **Autorisés** : style image par image `#128` (pantins à 15 dessins par seconde), suivi latéral dans un seul sens `#029`, raccord de forme `#042` (roue, pièce, pupille, lune : même centre, même taille), coupe sèche `#046`, arrêt sur image `#040`, écran partagé en diagonale `#144`, éclatement en bandes `#142`, poussée dans une lettre jusqu'à remplir le cadre `#027`.
- **Interdits** : fondu enchaîné `#044`, dégradés et lueurs `#022`, flou de profondeur `#105`, rebond mou `#123`, caméra à l'épaule `#034`, caméra saccadée.
- Cycles de course d'environ 8 dessins, un pas par temps, corps très penché. Les lettres atterrissent avec un claquement de carton.
- **Temps suspendu** : sur un coup de cuivres, toute l'image se fige (défilement du fond compris) pendant deux temps de silence total, puis repart.

## 5. Rythme et montage

- La musique coupe l'image : chaque coup de cuivres est un point de montage. L'intervalle entre les coupes raccourcit quand la poursuite accélère.
- Plans de 1 à 4 s ; un lieu = une ligne de texte = un plan large puis un rapproché.
- Pantins, mains, lettres qui tombent : 15 dessins par seconde (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s). Caméra, glissement des textes, croissance de la grille : fluides.
- Fin possible : un grand accord pour le titre, puis une courte ponctuation.
- **Version courte (8 à 12 s)** : deux lieux faits de lettres (un plan large et un rapproché de 1 à 2 s chacun), puis l'assemblage du titre tenu 2 s ; couper les autres lieux.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (encres, bords coupés mis en cache, fentes, ombre, texture), `lettres.js` (contours des glyphes re-découpés), `pantins.js` (silhouettes articulées, poses, cycles), `film.js` (grille de tempo, source unique du minutage).

```js
// bord « aux ciseaux » : coupé UNE fois dans le repère de la pièce, puis mis en cache
function couper(poly, graine) {
  const pts = rééchantillonner(poly, 9.5);               // un point tous les 9 à 10 px
  return pts.map((p, i) => deplacerSurNormale(p, bruitLent(i, graine) * 1.8)); // 1,2 à 2,2 px
}
const posePantin = t => Math.floor(t * 15) / 15;         // le pantin à 15 dessins/s, la caméra en continu
```

- **Techniques clés** : les pièces d'un personnage sont **fusionnées en un seul contour** dans un calque hors écran, avec de fines fentes seulement à l'épaule, au coude, à la hanche et au genou (`destination-out`), puis la fente est tracée autour du personnage entier. Chaque lettre est re-découpée (bruit de bord, rotation de ±0,8°, ligne de base de ±1,5 px).
- **Pièges** : un bord recalculé dans le repère de l'écran grouille quand la pièce bouge ; un `clear()` qui remet la transformation à zéro tue la caméra sans prévenir ; un personnage entièrement caché derrière une lettre se lit comme « personne » (laisser dépasser chapeau, nez, accent) ; un raccord de forme rate si le centre du cercle bouge à la coupe ; un objet rond posé dans un mot recouvre les lettres voisines (composer le mot autour d'un vide).

## 7. Son

- **Musique** : big band d'espionnage des années 60, composition originale : trompettes et trombones en staccato, guitare « surf » avec réverbération à ressorts, contrebasse qui marche, balais, bongos, vibraphone, flûte, orgue, clavecin. Tons mineurs, lignes chromatiques. Éviter les motifs célèbres des grandes sagas d'espionnage.
- Placer les cuivres environ 8 ms en avance pour que le pic du son tombe sur l'image de la coupe.
- **Bruitages** (matière papier et métal) : ciseaux, glissement de carton, claquement d'une lettre qui tombe, déchirure, clés, serrure, clic de bande magnétique. Les lieux sont seulement suggérés (un passage d'avion, des roues de train au tempo).
- **Silence** : zéro absolu, queues de réverbération comprises ; un seul clic ou souffle de bande peut rester.
- **Voix** : un « briefing » passé par un magnétophone (bande passante réduite, légère saturation), quelques phrases très courtes.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Quatre encres au plus dans chaque image, aucune en dégradé.
- [ ] Tous les bords sont coupés (aucune courbe vectorielle parfaite) et ne grouillent pas quand la pièce bouge.
- [ ] Chaque lieu est une ligne de texte qu'on voit entière et lisible à un moment.
- [ ] Les personnages n'ont pas de visage (au plus une fente d'œil en gros plan) et se lisent en silhouette.
- [ ] Les coupes tombent sur les coups de cuivres.
- [ ] Aucun accessoire de fond en noir ; l'objet poursuivi a sa doublure noire.
- [ ] Aucun fondu ; au moins un raccord de forme et un temps suspendu.
- [ ] Les textes-décors sont des rôles ou des mots du sujet, jamais des noms de vraies personnes.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine, *The Velvet Cipher* (44 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/spy-titles.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/spy-titles.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/spy-titles/STYLE.md`, `DEMO.md`, `demo/paper.js`, `demo/glyph.js`, `demo/chars.js`, `demo/title.js`, `demo/story.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices League Gothic et League Spartan : OFL 1.1.
- Adaptation Flot Web : traduction, composition verticale en colonne, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
