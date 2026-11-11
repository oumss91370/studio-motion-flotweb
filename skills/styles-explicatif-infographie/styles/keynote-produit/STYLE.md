# Keynote produit (style Apple keynote)

## 1. Identité

- **Nom** : Keynote produit. « Style Apple keynote » désigne une inspiration (les présentations de produit des grandes marques de technologie) ; ce n'est ni un contenu officiel, ni une affiliation.
- **Fiche fusionnée** de deux sources : la grammaire « interface de keynote » de huashu (le produit réel comme héros, ressorts, typographie serrée) et le film de lancement « à la manière d'un lancement de Mac » de Charlie Hills (une pastille qui grandit en widgets, scène par scène).
- **La règle en une phrase** : **un écran, une seule chose** ; le **produit lui-même** (capture d'écran, enregistrement, photo) est le héros ; les **noms et les chiffres se posent au moment où la voix les dit** ; lettres serrées ; ressorts sans rebond ou presque.
- **Marche pour** : lancement de produit ou de fonction, mise à jour, « trois nouveautés », annonce de prix ou de caractéristiques, passage « c'est quoi ce produit » dans une vidéo plus longue. Idéal quand la voix dit **un nom + un chiffre** (« délai de 320 millisecondes »).
- **Ne marche pas pour** : expliquer un mécanisme (voir `maths-animees`), une tendance chiffrée (voir `graphique-anime`), une mauvaise nouvelle ou un sujet grave (ce langage porte une émotion de « bonne nouvelle »), un contenu sans héros à agrandir, de la vulgarisation ou du récit. Sans captures réelles du produit, préférer `keynote-sombre`.

**Avertissement : c'est le style qui ressemble le plus vite à un modèle tout fait.** Fond à taches de lumière + cartes en verre dépoli + texte en dégradé + apparition centrée depuis le flou + cartes qui flottent : les cinq ensemble, et le spectateur reconnaît un gabarit. **Deux de ces cinq habillages au plus par film.**

## 2. Palette, typographie, matières

- **Les couleurs suivent le produit** : fond et accent viennent de la marque du client, pas d'un violet-bleu-cyan par défaut (qui tombe de plus sous la règle commune « pas plus de 30 % d'images bleu-violet »).

| Rôle | Valeur |
|---|---|
| Fond presque noir | `#050508` (variantes relevées : `#08090a`, `#0f1011`, `#141516`) |
| Texte principal | `#f5f5f7` |
| Texte secondaire | blanc cassé à 60 % |
| Surtitre | `#a7a7b4`, interlettrage +6 px |
| Bordure fine | blanc à 8 % |
| Fond clair (variante scènes colorées) | un dégradé plein écran par scène, à la couleur de la fonction |

- **Police** : Inter (libre). Titres en 600 ; **au-dessus de 64 px, interlettrage serré de −0,02 à −0,03 em**.
- **Police de repli** : aucune à prévoir, Inter est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/inter` (vérifié par `npm view` le 11/11/2026).
- **Formes** : rectangles arrondis, pilules, icônes au trait fin (bouts ronds, épaisseur constante). **Rayons concentriques** : rayon intérieur = rayon de la carte − marge intérieure (carte 36 px, marge 14 px, donc icône 22 px).
- **Habillages facultatifs** (à doser) : taches de lumière (4 dégradés radiaux très floutés, qui dérivent sur 9 à 13 s, avec 3,5 % de grain fixe contre les bandes) ; carte en verre dépoli (flou de ce qui est **derrière** elle, 7,5 % de blanc, bande de lumière en haut, bordure en dégradé, grande ombre) ; nom du produit en dégradé clair ; balayage de lumière en biais (−20°, bande de 110 à 140 px, 0,8 à 0,9 s).
- **Interface dessinée** : si l'on dessine des widgets, ils n'affirment rien : le texte de remplissage est fait de **lignes grises** ; tout mot d'interface que le client n'a pas fourni (libellé de bouton, heure) lui est soumis. Ne pas reproduire la barre de menus, l'encoche ni les commandes d'un vrai système d'exploitation : dessiner une barre et une pastille génériques.

## 3. Composition 9:16

- **La capture est grande** : en vertical, sa largeur fait **au moins 90 % de la largeur** (au moins 80 % en 16:9), entière, sans recadrage, avec autour une version floutée et assombrie de la même image. Une petite carte qui flotte sur un grand fond lumineux, c'est un « fond mort ».
- Quand la voix parle d'une zone qu'on ne lit pas, **on pousse dessus** ; puis on revient à la capture entière ou on glisse vers la zone suivante. Une ou deux poussées par capture, pas davantage.
- **Tailles** : titre de 6 mots au plus ou un nom de produit, 90 à 130 px ; sous-titre d'une phrase de 12 mots au plus, 44 à 52 px ; **grand nombre sur au moins 55 % de la largeur** (soit 590 px), unité un cran plus petite et plus grise.
- **Le nombre qui commente une capture se pose sur elle** : la caméra revient à la capture entière, la capture s'assombrit, le nombre tombe dessus. On ne coupe pas vers un écran séparé.
- Trois cartes côte à côte : seulement pour une liste de fonctions sans capture ; en vertical, les **empiler** (largeur 880 px, écart de 40 px).
- **Variante « pastille »** : une barre fine en haut (sous y 160, cinq mots au plus) et, au centre de cette barre, une **pastille noire qui grandit en widget**, une scène à la fois ; une phrase centrée dessous (y 900 à 1200), dont le ou les deux derniers mots prennent une teinte plus claire de la couleur du fond.
- **Compter les mises en page** : la même deux fois de suite, on en change (poussée dans une capture, nombre qui tombe, avant/après). « Titre, trois cartes, grand nombre » en boucle, c'est un diaporama.
- Carton de fin : visible au moins 1,2 s, dans la zone utile (au-dessus de y 1560).

## 4. Ce qui bouge

- **Action principale** : la caméra pousse dans la capture vers la zone dont on parle, ou la pastille s'ouvre en widget ; le nom ou le chiffre se pose **à l'instant où la voix le dit**.
- **Boucles de fond** : (1) quelque chose de petit vit dans l'interface pendant la tenue (une barre de progression, un curseur, un compteur) ; (2) si l'on a choisi les taches de lumière, leur dérive lente. **Pas de cartes qui flottent, pas de poussée lente et continue pour meubler** : après l'arrivée, on s'arrête.
- **Autorisés** : courbes d'accélération `#009` (ressorts), travelling avant `#027` (lent : environ 0,9 s ; rapide : 0,28 s, seulement pour une révélation ou une comparaison), suivi latéral `#029` entre deux zones (0,7 s), compteur `#007`, reflet de lumière `#022`, morphing de forme `#012` (la pastille), raccord de forme `#042`, transition entre vues `#161` (élément partagé), plan fixe `#175`, décalage en cascade `#002` (cartes à 0,1 s d'écart).
- **Interdits** : rebond marqué `#123`, flottement décoratif `#096`, dégradé animé `#095` comme seul contenu, fondu enchaîné `#044` entre deux textes (on voit deux couches de mots superposées), trois poussées vers l'avant d'affilée, particules `#015`.
- **Ressorts** : rebond de 0 par défaut ; 0,15 pour une entrée de carte (durée 0,75 s) ; 0,3 se voit ; au-delà de 0,4, cela fait bon marché. La pastille : largeur et hauteur sur **deux ressorts séparés**, ouverture douce, fermeture sans dépassement ; si elle se rouvre avant d'avoir fini de se fermer, elle repart **de là où elle est**.
- **Nombre qui tombe** : 0,17 s (échelle 1,55, puis 0,94, puis 1). **Compteur** : 0,9 s, décélération forte (le dernier chiffre se pose lentement), chiffres à largeur fixe. Un même nombre ne se compte qu'une fois.
- **Texte** : apparition depuis un flou de 18 à 26 px, montée de 16 à 40 px, en 0,7 à 1 s ; surtitre, nom, sous-titre décalés de 0,2 à 0,4 s. À ne pas répéter sur chaque écran.

## 5. Rythme et montage

- **Durée des plans** : 5 à 8 s en rythme de présentation ; 1,5 à 3 s en montage rapide ; environ 2,5 s par scène pour la variante « pastille », 6 à 8 scènes (une fonction + une phrase courte chacune).
- **Un écran, une chose** : un nom, un chiffre, une carte. Après un passage dense, un écran vide pour respirer.
- **Calage sur la voix** : le texte commence à apparaître 0,2 à 0,3 s **avant** le nom (l'apparition dure 0,7 s : il est net quand on le dit) ; début du compteur = instant où le chiffre est dit − durée du compteur.
- **Transitions** : (1) **poussée floue** : l'ancien plan rétrécit à 0,92 et se floute, le nouveau arrive de 1,06 à 1, en 0,55 s ; (2) **élément partagé** : la carte choisie s'ouvre depuis son propre rectangle jusqu'au plein écran, rayon de 38 à 0 ; (3) raccord de forme (le nom du produit à la place du titre de la carte) ; (4) la nouvelle image arrive derrière un balayage de lumière.
- **Version courte (8 à 12 s)** : prendre le rythme « montage rapide » : trois ou quatre scènes de 2,5 s (une fonction, une phrase), puis le nom ou le chiffre tenu 2 s ; laisser de côté le rythme de présentation (5 à 8 s par plan).

## 6. Recette technique

- **Moteur** : HyperFrames, éléments HTML/CSS animés par GSAP (captures en `<img>`, texte en balises, ressorts par `CustomEase` ou par une fonction de ressort).
- **Structure** : une scène par écran ; les captures du client dans `assets/` ; une liste de faits (`FAITS.md`) : **seuls les faits de cette liste vont à l'écran**.

```js
// ressort paramétré par durée et rebond (amortissement = 1 − rebond)
function ressort(t, { duree = 0.5, rebond = 0 } = {}) {
  const w = 2 * Math.PI / duree, z = 1 - rebond;
  if (z >= 1) return 1 - Math.exp(-w * t) * (1 + w * t);
  const wd = w * Math.sqrt(1 - z * z);
  return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t));
}
// pousser dans une capture vers une zone (x, y, largeur en pixels de la capture)
const pousser = (zone, duree = 0.9) => tl.to("#capture", { scale: 990 / zone.l, x: -zone.x * 990 / zone.l, y: -zone.y * 990 / zone.l,
                                                         transformOrigin: "0 0", duration: duree, ease: "power2.inOut" }, tDit(zone.mot) - duree);
```

- **Pièges** : sous une poussée floue ou une ouverture de carte, **glisser d'abord une copie agrandie (1,08) et très floutée de l'ancien plan**, sinon des bords noirs apparaissent ; le nouveau plan doit être **opaque dès sa première image** dans la carte qui s'ouvre ; un flou tire des pixels transparents depuis l'extérieur du cadre et casse le déterminisme s'il s'accumule ; du « verre » sur un fond uni n'est qu'un rectangle gris (le verre ne floute que ce qui est derrière lui) ; l'unité collée au nombre quand le compteur change de largeur ; pour la variante pastille, **nommer la pastille dans le plan de scène** (« la pastille en haut au centre de l'écran »), sinon on obtient un ordinateur entier.

## 7. Son

- **Musique** : nappe sobre et pulsation discrète, piano feutré ou synthétiseur doux ; une montée légère sur la dernière phrase.
- **Bruitages** : un souffle court sur une poussée de caméra, un impact feutré quand un nombre tombe, des tics fins pendant un compteur (un seul son continu, pas un par chiffre), un scintillement sur le balayage de lumière, un « pop » doux à l'ouverture de la pastille. Deux ou trois par écran au plus.
- **Silence** : une demi-seconde avant le chiffre principal.
- **Voix** : c'est elle qui commande. Phrases courtes : un nom, un chiffre.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Les trois fautes classiques : du verre sans rien derrière ; des ressorts trop élastiques et trop de choses en mouvement ; de grandes lettres non serrées et des taches de lumière boueuses.

- [ ] Chaque écran dit une seule chose.
- [ ] S'il existe des captures du produit, elles sont le plan principal, à 90 % de la largeur au moins.
- [ ] Deux habillages « à effet » au plus dans tout le film.
- [ ] Chaque nom et chaque chiffre se pose à l'instant où la voix le dit.
- [ ] Après une arrivée, l'image s'arrête : ni flottement, ni poussée lente.
- [ ] Aucune mise en page ne revient deux fois de suite.
- [ ] Tous les mots et chiffres à l'écran viennent de la liste de faits du client.
- [ ] Aucun bord noir pendant les transitions ; carton de fin visible 1,2 s au moins.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Grammaire « interface de keynote », planche de la démo (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t2_keynote_ui_总览.jpg — crédit : 花叔 Huashu (alchaincyf).
- Film de lancement à pastille : aperçu animé dans le fichier README de l'auteur, https://github.com/charlie947/motion-graphics-skills (fichier `assets/readme/demo-launch.gif`) — crédit : Charlie Hills.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/t2_keynote_ui.md`, `scripts/engine/demos/t2_keynote_ui/`, `scripts/engine/lib/ui.js`, `motion.js`. Licence MIT (© 2026 alchaincyf, 花叔).
- Dépôt `charlie947/motion-graphics-skills`, commit `229022e`, fichier `skills/apple-launch-film/SKILL.md`. Licence MIT (© 2026 Charlie Hills).
- Police Inter : OFL 1.1.
- Adaptation Flot Web : fusion des deux sources, traduction du chinois et de l'anglais, interface générique à la place des éléments d'un système réel, composition verticale, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
