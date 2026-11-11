# Néon vaporwave

> **Style sous dérogation.** Sa palette est bleu-violet par nature, ce que la porte de livraison refuse d'ordinaire. Lis `../../references/derogation-bleu-violet.md` avant de produire : choix explicite du client, contrepoids chauds dans chaque plan, raison écrite dans la note de livraison.

## 1. Identité

- **Nom** : Néon vaporwave.
- **Inspiration** : l'esthétique « vaporwave » née sur Internet vers 2011 et le néon cyberpunk : nostalgie des années 80-90 passée au magnétoscope, couchers de soleil à bandes, grilles en perspective, palmiers, statues antiques, fenêtres d'anciens systèmes d'exploitation. Genre collectif : on ne reprend aucune pochette, aucun logo, aucune marque d'ordinateur.
- **Ce que c'est** : une scène nocturne dessinée en **tubes néon** (halo large + cœur presque blanc) sur fond violet profond, avec une **grille en perspective qui défile**, un **soleil à bandes** qui monte, une enseigne qui clignote, le tout **relu par une cassette vidéo** (séparation des couleurs, bande de bruit, lignes, incrustation « PLAY »).
- **Marche pour** : musique et playlists, visuel d'attente d'un direct, annonce de soirée, bande-annonce rétro, pause contemplative, boucle d'ambiance.
- **Ne marche pas pour** : explication, chiffres, tutoriel, marque sérieuse, tout film où le texte porte le message (le look fatigue vite l'œil et gêne la lecture). Format court : 10 à 30 s.
- Carte notée ★★★ par son auteur.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Magenta néon | `#FF4FD8` |
| Rose chaud | `#FF2F8F` |
| Cyan néon | `#3FF6FF` |
| Violets profonds (fond) | `#12052A` · `#2A0B4A` ; mur en dégradé vertical `#0D0322` → `#4A0F6A` |
| **Jaune soleil** (contrepoids chaud) | `#FFD84A` |
| **Orange** (contrepoids chaud) | `#FF8A3A` |
| Vêtement du personnage (lisible sur peau rosée) | lavande `#8F7CF6`, col blanc, trait cyan |

- **Règle des contrepoids** : le soleil jaune → orange → magenta (ou une autre source jaune ou orange) est visible **dans chaque plan** ; le texte à lire est blanc cassé ou jaune, jamais magenta sur violet.
- Lumière du personnage : contour lumineux **rose côté fenêtre, cyan côté opposé**.
- **Typographie** : **Press Start 2P** (OFL) pour l'incrustation de magnétoscope (« PLAY », date, compteur). Les enseignes néon sont **dessinées en traits** (1 à 3 traits par lettre), pas écrites avec une police : la police ne contient ni les caractères pleine largeur ni les symboles (▶), et retomberait en silence sur une police système. Titres : capitales espacées (interlettrage ≈ 7 px).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Space Mono à la place de Press Start 2P. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/press-start-2p` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : tube néon, grille filaire, marbre gris-violet d'une statue (veines, liseré rose), plastique gris d'une fenêtre d'ancien système (barre de titre bleu marine, barre de progression en blocs).

## 3. Composition 9:16

- Trois étages : **ciel et soleil** (y 200 à 900), **ligne d'horizon** avec montagnes filaires vers y 900 à 1000, **grille de sol en perspective** (y 1000 à 1920) dont le point de fuite est au centre de l'horizon (x 540).
- Soleil : disque de 520 à 640 px de diamètre, centré x 540, découpé de 7 fentes horizontales de plus en plus larges vers le bas.
- Sujet (personnage, objet, statue) en silhouette lumineuse entre y 700 et 1400, à gauche de x 945. Palmiers en silhouette sur les bords.
- Enseigne ou titre néon en haut (y 200 à 420), traits de 10 à 14 px avec halo.
- Incrustation magnétoscope : « PLAY ▶ » en haut à gauche (y 180), date en bas à gauche (y 1500). Elle est dessinée **par-dessus** l'effet cassette et n'est pas déformée.
- Texte utile : au plus 2 lignes de 5 mots, 72 à 96 px, blanc cassé, sur une zone sombre.
- 16:9 : même empilement, plus de place pour une fenêtre d'interface rétro sur le côté.

## 4. Ce qui bouge

- **Action principale** : le soleil à bandes qui monte lentement derrière le sujet, ou un seul geste lent du personnage.
- **Boucle de fond 1** : la **grille de sol défile** vers le spectateur (lignes horizontales à `y = horizon + k / d`, plus épaisses en approchant).
- **Boucle de fond 2** : l'enseigne **clignote lettre par lettre** (chaque lettre est éteinte ≈ 7 % du temps, tube sombre dessiné à la place ; une extinction dure au moins 3 images, une même lettre ne s'éteint pas plus de 3 fois par seconde, et jamais toute l'enseigne à la fois : un néon lumineux sur fond sombre est un fort contraste, et un clignotement plus rapide est un risque pour les personnes photosensibles), palmiers qui se balancent, bande de bruit qui descend.
- **Autorisés** : `#023` glitch (déchirure de cassette, pour les transitions), `#111` séparation des couleurs, `#027` avancée lente, `#125` pulsation des néons, `#016` parallaxe (soleil, montagnes, grille), `#094` texte défilant, `#039` accéléré du ciel, `#045` volet par défilement vertical de cassette.
- **Interdits** : montage rapide, `#024` secousses, `#011` écrasement et étirement, `#001` rebonds joyeux, `#015` particules scintillantes génériques, lueur diffuse sans tube dessiné (c'est précisément le look refusé par la porte).
- Tout est lent. Le seul mouvement nerveux est celui de la cassette.

## 5. Rythme et montage

- Plans longs de 4 à 8 s, 2 à 5 plans par film. Musique lente (70 à 100 BPM).
- **Transition signature** : déchirure de cassette + défilement vertical de l'image (≈ 0,4 s).
- La bande de bruit de suivi (≈ 70 px de haut) traverse l'image de haut en bas en continu ; un saut de séparation des couleurs plus fort arrive de temps en temps (≈ 12 % des dessins).
- Fin : arrêt sur image avec « PAUSE », ou la cassette qui s'éjecte (image qui s'écrase en une ligne).
- **Version courte (8 à 12 s)** : un ou deux plans : le soleil monte, la grille défile, **une déchirure de cassette avant 3 s** (c'est l'accroche), le texte utile tenu 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames ; toute la scène est dessinée dans un canvas hors écran, puis une **passe cassette** la recopie à l'écran. L'incrustation est dessinée après.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `neon.js` (tube lumineux), `decor.js` (mur, soleil, montagnes, grille), `enseigne.js` (lettres en traits + clignotement à graine), `cassette.js` (passe finale), `incrustation.js`.
- **Techniques clés** :
  ```js
  // tube néon : le même tracé deux fois
  function tube(ctx, tracer, couleur, largeur = 10, halo = 28) {
    ctx.save(); ctx.shadowColor = couleur; ctx.shadowBlur = halo;
    ctx.strokeStyle = couleur; ctx.lineWidth = largeur; tracer(); ctx.stroke(); ctx.restore();
    ctx.strokeStyle = "#fff8ff"; ctx.lineWidth = 3; tracer(); ctx.stroke();   // cœur
  }
  // fentes du soleil : découpe en destination-out, largeur 2 + q*q*16 (q = profondeur 0..1)
  ```
  - **Séparation des couleurs** : pour chaque canal, copier la scène, la multiplier par du rouge, du vert ou du bleu pur, puis additionner les trois copies décalées de 3 ± 1,5 px sur fond noir.
  - **Bande de bruit** : dans la bande, décaler chaque tranche de 6 px horizontalement de ±30 px et ajouter des lignes gris-blanc.
  - **Lignes de balayage** : motif de 4 px (une rangée à 28 % de noir, une à 12 %).
  - Clignotement : hasard à graine indexé sur le numéro d'image, jamais `Math.random()`.
- **Pièges** :
  - Vêtement rose sur peau rosée : le personnage a l'air nu. Prendre une couleur distincte (lavande) avec col blanc.
  - Halo sur chaque pièce du personnage : les jonctions (taille, bras) brillent aussi. Pour un contour extérieur pur, dessine d'abord la silhouette hors écran, puis trace son bord.
  - La passe cassette fait bouger tout l'écran (≈ 25 % de différence d'une image à l'autre) : l'encodage gonfle ; garde le bruit modéré et vérifie le poids du fichier.
  - Sur une plateforme qui recompresse, les lignes fines produisent du moiré : teste l'export à 540 px de large.

## 7. Son

- **Musique** : nappes de synthétiseur lentes, piano électrique, saxophone lointain, boîte à rythmes douce, beaucoup de réverbération ; ou un morceau du client ralenti et étouffé. Pas de morceau existant ralenti sans droits.
- **Bruitages** (≈ 3 à 5 par 10 s) : clac d'insertion de cassette, ronflement du magnétoscope, grésillement de néon, souffle de bande, bip d'interface rétro.
- **Ambiance** : ville lointaine la nuit ou mer calme.
- **Traitement** : léger pleurage sur la musique pour rappeler la bande. Voix rare, chuchotée ou absente. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : dégradé violet nu avec lueurs floues (le look « IA » exact), texte magenta illisible, aucun jaune ni orange, clignotement aléatoire non reproductible, effet cassette plaqué sur l'incrustation.

- [ ] Dérogation préparée : image de style validée par le client, raison écrite, part d'images bleu-violet mesurée.
- [ ] Une couleur chaude saturée (jaune ou orange) visible dans chaque plan.
- [ ] Chaque lueur vient d'un tube dessiné (halo + cœur clair), aucune lueur flottante.
- [ ] La grille de sol défile et converge vers un seul point de fuite.
- [ ] Le soleil porte ses fentes horizontales, plus larges vers le bas.
- [ ] Passe cassette présente : séparation des couleurs, bande de bruit, lignes ; incrustation nette par-dessus.
- [ ] Tout texte à lire est blanc cassé ou jaune, contraste ≥ 4,5:1.
- [ ] Même image rendue deux fois = identique (clignotements à graine).

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt d'origine. Planche commune : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg (© 花叔 Huashu ; à consulter, pas à réutiliser en vitrine).
- Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/26_vaporwave.md` (carte traduite du chinois), `scripts/engine/scenes/26_vaporwave.js` ; règle bleu-violet : `scripts/film_gate.py`, `references/色板.md`. Licence MIT, © 花叔 Huashu.
- Police Press Start 2P : SIL OFL 1.1.
- Adaptation Flot Web : traduction, composition 9:16, règle des contrepoids chauds, procédure de dérogation, sections rythme et son (non fixées par la source), numéros du dictionnaire.
