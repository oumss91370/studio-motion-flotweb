# Nombre-jalon

## 1. Identité

- **Nom** : Nombre-jalon (un cap franchi, révélé en particules).
- **Inspiration** : les annonces de cap des créateurs et des marques (« 10 000 abonnés », « 1 000 clients »), traitées avec le sérieux d'un lancement de produit haut de gamme plutôt qu'avec des confettis.
- **Ce qui le fait reconnaître** : **des milliers de points minuscules dérivent comme un ciel de nuit**, se rassemblent en **un vrai nombre**, un filet se trace dessous, le libellé se pose ; l'ensemble tient, scintille, puis les points se dispersent **exactement** jusqu'à leur place de départ. **Chaque point est une personne** : un abonné, un client, un euro.
- **Ton** : premium, pas la fête. Aucun rebond, aucun dépassement, aucun confetti, aucune gerbe d'étincelles.
- **Marche pour** : fêter un cap (abonnés, clients, chiffre d'affaires, téléchargements, années d'existence), ouvrir ou fermer un bilan, illustrer « le chiffre du mois » dans une vidéo plus longue.
- **Ne marche pas pour** : plusieurs chiffres (voir `graphique-anime`), un chiffre qu'il faut expliquer (voir `keynote-produit`), **un chiffre sans source** : pas de source, pas de vidéo.
- **Règle d'honnêteté, non négociable** : le nombre est le vrai nombre du client, tel que le montre son tableau de bord. On ne l'arrondit jamais vers le haut, on n'ajoute jamais « + », on ne remplace jamais un résultat par un objectif. Si la source dit 12 431, la vidéo dit 12 431, ou le client choisit lui-même un chiffre rond **inférieur**.

## 2. Palette, typographie, matières

Trois couleurs, toutes prises dans la fiche « ma chaîne » du client (skill `marque`) :

| Rôle | Exemple sombre | Exemple clair |
|---|---|---|
| Fond | `#0b0d12` | `#f6f1e7` |
| Points et nombre (encre) | `#f3efe6` | `#1a1a1e` |
| Filet d'accent | couleur de la marque, par exemple `#ffb23f` | couleur de la marque |

(Valeurs d'exemple : la source ne fixe pas de palette, elle demande celle du client.) Éviter un fond bleu-violet en dégradé.

- **Police** : celle du client, en **graisse grasse** pour le nombre (c'est sa silhouette qui sert de cible aux points) ; le fichier de police doit être fourni et chargé depuis le projet. **Si la police manque, s'arrêter et la demander.** À défaut : Inter Tight 800 (libre).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Points** : environ **3 200** en 1080×1350 dans la source ; compter **4 000 à 4 500** en 1080×1920 pour un nombre de même largeur. Opacités variées, léger scintillement. **Environ 85 % des points vont au nombre** (2 700 sur 3 200), chacun de 2,5 px à opacité presque pleine ; le reste demeure en étoiles plus pâles qui dérivent.
- **Seul texte à l'écran** : le nombre et son libellé. Rien d'autre.
- **Matières** : aucune texture ; pas de lueur diffuse autour du nombre.

## 3. Composition 9:16

- Le nombre est **centré, entre y 720 et y 1000** ; il occupe **800 à 860 px de large** au plus (x 110 à 945), séparateur de milliers compris.
- **Écriture française du nombre** : espace entre les milliers (« 250 000 », et non « 250,000 »), virgule décimale, symbole après (« 12 431 € »). Le nombre s'affiche **exactement** comme le client le valide.
- **Nombre long** (7 chiffres ou plus) : réduire la taille plutôt que de couper ; en dessous de 150 px de haut, passer sur deux lignes (le nombre, puis l'unité).
- **Filet d'accent** : fin (4 à 6 px), sous le nombre, de sa largeur, à 40 px en dessous.
- **Libellé** : mot pour mot celui du client (« abonnés », « clients servis »), 54 à 64 px, sous le filet, vers y 1100 à 1180.
- Les étoiles libres occupent tout le cadre, y compris hors de la zone utile : elles ne portent aucune information.
- Rien d'autre : pas de logo, pas de sous-titre, pas de date (la source du chiffre va dans la légende de la publication).

## 4. Ce qui bouge

- **Action principale** : les points sont attirés vers le nombre, **comme par une gravité, pas comme un claquement** : un long amorti, en cascade.
- **Boucles de fond** : (1) la dérive lente et le scintillement des points libres ; (2) pendant la tenue, le nombre **scintille seulement** (l'opacité des points varie un peu).
- **Autorisés** : particules `#015`, courbes d'accélération `#009` (amorti long), décalage en cascade `#002`, tracé de ligne `#004` (le filet, de gauche à droite), révélation en fondu avec montée de 12 px pour le libellé, boucle aller-retour `#127`, plan fixe `#175`, flottement `#096` des points libres.
- **Interdits** : rebond `#123`, dépassement `#010`, éclat `#003`, confettis, secousse `#024`, lueur `#022`, compteur `#007` qui fait défiler de faux chiffres (le nombre **se forme**, il ne se compte pas), zoom, toute coupe.
- La caméra ne bouge pas.

## 5. Rythme et montage

Boucle parfaite de **12 secondes** :

| Temps | Ce qui se passe |
|---|---|
| 0 à 2 s | les points dérivent ; rien d'autre |
| 2 à 6,5 s | les points se rassemblent en nombre, long amorti, départs décalés |
| 6,5 à 7,5 s | le filet d'accent se trace de gauche à droite |
| 7,5 à 8,5 s | le libellé apparaît en montant de 12 px environ |
| 8,5 à 10,5 s | tenue ; le nombre scintille |
| 10,5 à 12 s | libellé et filet s'effacent ; les points retournent à leur place de départ exacte |

- **L'image de la seconde 12 est identique à celle de la seconde 0** : la boucle n'a pas de saut.
- **Dans une vidéo verticale rythmée**, 12 s c'est long : ne garder que le rassemblement accéléré (2 à 2,5 s), le filet et le libellé (1 s), et une tenue de 1,5 à 2 s ; pas de retour.
- Une seule scène, aucune transition.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`.
- **Structure** : un seul fichier de scène ; `cibles` calculées une fois au chargement ; tout le reste en fonction du temps.

```js
// 1) cibles : on dessine le nombre en gras hors écran, et on échantillonne ses pixels remplis
const tampon = document.createElement("canvas").getContext("2d", { willReadFrequently: true });   // rendu identique à chaque lecture
tampon.font = `800 ${taille}px "PoliceClient"`; tampon.fillText(NOMBRE, 0, taille);
const cibles = melangerAGraine(pixelsRemplis(tampon, 3), GRAINE).slice(0, Math.round(N * 0.85));
// 2) chaque point : une place de départ à graine, une cible (ou aucune), un retard à graine
const points = Array.from({ length: N }, (_, i) => ({ depart: placeAGraine(i), cible: cibles[i] || null, retard: hasard(i) * 1.6 }));
// 3) position = fonction du temps seul ; aller de 2 s à 6,5 s, retour de 10,5 s à 12 s
function position(p, t) {
  const derive = { x: Math.sin(t * 2 * Math.PI / 12 + p.phase) * 6, y: Math.cos(t * 2 * Math.PI / 12 + p.phase) * 6 };   // période de 12 s : boucle exacte
  if (!p.cible) return somme(p.depart, derive);
  const aller = adoucirLong(borner((t - 2 - p.retard) / 2.9)), retour = adoucir(borner((t - 10.5) / 1.5));
  return melange(somme(p.depart, derive), p.cible, aller * (1 - retour));
}
```

- **Techniques clés** : une graine fixe pour chaque position ; la dérive et le scintillement ont des périodes qui **divisent 12 s** ; attendre le chargement de la police avant de calculer les cibles.
- **Pièges** : un nombre **gris et mou à taille téléphone** quand trop peu de points couvrent chaque chiffre (donner 85 % des points au nombre, 2,5 px, presque opaques) ; le navigateur peut dessiner la même image de deux façons après des lectures de pixels répétées (créer le tampon avec l'option de lecture fréquente) ; un `Math.random()` au moment du rendu rend chaque export différent et casse la boucle ; **mesurer** la jointure (zéro pixel de différence entre l'image 0 et l'image 12 s), ne pas la juger à l'œil ; l'espace des milliers doit rester visible (ne pas laisser des points le combler).
- **Contrôle** : capturer les images à 0, 2, 4,5, 6,5, 7,5, 9,5, 11 et 12 s ; vérifier que le nombre se lit exactement, que rien n'est coupé ni superposé.

## 7. Son

- **Musique** : une nappe douce qui monte lentement pendant le rassemblement et se pose sur un accord au moment où le nombre est formé. Pas de fanfare.
- **Bruitages** : trois au plus : un scintillement très fin pendant que les points convergent (un seul son continu), une note claire ou un léger tintement quand le nombre se fige, un frottement doux sur le tracé du filet.
- **Silence** : les deux premières secondes sont presque silencieuses ; c'est ce calme qui donne son poids au nombre.
- **Voix** : aucune en mode boucle. Dans une vidéo, la voix dit le nombre à l'instant où il est formé.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le nombre est exactement celui de la source, que le client a montrée (capture ou lien).
- [ ] Aucun « + », aucun arrondi vers le haut, aucun objectif présenté comme un résultat.
- [ ] Le nombre se lit nettement à taille téléphone, espace des milliers compris.
- [ ] Seuls le nombre et son libellé sont écrits à l'écran.
- [ ] Aucun rebond, aucun dépassement, aucun confetti ; le rassemblement est long et amorti.
- [ ] La dernière image est identique à la première (en mode boucle), vérifié par mesure.
- [ ] Deux rendus de la même seconde donnent exactement la même image.
- [ ] Le nombre tient entre x 110 et x 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Aperçu animé de l'auteur : https://github.com/charlie947/motion-graphics-skills/blob/main/assets/readme/demo-milestone.gif
- Crédit : Charlie Hills, https://github.com/charlie947/motion-graphics-skills (licence MIT).

## 10. Origine

- Dépôt `charlie947/motion-graphics-skills`, commit `229022e`, fichier `skills/milestone-reveal/SKILL.md` ; voir aussi l'effet 16 « Logo en particules » dans `references/effets.md`.
- Licence : MIT (© 2026 Charlie Hills).
- Adaptation Flot Web : traduction, format vertical et nombre de points recalculé, écriture française des nombres, version courte pour vidéo rythmée, portage vers HyperFrames, numéros de mouvements, section son.
