# Trait continu

## 1. Identité

- **Nom** : Trait continu (« One-line Drawing », dessin d'un seul trait).
- **Inspiration** : les dessins animés où une seule ligne est à la fois le monde et le personnage, les photographies de dessins faits à la lumière d'un seul geste, les films expérimentaux où le trait est dessiné *sur* la musique. On emprunte la grammaire, jamais un personnage, une voix ou une illustration existante.
- **Ce que c'est** : **une ligne d'encre continue** sur papier blanc chaud. La plume ne se lève jamais : tout le film peut être un seul tableau de points, du premier contact à la dernière image. **Tout est une ligne** : personnages, lieux, objets, même le temps. Ni aplat, ni ombre, ni deuxième épaisseur, ni décor. **On regarde la ligne se dessiner** ; la caméra suit la plume avec un peu de retard et d'anticipation. À part l'encre : le papier et l'ombre douce du stylo. **Un accent de couleur au plus, utilisé une seule fois.**
- **Marche pour** : un parcours, une chronologie, une transformation (graine → arbre → table), une vie, une signature de marque, un graphique qui raconte, une transmission.
- **Ne marche pas pour** : comparaison de plusieurs objets en même temps, produit à montrer en détail, beaucoup de texte, montage rapide.
- **À ne pas confondre** : pas un tableau blanc (ni main, ni effacement, ni panneaux de texte) ; pas du lavis ; pas une animation au trait avec des coupes.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Papier | `#F4EFE4` |
| Encre (noir chaud) | `#1D1A17` |
| Accent unique (exemples : rouge amour ou danger, bleu eau ou froid, or argent ou prix) | `#C8362E` · `#2F6FB0` · `#C9A227` |

- L'accent colore **un tronçon** de la ligne qui a un sens, puis la ligne redevient encre ; il reste visible dans l'image finale si elle est révélée. Jamais de second accent.
- **Typographie** (OFL) : sous-titres en **Caveat** (écriture), titres en **Sacramento** (une cursive monoligne, elle-même un dessin d'un trait).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat ; Playfair Display à la place de Sacramento. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat`, `@fontsource/sacramento` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Papier* : marbrure procédurale, longues fibres qui s'effacent quand on dézoome (sinon elles scintillent), fin grain par-dessus l'encre en gros plan, léger vignettage. Tout est ancré au papier.
  - *Encre* : un **polygone rempli** autour du tracé (pas un simple trait de contour). Largeur = largeur de base × pression × bruit fin (±8 %). La pression vient de la vitesse : rapide = fin, lent = épais.
  - Bavure : le même polygone un peu plus large, flouté, composé à ≈ 20 %. Petites flaques rondes là où la vitesse tombe. Tremblement et manques de brosse sèche pour l'âge, la peur ou la fatigue.
  - Un arrêt laisse une **tache en goutte** : pointe à la plume, ventre qui s'affaisse vers le bas, liseré sombre au bord.
  - **Le stylo n'est jamais dessiné** : seulement son ombre floue en coin et un minuscule point de contact. Des mains éventuelles n'apparaissent que comme ombres.

## 3. Composition 9:16

- Le dessin vit sur une grande feuille ; le cadre vertical la suit. Conçois le tracé pour qu'il **monte et descende** autant qu'il avance : en 9:16, une ligne qui ne va que vers la droite sort du cadre en une seconde.
- La plume reste dans les **70 % centraux** du cadre (x 160 à 920, y 290 à 1560 : la source descendait à y 1630, sous la limite basse du studio), ramenée en douceur si elle s'en approche.
- Épaisseur de base à l'écran : 5 à 8 px ; **largeur minimale garantie à l'écran** pendant les reculs, pour que la vue large garde son poids.
- **Sous-titres écrits comme la ligne** : Caveat 56 à 64 px, encre à ≈ 84 %, sans boîte, centrés vers y ≈ 1440, écrits de gauche à droite (≈ 0,2 s + 17 ms par caractère) derrière un halo couleur papier pour qu'aucune ligne ne traverse les lettres ; disparition en ≈ 0,45 s. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Titre : dans du papier vide, loin du dessin, parti avant que la caméra n'y entre.
- 16:9 : identique ; le défilement latéral « la ligne court devant » y est plus à l'aise.

## 4. Ce qui bouge

- **Action principale** : la plume qui avance. Vitesse de 300 à 700 unités par seconde pour les lignes de voyage, 50 à 150 pour les petits détails. **Le trait le plus important est en général le plus lent.**
- **Boucle de fond 1** : la caméra elle-même, un seul mouvement continu (centre, zoom, quelques degrés de roulis) qui suit la plume en la moyennant sur ≈ −0,55 à +0,4 s.
- **Boucle de fond 2** : l'ombre du stylo qui glisse et la respiration de l'épaisseur.
- **Gestes natifs** : la plume ne se lève jamais ; la ligne est le temps (son caractère change avec l'âge ou l'effort) ; la transformation (le dernier trait d'une image est le premier de la suivante) ; **l'arrêt est un événement** (la plume s'arrête, l'encre s'étale, la musique se tait 1,5 à 3 s) ; la révélation d'échelle (chaque vignette faisait partie d'une seule grande image) ; le passage de main ; la ligne qui devient graphique.
- **Autorisés** : `#004` tracé de ligne, `#126` trajet de mouvement, `#012` métamorphose (par le tracé), `#172` plan-séquence, `#174` plan qui suit, `#027` avancée lente pendant un arrêt, `#028` recul continu, `#170` roulis avec la ligne, `#184` très gros plan sur la plume.
- **Interdits** : **toute coupe** (`#041`, `#046`, `#192`), `#044` fondu enchaîné, `#128` saccadé (ici tout est dessiné à chaque image), aplats, ombres, deuxième couleur, texte typographié.
- Repasser sur une ligne existante est permis et invisible (elle épaissit à peine).

## 5. Rythme et montage

- Aucune coupe : **un seul plan** de la première à la dernière image. Le rythme vient de la vitesse de la plume.
- Le temps est réparti par chapitres, puis par courbure : un virage serré reçoit plus de temps (la vitesse ne saute jamais). Les temps forts de la musique sont épinglés sur des points précis du tracé.
- Durée conseillée : 20 à 45 s. Un arrêt (silence) et une révélation finale suffisent.
- Écris la musique **sur le dessin** : notes clés sur les angles, ligne rapide = notes courtes, ligne arrêtée = une note longue qui s'éteint, la note la plus haute sur le contact le plus important.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `trace.js` (chapitres écrits comme des chemins SVG, échantillonnés à pas constant, reliés par des raccords à tangente continue, temps réparti selon la courbure), `encre.js` (pression, bavure, flaques, tremblement, brosse sèche, tronçon d'accent, tache), `papier.js`, `camera.js` (cadrages clés + suivi de la plume), `ombres.js`, `sous-titres.js`.
- **Techniques clés** :
  ```js
  const pression = 0.66 + 0.8 * Math.exp(-vitesse / 300);   // rapide = fin, lent = épais
  const poids    = 1 + K * courbure;                        // temps par point : les virages durent plus
  const largeur  = base * pression * (1 + 0.08 * bruit(i)) * Math.max(zoom, zoomMini);
  ```
  - Le dessin tient dans un fichier de chemins et une table de chapitres : remplace-le par le tien.
  - Prévois une vue de contrôle qui rend **tout le tracé d'un coup** à l'échelle finale.
- **Pièges** :
  - **Un raccord parasite ruine une révélation** : chaque ligne en trop se lit comme une ride, une barbe ou un masque. Corrige l'ordre de parcours (où chaque chapitre entre et sort), pas le dessin. Pense-le comme un chemin qui passe une fois partout : un motif fermé se quitte par où on y est entré.
  - Teste la révélation tôt et souvent, après chaque modification.
  - Deux lignes trop proches se tressent une fois l'épaisseur appliquée : garde un écart.
  - Une tache ronde se lit comme un grain de beauté : fais une goutte qui s'affaisse.
  - Deux ombres de main translucides se doublent là où elles se croisent : un seul calque par main.
  - Le titre percute le dessin quand la caméra bouge : vérifie chaque image de sa fenêtre.

## 7. Son

- **Musique** : **un seul instrument soliste, une seule ligne mélodique ininterrompue**, l'équivalent sonore du dessin : violoncelle, violon, alto ou harpe, clarinette, flûte ou basson, une voix fredonnée, une guitare seule. Une seconde couleur seulement en rare accent. Aucune nappe.
- **Le stylo sur le papier est le son le plus important** : un frottement dont la brillance et le niveau suivent la vitesse de la plume, placé à gauche ou à droite selon sa position, interrompu dans les manques d'encre. Plus : un petit choc de bois au premier contact, un léger gonflement humide pour une tache, une page soulevée. (C'est un son continu : il compte pour un dans le budget, les autres restent rares.)
- **Le silence est littéral** : musique à zéro, queues de réverbération comprises.
- **Voix** : chaude, peu de phrases, courtes, qui laissent la place à la ligne. Musique baissée d'environ 5 dB sous la voix. Mix −14 LUFS, aucun grain ajouté.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : plusieurs traits qui apparaissent en même temps ; une coupe ; un aplat ; la plume qui sort du cadre ; trait uniforme de logiciel ; révélation illisible.

- [ ] Du début à la fin, une seule ligne : aucun lever de plume, aucune coupe.
- [ ] L'épaisseur varie avec la vitesse (plus épais dans les virages lents).
- [ ] Encre et papier seulement, plus un accent utilisé une fois.
- [ ] La plume reste dans les 70 % centraux du cadre à chaque image.
- [ ] La vue d'ensemble finale se lit en 2 secondes par quelqu'un qui n'a pas vu le film.
- [ ] Au moins un arrêt avec tache d'encre et silence complet.
- [ ] Les sous-titres sont écrits, sans boîte, hors de la zone y > 1560.
- [ ] Le stylo et la main ne sont visibles que par leur ombre.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *The Line That Never Lifted* (48 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/one-line.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/one-line.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/one-line.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre le dessin ni l'histoire.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/one-line/STYLE.md`, `DEMO.md`, `demo/geom.js`, `ink.js`, `paper.js`, `cam.js`, `hands.js`, `subs.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, contraintes de tracé pour le vertical, numéros du dictionnaire de mouvements, cadence 30 i/s (24 i/s dans l'original).
