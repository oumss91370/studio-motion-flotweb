# Cartoon plat années 50

## 1. Identité

- **Nom** : Cartoon plat années 50 (« mid-century »).
- **Inspiration** : les courts métrages modernistes du début des années 50 (couleur et trait sur deux cellulos séparés, personnages géométriques, décors en plans de couleur, animation limitée), les films de classe de la même époque (un narrateur calme, une phrase par image, cartons numérotés), et les modes d'emploi d'électroménager (médaillons numérotés, flèches courbes, bulles rondes, étoiles). On n'en copie ni les personnages, ni les dessins, ni le lettrage, ni la musique.
- **Ce que c'est** : un **style d'usage**. Il ne raconte pas une histoire, il fait faire quelque chose : guide d'installation, mode d'emploi, fiche recette, règles de sécurité. Le spectateur doit repartir capable de le faire. Couleur plate d'aspect imprimé, trait d'encre fin qui respire et ne se ferme jamais tout à fait. **Chaque aplat est un cellulo imprimé quelques pixels à côté de son trait**.
- **Marche pour** : installation d'un produit en 2 à 5 étapes, règles (piscine, atelier, musée), recette, prise en main d'une appli, annonce de magasin ou d'évènement.
- **Ne marche pas pour** : expliquer *pourquoi* (prends un tableau blanc), récit à suspense, sujet sombre, tout ce qui demande du réalisme.
- Ce n'est pas le cartoon des années 30 (pas de noir et blanc, pas de monde qui rebondit, pas de jazz endiablé).

## 2. Palette, typographie, matières

Fond papier chaud, encre presque noire chaude, complémentaires douces « âge atomique ». Rien de pur, rien de fluo.

| Rôle | Hex |
|---|---|
| Papier (et ses deux ombres) | `#F4EAD5` · `#E6D8BC` · `#D4C29F` |
| Encre (noir chaud) | `#2B2420` |
| Corail (accent : le vêtement du présentateur) | `#E4613F` / foncé `#B8452B` |
| Moutarde (fond d'accroche, pois) | `#E8B43A` / clair `#F3D37F` |
| Turquoise (**le produit**) | `#3FA7A0` / foncé `#257A74` |
| Fonds des étapes | bleu poussière `#7F9CC0` · avocat `#A7AE5B` · rose `#F0B4A8` · prune `#6E4A6B` |
| Kraft (carton) | `#C9955D` |

- **Une couleur de fond par scène** : teinte plus claire pour le mur, plus foncée pour le sol. Jamais le produit sur sa propre couleur, jamais le présentateur sur son accent.
- **Le produit garde une seule couleur** pendant tout le film ; l'accent est une autre teinte. Autres gammes possibles : tomate / olive / bleu poudre sur avoine ; prune / citron vert / sable sur blanc cassé.
- **Typographie** (OFL) : **Oleo Script Bold** pour le mot d'accroche manuscrit ; **Alfa Slab One** pour titres, chiffres et en-têtes (encre sur plaque de couleur décalée) ; **Jost 500/600** pour le texte, les étiquettes et les légendes.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place d'Oleo Script ; Archivo Black à la place d'Alfa Slab One ; Outfit à la place de Jost. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/oleo-script`, `@fontsource/alfa-slab-one`, `@fontsource/jost` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : léger « pinceau sec », grain de papier discret (impression, pas pellicule), vignettage chaud. Ombre portée = copie de la forme décalée en bas à droite, teinte papier à ≈ 50 %. Ombre de forme = un plan plus foncé découpé dans la forme, jamais de dégradé.
- **Ornements** : étincelles à 4 branches, étoiles à 8-18 pointes, rayons de soleil (≈ 30 secteurs translucides), formes en boomerang et en haricot, pois.

## 3. Composition 9:16

- Une scène = un plan de couleur, une bande de sol, une ligne d'horizon interrompue, un ou deux accessoires. On ne dessine pas la pièce.
- Vertical (mise en page tenue au rendu réel du 11/11/2026) : **présentateur en pied à gauche** (x 80 à 520, y 420 à 1350), **produit à droite ou devant**, **bulle ronde de gros plan** de 420 à 520 px de diamètre en haut (centre vers x 560, y 520) reliée par un filet à la main qui agit.
- **En-tête d'étape** en haut (y 180 à 330) : disque d'encre avec chiffre papier, petit « ÉTAPE n SUR N » espacé, titre de l'étape sur plaque crème, 64 à 80 px.
- **Carton de légende** en bas (y 1380 à 1540, x 140 à 900) : dalle arrondie couleur papier, fin filet d'encre, 44 à 48 px (lu sans peine à 360 px de large au rendu réel ; la taille est déclarée dans les réglages de la section 8). Le petit « ÉTAPE n SUR N » de l'en-tête ne descend pas sous 32 px. Durée ≥ max(1,8 s ; voix + 0,6 s ; caractères ÷ 12 + 1 s).
- Sujets clés à au moins 1/3 de la hauteur, hors de la bande de légende. Image de résumé **parfaitement fixe ≥ 3 s** : c'est celle qu'on capture.
- 16:9 : présentateur à gauche, produit au centre, bulle à droite.

## 4. Ce qui bouge

- **Action principale** : **une action de la main par étape**, posée exactement sur un temps. Le corps du présentateur est un dessin tenu : seuls bras, mains, yeux et bouche bougent.
- **Boucle de fond 1** : le décalage couleur / trait saute de ±1 à 2 px « en deux » : l'image scintille comme une peinture calée à la main pendant que la caméra glisse.
- **Boucle de fond 2** : petites étoiles qui tournent aux bouts des cartons, rayons de soleil qui pivotent lentement.
- **Autorisés** : `#001` apparition avec rebond (médaillons, étiquettes, titres : ≈ 0,25 s, fort dépassement), `#121` anticipation de la main (recul ou levée), `#122` suivi (recul, repos), `#004` trait qui se dessine (trajets, flèches), `#017` transition par masque rond (iris à travers un médaillon), `#018` volet en bloc de couleur, `#144` écran partagé « bon / mauvais », `#175` plan fixe, `#188` fermeture à l'iris sur un objet, `#027` avancée lente de quelques pour cent.
- **Interdits** : caméra à l'épaule (`#034`), `#044` fondu enchaîné, `#011` écrasement et étirement du corps, dégradés, néon, `#015` particules.
- Action de la main : anticipation, action rapide (0,15 à 0,25 s, ralentie à la fin), suivi. Pour atteindre le sol : pose à genoux, jamais des bras étirés.

## 5. Rythme et montage

- 30 à 40 s pour 2 à 5 étapes ; 3 à 4 s par règle pour une fiche de règles ; 15 à 25 s pour une annonce.
- Ordre de l'information pour un guide : nom du produit → titre → titre de l'étape → détail **sur le temps de l'action** → résultat → astuce → appel à l'action. Titre ≥ 4 s dans un film de 30 s ou plus (voir la version courte pour 8 à 12 s) ; le titre de l'étape reste toute l'étape.
- Transitions : cercles (iris), volets en bloc de couleur, coupes sur un temps.
- **Silence comme outil** : coupe tout, ambiance comprise, pendant le temps qui précède l'action la plus importante ; le premier son après (le clic, le versement) *est* l'étape.
- La donnée tombe sur l'image, jamais sous forme de diapositive.
- **Version courte (8 à 12 s)** : une accroche d'un mot (1,5 s au plus, pas de titre de 4 s), **deux étapes** de 2,5 à 3 s avec leur action de main sur un temps, puis le résumé fixe tenu 3 s ; couper l'astuce, l'appel à l'action et l'une des deux bulles de gros plan. Légendes de 2 à 4 mots (durée ≥ caractères ÷ 12 + 1 s). (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames. Deux voies, à choisir avant de dessiner :
  - **SVG en ligne** (voie du rendu réel du 11/11/2026, à prendre dès qu'il y a un personnage) : les pièces du skill `personnages` s'emploient telles quelles, les textes sont de vrais textes (le relevé et le contrôle de lecture les voient), `lint` et `check` passent. Limite : le ruban d'encre à largeur variable n'est pas fait ; les manques, oui (tirets).
  - **Canvas 2D** avec `renderAt(t)` (voie de la source) : rubans d'encre complets, mais les textes sont à relever à la main et les pièces SVG doivent être converties (voir `personnages/references/pieces-svg.md`, « Pièces SVG dans un style au trait propre »).
- **Extrait vérifié par un rendu réel** (voie SVG) : chaque forme est écrite **deux fois**, un aplat et un trait. Le décalage du cellulo et les manques du trait sont deux variables CSS que l'on change à chaque dessin (15 par seconde : tenues régulières de 2 images, mesurées sur le MP4).
  ```html
  <style>
    #scene { --dx: 4px; --dy: 4px; --do: 0; }
    .ap { stroke: none; transform: translate(var(--dx), var(--dy)); }          /* le cellulo couleur, décalé */
    .tr { fill: none; stroke: #2B2420; stroke-width: 4.5; stroke-linecap: round; stroke-linejoin: round;
          stroke-dasharray: 92 13 41 9 128 17 66 11; stroke-dashoffset: var(--do); }   /* le trait, avec ses manques */
    .en { fill: #2B2420; }                                                      /* forme pleine d'encre : suit le trait */
  </style>
  <rect class="ap" x="341" y="436" width="34" height="118" rx="15" fill="#B8452B"/><rect class="tr" x="341" y="436" width="34" height="118" rx="15"/>
  <script>
    function renderAt(t) {
      const tq = Math.floor(t * 15 + 1e-6) / 15;                               // temps des dessins
      scene.style.setProperty("--dx", (3 + hasard(tq, 1) * 2).toFixed(1) + "px");
      scene.style.setProperty("--dy", (3 + hasard(tq, 2) * 2).toFixed(1) + "px");
      scene.style.setProperty("--do", String(Math.floor(hasard(tq, 3) * 60)));   // les manques changent de place
      bras.setAttribute("transform", `rotate(${angleBras(tq)} 358 448)`);       // pivot de la pièce, en unités du gabarit
    }
    window.addEventListener("hf-seek", e => renderAt(e.detail.time)); renderAt(0);
    window.__timelines = window.__timelines || {};
    window.__timelines["main"] = gsap.timeline({ paused: true });   // timeline vide enregistrée (voir le skill `rendu`, film en canvas piloté par hf-seek)
  </script>
  ```
  - **Texte à deux plaques** : la copie de couleur décalée sous le mot d'encre porte `aria-hidden="true"` et **`data-layout-ignore`** ; sans cela, `check` sort `content_overlap` et `contrast_aa_failure` (deux textes l'un sur l'autre). Seul le mot d'encre porte `data-texte`.
  - **Épaisseur du trait du personnage** : 3 à 5 px, comme tout le reste. La fiche de style l'emporte sur le contour épais conseillé par défaut dans le skill `personnages`.
- **Structure en voie canvas** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `toon.js` (forme dans le style, rubans d'encre, plans, texte à deux plaques, flèche de notice, ornements, décalage global), `persos.js` (présentateur, mains gantées, produit), `icones.js`, `film.js` (bulle de gros plan, médaillon, étiquette, en-tête d'étape, transitions), `contenu.json` (textes et couleurs du client).
- **Techniques clés** (voie canvas) :
  ```js
  const tq = Math.floor(t * 15) / 15;
  const dx = 3 + hasard(tq, 1) * 2, dy = 3 + hasard(tq, 2) * 2; // décalage du cellulo
  ctx.save(); ctx.translate(dx, dy); remplir(forme, couleur); ctx.restore();
  tracerRuban(forme, { largeur: 4, respiration: 0.4, manques: 0.18 });
  ```
  - Trait : rubans d'encre de 3 à 5 px, largeur qui varie de ±40 %, 12 à 25 % de manques. Mains : un seul contour autour de la paume et des doigts réunis (tout tracer d'abord, remplir ensuite).
  - Gros plan : **dessiné à l'échelle dans une bulle ronde**, jamais en zoomant le monde (le zoom triple l'épaisseur de l'encre).
  - Le décalage s'applique à tout, texte compris ; on le coupe seulement pour un schéma qui doit être net.
- **Pièges** : nez en triangle collé (une seule courbe ouverte du front au bout du nez) ; bras en bâtons qui partent du cou (épaules aux coins du torse) ; doigts en boudins ; trajet qui ignore les obstacles (suis les vraies règles du produit, pose-le région par région) ; transition qui dessine la scène suivante avant son début.

## 7. Son

- **Musique** : petit ensemble de jazz « cool » original : flûte ou trompette bouchée, vibraphone, contrebasse en pizzicato, balais, célesta, bongos ou claquements de doigts. Pas de ragtime, pas de grand orchestre d'espionnage, pas de piano-cordes. Idée : **un accord de vibraphone par étape**, rejoués un à un pendant le résumé.
- **Bruitages par matière** (≈ 5 par 10 s) : carton, plastique d'appareil, verre et céramique, versement, tampon de caoutchouc étouffé pour un médaillon, papier pour un volet, « chk » de l'iris.
- **Ambiance** : ton de pièce chaud très bas, tic-tac d'horloge sur la grille de tempo.
- **Voix** : autorité calme de salle de classe, une proposition par phrase (« Étape un. Posez-le contre un mur. »). Musique baissée d'environ 8 dB sous la voix. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : corps entier animé, couleurs pures, pièce dessinée en détail, texte de détail sans temps de lecture, zoom du monde pour le gros plan.

- [ ] Chaque aplat est décalé de son trait, et ce décalage saute « en deux ».
- [ ] Le trait ne se ferme pas partout (manques visibles).
- [ ] Le produit garde la même couleur du début à la fin et n'est jamais posé sur un fond de sa couleur.
- [ ] Une seule action de la main par étape, calée sur un temps.
- [ ] Le corps du présentateur ne bouge pas pendant l'action de la main.
- [ ] Chaque texte tient au moins caractères ÷ 12 + 1 s.
- [ ] Une image de résumé fixe d'au moins 3 s.
- [ ] Le spectateur peut refaire le geste après une seule vision (test avec un regard neuf).

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 15
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *Meet Pip* (40 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/midcentury-toon.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/midcentury-toon.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/midcentury-toon/STYLE.md`, `DEMO.md`, `demo/engine/toon.js`, `engine/chars.js`, `engine/icons.js`, `film.js`, `content.json`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : Oleo Script, Alfa Slab One, Jost (SIL OFL 1.1).
- Adaptation Flot Web : traduction, mise en page 9:16, numéros du dictionnaire.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections, en SVG en ligne avec les pièces du skill `personnages` ; cadence de 15 dessins par seconde régulière ; son hors cible faute de musique.
