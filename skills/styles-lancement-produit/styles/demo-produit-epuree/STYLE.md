# Démo produit épurée (la caméra fait le montage)

## 1. Identité
- **Nom** : Démo produit épurée. Identifiant : `demo-produit-epuree`.
- **Inspiration** : la démo calme et soignée qu'une jeune entreprise bien financée met sur sa page d'accueil.
- **Principe** : tout le secret est la **retenue**. Un fond clair et aéré, **une courte ligne de texte à la fois**, et l'interface du produit **reconstruite proprement et filmée de très près** pendant qu'on s'en sert. **C'est la caméra qui raconte** : elle pousse vers une ligne de texte, accompagne la frappe, recule pour révéler le résultat, glisse vers la fonction suivante.
- **Pour quels sujets** : présentation des fonctions d'un logiciel ou d'une appli, vidéo de page d'accueil, tutoriel d'accueil, « voici ce que ça fait » en 45 à 90 s (ou 25 à 35 s pour les réseaux).
- **Ne marche pas pour** : un teaser qui doit exciter (voir `teaser-haute-energie`), un produit sans interface, un sujet à raconter par une voix (le texte à l'écran est ici la seule « voix »).

## 2. Palette, typographie, matières
- **Palette par défaut** : fond `#F7F7F8`, texte `#111114`, secondaire `#8A8A94`, surfaces d'interface blanches à bordure `#E7E7EC`, accent de marque `#2E6BFF`, boîte de surlignage = accent à 15-20 % d'opacité. Les couleurs de la fiche « ma chaîne » remplacent l'accent. **Un seul accent.**
- **Dégradé de marque** : blanc → accent pâle → accent, en lentes bandes diagonales soyeuses (à dessiner une fois sur un canvas, pas avec un flou CSS).
- **Typographie** : la police de la marque si elle est connue, sinon Inter ou Geist. **Petite et de graisse normale pour les lignes de titre : elles deviennent grandes par la caméra, pas par la taille de police.** Interlettrage serré sur les grands textes.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Geist ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/geist` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Interface réelle, rendue propre** : reconstruite en vectoriel net (pas des captures), d'après ce qu'on sait du produit ou de son site : sa vraie disposition, ses libellés, ses couleurs, ses rayons, simplifiée à ce que la scène demande. Le contenu est une donnée d'exemple crédible qui colle au produit. Ombres douces, bordures de 1 px, beaucoup de blanc.
- **Curseur** : une flèche normale, sur des courbes douces, qui arrive un temps avant de cliquer, avec un petit enfoncement et une onde douce sur le bouton cliqué ; les états de survol changent.
- **Interdits de matière** : fond chargé derrière l'interface, plus d'un accent, émojis, grosses ombres portées, verre dépoli partout, chiffres ou témoignages inventés.

## 3. Composition 9:16
- **Une seule chose à la fois** : jamais plus d'une ligne de texte plus un élément d'interface à l'écran. Texte et interface ne partagent presque jamais le cadre : scène de texte, puis scène d'interface.
- **Ligne de titre** : une phrase courte, centrée vers y 820. Après la poussée de caméra, elle occupe environ **75 % de la largeur** (≈ 810 px) ; si elle est longue, la couper en deux lignes dès l'écriture, de sorte que chaque ligne fasse 54 px ou plus à l'écran après la poussée.
- **Surlignage** : une boîte d'accent douce balaie de gauche à droite derrière **un** mot ou groupe clé.
- **Moment d'interface** : rogné sur **la seule partie qui compte**, montré grand : l'élément remplit 80 à 90 % de la largeur, entre y 300 et y 1400. En vertical, recomposer : un champ de saisie pleine largeur, une colonne de cartes de résultat, un tableau réduit à 2 ou 3 colonnes.
- **Le recul** : après l'action, la caméra recule pour montrer tout l'écran un temps, puis glisse.
- **Carte de fin** (3 s) : logo ou nom sur le dégradé de marque, adresse ou appel à l'action en petit dessous.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : la ligne de titre fait environ 28 px avant la poussée ; mêmes règles.

## 4. Ce qui bouge
- **Action principale** : la caméra. **Chaque scène est son propre calque avec sa propre caméra** : dans une scène, elle pousse, accompagne et recule ; entre deux scènes, le calque sortant se dissout dans un court flou (0,3 à 0,4 s) vers le suivant, **qui est déjà en mouvement**.
- **Boucles de fond** : (1) les bandes soyeuses du dégradé de marque qui dérivent lentement ; (2) la dérive lente de la caméra pendant les tenues.
- **Mouvements de caméra** : amortis lisses de 0,6 à 1,2 s ou ressorts très amortis (amortissement ≥ 0,95). **Rien ne rebondit.**
- **Moments d'interface à vitesse réelle** : frappe à ~25 caractères par seconde, la caméra suit le curseur de texte ; étapes d'un agent qui se cochent une à une (roue → coche, « 247 résultats trouvés ») ; cartes de résultat qui s'empilent avec les plus lointaines floues ; tableau qui se remplit ligne par ligne ; nouvelle colonne dont chaque cellule « réfléchit » avec un reflet avant d'afficher sa valeur ; info-bulle qui s'ouvre.
- **Autorisés** : #027 poussée, #028 zoom, #029 suivi de la frappe, #080 surlignage, #006 frappe dans un champ, #002 cascade, #069 squelette de chargement, #070 roue, #083 curseur, #085 onde, #105 flou de profondeur, #016 parallaxe (scène des intégrations), #044 fondu-flou court entre scènes, #007 compteur (vrais nombres seulement).
- **Interdits** : coupes franches, #123 rebonds, texte et interface entassés, caméra immobile sur une interface entière en petit, plusieurs lignes de texte à la fois.

## 5. Rythme et montage
- **60 secondes par défaut** ; de 45 à 90 s ; **25 s au moins** pour la version réseaux : en dessous, les tenues de 2 s par ligne ne tiennent plus (un essai en 10 s l'a montré ; voir la version courte en fin de section, à réserver à un aperçu). Budget :

| Durée | Fonctions | Sections optionnelles |
|---|---|---|
| 25 à 35 s (réseaux) | 2, environ 8 s chacune | aucune |
| 45 s | 2 à 3, environ 9 s chacune | preuve ou intégrations, pas les deux |
| 60 s | 3 à 4, environ 10 s chacune | l'une des deux |
| 90 s | 4 à 5, environ 12 s chacune | les deux |

- **Structure** : 1) ouverture (0 à 5 s) : un petit mot au centre (« Voici »), qui se dissout dans le moment de marque ; 2) le problème ou la demande (≈ 5 s) : une ligne que le spectateur reconnaît, ou directement le champ de saisie du produit ; 3) **chapitres de fonction** (3 à 5) : ligne de titre → poussée et surlignage → moment d'interface → recul ; 4) preuve (optionnelle, vrais nombres seulement) ; 5) intégrations (optionnel) : tuiles d'applis qui flottent en profondeur, vrais logos seulement s'ils sont fournis ; 6) conclusion : une phrase avec un mot surligné qui tourne entre les usages ; 7) carte de fin (3 s).
- **Écrire d'abord le script et la feuille des temps** : chaque ligne de texte à l'écran, le moment d'interface qui la suit, son temps ; additionner contre le budget.
- **Tenues** : chaque ligne de titre tient environ 2 s après s'être posée ; pause de 0,5 s après chaque résultat pour qu'on le lise.
- Version réseaux : la première ligne est l'accroche et apparaît dès l'image 0.
- **Version courte (8 à 12 s)** : une ligne d'accroche (échelle de départ d'au moins 1,7 pour qu'elle se lise à l'image 0), **une seule scène de produit** (une poussée, un clic, un résultat), la carte de fin ; ni preuve ni intégrations ; tenue de 1,25 s au moins par ligne (au lieu de 2 s). Garder un mouvement visible à tout instant : la dérive de caméra seule ne suffit pas à la porte de livraison. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique
- **Moteur** : HyperFrames + GSAP. **Une scène par fichier de `compositions/`**, chacune avec son nœud « caméra » qui porte tout le contenu de la scène, et sa propre timeline. Ne mets pas les scènes en `<section class="clip">` dans `index.html` : au rendu réel du 11/11/2026, cette écriture a donné trois avertissements `nested_structure_needs_subcomposition` (un `.clip` qui contient une structure). `index.html` ne fait que placer les scènes dans le temps :
```html
<!-- index.html : la racine place chaque scène ; les sons restent ici -->
<div id="root" data-composition-id="main" data-start="0" data-duration="30" data-width="1080" data-height="1920" data-fps="30">
  <div id="scene-1" data-composition-id="scene-1" data-composition-src="compositions/scene-1.html"
       data-start="0" data-duration="5" data-track-index="1" data-width="1080" data-height="1920"></div>
  <div id="scene-2" data-composition-id="scene-2" data-composition-src="compositions/scene-2.html"
       data-start="4.65" data-duration="9" data-track-index="2" data-width="1080" data-height="1920"></div>
</div>
<script>window.__timelines["main"] = gsap.timeline({ paused: true });</script>

<!-- compositions/scene-2.html : styles, balises et scripts dans <template> ; la racine se stylise par #root -->
<template>
  <style>#root { position: absolute; inset: 0; } #cam { position: absolute; inset: 0; transform-origin: 540px 820px; }</style>
  <div id="root" data-composition-id="scene-2" data-width="1080" data-height="1920"><div id="cam">…</div></div>
  <script>const tl = gsap.timeline({ paused: true }); /* tweens de la scène, en temps local */ window.__timelines["scene-2"] = tl;</script>
</template>
```
  Cette structure (racine + fichiers de `compositions/`) est celle qui a rendu sans avertissement le film d'essai `info-sous-titres` du 11/11/2026 ; elle n'a pas été re-rendue pour ce style. Les deux scènes se recouvrent de 0,35 s pour le fondu-flou.
```js
// chapitre : la ligne se pose, la caméra pousse dessus, un mot se surligne
tl.fromTo("#l3 .mot", {opacity: 0, y: 8}, {opacity: 1, y: 0, stagger: 0.09, duration: 0.4}, 0)
  .to("#cam3", {scale: 2.6, duration: 1.0, ease: "power2.inOut"}, 0.9)          // 28 px → ~73 px à l'écran
  .fromTo("#l3 .surligne", {scaleX: 0}, {scaleX: 1, transformOrigin: "left", duration: 0.45}, 1.7);
// moment d'interface : la caméra suit le curseur de texte pendant la frappe
const pos = i => mesure.measureText(texte.slice(0, i)).width;                   // position du curseur de texte
tl.to(etat, {n: texte.length, duration: texte.length / 25, ease: "none", onUpdate() {
  champ.textContent = texte.slice(0, Math.round(etat.n));
  gsap.set("#cam4", {x: -(pos(Math.round(etat.n)) - 300) * 2.2});               // la caméra accompagne
}}, 0.3)
  .to("#cam4", {scale: 1, x: 0, duration: 1.1, ease: "power2.inOut"}, ">+0.5"); // le recul
```
- Entre scènes : `filter: blur()` court (0 → 8 px) + opacité sur le calque sortant, pendant que l'entrée du suivant a déjà commencé. Donner un `filter: blur(0px)` explicite au départ.
- **Polices embarquées** ; dégradé soyeux dessiné une fois sur un canvas.
- **Constats du rendu réel** (11/11/2026) : après un recul de caméra, un texte d'interface tombe vite sous 28 px à l'écran (recul limité à 0,86 au lieu de 0,8) ; les textes d'interface de 34 à 42 px sont petits sur téléphone : rogner plus serré ; le curseur ne reste pas posé sur le texte qu'on tape ; un texte tapé reste lisible 1,25 s au moins après le dernier caractère ; ligne de titre à l'image 0 : échelle de départ 1,7, sinon elle fait 45 px et ne s'y lit pas.
- **Pièges** : jamais `will-change` sur ce que la caméra agrandit ; une interface entière réduite est illisible (rogner) ; un texte de titre trop gros « avant la caméra » supprime l'effet de poussée ; données d'exemple incohérentes d'une scène à l'autre (garder le même exemple tout du long).
- **Caméra et curseur** : `references/camera-et-curseur.md`. **Vérité des contenus** : `references/script-de-lancement.md` §4. **Finition** : `references/etalonnage.md` (registre clair seulement, sans halo).

## 7. Son
- **Un lit doux et lumineux, 100 à 110 BPM** (accords de piano ou de cordes pincées, percussion légère qui entre après l'ouverture, une levée vers la conclusion), discret et chaud. La musique reste un fond, elle ne conduit pas.
- **Petits bruitages** (budget du skill `son`, vrais enregistrements d'abord) : tics de touches pendant la frappe, clics doux, un léger tic par étape accomplie, un souffle doux sur les grands mouvements de caméra, un petit carillon sur la carte de fin.
- −14 LUFS (la source vise −16).
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Jamais plus d'une ligne de texte et d'un élément d'interface à l'écran.
- [ ] Aucune coupe franche : chaque changement est un mouvement de caméra ou un fondu-flou court.
- [ ] Chaque moment d'interface est rogné et grand ; chaque chapitre a son recul.
- [ ] L'interface ressemble au vrai produit (libellés, couleurs, rayons) ; mêmes données d'exemple partout.
- [ ] Un seul accent ; rien ne rebondit.
- [ ] Aucun chiffre ni témoignage inventé ; logos de tiers seulement s'ils ont été fournis.
- [ ] Le texte à l'écran raconte l'histoire à lui seul (lecture muette) ; chaque ligne tient ~2 s.
- [ ] Texte net pendant les poussées ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- GIF de démonstration du dépôt d'origine : https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-default.gif. Crédit : Bart, dépôt sous licence MIT. Lien seulement ; aperçu Flot Web en 9:16 à produire.

## 10. Origine
- Dépôt : Barty-Bart/motion-graphics, commit `3d83d98`. Fichier : `skills/explainer-default/SKILL.md`.
- Licence : MIT (© 2026 Bart).
- Adaptations Flot Web : français, **réécrit pour HyperFrames**, composition 9:16 et version courte pour les réseaux, −14 LUFS.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : image conforme, mais 10 s est trop court pour ce style (tenues de lecture refusées) et le mouvement, discret, était refusé par l'ancienne porte ; à produire en 25 s au moins.
