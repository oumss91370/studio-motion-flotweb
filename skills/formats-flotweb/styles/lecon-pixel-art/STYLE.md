# Leçon en pixel art (rater le niveau, apprendre, le réussir)

## 1. Identité
- **Nom** : Leçon en pixel art. Identifiant : `lecon-pixel-art`.
- **Inspiration** : les jeux de plateforme en pixel art (niveaux, coffres, blocs à frapper, « partie terminée », « niveau réussi »). Le vocabulaire du genre est générique ; aucun jeu existant n'est repris (ni personnage, ni interface, ni police, ni mélodie).
- **Principe** : une leçon racontée **comme un niveau de jeu**. On voit d'abord la mauvaise façon de faire échouer le niveau, puis la leçon, puis les « objets » à ramasser (les points clés), puis le même niveau réussi grâce à eux. Le spectateur retient parce qu'il a vu l'échec avant la règle.
- **Pour quels sujets** : apprendre à se servir d'un outil, une méthode en 3 points, une erreur fréquente et sa correction, un conseil de métier : tout ce qui se dit « ne fais pas ça, fais plutôt ça ».
- **Ne marche pas pour** : une histoire vraie à raconter (voir `science-pixel-art`), un sujet grave, un sujet sans « bonne et mauvaise façon ».
- **Ce que la fiche « ma chaîne » fournit** : le **héros** (personnage récurrent original du client ; à défaut un héros simple créé avec le skill `personnages`), l'univers et sa palette, la voix (celle du client ou une voix choisie), le ton, le sujet de la chaîne, la durée, ce que la chaîne ne fait jamais.

## 2. Palette, typographie, matières
- **Un seul univers, toujours le même**, aux couleurs de la chaîne. Structure d'une palette de plateforme : un ciel, deux tons de relief lointain, un sol, une couleur de danger, une couleur de récompense, une couleur de texte. Exemple par défaut : ciel `#8FD3F4`, relief `#B8E0A8` et `#7CC08F`, sol `#C98B5E`, danger `#E63946`, récompense `#FFC857`, texte `#1D2B53`.
- **Pas d'écran sombre hors univers** : même l'échec se joue dans le décor.
- **Pixel art strict** : grille logique **135×240**, agrandie **×8** au plus proche voisin (1080×1920). Aucun lissage, aucun dégradé, aucun déplacement d'une fraction de pixel.
- **Police** : une police pixel maison ou libre (5×7, accents français dessinés), **18 caractères par ligne au plus** : un caractère avance de 6 px de grille, et la zone utile en fait 106 (la source disait 25 : c'est la largeur du cadre entier, zones d'interface comprises). Texte courant à l'échelle 1 (56 px à l'écran), titres à l'échelle 2 (112 px, 9 caractères).
- **Police de repli** : aucune police pixel n'est fournie par HyperFrames : dessiner les lettres en pixels dans le canvas (voir section 6) ; pour un texte HTML hors canvas, Space Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/pixelify-sans` ou `@fontsource/silkscreen` (accents français présents dans les deux, vérifié le 11/11/2026) si l'on préfère une police de fichier ; `@fontsource/press-start-2p` aussi.
- **Composants** : affichage d'inventaire (« COFFRE 1/3 »), mot-titre qui claque, bulle de dialogue qui surgit, fenêtre de discussion stylisée (jamais l'interface d'un vrai produit recopiée), blocs à frapper, coffres, ennemis simples.
- **Héros original** : ne jamais le rapprocher de la mascotte d'une marque, d'un logiciel ou d'un personnage existant ; pas de logo de tiers.

## 3. Composition 9:16

Grille de travail : 135×240, soit 1080×1920 à la sortie.
- **Zones d'interface, en pixels de la grille** : **haut y < 20** (160 px), **bas y ≥ 195** (1560 px), **droite x ≥ 118** (944 px) entre y 20 et 195. Le décor va jusqu'aux bords, mais **aucun texte, affichage, compteur, bouton, bulle, visage ni objet clé** dans ces zones.
- **Zone utile : x 8 à 114, y 22 à 192.** (x 8 = 64 px à l'écran : la porte de livraison refuse un texte à moins de 60 px du bord gauche ; au rendu réel, un texte d'inventaire posé à 56 px du bord, soit x 7, a été refusé.)
- **Affichage d'inventaire** : cases à y ≥ 22 ; les mots-titres se posent à y ≥ 44, **sous** l'affichage.
- **Fenêtres de menu ou de discussion** : x 8 à 114, y 48 à 192 ; barre de saisie au-dessus de y 192.
- **Cartes et boutons** : largeur ≤ 104 px à partir de x 8 ; raccourcir le libellé plutôt que déborder à droite.
- **Récapitulatif et annonce de la suite** : l'appel à s'abonner et le dernier texte au-dessus de y 192.
- **Pas de sous-titres incrustés** dans ce format (le texte à l'écran est celui du jeu) ; fournir un fichier de sous-titres à part si le client en veut.
- **Couverture** : phrase d'accroche en gros en police pixel, le héros, une situation qui intrigue ; titre et personnage dans le centre 3:4.

## 4. Ce qui bouge
- **Action principale** : le héros qui joue le niveau : il court, saute, frappe un bloc, ouvre un coffre, combat. Les combats varient (coup d'épée, projectile bloqué au bouclier, saut sur un ennemi).
- **Boucles de fond** : (1) le défilement du décor en couches ; (2) la vie du niveau : pièces qui tournent, ennemis qui patrouillent, nuages.
- **Les sprites sautent d'image en image** (10 à 15 dessins par seconde) ; le défilement reste régulier, en pixels entiers.
- **Les choses clignotent, elles ne fondent pas** : apparition et disparition par tout ou rien, par mosaïque ou par changement de palette.
- **Transitions du format** : volet en blocs de pixels, iris, rembobinage façon cassette, lignes de vitesse, tremblement, panoramique latéral.
- **Autorisés** : #141 pixellisation, #188 iris, #045 volet en blocs, #024 secousse d'impact, #025 panoramique latéral, #001 pop d'une bulle, #128 animation saccadée, #003 éclat à l'ouverture d'un coffre, #046 coupe sèche.
- **Interdits** : **zoom de caméra**, fausse 3D, #044 fondu en transparence, flou, dégradés, écran noir, phrases bateau (les répliques de bascule doivent accrocher).

## 5. Rythme et montage
- **50 à 110 s**, **une coupe toutes les 1 à 2 s**. **L'accroche parle dès la première seconde** : jamais de début muet.
- **Boucle d'un épisode** :
  1. **La demande** : le héros (ou celui qui parle) pose le problème ; bulles de discussion.
  2. **Le niveau raté** : la mauvaise façon de faire → « PARTIE TERMINÉE ».
  3. **La leçon**, dite simplement.
  4. **L'inventaire** : le panneau reste fixe en haut ; le héros frappe un bloc ou ouvre un coffre **à chaque point clé**.
  5. **Le niveau réussi** : combats variés → « NIVEAU RÉUSSI » ; récapitulatif pendant la course finale.
  6. **Récapitulatif + annonce du niveau suivant.**
- **Script** : un tableau minuté (temps / image / voix / son) + les répliques dans l'ordre d'enregistrement. La première phrase sert aussi à la couverture.
- **Sujet vérifié** dans la documentation officielle quand il est technique ; dire ce qui relève de l'astuce de terrain.
- **L'animation se cale sur la voix**, jamais l'inverse : repères par mot.
- **Aperçu de 10 s** de tout nouvel environnement, à faire valider par le client avant l'épisode complet.
- **Version courte (8 à 12 s)** : garder quatre temps sur six : la demande (2 s), le niveau raté, la leçon avec **un seul** objet d'inventaire, le niveau réussi ; couper le récapitulatif et l'annonce de la suite. « PARTIE TERMINÉE » tient 1 s au moins, « NIVEAU RÉUSSI » (dernier texte) 2 s. Accroche avant 3 s : la bulle de la demande dès la première seconde. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique
- **Moteur** : HyperFrames ; un `<canvas>` de 135×240 agrandi en CSS, dessiné depuis `hf-seek` par une fonction pure du temps.
```html
<canvas id="jeu" width="135" height="240" style="width:1080px;height:1920px;image-rendering:pixelated"></canvas>
<script>
const ctx = jeu.getContext("2d"); ctx.imageSmoothingEnabled = false;
function rendre(t) {                        // aucune horloge, aucun état gardé d'une image à l'autre
  const s = sceneA(t);                      // scène trouvée d'après les repères de la voix
  dessinerDecor(ctx, Math.round(s.defilement));            // pixels entiers
  dessinerHeros(ctx, s.x | 0, s.y | 0, Math.floor(t * 15) % 4);   // 15 dessins par seconde (une image sur deux à 30 i/s)
  dessinerInventaire(ctx, s.objets);        // cases à y >= 22
}
window.addEventListener("hf-seek", e => rendre(e.detail.time));
</script>
```
- **Brancher sur HyperFrames sans erreur de `lint`** : la recette ci-dessus, recopiée telle quelle, donne l'erreur `missing_timeline_registry` (rendu réel du 11/11/2026). Il faut enregistrer une **timeline vide** après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`) : c'est ce qu'a fait le film d'essai. Ne pas écrire `data-no-timeline` : il fait taire aussi le contrôle qui détecte un film figé. Le dessin reste piloté par `hf-seek`. Détails : skill `rendu`, section « Film en canvas piloté par `hf-seek` ». Le texte d'un canvas n'est vu ni par `check` ni par le relevé automatique : écrire le relevé des textes à la main, depuis la grille (position × 8).
- **Briques à écrire une fois et à réutiliser** (par l'agent : aucune n'est fournie par le plugin) : police pixel, sprites, niveau, pièce, mot qui claque, bulle, volet, iris, rembobinage, lignes de vitesse, secousse, éclat.
- **Voix du client enregistrée en une prise** : transcrire avec les mots horodatés ; repérer les « on refait », « on reprend » et **garder la dernière prise complète de chaque réplique** ; ramener les silences internes de plus de 0,5 s à 0,3 s ; 0,35 s entre deux répliques ; retranscrire chaque morceau pour vérifier le texte. Traitement doux : réduction de l'écho de pièce, débruitage léger, coupe-bas, compression légère **sans gain de rattrapage**. Ne pas pousser les aigus ni compresser fort (cela fait ressortir l'écho) ; pas de débruiteur sur les voyelles tenues de l'accroche (grésillement).
- **Planche de contrôle** de 6 à 18 images clés, **avec les trois zones d'interface tracées en rouge par-dessus** : aucun export tant qu'un texte, un chiffre, l'affichage ou un bouton touche le rouge. Refaire ce contrôle sur la planche finale calée sur la voix, pas seulement sur le premier jet.
- **Export** : agrandissement au plus proche voisin (`scale=…:flags=neighbor`) ; débit élevé et constant pour les plateformes qui recompressent (le pixel art pèse peu, et un fichier trop léger ressort flou après recompression). Le rendu de 10 s du 11/11/2026 pesait 143 Ko (≈ 0,1 Mbit/s). Commande essayée sur ce fichier : `ffmpeg -i rendu.mp4 -c:v libx264 -preset slow -b:v 8M -minrate 8M -maxrate 8M -bufsize 16M -x264-params "nal-hrd=cbr:force-cfr=1" -pix_fmt yuv420p -c:a copy film.mp4` : 9,9 Mo, 7,9 Mbit/s constants. Baisser seulement la qualité (`-crf`) ne suffit pas : à `-crf 12`, le fichier reste à 147 Ko.
- **Pièges** : image réduite au lieu de dessiner plus petit (pixels baveux) ; texte de plus de 18 caractères qui déborde à droite ; jingle sous les premiers mots (il fait grésiller l'accroche).

## 7. Son
- **Voix + bruitages de jeu uniquement, pas de musique** dans ce format (c'est l'exception de la catégorie ; une nappe de jeu très légère reste possible si la fiche « ma chaîne » en veut une).
- **Les bruitages de jeu (bips, sauts, pièces, coffres, jingles) sont synthétisés par nature** : c'est le son juste pour ce genre. Discrets, environ moitié moins forts que la voix, avec baisse automatique sous elle.
- **Coupés net sous les toutes premières répliques.**
- −14 LUFS, aucune saturation.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La première seconde parle déjà ; aucune image de début muette ou noire.
- [ ] Les six temps de la boucle sont là : demande, niveau raté, leçon, inventaire, niveau réussi, récapitulatif.
- [ ] Chaque point clé a son coffre ou son bloc, au moment où la voix le dit.
- [ ] Aucun texte, affichage, bouton, bulle ou visage dans les zones rouges (planche avec les zones tracées).
- [ ] Aucun zoom, aucun flou, aucun fondu, aucun dégradé ; pixels nets (agrandissement entier).
- [ ] Une coupe toutes les 1 à 2 s ; l'animation suit la voix.
- [ ] Le héros est original ; aucun logo ni interface de tiers recopiés.
- [ ] Sujet technique vérifié ; bruitages coupés sous l'accroche ; −14 LUFS.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Format maison Flot Web : pas d'aperçu de tiers. Aperçu à produire avec le plugin.

## 10. Origine
- Source : format de production « leçon en pixel art » du plugin Flot Web (fiche de série), **rendu générique** : toute référence à la série, à son héros, à son univers, à ses comptes, à sa voix, à ses dossiers et à ses outils de publication a été retirée ; le format lit la fiche « ma chaîne » du client.
- Aucun code de tiers. Règles de pixel art communes : voir aussi la catégorie `styles-jeu-retro`.
- Adaptations : moteur HyperFrames (`hf-seek`), palette par défaut neutre, −14 LUFS.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche (après ajout d'une timeline vide pour `lint`) ; export conforme (−13,2 LUFS), textes lisibles à 360 px, aucun texte dans les zones d'interface.
