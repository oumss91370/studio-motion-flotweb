# Symphonie en time-lapse

## 1. Identité
- **Nom** : Symphonie en time-lapse. Identifiant : `symphonie-time-lapse`.
- **Inspiration** : la tradition des « symphonies urbaines » et des films contemplatifs sans paroles portés par une musique minimaliste répétitive. Rien n'est repris de ces films : ni images, ni mélodie, ni lettrage, ni nom dans la vidéo.
- **Principe** : un film de lieu monté comme une partition. Le time-lapse change la circulation, la foule et les nuages en rivières de lumière ; les coupes se resserrent avec les subdivisions de la musique ; **une** chose fragile est ralentie presque jusqu'à l'arrêt ; le film finit par une coupe sèche au noir sur un temps fort. Pas de narrateur : la musique porte tout. « Les machines vite, les gens lentement. »
- **Pour quels sujets** : une ville, un port, un marché, un campus, une usine, un chantier, une rivière sur un an ; ouverture d'une vidéo plus longue ; film d'ambiance d'un lieu ou d'un événement.
- **Ne marche pas pour** : un sujet qui demande des explications, un produit, un portrait. Ce n'est pas un clip de voyage sur une chanson pop, ni un vlog, ni un diaporama de cartes postales.

## 2. Palette, typographie, matières
| Rôle | Valeur |
|---|---|
| Texte (blanc chaud) | `#EDE8DF` |
| Ligne secondaire | `#B0AAA0` |
| Orange sodium, seul accent (filet sous les chiffres, ligne de source, tracés de foule, aiguille de l'anneau du jour) | `#D9772F` |
| Cache et noir | `#000000` |

- **Polices libres** : Michroma en capitales très espacées (0,06 à 0,32 em) pour chiffres et titres ; sans léger pour les lignes d'explication.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place de Michroma. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/michroma` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : uniquement des images réelles (time-lapse, hyperlapse, vues aériennes, ralenti, film d'archive, photos, page scannée d'un texte ancien). Jamais d'image générée, d'archive colorisée ou restaurée.
- **Look unique « copie 35 mm »** : hautes lumières chaudes, noirs relevés (7/255), saturation 0,86, halo sur les hautes lumières (0,09 de jour, 0,15 à 0,2 de nuit), grain, flottement de ±0,5 px, vignette douce. Balance des blancs automatique **à zéro pour les plans de nuit** (sinon le sodium vire au blanc). L'archive reste en noir et blanc et passe par la même courbe.

## 3. Composition 9:16
- **Image plein cadre**, recadrée dans la source (les vues aériennes à la verticale et les rues en perspective centrale se prêtent le mieux au vertical). Agrandissement : image récente ≤ 1,5×, archive ≤ 2,5×.
- **Texte aligné à gauche**, marge x 90, jamais centré, jamais sur une boîte : la lisibilité vient d'un assombrissement elliptique très doux derrière le bloc (opacité ≤ 0,6), placé sur la moitié sombre de l'image.
- **Carte chiffre** : entre y 900 et y 1300. Nombre en Michroma 96 px (60 px si trois nombres s'empilent), filet sodium de 2 px qui pousse dessous, une ligne de 34 px qui dit ce qu'on compte et l'année de la source.
- **Année d'archive** : 28 px, en bas à gauche du panneau d'archive, au-dessus de y 1540.
- **Grille** (l'écran partagé du style) : 1×2 → 2×2 → 2×4 → 3×6 en vertical, gouttières noires de 6 px.
- **Contrepoint** : archive en haut, aujourd'hui en bas ; la gouttière pousse depuis le centre en 8 images.
- Zones d'interface : rien d'important au-dessus de y 160, sous y 1560, à droite de x 945. L'anneau du jour (anneau fin de 24 h avec aiguille sodium) se place en bas à gauche, pas à droite.
- **16:9** : cache 1,85:1 (bandes de 21 px), texte à x 168 à 196.

## 4. Ce qui bouge
- **Action principale** : la vitesse. De 0,3× à 75× ; toute vitesse au-dessus de 1× utilise le **mélange d'images** (chaque image de sortie fait la moyenne des images sources qu'elle couvre) : les phares deviennent des lignes, la foule un brouillard, les nuages de l'eau. Environ 40 % d'obturation suffit à midi (au-delà, les nuages virent à la bouillie grise).
- **Boucles de fond** : (1) le long time-lapse à caméra fixe (≥ 12 h) qui revient trois ou quatre fois et sert d'horloge ; (2) l'anneau du jour, qui se fige et s'assombrit pendant le freinage et tourne à l'envers pendant le retour en arrière.
- **Gestes** : rampe de vitesse lissée et toujours motivée (1× → 6×, ou freinage 2,2× → 0,3× en 0,55 s sur la mesure où la musique s'arrête) ; foule changée en tracés (caméra fixe seulement) ; alternance jour/nuit de la même caméra, **3 alternances par seconde au plus** (la source alternait toutes les 2 images : entre une image claire et une image sombre, sur tout le cadre, c'est un stroboscope, risque pour les personnes photosensibles) ; retour en arrière final (les plans précédents reviennent en ordre inverse, 4 images puis 2 images chacun) ; chiffre qui se verrouille un chiffre par double-croche.
- **Autorisés** : #039 time-lapse, #171 hyperlapse, #038 rampe de vitesse, #037 ralenti, #107 pose longue, #042 raccord de forme (horloge → horloge, arche → arche), #144 écran partagé, #181 vue à la verticale, #046 coupe sèche, #007 compteur.
- **Interdits** : #044 fondu (sauf ouverture depuis le noir pour la page et le carton de fin), #043 panoramique filé, #024 secousse, zoom numérique au-delà de la limite, bandeaux de noms, titres centrés.

## 5. Rythme et montage
- **La partition est le script** : écrite d'abord, avec un arc clair : répétition minimale → accélération → sommet → arrêt soudain → nouvelle accélération → arrêt net → coda calme. Tempo 96 à 132 BPM ; à 30 i/s, préférer un tempo dont le temps fait un nombre entier d'images (120 BPM = 15 images).
- **Table des coupes à 120 BPM** : croches = plans de 30 → 15 images ; triolets contre croches = 15 → 7 ou 8 ; doubles croches = cases de grille qui s'allument toutes les 1 à 2 images ; accord tenu (le freinage) = 1 ou 2 plans de 3 à 4 s ; avant l'arrêt net = 7 → 4 → 2 images. **Sécurité** : en dessous de 10 images par plan (plus de 3 coupes par seconde), n'enchaîner que des plans de luminosité voisine, pendant 1 s au plus ; jamais d'alternance clair / sombre en plein cadre.
- Toutes les heures de coupe viennent d'une seule fonction `mesure(n, temps)` ; aucune durée de plan n'est tapée en secondes. On ne coupe jamais plus vite que la subdivision en cours.
- **Coupes sèches uniquement**, plus la coupe au noir finale. Après l'arrêt net, ne pas finir sur du noir mort : une page (≈ 1 s), puis la citation sur un dernier plan en mouvement (≈ 4 s), puis le carton de fin sur ce même plan assombri.
- Texte : un titre, 2 à 4 chiffres officiels, une année d'archive, une phrase d'un vrai texte du domaine public à la fin. Chaque bloc tient au moins (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : trois mesures : répétition, accélération, arrêt soudain ; le long time-lapse fixe ne revient qu'une fois.

## 6. Recette technique
- **Moteur** : ffmpeg prépare les plans (vitesse, mélange d'images, étalonnage), HyperFrames assemble (vidéos, grille, cartes chiffres, anneau) et rend.
- **Rivière de lumière** (préparation) : intégrer la courbe de vitesse vers le temps source, puis moyenner les images couvertes ; exemple simple à vitesse constante : `ffmpeg -i plan.mp4 -vf "tmix=frames=24,setpts=PTS/40" -an plan-40x.mp4` (nuit : 40× avec ~30 images mélangées ; nuages : 37,5× avec 24).
- **Freinage en ralenti** : `minterpolate` (compensation de mouvement) pour les sujets doux ; simple fondu des deux images voisines pour les lignes fines (câbles, rails, texte), que la compensation déchire.
- **Grille** : cases `<video class="clip">` muettes en CSS grid ; ordre d'allumage dispersé à graine fixe ; étapes posées sur `mesure()`.
- **Tracés de foule** : fond = médiane par pixel du plan fixe ; taches différentes du fond = personnes ; relier chaque centre au plus proche de l'image précédente ; à calculer hors page (script) et à livrer en séquence d'images transparentes.
- **Pièges** : coupes cachées dans les rushes d'hyperlapse (détecter avec `select='gt(scene,0.25)'`, garder chaque extrait dans un seul plan, sinon le mélange crée des fantômes) ; filigranes et cartons de remerciement cachés dans les sources libres (planche à 1 image par seconde avant de choisir) ; texte sur ciel clair qui disparaît.

## 7. Son
- **Musique seule.** Ni narrateur, ni son d'origine des rushes (ce sont les musiques des autres), ni bruitages : c'est l'exception assumée au budget de bruitages du skill `son`. Si une voix est exigée : une phrase courte au tout début ou à la fin, jamais sur les coupes.
- Écriture : arpèges sur un accord par mesure, couches ajoutées (croches → triolets → doubles croches), **rupture** = tous les arpèges s'arrêtent d'un coup sur un accord tenu, **arrêt net** = tous les instruments coupés en 15 ms en laissant sonner la réverbération, coda sur un accord doux non résolu. Orgue, bois en staccato et cordes par défaut ; chœur, pianos ou arpèges de synthé analogique possibles.
- Un coup de glockenspiel par chiffre qui se verrouille (seul « bruitage » admis). Master −14 LUFS, crête −1,2 dBTP.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Aucune coupe hors de la grille musicale (écart 0 image).
- [ ] Au moins un freinage et exactement un arrêt net au noir sur une barre de mesure.
- [ ] Le time-lapse « horloge » revient au moins trois fois depuis la même position.
- [ ] Aucune personne ordinaire identifiable n'est le sujet du ralenti ou d'un gros plan (ralentir une chose ; montrer les gens en foule, tracés ou fantômes).
- [ ] 2 à 4 chiffres, chacun avec page officielle et année dans `FAITS.md`.
- [ ] Pas de fantômes de mélange à travers une coupe cachée ; plans de nuit non blanchis.
- [ ] Crédits CC BY complets sur le carton de fin (4 à 5 s, en petit), jamais dix secondes de texte sur noir.
- [ ] Texte à gauche, hors zones d'interface, sans boîte.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/city-symphony.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/city-symphony.jpg
- Crédit : « One Day in New York », LemoLab, CC BY 4.0. Rushes de tiers sous CC BY et domaine public : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/city-symphony/STYLE.md`, `style.json`, `demo/tools/` (`timeline.py`, `prep.py`, `render.py` : `Trails`, `grid_plate()`, `split_plate()`, `lock_digits()`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, cadrage 9:16, assemblage HyperFrames. Sources et droits : `references/materiel-et-droits.md`.
