# Tuyau de caoutchouc années 1930

## 1. Identité

- **Nom** : Tuyau de caoutchouc années 1930 (« rubber hose »).
- **Inspiration** : les courts métrages encrés à la main du début du parlant (vers 1930-1933), où « le monde entier danse », et la finition moderne de ce look par les jeux vidéo récents qui le reprennent. On emprunte la grammaire, jamais un personnage, une silhouette, un nom ou une mélodie.
- **Ce que c'est** : noir et blanc encré, personnages aux **membres en tuyau** (même largeur partout, ni coude ni genou), **gants blancs à quatre doigts**, **yeux « part de tarte »** (pupille noire avec un coin découpé), grosses chaussures rondes, corps qui s'écrasent et s'étirent comme des ballons. Tout respire en rythme : meubles, machines, plantes, murs. L'image ressemble à une copie 35 mm usée projetée.
- **Marche pour** : jingle, slogan à retenir, mascotte de marque, lancement joyeux, comptine de sécurité, « making-of » dessiné, objet du quotidien qui prend vie.
- **Ne marche pas pour** : sujet grave ou technique, données chiffrées, produit haut de gamme sobre, vidéo sans musique (la musique synchronisée est le moteur du style).
- **Règle de dessin** : si le héros est un objet, **l'objet entier est le corps** (visage sur l'objet). Pas de « tête d'objet sur un corps humain ».

## 2. Palette, typographie, matières

Strictement en niveaux de gris : aucune teinte, même dans les défauts de pellicule.

| Rôle | Hex |
|---|---|
| Papier | `#F1EEE6` |
| Gris clair / moyen / moyen foncé / foncé | `#C8C5BC` · `#9A978F` · `#6B6963` · `#3B3A37` |
| Encre | `#0E0D0C` |
| Blanc des personnages | `#FCFBF7` |
| Murs, carrelage, meubles (décor) | `#8C8981` · `#A29F97` · `#66635D` à `#7C7972` |

- Les personnages possèdent les extrêmes (blanc pur, encre) ; les décors vivent dans les gris moyens. Contraste final ×1,14 : une copie des années 30 a des noirs riches, jamais un gris plat.
- Ombre de forme : **une seule bande** gris clair à bord dur, côté opposé à une lumière haut gauche. Jamais de dégradé.
- **Typographie** (polices libres OFL) : titres en **Shrikhand** (face blanche, contour encre ≈ 14 % de la hauteur de capitale, ombre portée encre en bas à droite) ; sous-titres de titre en **Limelight** capitales ; cartons en **IM Fell English SC**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Shrikhand et de Limelight ; EB Garamond à la place d'IM Fell English SC. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/shrikhand`, `@fontsource/limelight`, `@fontsource/im-fell-english-sc` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : personnages en aplats ; décors peints une fois en aquarelle grise (lavis plat, taches douces ±5 %, bords assombris, fin contour gris foncé, grain de papier), mis en cache à 1,25-1,5× pour rester nets en zoom. Motifs d'époque : papier peint à rayures, damier, briques, lambris.
- **Défauts de pellicule** (passe de composition) : flottement de fenêtre ±1,2 px avec un saut rare, scintillement ±4 %, 0 à 3 rayures verticales qui dérivent, 3 à 8 poussières par image, un poil de temps en temps, fort vignettage, petit saut à chaque coupe, léger flou.

## 3. Composition 9:16

- L'original est une fenêtre 4:3 dans un cadre 16:9. En vertical : une **fenêtre de projection à coins arrondis** (rayon ≈ 28 px) de 1000×1400 posée en x 40, y 160, sur fond noir. Ce cadre déborde de la zone utile : c'est du décor ; tout texte à lire (et le moment clé de l'action) reste entre x 60 et x 945, y 160 et y 1560. Tout le film se joue dedans ; la bande noire du bas (y > 1560) reste vide.
- Scène comme un théâtre : sol au tiers bas de la fenêtre, personnage principal à **1/4 à 1/3 de la hauteur** au minimum, visage lisible. Pas de plan très large pour un gag : en vertical, deux personnages au maximum côte à côte.
- **Sous-titres = carton d'époque** : petite plaque presque noire `rgba(12,11,10,.92)` avec double filet blanc et ornements d'angle, texte IM Fell English SC 44 px, blanc papier ; en bas de la fenêtre (y ≈ 1450) par défaut, en haut si l'action est basse. Dessiné dans la scène : il flotte et scintille avec la pellicule. Apparition et disparition sèches, sans fondu.
- Titre : 120 à 150 px, sur 2 lignes si besoin, lettres qui sautillent en vague sur le temps.
- 16:9 : fenêtre 1440×1080 centrée, bandes noires de côté.

## 4. Ce qui bouge

- **Action principale** : un personnage poursuit un but simple (attraper, livrer, réveiller), chaque pas sur une note.
- **Boucle de fond 1** : tous les objets au repos respirent sur le temps, `cos(2π × temps)`, amplitude 5 à 7 %, étirés sur le temps, écrasés sur le contretemps, tous en phase.
- **Boucle de fond 2** : léger frémissement du trait (±1,2 px, 3 dessins en cycle, « en deux » ; petite surface seulement) et défauts de pellicule.
- **Autorisés** : `#011` écrasement et étirement, `#121` anticipation (accroupi à 0,8, tenue, détente), `#122` suivi, `#123` rebond, `#136` trait qui frémit, `#012` métamorphose (une queue devient un point d'interrogation), `#029` travelling latéral qui accompagne un coureur, `#188` fermeture à l'iris, `#040` arrêt sur image quand l'orchestre s'arrête.
- **Interdits** : `#044` fondu enchaîné, `#023` glitch, `#022` balayage de lumière, `#016` parallaxe moderne lissée, toute couleur, toute articulation (coude, genou), tout ombrage en dégradé.
- Marche : un pas par temps avec rebond du corps (triste = petits pas, bras mous). Course : jambes en moulinet, buste penché, traits de vitesse.

## 5. Rythme et montage

- Choisis un tempo où **un temps = un nombre pair d'images** : à 30 i/s, 120 BPM (15 images) ne convient pas ; prends 150 BPM (12 images), 112,5 BPM (16 images) ou 90 BPM (20 images). Chaque temps tombe ainsi sur un dessin.
- Plans de 3 à 6 s, coupes franches sur un temps. Transitions du style : iris (qu'un personnage peut attraper), carton qui se roule comme un store. Aucun fondu.
- Un arrêt de l'orchestre avant chaque gros gag : tout se fige, respiration du décor comprise.
- Au pic de joie : amplitude de respiration ×3, le décor entier s'écrase (≈ 2,5 %) autour de la ligne de sol.
- **Version courte (8 à 12 s)** : un seul gag : le but, un obstacle, l'arrêt de l'orchestre (0,5 s), la chute ; **un carton au plus** (3 mots, 2 s) ; couper le titre qui sautille, ou le garder 1,5 s en ouverture et renoncer au carton. Accroche avant 3 s : le personnage marche déjà sur le temps à l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames, un canvas 2D, fonction `renderAt(t)` (voir `SKILL.md` de la catégorie).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `encre.js` (trait constant + frémissement), `persos.js` (rigs, yeux, gants, chaussures), `decors.js` (fonds en cache), `pellicule.js` (passe de défauts), `scenes.js`, `timeline.js` (temps musicaux = source unique).
- **Techniques clés** :
  ```js
  const BEAT = 60 / 150;                         // 12 images à 30 i/s
  const tq = Math.floor(t * 15) / 15;            // dessins « en deux » à 30 i/s
  const k = Math.cos(2 * Math.PI * tq / BEAT);   // respiration du décor
  ctx.scale(1 - 0.06 * k, 1 + 0.06 * k);         // autour du point d'appui de l'objet
  ```
  - Membre en tuyau : une seule courbe de Bézier de l'épaule à la main, largeur ≈ 1/20 de la hauteur du personnage, bouts ronds.
  - Gant : paume + 3 gros doigts + pouce, manchette évasée, 3 traits sur le dos. Trace tout en épais d'abord, remplis ensuite : seul le contour de l'ensemble reste.
  - Tout passer en gris **après** avoir dessiné les personnages (une seule désaturation finale), sinon un gant ou une tasse garde une teinte chaude.
  - Grain : à l'encodage, pas dans la page.
- **Pièges** : un membre dessiné derrière le corps disparaît dans la silhouette (fais-le sortir) ; des bouffées de fumée alignées se lisent comme une bulle de pensée (disperse-les, fais-les grossir) ; un corps en segments droits se voit tout de suite (lisse les courbes) ; vérifie la dernière image de chaque plan (personnage qui chevauche un accessoire du décor).

## 7. Son

- **Musique** : orchestre de danse années 30 ou ragtime : piano stride, clarinette, trompette (ouverte et sourdine « wah-wah »), trombone, tuba, banjo sur 2 et 4, caisse claire aux balais, xylophone, woodblocks, sifflet à coulisse. Aucune nappe de cordes, aucun synthé moderne. Un thème original court et syncopé, repris dans plusieurs arrangements.
- **Bruitages** (budget ≈ 5 par 10 s, les plus lisibles d'abord) : sifflet à coulisse pour un étirement ou une chute, « boing » de ressort, woodblock pour un regard, porcelaine et verre, grincement de caoutchouc. Un instrument peut « répondre » à un personnage.
- **Voix** : peu de répliques, personnage d'époque (annonceur radio, maître de cérémonie). Traitement radio : passe-haut ≈ 260 Hz, passe-bas ≈ 4,6 kHz, légère saturation.
- **Vieillissement optique** sur musique et bruitages : bande 110 Hz à 6,2 kHz, léger pleurage ; souffle, craquements et cliquetis de projecteur restent seuls dans les silences. Mix final −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : image grise et plate ; plan trop large (le gag devient illisible) ; coudes et genoux ; fondus ; musique plaquée après coup ; filtre « rétro » sur une animation moderne.

- [ ] Aucune teinte dans l'image finale (vérifier une capture désaturée : identique).
- [ ] Les blancs et les noirs les plus forts sont sur les personnages, pas sur le décor.
- [ ] Les membres ont une largeur constante et aucune articulation.
- [ ] Les objets au repos respirent sur le temps, et se figent quand la musique s'arrête.
- [ ] Chaque temps musical tombe sur une image de dessin (tempo à nombre pair d'images).
- [ ] Aucun fondu enchaîné ; au moins une transition à l'iris ou au carton.
- [ ] Personnage ≥ 1/4 de la hauteur de la fenêtre dans tout plan de gag.
- [ ] Aucun personnage, silhouette ou mélodie existants.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 11
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *Coffee Cup Chase* (50 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/rubber-hose.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/rubber-hose.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire, les plans ni les personnages.
- Carte huashu : pas d'aperçu isolé (planche commune `assets/全风格总览.jpg` du dépôt, à ne pas utiliser comme vitrine).

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/rubber-hose/STYLE.md`, `DEMO.md`, `demo/toon.js`, `film.js`, `chars.js`, `cast.js`, `bg.js`, `ui.js`. Licence MIT (code et textes), © 2026 LemoLab ; film et images CC BY 4.0.
- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/33_rubberhose.md`, `scripts/engine/scenes/33_rubberhose.js` (rebond par temps avec phases décalées, désaturation finale, valeurs de pellicule). Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : fiche fusionnée et traduite, section 9:16, tempos recalculés pour 30 i/s, numéros du dictionnaire de mouvements.
