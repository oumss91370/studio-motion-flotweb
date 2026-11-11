# Livre d'images isométrique

## 1. Identité

- **Nom** : Livre d'images isométrique (une règle du quotidien, expliquée calmement).
- **Inspiration** : les explications isométriques sur les usages en public (files d'attente, quais, passages piétons) et les livres d'images en coupe où l'on soulève un toit ou un mur pour voir l'intérieur. On en garde le rythme calme, les gens comme schéma et la lettre posée au sol ; on n'en recopie ni personnage, ni mise en page, ni police, ni musique.
- **Ce qui le fait reconnaître** :
  - **Un vrai lieu, plein cadre** : un quai, une porte, une cabine, un guichet. Le sol déborde de chaque bord de l'image. Pas de plateau flottant, pas de cadre, pas d'assombrissement des coins.
  - **Les gens sont le schéma** : de fines silhouettes **vues de dos, sans visage ni mains**, qui ne bougent que lorsque la règle le dit. Qui avance en premier, qui attend, qui s'assoit : c'est l'information.
  - **La lettre est couchée au sol** : chaque idée est un mot clé ou un nombre **peint sur le sol**, en grande et petite taille, avec un seul caractère d'accent, qui se pose lettre par lettre.
  - **La coupe** : tout ce qui est entre la caméra et l'action (toit, auvent, haut d'un mur, façade vitrée) est coupé bas ou **se soulève comme un rabat de papier**.
  - **Propre, toujours** : un lieu, une action, une phrase par temps. De grandes plages de sol calme. Une image dont il faut chercher le sujet est ratée.
- **Marche pour** : les règles du quotidien et leurs raisons (« pourquoi on embarque dans cet ordre »), files d'attente, comparaisons de deux façons de faire, consignes d'un lieu (cabinet, salle de sport, restaurant, école), petit fait étonnant sur l'organisation.
- **Ne marche pas pour** : un système à pièces et à flux (voir `infographie-isometrique`), un objet technique (voir `isometrique-trait-fin` (catégorie « Matières et 3D »)), émotion et humour (aucune expression, aucun gag). Ce n'est pas une diapositive (ni en-tête, ni titre centré, ni carte).

## 2. Palette, typographie, matières

| Rôle | Couleur (exemple de la source) |
|---|---|
| Papier (sol) | `#F1E8D8` |
| Béton extérieur (un peu plus froid) | `#EAE2D3` |
| Moquette intérieure (un peu plus chaude) | `#F2E5CE` |
| Encre | `#2A2E29` |
| **Accent, réservé à la règle** | kaki rouge `#D0573A` |
| Teinte du lieu (sièges, bandes, signalétique) | vert `#3D6B59`, version pâle `#A7C2B2` |
| Couleur de marquage au sol | gingembre `#E2AE3A` |
| Hauts des personnages (4 tons sourds) | ocre, bleu brume, gris violet, avoine |

- **L'accent ne décore jamais** : il n'apparaît que là où est la règle (le caractère clé, le contour « placez-vous ici », une flèche, un panneau allumé, le nombre gagnant). Beaucoup d'images n'en ont pas du tout : sa rareté fait que l'œil y va.
- La teinte du lieu et la couleur de marquage doivent être **nettement distinctes**, en teinte et en valeur, des quatre hauts : les gens doivent se détacher du lieu.
- **Ombrer vers la terre d'ombre chaude et le papier, jamais vers le gris ni le violet** : des ombres sales sont le moyen le plus rapide de perdre ce look.
- **Trois tons par couleur** : dessus éclairci vers le papier chaud, une face à la couleur de base, l'autre assombrie vers la terre d'ombre. Les corps courbes sont à facettes dans les mêmes tons. Aucun contour, aucune ombre portée, aucune texture, aucun reflet.
- **Polices** (libres) : Newsreader (à empattement, pour le sol : 700 pour les mots clés, 500 pour les petits mots) ; une police sans empattement sobre pour les sous-titres.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Newsreader. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/newsreader` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Personnages** : panneaux ancrés aux pieds, 1,6 à 1,8 m : tête ronde sombre avec un liseré de peau à l'oreille, torse en deux tons, deux jambes de pantalon, chaussures sombres ; en option cheveux longs, jupe, valise à roulettes. Assis : seulement les épaules et l'arrière de la tête au-dessus d'un dossier bas.
- **Objets nouveaux** (véhicules, machines, bâtiments) : faits de boîtes et de prismes à taille réelle, reconnaissables à leur silhouette, plus simples que les personnages ; roues petites, basses, en un seul ton sombre.
- Les sols ne portent que leurs marquages utiles (couloirs peints, chevrons, lignes d'arrêt) et un quadrillage de dalles très discret.

## 3. Composition 9:16

- Un lieu vu en isométrie remplit bien un cadre vertical si l'action suit **un axe qui monte à l'écran** : une file, un couloir, une allée de cabine, un quai. Orienter le lieu pour que la file parte du bas et s'éloigne vers le haut à droite ou à gauche (les marcheurs **s'éloignent de la caméra** : un personnage qui vient vers elle montre un dos qui a l'air faux).
- **Lettres au sol** : grandes ≈ 1,5 m sur le sol, petites ≈ 0,8 m ; à l'écran, les grandes font **au moins 110 px**. Une phrase par temps, une seule ligne quand le cadre est serré, **un seul caractère ou nombre en accent** par phrase.
- La lettre repose sur un sol dégagé : rien dessus, **rien de haut devant elle**, à 5 % au moins de chaque bord, hors de la zone de droite (x supérieur à 945) et de la bande des sous-titres.
- Les panneaux du lieu sont dessinés à l'angle isométrique, jamais comme une carte à plat face à l'objectif.
- **Sous-titres** : une bande pâle entre y 1400 et y 1540, **une seule ligne en français** (46 à 50 px), changée d'un coup, jamais deux à l'écran. Le sol ne porte que le mot clé ou le nombre de la phrase, jamais la phrase.
- **Nombres à retenir** : trois au plus dans le film, chacun dit avec ce à quoi il se compare, et tenu au moins 2,5 s.
- Une file droite se lit comme de l'ordre ; une foule en serpentin se lit comme un bloc.

## 4. Ce qui bouge

- **Action principale** : les gens font la chose **dans l'ordre**. L'ordre du mouvement est l'explication.
- **Boucles de fond** : (1) la marche (les jambes en ciseaux, les bras en contretemps, une valise qui roule) de ceux dont c'est le tour ; (2) une dérive lente de la caméra avec une légère poussée (6 à 8 % de zoom).
- **Autorisés** : machine à écrire `#006` appliquée au sol (les caractères se posent à 0,14 s d'écart : fondu, échelle de 1,22 à 1, d'un fantôme pâle à l'encre), tracé de ligne `#004` (un contour, une flèche qui pousse devant les marcheurs, une lumière qui court sur un chemin), décalage en cascade `#002`, suivi `#174` de la tête d'une file, travelling de suivi `#029` le long du sol, plan fixe `#175`, zoom `#028` (changement d'échelle : pièce, bâtiment, site), plan d'ensemble `#183`, compteur `#007` (qui redescend pendant un retour en arrière).
- **Interdits** : rotation de la vue `#030` (l'angle isométrique ne change jamais : la caméra ne fait que glisser et zoomer), fondu `#044`, volet `#045`, tourné de page `#140`, image noire ou vide, rebond `#123`, apparition éclair `#001` (tout est amorti, rien ne surgit), expressions, ombres portées, personnes plus rapides que 3 m par seconde.
- **Un temps** = une phrase au sol + une marque de schéma + une action.
- **Les corps respectent l'espace** : personne ne traverse un siège, un mur ou une autre personne ; une file garde environ 0,75 m entre les pieds ; pour s'asseoir, on entre dans la rangée, on avance de côté, on s'assoit.
- **Le couvercle** : un toit bascule sur sa charnière du fond, côté papier vers le haut, puis glisse hors champ ; la caméra s'élève pour voir tout l'intérieur. Il finit de tourner **dans le cadre**.
- **Retour en arrière** : le même mouvement à l'envers, plus vite, avec un compteur qui redescend.
- Pour comprimer un long processus : montrer des **places qui se remplissent**, pas des gens qui filent.

## 5. Rythme et montage

- 30 images par seconde, fluide. Calme : plans de 4 à 8 s ; une phrase de voix par action, qui commence quand l'action commence.
- Transitions : un mouvement continu, un couvercle qui s'ouvre, un retour le long du même chemin, ou une coupe sur le temps **au même angle**. Un recul montre son sujet suivant (une marque qui se trace) en moins d'une demi-seconde.
- Structures possibles : une règle montrée une fois, bien ; le même groupe qui la fait de deux façons, comparées (avec un retour en arrière entre les deux) ; une journée dans un lieu en cinq petites règles ; une chose qui voyage par plusieurs arrêts sur un même sol continu.
- Fin type : le lieu vide, la règle restée au sol ; ou un saut d'échelle vers le bâtiment.
- **Version courte (8 à 12 s)** : une seule scène : deux ou trois actions dans l'ordre (3 s chacune), mots clés au sol ; couper l'élévation finale de la caméra. Accroche : le premier personnage bouge dès la première seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`, tri du peintre. `blender` n'est pas indiqué : le style refuse lumière et ombres.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `iso.js` (projection, caméra qui glisse et zoome, boîtes, prismes, cylindres, facettes, dessin sur un plan), `kit.js` (trois tons chauds, lettres au sol, personnages, sous-titres), `lieu.js` (sol, marquages, bâtiments en coupe), `film.js` (timeline bâtie sur la durée des phrases, simulation de file).

```js
// trier par l'EMPREINTE AU SOL, jamais par le centre de la boîte (sinon un dossier passe devant le passager assis derrière)
const cle = o => o.x + o.y;                                  // x + y au niveau du sol
// trois tons chauds
const tons = c => ({ dessus: melange(c, "#F1E8D8", .25), gauche: c, droite: melange(c, "#5a4634", .22) });
// file simulée UNE fois au chargement (déterministe), puis échantillonnée avec interpolation
const position = (i, t) => interpoler(TRAJETS[i], t * 30);   // jamais d'arrondi à l'image : sinon ça saccade au ralenti
// lettre au sol : caractère k
const pose = (t, k) => adoucir(borner((t - t0 - 0.14 * k) / 0.3));   // opacité, et échelle 1.22 → 1
```

- **Piège principal, la hauteur cache** : tout ce qui est haut de H mètres cache le sol jusqu'à H mètres derrière lui. Une ceinture de 0,8 m couvre une lettre posée 0,8 m derrière ; le flanc d'un camion de 3,2 m cache les jambes des gens jusqu'à 3,2 m derrière. Garder les lettres et les gens importants **du côté caméra** des objets hauts, ou couper ces objets ; vérifier chaque image où un véhicule passe.
- **Autres pièges** : un chemin en zigzag se lit comme du bruit (suivre les axes du monde, peu d'angles droits) ; des assis qui disparaissent derrière des dossiers trop hauts ; une couleur ombrée vers le violet par un réglage par défaut ; un mouvement de caméra qui traîne un mot sur le bord du cadre (vérifier les deux bouts du mouvement) ; contrôler une foule **image par image**, pas à l'œil (sauts, arrêts-départs, personnes plus proches qu'une largeur de corps).

## 7. Son

- **Musique** : piano droit doux et vibraphone. **Une note de vibraphone par caractère qui se pose** (les mots clés plus fort, l'accent doublé au glockenspiel) ; pizzicato et shaker quand les gens marchent. Ces notes font partie de la musique : elles ne comptent pas comme des bruitages.
- **Les actions répétées deviennent du rythme** : une file bloquée, ce sont des pizzicatos cassés ; une file ordonnée, un accord par groupe.
- **Ambiance et bruitages** : l'air calme du lieu (hall, cabine, moteurs lointains), une note grave tenue qui recouvre chaque coupe ; les sons utiles du lieu (un carillon d'annonce, des roulettes sur la moquette puis sur le métal, un coffre qui se ferme).
- **Retour en arrière** : la dernière seconde de musique jouée à l'envers.
- **Voix** : lectrice ou lecteur calme et assez rapide ; la musique baisse nettement sous la voix et remonte entre les phrases.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Un seul lieu, plein cadre : aucun plateau flottant, aucun cadre, aucun coin assombri.
- [ ] Les personnages sont vus de dos, sans visage ni mains, et s'éloignent de la caméra.
- [ ] Les gens ne bougent que dans l'ordre que la règle impose ; personne ne se traverse.
- [ ] Les mots sont peints au sol, avec un seul caractère d'accent, et rien de haut ne les cache.
- [ ] L'accent n'apparaît que là où est la règle.
- [ ] Les ombres vont vers le brun chaud, jamais vers le gris ou le violet ; aucune ombre portée.
- [ ] L'angle de vue ne change jamais.
- [ ] Trois nombres à retenir au plus, chacun tenu 2,5 s au moins ; grandes lettres d'au moins 110 px.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine, *Seventy-Two Seats* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/isometric-picture-book.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/isometric-picture-book.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, images sous CC BY 4.0. **La piste de voix de ce film est exclue de la licence CC BY 4.0** (voix d'un service en ligne) : donner le film en lien seulement, ou le montrer **sans le son** ; ne jamais réutiliser sa voix.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/isometric-picture-book/STYLE.md`, `DEMO.md`, `demo/engine.js`, `demo/kit.js`, `demo/film.js`, `demo/tools/motion_check.mjs`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour les images du film (voix exclue). Police Newsreader : OFL 1.1.
- Adaptation Flot Web : traduction, textes au sol et sous-titres en une seule langue (la règle bilingue chinois-anglais de la démo est retirée), orientation verticale, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
