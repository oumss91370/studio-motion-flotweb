# Terminal ASCII

## 1. Identité

- **Nom** : Terminal ASCII (écran cathodique monochrome).
- **Inspiration** : les terminaux monochromes et les journaux de téléscripteur des années 1970-1980 (texte tapé, curseur, lignes d'état), l'art ASCII (des images faites de la densité des caractères), les musiques de film au synthétiseur analogique du début des années 1980. On ne recopie le texte d'interface, les polices ni les logos d'aucun film, et on ne nomme aucune agence réelle.
- **Ce qui le fait reconnaître** : un seul écran, **ambre** (ou vert) sur verre sombre, bombé sur les bords, avec des lignes de balayage. **Chaque image, titre, paysage, visage, sous-titre, est faite de vrais caractères posés sur une grille** et choisis selon leur densité d'encre. Il n'y a qu'une caméra : la **taille de la police**. Plus gros = on s'approche ; plus petit = on s'éloigne.
- **Ambiance** : froide, patiente, calme comme une machine ; du texte tapé, un curseur qui clignote en guise de suspense, et une seule surprise chaleureuse.
- **Marche pour** : outil pour développeurs, science-fiction, marque technique, journal de bord (lancement, migration, sauvetage raconté par ses horodatages), message intime tapé au clavier.
- **Ne marche pas pour** : produit qu'il faut voir, sujet coloré ou gourmand, public enfant, texte long. **Jamais** une image passée dans un « filtre ASCII ». Ce n'est pas la pluie verte des films de pirates informatiques, ni du pixel art, ni un affichage tête haute de science-fiction.

## 2. Palette, typographie, matières

- **Un seul phosphore** porte tout, dans sa propre échelle de luminosité.

| Phosphore | Sombre → normal → surexposé |
|---|---|
| Ambre | `#7a3200` → `#ffb000` → `#fff3d6` |
| Vert | `#0b4d1c` → `#33ff66` → `#eaffea` |
| Blanc | `#5a5a58` → `#e8e8e0` → `#ffffff` |
| Verre éteint | noir chaud `#0a0806` |

- **Au plus une seconde couleur douce**, pour une seule chose (l'objet émouvant), allumée à un seul moment, sur un temps fort, et jamais retirée à la légère. Exemples : écran ambre + blanc bleuté glacé pour quelque chose de lointain ; écran vert + rose chaud pour un être vivant.
- Le seul autre outil est la luminosité : atténué, normal, gras, et vidéo inverse.
- **Police** : une seule, à chasse fixe et d'aspect bitmap : VT323 (libre). Cellule de 0,4 em × 0,8 em (rapport 1:2).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Space Mono à la place de VT323. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/vt323` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Échelle de densité** : la couverture d'encre mesurée de chaque caractère, en trois luminosités, donne environ 20 niveaux. Les cellules sous un seuil restent vides : **c'est le vide qui rend l'art ASCII lisible**.
- **Tube cathodique** (traitement final) : couleur le long de l'échelle du phosphore, halo à plusieurs niveaux, lignes de balayage fines, légère courbure en barillet, masque arrondi, reflet faible, scintillement d'environ 1 %. **Pas de grille rouge-vert-bleu** : un tube monochrome n'en a pas.
- **Rémanence** : un texte qui disparaît s'éteint en 0,1 s environ.

## 3. Composition 9:16

- L'écran est dessiné **en portrait**, comme un moniteur pivoté. Le nombre de colonnes change par plan :

| Plan | Colonnes sur 1080 px | Taille d'un caractère |
|---|---|---|
| Titre | 10 à 12 | environ 90 à 108 px de large |
| Terminal lisible | 36 à 45 | 24 à 30 px de large |
| Image en caractères | 110 à 160 | 7 à 10 px de large |

(Les 80 colonnes classiques donneraient des lettres de 13 px : illisible sur téléphone. En 16:9, garder 20 / 80 / 200 colonnes.)

- Le texte reste dans la zone sûre à l'intérieur de la courbure : x 80 à 945, y 180 à 1540.
- **Sous-titres = sortie du terminal** : une **bande JOURNAL** réservée, entre y 1380 et y 1540 : un séparateur atténué, une étiquette en vidéo inverse, une invite, puis la phrase en capitales à 46 px environ, **tapée mot par mot en même temps que la voix**. Elle vit hors de la grille qui zoome, comme une ligne d'état. Quand personne ne parle, elle montre l'état du système (barre de progression, message d'attente).
- Sujets reconnaissables : des **silhouettes**, pas du bruit. Sombre = caractères rares et atténués ; clair = caractères denses et gras ; côté ombre = des points seulement. Loin = plus sombre et plus clairsemé ; un fin liseré clair sépare les plans.

## 4. Ce qui bouge

- **Action principale** : du texte se tape, et la grille change d'échelle (la caméra).
- **Boucles de fond** : (1) le curseur qui clignote ; (2) la physique du tube (scintillement, rémanence, léger bruit).
- **Autorisés** : machine à écrire `#006`, compteur `#007` (rouleau de chiffres, rapide puis ralenti), brouillage de texte `#129`, pixellisation `#141` (texte qui devient image quand la grille rétrécit), travelling avant `#027` et zoom `#028` par la taille de police, très gros plan `#184` (pousser dans un seul caractère fait de texte plus petit), coupe sèche `#046` (effacement d'écran), plan fixe `#175`, particules `#015` seulement dans un moment de transformation annoncé.
- **Interdits** : fondu enchaîné `#044` entre deux écrans, parallaxe `#016`, orbite `#030`, rebond `#123`, flou de mouvement, lignes vectorielles et panneaux flottants, tout caractère hors grille en dehors du moment de transformation.
- Seules trois choses bougent en continu : l'échelle de la grille, la physique du tube, les particules d'une transformation. Tout le reste saute de cellule en cellule.
- **La vitesse de frappe est un jeu d'acteur** : la machine tape vite et régulièrement (10 à 40 ms par caractère) ; les phrases dramatiques ralentissent sur des valeurs de notes ; la frappe humaine est irrégulière, avec des pauses et des rafales.
- Allumage : un point, une ligne, puis l'image. Extinction : retour au point.

## 5. Rythme et montage

- Lent et patient : plans de 4 à 10 s. Le silence est l'instrument principal.
- Les coupes se font **sur l'écran** : effacement, redessin, défilement, mise sous tension.
- Pousser dans un caractère : tenir là où le caractère entier se lit, puis pousser jusqu'à ce que son texte intérieur se lise.
- La seconde couleur arrive une fois, sur un temps fort, avec un accord qui s'ouvre.
- **Version courte (8 à 12 s)** : un écran : mise sous tension (0,5 s), une ligne tapée, la poussée dans un caractère ; 1 s de silence au plus ; couper l'effacement et le redessin. Accroche : le curseur tape avant 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D pour la grille + passe WebGL pour le tube.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `term.js` (atlas de caractères, dessin de la grille, échelles de densité, image → cellules), `art.js` (scènes en niveaux de gris dessinées en code pour le « négatif »), `tube.js` (traitement cathodique), `film.js` (timeline, événements, sous-titres).

```js
// image → caractères : on peint un négatif en niveaux de gris aligné EXACTEMENT sur la grille
function cellule(negatif, i, j, cw) {
  const m = moyenne(negatif, i * cw, j * 2 * cw, cw, 2 * cw);          // cellule haute de 2·cw
  const v = m + 0.9 * (m - moyenneLocale(negatif, i, j));              // contraste local : garde les contours
  return v < SEUIL ? " " : RAMPE[Math.floor(Math.pow(v, 1.25) * (RAMPE.length - 1))];
}
const centreY = j => (j + 0.5) * 2 * cw;                               // et non (j + 1) · cw
```

- **Techniques clés** : un grand atlas de caractères pré-rendu, agrandi par `drawImage`, garde les zooms continus et nets ; petit tramage par cellule ; rémanence calculée par formule (pas d'état gardé d'une image à l'autre) ; particules nées de points au hasard **dans** les caractères d'origine, petites, en fondu, qui glissent vers leur cellule.
- **Pièges** : un négatif mal aligné dérive sur des centaines de colonnes ; si chaque pixel sombre devient un caractère, on obtient des murs de `-+-+` (seuil, gamma, contraste local) ; un sujet texturé au bruit se lit comme une tache ; des particules parties du centre des lettres s'empilent en barres lumineuses ; la vidéo inverse demande un fond noir opaque ; à l'allumage, un paramètre à zéro dessine quand même le point central.

## 7. Son

- **Musique** : synthétiseur analogique original : oscillateurs en dents de scie et carrés, filtre résonant qui bouge, séquenceurs, léger pleurage de bande, longue réverbération sur les nappes. **Jamais de musique 8 bits.**
- **Le silence est l'instrument principal** : la seule ambiance de pièce sous la frappe et le curseur ; un quasi-silence court avant une transformation ; tout couper d'un coup sur un choc.
- **Bruitages** : clic de relais et bourdonnement de mise sous tension, touches de clavier mécanique (barre d'espace plus sourde, Entrée plus lourde), tics de téléscripteur, tonalités de modem, bips d'erreur, grappes de petits tics aigus pour les particules, ventilateur. Ici la synthèse est légitime : ce sont des sons de machine.
- **Voix** : si c'est la machine qui parle, la traiter (bande passante de téléphone, légère saturation) et vérifier que chaque phrase reste compréhensible. Peu de phrases, courtes.
- Pas de grain ajouté à l'export : le bruit vit dans l'image.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Tout ce qui est à l'écran est un vrai caractère sur la grille (aucune image filtrée, aucune ligne vectorielle).
- [ ] Un seul phosphore ; la seconde couleur apparaît une fois au plus.
- [ ] Aucun caractère du texte lisible ne fait moins de 24 px de large.
- [ ] Les images en caractères ont du vide : on reconnaît la silhouette en plissant les yeux.
- [ ] La caméra ne bouge que par la taille de la grille.
- [ ] La bande JOURNAL est tapée en rythme avec la voix et ne chevauche jamais l'image.
- [ ] Les transitions se font sur l'écran (effacement, défilement, extinction), sans fondu.
- [ ] La même seconde rendue deux fois donne exactement la même image.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine, *Tranquility.log* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/ascii-crt.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/ascii-crt.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/ascii-crt/STYLE.md`, `DEMO.md`, `demo/term.js`, `demo/art.js`, `demo/crt.js`, `core/post/crt.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Police VT323 : OFL 1.1.
- Adaptation Flot Web : traduction, écran en portrait et nombres de colonnes recalculés, exemples de couleurs, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
