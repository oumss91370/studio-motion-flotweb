# Teaser haute énergie

## 1. Identité
- **Nom** : Teaser haute énergie. Identifiant : `teaser-haute-energie`.
- **Inspiration** : la bande-démo d'un studio de motion design : 12 à 20 secondes où quelque chose tombe sur chaque demi-seconde.
- **Principe** : ça frappe à chaque temps, mais ça ne ressemble jamais à des coupes au hasard, parce qu'**une forme porte l'œil à travers chaque transition** : une étincelle devient une ligne, la ligne inonde l'écran et devient le fond suivant, un point final se détache et devient la bille autour de laquelle la scène suivante se construit.
- **Pour quels sujets** : annonce de lancement, teaser d'une sortie, ouverture d'une vidéo plus longue, publicité courte, vidéo « c'est en ligne ».
- **Ne marche pas pour** : expliquer comment le produit marche (voir `demo-produit-epuree`), un produit sérieux ou institutionnel qui demande du calme, un sujet sans phrase à retenir.
- **Une seule chose à retenir** : le client la donne en une ligne (« tape une idée, obtiens une appli en ligne »).

## 2. Palette, typographie, matières
- **Palette par défaut** : encre `#0B0B10`, accent `#FF4F1A`, crème `#EDEBE4`, bleu électrique `#2F47FF`, blanc. **La couleur principale de la marque remplace l'accent, sa seconde couleur remplace le bleu** ; une marque à une seule couleur prend une nuance profonde de cette couleur comme seconde.
- **Trois couleurs au plus par scène** (noir et blanc non comptés).
- **Polices libres** : une grotesque très grasse pour les mots claqués (Inter Tight 900, Archivo Black) ; un serif italique pour la ligne « humaine » (Instrument Serif Italic) ; une mono pour l'habillage et les légendes (JetBrains Mono, Geist Mono). Si la marque a ses polices : la sienne pour le nom, la mono pour l'habillage.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; Playfair Display à la place d'Instrument Serif ; JetBrains Mono à la place de Geist Mono ; Archivo Black, JetBrains Mono : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight`, `@fontsource/instrument-serif`, `@fontsource/geist-mono` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Habillage « viseur » sur chaque scène** : fins crochets dans les coins, `SCÈNE 02 / 07`, une étiquette de catégorie en petite mono (`TYPO`, `PRODUIT`, `DONNÉES`), un code temporel qui défile avec un point rouge. Petit et à ~50 % d'opacité : ça doit évoquer le viseur d'une caméra.
- **Texture** : vignette radiale douce sur chaque aplat, grain très subtil (quelques tuiles à graine fixe qui alternent), vrai flou de mouvement.
- **Interdits de matière** : look de modèle tout fait, lueurs partout, émojis.

## 3. Composition 9:16
- **Mot claqué** : capitales, 180 à 300 px, sur 1 à 3 lignes empilées, centré entre y 560 et y 1150 ; lettres révélées par masques sur des doubles croches successives. Petit surtitre mono au-dessus (`VOICI — 2026`, 30 px), ligne en serif italique dessous (ce que c'est, 2 à 4 mots, 54 à 70 px).
- **Habillage viseur** en vertical : crochets à 60 px des bords ; les libellés du haut **sous y 170**, ceux du bas **au-dessus de y 1540**, rien à droite de x 945. Taille 28 px au moins pour tout libellé à lire (la source dit 12 à 14 px en 1080p horizontal : illisible sur un téléphone) ; un libellé purement décoratif plus petit se marque `data-passage`.
- **Carte de produit** : largeur 820 à 900 px, légèrement inclinée en 3D, deux cartes fantômes empilées derrière.
- **Triplet de mots** : un mot par écran, chacun avec son traitement et son fond.
- **Carte de fin** (tenue 2 s) : nom avec le point d'accent, ligne en serif italique, ligne mono espacée, filet fin ; entre y 650 et y 1150.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : mêmes scènes, mots sur une ligne.

## 4. Ce qui bouge
- **Action principale** : **les transitions sont des objets, pas des coupes.** Chaque scène passe à la suivante par une forme : inondation de couleur, volet par une barre qui grandit, point qui devient le fond suivant, mot qui traverse la caméra. Une coupe franche entre scènes n'est admise que sur un temps fort, **deux fois au plus**.
- **Boucles de fond** : (1) le code temporel du viseur qui défile ; (2) une inclinaison ou une orbite lente de la caméra pendant le visuel signature.
- **Tout tombe sur la grille** : grands changements sur les temps, typographie sur les croches ou doubles croches. Léger dépassement sur les impacts (amortissement ≈ 0,6 à 0,7), puis ça se pose.
- **L'inondation de couleur doit couvrir le coin le plus éloigné** (rayon = distance au coin × 1,05), en 0,3 à 0,35 s.
- **Scènes au choix (6 à 8, de 1,5 à 3 s)** :
  1. **Ouverture étincelle** : fond presque noir avec grille discrète ; une petite marque d'accent apparaît, pulse, s'étire en fine ligne horizontale, tremble une fois, puis **s'élargit verticalement en inondation plein écran**.
  2. **Claquement de la marque** : le nom en très gras ; le point final ou le point d'une lettre **se détache et grandit** pour lancer la scène suivante.
  3. **Triplet cinétique** : la promesse en trois mots courts, **deux temps chacun** (trois pour un mot manuscrit, pour qu'on le lise), fonds échangés sec sur le temps ; dans cette scène, les échanges sont le rythme et ne comptent pas comme des coupes.
  4. **Visuel signature** : un moment « comment ont-ils fait ça » qui symbolise le produit : champ de cubes en 3D qui ondule depuis le centre (briques → cubes), flux de particules qui se condense en anneau (données, IA → particules), goutte liquide qui change de forme (souplesse → liquide).
  5. **Micro-moment produit** : une vraie interaction en carte flottante : le curseur bascule un interrupteur, appuie sur le bouton, la barre se remplit, le bouton passe à « Fait ✓ », une notification glisse. Vrais libellés du produit.
  6. **Preuve** (seulement s'il existe de vrais nombres) : grand compteur aux chiffres flous pendant qu'ils tournent, anneau, barres en cascade. Sinon : sauter la scène, ou montrer les vraies capacités en liste qui claque.
  7. **Pont de morphing** : la forme précédente se réduit à un point, le point devient une onde, qui devient le point du logo.
  8. **Carte de fin.**
- **Autorisés** : #018 transition par forme, #017 transition par masque, #020 traversée de zoom, #012 morphing, #008 typographie cinétique, #005 révélation par masque, #010 dépassement, #007 compteur, #132 graisse de police variable, #004 mot manuscrit qui se trace, #015 particules (dans le visuel signature seulement), #046 coupe sur un temps fort (2 au plus).
- **Interdits** : coupes au hasard, scène sans mouvement, lueurs sur tout, texte trop petit pour être lu d'un coup d'œil, plus d'une idée par scène.

## 5. Rythme et montage
- **15 secondes par défaut** (128 BPM, 8 mesures) ; de 12 à 20 s. Grille de 120 à 140 BPM. À 30 i/s, **120 BPM = 15 images par temps** (entier) est le plus simple ; à 128 BPM, placer chaque évènement par son temps en secondes, arrondi à l'image.
- **Feuille des temps d'abord** : une ligne par scène : début sur la grille, ce qui entre, ce qui sort, le son.
- Six scènes fortes valent mieux que huit faibles. **Une idée par scène.**
- L'image 0 est la vignette : la marque d'accent est déjà visible (jamais un noir vide).
- Brief en **un seul message**, puis l'agent travaille seul et dit ce qu'il a décidé pour ce qui manquait.
- **Version courte (8 à 12 s)** : 12 s : six mesures à 120 BPM au lieu de huit ; on enlève une scène entière, on ne raccourcit pas chacune.

## 6. Recette technique
- **Moteur** : HyperFrames + GSAP ; le visuel signature sur un `<canvas>` piloté par `hf-seek` (ou en Three.js ; Blender si le client veut un rendu photoréaliste).
```js
const TEMPS = 60 / 120, t = (mesure, temps = 0) => (mesure * 4 + temps) * TEMPS;   // grille : 120 BPM
// 1. l'étincelle devient une ligne, la ligne inonde l'écran
tl.fromTo("#marque", {scale: 0}, {scale: 1, duration: 0.25, ease: "back.out(2)"}, t(0))
  .to("#marque", {width: 1080, height: 4, borderRadius: 0, duration: 0.35, ease: "power3.inOut"}, t(0, 1))
  .to("#marque", {height: 1920 * 1.05, duration: 0.32, ease: "power3.in"}, t(0, 3));   // devient le fond suivant
// 2. lettres révélées sur des doubles croches
gsap.utils.toArray("#nom .lettre").forEach((l, i) =>
  tl.fromTo(l, {yPercent: 105}, {yPercent: 0, duration: 0.3, ease: "back.out(1.4)"}, t(1) + i * TEMPS / 4));
```
- **Calques** : fonds de scène transparents ; un seul fond de scène général derrière eux, pour qu'un calque ne cache jamais le précédent par accident. Texte en position absolue avec `white-space: nowrap`.
- **Polices embarquées** ; pour un changement de graisse fin → très gras, une police variable.
- **Ce qui a besoin d'un passé** (simulation de particules, caméra qui traîne) est **calculé une fois au chargement** puis relu : jamais d'état d'une image à l'autre.
- **Vitesse de rendu** : les grands `filter: blur()` sont très lents à capturer ; dessiner dégradés et halos une fois sur un canvas et déplacer cette image.
- **Flou de mouvement** : celui du moteur ; jamais à travers une coupe franche.
- **Contrôle** : une image fixe par ligne de la feuille des temps → brouillon rapide sans flou → final.
- **Faits et logos** : aucun chiffre, note, avis ou offre inventé ; logo seulement si le client fournit le fichier, sinon le nom en texte ; logos de tiers seulement s'ils sont fournis (sinon tuiles neutres avec le nom). Voir `references/script-de-lancement.md` §4.

## 7. Son
- **Percutant** : grosse caisse sur chaque temps, clap sur 2 et 4, basse profonde qui suit les scènes, montée filtrée vers le claquement de la marque et vers la carte de fin, impact sur chaque inondation, souffle sur chaque transition portée, résonance douce sur la carte de fin. La musique passe **sous** les impacts.
- La source synthétise toute la bande-son. Ici : un morceau sous licence claire ou la musique du client à **son tempo mesuré**, de **vrais enregistrements** pour impacts et souffles (skill `son`), synthèse en repli.
- **Dérogation au budget** : dans ce style, la densité rythmique fait partie du genre ; compter impacts et souffles comme des éléments de la musique s'ils tombent tous sur la grille, et garder les autres bruitages (clics, notification) dans le budget d'environ 5 par 10 s.
- −14 LUFS (la source vise −16).
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Chaque transition est portée par une forme ; deux coupes franches au plus, sur des temps forts.
- [ ] Chaque grand changement tombe sur un temps (écart ≤ 1 image).
- [ ] Une idée par scène ; trois couleurs au plus par scène.
- [ ] La chose à retenir se lit à l'écran, sans le son.
- [ ] Aucun chiffre, note ou offre inventé ; la scène « preuve » est absente s'il n'y a pas de vrais nombres.
- [ ] L'habillage viseur est lisible (≥ 22 px) et hors des zones d'interface.
- [ ] Carte de fin tenue 2 s ; image 0 non vide.
- [ ] −14 LUFS mesuré ; aucun flou de mouvement à travers une coupe.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- GIF de démonstration du dépôt d'origine : https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-high-energy.gif. Crédit : Bart, dépôt sous licence MIT. Lien seulement ; aperçu Flot Web en 9:16 à produire.

## 10. Origine
- Dépôt : Barty-Bart/motion-graphics, commit `3d83d98`. Fichier : `skills/explainer-high-energy/SKILL.md`. Règle de l'inondation de couleur : howseen-ai/claude-motion-design, commit `3d90d34` (MIT).
- Licence : MIT (© 2026 Bart).
- Adaptations Flot Web : français, **réécrit pour HyperFrames** (la source a son propre moteur de rendu), composition 9:16, habillage agrandi, vrais enregistrements d'abord, −14 LUFS.
