# Parcours en plan-séquence (un héros traverse le produit)

## 1. Identité
- **Nom** : Parcours en plan-séquence. Identifiant : `parcours-plan-sequence`.
- **Inspiration** : les boucles d'interface hypnotiques où une bille traverse une suite de petits mécanismes qui réagissent à son passage.
- **Principe** : une histoire visuelle en une seule prise. **Un seul élément héros** (par défaut une bille blanche, qui commence comme le bouton d'un interrupteur) voyage à travers une chaîne de petites **stations** d'interface, et chaque station réagit : il roule le long d'un curseur de réglage et le pousse à 100, tombe du bout et rebondit sur une pile de notifications qui surgissent à son passage, atterrit sur un clavier et saute de touche en touche en tapant un mot, appuie sur « Entrée » et repart dans les airs. **La caméra ne coupe jamais** : elle garde le héros près du centre, zoome sur chaque interaction, et au sommet elle recule très loin pour montrer tout le parcours d'un coup, avant de replonger là où tout a commencé.
- **Pour un produit** : les stations sont **les étapes de son fonctionnement**, posées dans l'espace sur une seule grande toile, et le héros est ce qui circule dans ce fonctionnement. Le recul est le moment « maintenant tu comprends comment ça marche ».
- **Pour quels sujets** : montrer un parcours en 3 à 6 étapes (ce que fait l'utilisateur → ce que fait le produit → le résultat), boucle pour les réseaux, vidéo d'accueil d'un site.
- **Ne marche pas pour** : un produit sans enchaînement d'étapes, un message qui demande du texte explicatif, une liste de fonctions sans lien entre elles.

## 2. Palette, typographie, matières
- **Palette par défaut (sombre)** : toile `#0C0C0E`, grille de points `#1E1E22`, surfaces `#1C1C1F` / `#2C2C2E`, texte `#F2F2F7`, secondaire `#8E8E93`, accent `#0A84FF`, héros blanc `#FFFFFF`. L'accent devient celui de la fiche « ma chaîne » ; **le héros reste l'élément le plus lumineux de l'écran**. Variante claire possible (toile `#F2F2F4`, héros = accent).
- **La grille de points** bouge avec la caméra : c'est elle qui rend les mouvements de caméra lisibles.
- **Interface d'allure réelle** : interrupteurs, curseurs de réglage gradués, cartes de notification (carré d'icône, titre, ligne de texte, « maintenant »), clavier avec ses touches. Police : Inter ou Geist.
- **Le héros** : un objet simple et lisible dont parle l'histoire du produit, qui **ne disparaît jamais et n'est jamais remplacé** (il peut changer de forme un instant puis revenir) : bille ou bouton (par défaut, marche pour tout), curseur de texte, tuile de fichier, bulle de message, pièce ou commande, point de donnée.
- **Les libellés des stations racontent l'histoire** en quelques mots, avec un peu d'esprit, écrits depuis le vrai fonctionnement du produit (« Agent · écrit 12 fichiers », « Aperçu · prêt », « En ligne à l'adresse… »).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Geist ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/geist` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).

## 3. Composition 9:16
- **Une grande toile d'environ 3 fois le cadre**, stations placées dans l'ordre de visite. En vertical, le parcours **descend en zigzag** (ce qui tombe bien : la gravité va vers le bas) : droite en haut, descente au milieu, traversée en bas, puis le lancer qui remonte tout. Toile type : 2400×5200.
- Chaque station garde sa place pendant toute la vidéo.
- **Zoom serré pendant une interaction** : la station occupe 70 à 85 % de la largeur du cadre et le héros fait **70 à 100 px à l'écran** (la source dit 50 à 70 px en 1080p horizontal). Un peu plus large pendant les chutes et les sauts, pour que la station suivante soit déjà visible. Cadrer la station, pas de la toile vide.
- **Le héros ne quitte jamais la moitié centrale du cadre** (x 270 à 810, y 480 à 1440).
- **La révélation** : cadrage fixe qui contient tout le parcours (≈ 0,3×), avec une légère bascule 3D (15 à 25°) ; le héros est grossi et reçoit un halo doux pour rester le plus visible (**au moins 34 px à l'écran**).
- **Aucun texte par-dessus** qui expliquerait ce qui se passe : les libellés des stations sont le seul texte (≥ 30 px à l'écran pendant leur interaction).
- Zones d'interface : pendant chaque interaction, la station et son libellé restent entre y 170 et y 1550, à gauche de x 945.

## 4. Ce qui bouge
- **Action principale** : le trajet du héros, **fonction pure du temps**, fait de segments entre des **points de contact** (chaque contact sur un temps de la musique).
- **Boucles de fond** : (1) la grille de points qui défile avec la caméra ; (2) la caméra qui suit, sans jamais s'arrêter.
- **Mécanique → réaction de la station** :

| Mécanique | Le héros… | La station réagit |
|---|---|---|
| Interrupteur, bouton | est le bouton, ou l'enfonce | s'allume, la couleur se remplit |
| Curseur de réglage, progression | roule le long | la valeur compte dans une bulle, la piste se remplit |
| Pile de notifications | tombe et rebondit sur chaque carte | chaque carte surgit quand elle est touchée, avec un message qui raconte |
| Clavier, champ | saute de touche en touche | chaque touche s'enfonce, les lettres apparaissent |
| Liste, tableau | glisse le long des lignes | chaque ligne se surligne, se coche ou se trie |
| Graphique | devient le point de tête de la courbe | la courbe se trace derrière lui |
| Messagerie | arrive en bulle | la réponse se tape |
| Bouton « envoyer » | est lancé par lui | une notification ou une adresse apparaît |

- **Roulement** : position par amorti le long de la piste ; la valeur de la station **est dérivée de la position du héros**.
- **Sauts et chutes** : une parabole (`x` linéaire dans le temps, `y = y0 + v·t + ½·g·t²`, en résolvant `v` pour atterrir sur le contact suivant au temps voulu). **Gravité constante dans toute la vidéo.**
- **Impacts** : écrasement au contact (1,25 × 0,8 pendant ~60 ms, retour en ressort), étirement le long de la vitesse en vol (jusqu'à 1,15 × 0,9), et un petit enfoncement de ce qui a été touché.
- **Le lancer** : la dernière station projette le héros vers le haut et vers le départ en un long arc **au ralenti** (le plus lent au sommet, souvent 5 à 10 fois), pendant que toutes les stations **se réinitialisent à l'envers** derrière lui (valeurs qui décomptent, notifications qui partent, champ qui se vide), **pendant la tenue de la révélation**, pas à l'instant du lancer.
- **L'emplacement vide** : quand le héros faisait partie d'une station et la quitte, elle garde le contour pâle de l'emplacement, qui se remplit à son retour.
- **Autorisés** : #011 écrasement et étirement, #121 anticipation, #122 suivi d'élan, #123 rebond (physique, sur le héros seulement), #126 trajectoire, #174 caméra qui suit, #028 zoom, #037 ralenti (le lancer), #172 plan-séquence, #127 boucle, #007 compteur dérivé de la position.
- **Interdits** : coupes, fondus au noir, texte explicatif par-dessus, plus d'un héros, station qui ne réagit pas, physique « flottante », rebonds sur les éléments d'interface eux-mêmes.

## 5. Rythme et montage
- **12 secondes par défaut, en boucle sans couture** ; de 10 à 30 s (**plus long = plus de stations, pas des stations plus lentes**).
- Groove serré à 110-120 BPM : chaque contact du héros tombe sur un temps.
- **Tenue du résultat** : avant le lancer, tenir 0,4 à 0,6 s sur le résultat final (la notification, l'adresse en ligne), entièrement dans le cadre.
- **Révélation** : ~1 s de tenue sur tout le parcours pendant que le héros le traverse en arc ; puis plongée vers la première station, réglée pour que le héros y atterrisse quand la caméra arrive.
- **Jointure de la boucle** : sur l'atterrissage du héros à la première station ; l'image de fin doit être exactement l'image de début (l'écrasement d'atterrissage se voit donc aussi à l'instant 0).

## 6. Recette technique
- **Moteur** : HyperFrames ; toute la scène (héros, stations, caméra) est dessinée depuis `hf-seek` comme fonction pure du temps (DOM avec transformations, ou canvas).
```js
// un saut entre deux contacts : parabole résolue pour atterrir pile au temps voulu
function saut(a, b, t) {                         // a, b : {x, y, t} ; gravité G commune à toute la vidéo
  const d = b.t - a.t, u = (t - a.t) / d, tau = u * d;
  const v = (b.y - a.y - 0.5 * G * d * d) / d;
  return {x: a.x + (b.x - a.x) * u, y: a.y + v * tau + 0.5 * G * tau * tau};
}
// caméra : mélange du héros (avec 0,15 s d'avance) et de l'ancre de la station, lissé, CALCULÉ UNE FOIS au chargement
const cible = t => melange(avance(heros, t, 0.15), ancre(stationA(t)), poids(t));   // 0,7 en interaction, 0,15 en vol
const CAMERA = precalculer(cible, DUREE, 1 / 240);                                  // ressort amorti (raideur ≈ 6), puis relu
window.addEventListener("hf-seek", e => dessiner(e.detail.time % DUREE, lire(CAMERA, e.detail.time % DUREE)));
```
- **La caméra est la partie difficile : la régler avant de soigner quoi que ce soit d'autre.** Son lissage a besoin d'un passé : il est donc **calculé une fois au chargement** (pas à pas de 1/240 s) puis relu avec interpolation. Poids vers l'ancre : ~0,7 pendant une interaction, ~0,15 pendant les chutes, ~0,85 sur la tenue du résultat.
- **Révélation** : la caméra cesse de suivre et rejoint un cadrage fixe, avec `perspective` + `rotateX` de 15 à 25°.
- **Ralenti du lancer** : choisir d'abord la hauteur du sommet (elle fixe la durée réelle du vol), puis déformer le temps pour que ce vol remplisse la fenêtre de révélation.
- **Gravité vue de côté** : les cartes de notification forment un escalier (chacune décalée de plus que sa largeur, pour que le héros n'en traverse aucune) ; le clavier est vu de face.
- **Flou de mouvement** du moteur : le héros et le monde filent sur les mouvements rapides, cela fait partie du look.
- **Pièges** : `seek(durée)` ≠ `seek(0)` (boucle qui accroche) ; héros qui sort de la moitié centrale ; station cadrée trop large (le héros devient minuscule) ; caméra qui sursaute aux impacts (lissage trop faible) ; réinitialisation des stations trop tôt (le spectateur n'a pas vu le parcours complet).
- **Vérité des contenus** : libellés tirés du vrai fonctionnement ; aucun chiffre ni adresse inventés présentés comme réels (`references/script-de-lancement.md` §4).

## 7. Son
- **Les contacts du héros sont l'instrument principal** : chaque impact joue un tic accordé ou une note de marimba (**la hauteur monte à mesure que l'histoire avance**), les touches cliquent, le curseur de réglage égrène de fins tics qui accélèrent avec la valeur, les notifications font un petit « pop », le lancer un souffle montant, la plongée un souffle descendant. **Chaque son tombe exactement sur son contact visuel.**
- Groove minimal dessous : grosse caisse douce, charleston sec, basse pincée étouffée.
- **Dérogation au budget de bruitages** : ici les contacts sont la mélodie ; les compter comme de la musique (ils sont sur la grille et accordés). Vrais enregistrements d'abord (notes de marimba, clics de clavier réels), synthèse en repli.
- Boucle : replier la queue des sons qui dépassent la fin sur le début, pour que la jointure ne claque pas. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Aucune coupe, aucun fondu : une seule prise du début à la fin.
- [ ] Un seul héros, toujours visible, toujours dans la moitié centrale du cadre.
- [ ] Chaque station change visiblement **à cause** du héros ; aucune ne reste inerte.
- [ ] Gravité constante ; chaque contact tombe sur un temps (écart ≤ 1 image) avec son son.
- [ ] Tenue de 0,4 à 0,6 s sur le résultat avant le lancer ; révélation de tout le parcours ≥ 1 s.
- [ ] Boucle parfaite : dernière image = première image.
- [ ] Aucun texte explicatif par-dessus ; libellés des stations lisibles pendant leur interaction.
- [ ] Le héros fait au moins 70 px en interaction et 34 px pendant la révélation ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 30

## 9. Aperçu
- GIF de démonstration du dépôt d'origine : https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-engaging.gif. Crédit : Bart, dépôt sous licence MIT. Lien seulement ; aperçu Flot Web en 9:16 à produire.

## 10. Origine
- Dépôt : Barty-Bart/motion-graphics, commit `3d83d98`. Fichier : `skills/explainer-engaging/SKILL.md`.
- Licence : MIT (© 2026 Bart).
- Adaptations Flot Web : français, **réécrit pour HyperFrames**, toile verticale en zigzag descendant, tailles relevées pour le téléphone, vrais enregistrements d'abord, −14 LUFS.
