# Science en pixel art (une histoire vraie, puis le principe)

## 1. Identité
- **Nom** : Science en pixel art. Identifiant : `science-pixel-art`.
- **Inspiration** : les chaînes de vulgarisation en motion design pixel art, très denses, où chaque phrase a son image. On en reprend le format (structure, densité visuelle, rythme), jamais un sujet, un texte ni un dessin.
- **Principe** : **une histoire vraie et surprenante, puis le principe qui l'explique.** Un lieu, une date, une personne, un geste absurde, un chiffre fort. **Un visuel littéral par phrase** : on montre exactement ce que dit la voix. Un présentateur récurrent ouvre l'épisode devant un grand tableau, où l'accroche s'écrit ; le tableau grandit jusqu'à remplir l'écran, et l'histoire se joue dedans. La fin referme la boucle sur la première image.
- **Deux variantes** :
  - **Histoire + principe** (environ 2 minutes, boucle parfaite) : le format principal.
  - **Construction** (environ 70 s) : on explique **comment marche un objet** en le construisant, en vue en coupe, étape par étape (« Mais… (problème) / Alors, tu… (solution) », jusqu'à « Bravo, tu viens de construire… »).
- **Pour quels sujets** : un principe de science, de psychologie, d'économie, d'ingénierie, d'histoire des techniques : tout principe qu'une histoire vraie illustre.
- **Ne marche pas pour** : un sujet sans faits vérifiables, une opinion, une actualité chaude. **À refuser** : tout sujet qui reviendrait à un mode d'emploi dangereux ou illégal ; proposer à la place un angle science ou sécurité.
- **Ce que la fiche « ma chaîne » fournit** : le **présentateur** (personnage récurrent original du client), la palette de marque, la voix et la façon de s'adresser au public (tu ou vous), le ton, la durée, la phrase d'abonnement.

## 2. Palette, typographie, matières
- **Couleurs de marque de la fiche « ma chaîne »**, réparties en cinq rôles. Exemple par défaut : fond du tableau `#14213D`, trait clair `#F4F1DE` (et deux tons plus doux `#BFD7EA`, `#6FA8DC`), mot-titre jaune `#FFC857`, **rouge `#E63946` = danger ou négation**, **vert `#52B788` = vivant ou validé**, cadre du tableau `#6B4226`.
- **Les décors à l'intérieur du tableau sont en couleurs naturelles** (ciel, ville, bureaux).
- **Pixel art strict** : grille logique **270×480**, agrandie **×4** au plus proche voisin. Jamais de lissage.
- **Police** : pixel, 5×7, avec les accents français, **à dessiner dans le code** (elle n'est pas fournie ; construction des accents : voir la fiche `pixel-8-bits` de la catégorie `styles-jeu-retro`, section 6). Sur cette grille ×4, une lettre à l'échelle 1 fait 28 px à l'écran : c'est le plancher, réservé aux petits affichages ; **tout texte à lire se dessine à l'échelle 2** (56 px, 17 caractères par ligne dans la zone utile), les mots-titres à l'échelle 3 ou 4.
- **Police de repli** : aucune police pixel n'est fournie par HyperFrames : dessiner la police 5×7 en pixels dans le canvas, accents compris ; pour un texte HTML hors canvas, Space Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/pixelify-sans` ou `@fontsource/silkscreen` (accents français présents, vérifié le 11/11/2026) si l'on préfère une police de fichier.
- **Lumière tramée** (trame ordonnée 4×4) : halos, faisceaux, contre-jours. **C'est elle qui donne la profondeur.**
- **Personnages** : pixel art réaliste en couleur, **au moins 48 px de haut** sur la grille ; jamais de bonshommes bâtons. Le présentateur est validé une fois puis **ne change plus**.
- **Composants** : affichage persistant lié au sujet (température, compteur, date) ; mot-titre jaune qui surgit (rouge pour une négation, vert pour une validation) ; étiquette reliée à l'objet par un trait ; fiche de personnage ; compteur animé ; tampon penché avec une secousse.

## 3. Composition 9:16

Grille de travail : 270×480, soit 1080×1920 à la sortie.
- **Plein cadre, zones d'interface habillées** : le décor remplit tout l'écran. **Jamais de bandes noires, de cadre ni de mur autour de la scène, jamais d'image réduite.**
- **Trois zones couvertes par l'interface des applications, en pixels de la grille** : **haut y < 40**, **bas y ≥ 390**, **bande droite x ≥ 236** (entre y 40 et 390). On y met **la suite du décor** (ciel, route, forêt, sol, ville), jamais un titre, un chiffre, l'affichage ou un visage.
- **Zone utile : x 15 à 228, y 44 à 384.** (x 15 = 60 px à l'écran, limite gauche du studio ; x 8 ne ferait que 32 px et serait refusé par la porte de livraison.) L'affichage se place à y ≥ 44 ; les mots-titres entre y 44 et 190 ; dans la bande y 200 à 384, largeur 213 au plus, calés à gauche (x 15).
- **Plans dézoomés à 85 %** : on recule la caméra, on dessine personnages, objets, schémas et textes environ 15 % plus petits et on les ramène dans la zone utile, pendant que le décor continue jusqu'aux bords. **On dézoome en dessinant plus petit, jamais en réduisant l'image** : les pixels restent entiers et nets.
- **Ouverture au tableau** : grand tableau centré en haut, présentateur en bas à gauche, le visage au-dessus de la zone basse.
- **Aucun titre ne recouvre l'affichage ni un visage. Jamais de sous-titres complets** : des mots-titres seulement.
- **Couverture** : composée pour le centre 3:4, **sans cadre ni bandes** ; le plan d'accroche lisible en petit ; la phrase d'accroche sur un bandeau sombre en haut de la zone 3:4, trois lignes au plus, le mot fort en couleur ; le présentateur entier, tourné vers l'objet clé.

## 4. Ce qui bouge
- **Action principale** : le visuel littéral de la phrase en cours, avec son évènement (quelqu'un entre, une alarme se déclenche, un compteur grimpe).
- **Boucles de fond, toujours quelque chose qui bouge** : (1) **particules** : pluie, poussière dans la lumière, bulles, papiers, étincelles ; (2) **lumières** : ampoule qui se balance, alarme, gyrophare, projecteurs. Plus les personnages (marche, mains levées, bouche qui parle) et les défilements en parallaxe.
- **Dézoomer et remplir le cadre** : décor complet (ville, pièce, rue, bureau), plusieurs personnages, objets de contexte. **Jamais un objet seul dans le noir.**
- **Plans variés** : plan large d'un lieu, vue en coupe d'un bâtiment, gros plan (mains, objet), plan subjectif, carte. Pour un appel : **écran partagé où l'on voit les deux interlocuteurs en grand**, chacun dans son décor.
- **Cartes** : le pays allumé, les villes en halos, un point qui pulse avec des ondes et une étiquette ; le plan suivant montre la ville elle-même.
- **L'ouverture** : l'accroche s'écrit là où pointe le présentateur, **sa bouche bouge avec la voix** ; le mot fort s'écrit dans la couleur de danger ; puis **le tableau grandit en ~0,3 s jusqu'à remplir l'écran**. Le présentateur revient de temps en temps au fil de la vidéo.
- **Autorisés** : #004 tracé (écriture au tableau), #001 pop du mot-titre, #007 compteur, #016 parallaxe, #144 écran partagé, #015 particules d'ambiance, #020 traversée de zoom (le tableau qui grandit ; **un zoom se fait en redessinant à la nouvelle échelle**), #024 secousse du tampon, #128 animation saccadée, #127 boucle.
- **Interdits** : symbole abstrait à la place du visuel littéral (une ampoule barrée), objet seul sur fond vide, #044 fondu en transparence, lissage, image agrandie ou réduite, visuel de moins de 1,5 s, bruitage fort sur un zoom.

## 5. Rythme et montage
- **Histoire + principe** : 300 à 340 mots, phrases courtes, un ou deux traits d'humour discrets. Squelette :

| Bloc | Règle |
|---|---|
| Accroche | le titre de la vidéo, écrit au tableau pendant l'ouverture (~11 s) |
| Relance | un détail qui choque |
| Idée reçue | « On pense que… Sauf que… » |
| Situation | lieu et date |
| Escalade | 3 à 5 étapes datées ou numérotées, chacune pire que la précédente |
| Relance de milieu | « Et c'est là que ça devient intéressant » |
| Principe | l'explication par une **analogie du quotidien dessinée** |
| Preuve chiffrée | les chiffres qui confirment |
| Et toi ? | le lien avec la vie du spectateur |
| Boucle | la dernière phrase s'enchaîne grammaticalement sur la première |

- **Construction** : ~250 mots, ~70 s ; accroche = une situation du quotidien ; l'inventeur en **une seule phrase** ; l'objet en **vue en coupe** presque tout le temps, une étape de construction par plan, affichage lié (température, pression) ; 0,35 s entre les phrases. Pas de boucle obligatoire.
- **Une phrase = un plan.** Chaque visuel reste **au moins 1,5 s** ; une phrase ne se découpe en deux visuels que si elle dure plus de 3 s. En cas de doute, laisser l'image plus longtemps.
- **Version réseaux très courte** : quand on s'inspire d'un reel, les 2 à 3 premières secondes sont un plan d'accroche en plein cadre, **sans le tableau** ; le présentateur arrive juste après ; la boucle se referme sur ce plan.
- Pause de 0,7 s après un point, 0,3 s après une virgule (variante longue).
- **Recherche d'abord** : repérer l'instant spectaculaire (l'accroche), l'idée reçue à casser, 3 à 5 étapes d'escalade, une analogie du quotidien, un lien avec le spectateur.
- **Version courte (8 à 12 s)** : garder le plan d'accroche en plein cadre (2 à 3 s, sans le tableau), l'idée reçue en une phrase et le principe par son analogie dessinée ; couper l'ouverture au tableau (≈ 11 s), l'escalade et la preuve chiffrée. Chaque visuel reste 1,5 s au moins : quatre ou cinq visuels, pas plus.

## 6. Recette technique
- **Moteur** : HyperFrames ; un `<canvas>` de 270×480 agrandi en CSS (`image-rendering: pixelated`), dessiné depuis `hf-seek` par une fonction pure du temps. Les éléments 3D éventuels (un ou deux par épisode **au plus** : un mécanisme, un objet vu sous un angle difficile) sont rendus dans Blender, **réduits à la palette pixel art** et intégrés ; personnages, animaux et décors restent dessinés en pixel art.
```js
const SEGMENTS = [ ["pont", "Le pont se met à onduler."], ["foule", "Sur la rive, personne n'ose approcher."] ];   // une phrase = un plan
function rendre(t) {
  const s = segmentA(t), u = (t - s.debut) / s.duree;         // segment trouvé d'après la voix horodatée
  SCENES[s.id](ctx, u, t);                                    // décor complet + évènement + ce qui bouge toujours
  lumiereTramee(ctx, s.lampes, t);                            // halos et faisceaux en trame 4×4
  affichage(ctx, s.valeurs, 8, 44); if (s.titre) motTitre(ctx, s.titre, u);   // jamais sur l'affichage ni un visage
}
window.addEventListener("hf-seek", e => rendre(e.detail.time));
```
- **Livrables, dans cet ordre** : 1) la **recherche** (chaque fait avec sa source) ; 2) le script et la liste des segments ; 3) la voix, phrase par phrase, et sa chronologie ; 4) les scènes ; 5) **une planche d'une image par plan**, regardée ; 6) le rendu ; 7) la couverture.
- **Voix** : une phrase par génération ; chaque phrase mise au même niveau avant le mix, pour éviter les sautes de ton ; ne jamais relancer une génération « pour réessayer ».
- **Plans larges illisibles** : dessiner en interne à 540×960 puis rester sur une grille entière ; ne jamais descendre sous 48 px pour un personnage.
- **Boucle** : l'écart moyen entre la première et la dernière image doit être proche de zéro.
- **Si l'on part d'une référence** : `references/mesurer-une-reference.md` (tableau des plans mesuré, tailles relevées sur une grille de 10 %, plan d'implantation, planche de comparaison, liste des erreurs déjà faites). Réécrire tous les textes avec ses propres mots et **vérifier chaque chiffre soi-même**.
- **Brancher sur HyperFrames sans erreur de `lint`** : un film dessiné par `hf-seek` sort l'erreur `missing_timeline_registry` tant qu'aucune timeline n'est enregistrée (constaté sur le format voisin `lecon-pixel-art` au rendu réel du 11/11/2026 ; non rendu pour ce format-ci). Enregistrer une **timeline vide** après le script du dessin : `window.__timelines["main"] = gsap.timeline({ paused: true });`. Ne pas écrire `data-no-timeline` (il fait taire le contrôle qui détecte un film figé). Détails : skill `rendu`, section « Film en canvas piloté par `hf-seek` ».
- **Export** : agrandissement au plus proche voisin ; **débit élevé et constant** (commande essayée sur un film pixel art de 10 s : `ffmpeg -i rendu.mp4 -c:v libx264 -preset slow -b:v 8M -minrate 8M -maxrate 8M -bufsize 16M -x264-params "nal-hrd=cbr:force-cfr=1" -pix_fmt yuv420p -c:a copy film.mp4`, soit 7,9 Mbit/s au lieu de 0,1) : un fichier pixel art très léger est écrasé par la recompression des plateformes et ressort flou.
- **Nouvelle direction visuelle** : faire valider un extrait de 30 à 40 s par le client avant le rendu complet.

## 7. Son
- **Voix d'abord** ; bruitages **discrets** (environ 12 % du niveau de la voix) : un petit son au changement de plan important, craie, tic de compteur, tampon, sirène, sonnerie. **Jamais de bruitage fort sur les zooms.** Budget du skill `son` : environ 5 par 10 s, vrais enregistrements d'abord.
- **Nappe de musique de jeu très légère** (les sons de puce sont synthétisés par nature : c'est le son juste pour le pixel art).
- **−14 LUFS** ; si le client trouve cela trop fort pour une vidéo longue et calme, descendre à −16 et le noter dans sa fiche.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] **Chaque chiffre affiché a sa source** dans la recherche ; aucun point « à vérifier » n'apparaît à l'écran.
- [ ] Un visuel littéral par phrase ; aucun symbole abstrait ; aucun objet seul dans le noir.
- [ ] Aucune phrase sans image, chaque phrase tombe sur son plan, aucun visuel de moins de 1,5 s.
- [ ] Planche d'une image par plan avec **les trois zones tracées en rouge** : du décor dedans, aucun texte, affichage, chiffre ni visage.
- [ ] Personnages ≥ 48 px ; aucun titre sur l'affichage ou un visage.
- [ ] Pixels entiers partout (rien de réduit ni de lissé) ; décor jusqu'aux bords, sans bandes ni cadre.
- [ ] La boucle se referme (première et dernière images identiques) si le format en a une.
- [ ] Textes et dessins sont ceux du client ; sujet sans danger ; −14 LUFS.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Format maison Flot Web : pas d'aperçu de tiers. Aperçu à produire avec le plugin.

## 10. Origine
- Source : format de production « science en pixel art » du plugin Flot Web (fiche de série et protocole de reproduction d'une référence), **rendu générique** : toute référence à la série, à son présentateur, à ses couleurs de marque, à ses comptes, à sa voix, à ses dossiers et à ses outils de publication a été retirée ; le format lit la fiche « ma chaîne » du client.
- Aucun code de tiers. Règles de pixel art communes : voir aussi la catégorie `styles-jeu-retro`.
- Adaptations : moteur HyperFrames (`hf-seek`), palette par défaut neutre, Blender par le connecteur `blender` pour les rares éléments 3D, −14 LUFS.
