# Gravure sur cuivre

## 1. Identité

- **Nom** : Gravure sur cuivre (« Copperplate Engraving », taille-douce).
- **Inspiration** : les planches d'histoire naturelle et d'encyclopédie du XIXᵉ siècle (sujet centré, médaillons numérotés, titre en capitales romaines au-dessus d'un nom en italique, mentions du dessinateur et du graveur, cuvette de la plaque), la taille au burin des grands illustrateurs (hachures qui suivent la forme, ne se croisent que dans les demi-tons), les planches coloriées à la main après tirage. On ne copie jamais une planche, une pose, une bordure ou un titre.
- **Ce que c'est** : une **estampe en creux** : le trait est de l'encre retenue dans un sillon que le burin a taillé dans le cuivre. Trois règles :
  1. **Le ton est fait de lignes, jamais d'aplats.** La lumière est du papier nu ; le demi-ton, une famille de lignes parallèles ; l'ombre, une seconde famille qui la croise ; le noir profond, une troisième qui dessine des losanges. Aucun gris rempli.
  2. **Chaque ligne enfle et s'effile.** Le burin entre fin, mord plus profond au milieu et ressort en pointe. Un trait de largeur uniforme se lit comme un stylo ou du vectoriel : jamais.
  3. **La couleur vient après, à la main** : aquarelle transparente posée à plat, zone par zone, sur l'épreuve noire terminée, qui déborde un peu, s'accumule au bord, l'encre toujours dessus. Le film peut rester longtemps en noir ; l'arrivée de la couleur est un événement.
- C'est un **style « de scène »** : il sert un usage précis (voir la section 5), pour tout sujet qui a quelques faits à montrer.
- **Marche pour** : fiche de musée, « une minute sur… », figure de manuel, objet d'artisan, carte ou plan de site, anatomie d'un produit, espèce, outil, instrument.
- **Ne marche pas pour** : récit à personnages, humour, sujet rapide, interface.
- **À ne pas confondre** : pas la `gravure-sur-bois` (bloc noir, gouges blanches) ; pas un croquis à la plume (traits lâches et brisés) ; pas un plan technique ; pas un filtre sépia.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Papier vergé | `#f1e8d2` |
| Encre (presque noir chaud) | `#1c1510` |
| Lavis (exemple « insecte ») | ambre `#c98a3a`, gris-bleu `#8fa3b0` |
| Lavis (exemple « carte ») | vert de mer `#9cc0b0` sur terre chamois `#e3d2a6` |
| Lavis (exemple « anatomie ») | un seul rose garance `#c0586a` |
| Cuivre (quand on le montre) | `#b87348`, reflets `#f0c9a0` |

- L'estampe a **deux valeurs** ; tout le ton est de la densité de lignes.
- La couleur est **uniquement du lavis transparent**, en pigments de terre et de minéraux assourdis, **un seul pigment plus fort au maximum**. Jamais opaque, jamais sur les lettres, les filets ou le papier hors de la figure. Réserve-la : tout le sujet à un moment, ou seulement la partie qui compte, ou rien.
- **Typographie** (OFL) : **capitales romaines** (**Bodoni Moda** ; titre ≈ 56 à 72 px en vertical, interlettrage large ; étiquettes 28 à 32 px, jamais moins), **italiques** pour les noms savants, **écriture à la plume** (**Pinyon Script**) pour les notes : taille fixe, équilibrée sur deux lignes, jamais réduite. Les lettres romaines sont **taillées glyphe par glyphe** ; l'écriture est **tracée** d'un seul geste de gauche à droite.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Bodoni Moda et de Pinyon Script. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/bodoni-moda`, `@fontsource/pinyon-script` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Feuille* : papier vergé à texture ancrée (fibres, lignes de vergeure, rares rousseurs), **cuvette** de la plaque en léger relief, bordure filetée (un filet + un cheveu).
  - *Rapports de largeur* : contours les plus lourds (qui enflent de 0,45 à 1,35 ×), première hachure d'un cheveu à ≈ 2 px, la croisée ≈ 0,8 ×, la troisième ≈ 0,6 ×, poils et pointillé les plus fins. **Espacement relatif à la figure** (≈ 1/180 de sa hauteur) : une petite figure ne devient jamais grise.
  - *Une seule direction de lumière* pour tout le film (haut gauche) ; contours plus lourds du côté opposé ; le ton vient de la forme (sphères, cylindres), jamais d'une texture. Les lignes s'arrêtent aux formes placées devant.
  - *Médaillons* : cercle à double filet, fond réglé à la machine avec un halo blanc autour du sujet ; **traits de rappel** fins, d'un point sur la pièce jusqu'au bord, avec un petit numéro en italique.
  - *Coloriage* : multiplié sur le papier et **sous** l'encre : quelques pixels de débord, léger décalage, liseré au bord humide, granulation ; chaque zone **fleurit depuis le point où le pinceau a touché**.
  - *Cuivre* : métal poli chaud, fines rayures de polissage, reflet de fenêtre ; sillons = creux sombre + barbe claire vers la lumière. Le **burin** tenu bas, tourné de 15° au plus par rapport à la ligne ; le **copeau** est un ruban qui s'enroule devant la pointe.

## 3. Composition 9:16

- **La feuille est le monde** ; la planche verticale est le format historique. Feuille de 1080 × 1920 unités : cuvette et bordure à l'intérieur de x 60 à 1020, y 180 à 1540 ; titres, étiquettes et notes s'arrêtent à x 945 (la bande de droite ne porte que de la gravure).
- Mise en page type : **titre** en capitales (y 220 à 330), nom en italique dessous, **figure** centrée (y 400 à 1100, x 140 à 880), **médaillons** de détail dans la marge basse et sur les côtés (2 à 3, diamètre 220 à 300 px, à gauche de x = 945), mentions et échelle au pied de la planche.
- Sujet dans la cuvette ; étiquettes et médaillons dans les marges ; ordonne les détails pour qu'une avancée ne rogne jamais une note.
- **Sous-titres** : écriture à la plume sur une **languette de papier à bord frangé**, en bas au centre (y ≈ 1400 à 1520), 2 lignes au plus, jamais sur une étiquette. Tenue ≥ max(1,8 s ; réplique + 0,6 s). Une note gravée reste dans le cadre (caractères ÷ 12 + 1) s à partir du début de son écriture.
- Une figure « grandeur nature » minuscule à côté de la gravure agrandie donne l'échelle.

## 4. Ce qui bouge

- **Action principale** : **l'ordre de taille est l'animation** : contour → première hachure qui balaie chaque forme → croisée → noirs, poils, pointillé. Vitesse de burin constante, plusieurs traits à la fois (quelques-uns pour les contours, des dizaines pour les hachures). Une construction complète tient en quelques secondes.
- **Boucle de fond 1** : le copeau qui s'enroule et le reflet qui glisse sur le cuivre (quand on voit la plaque) ; sinon, un très léger souffle de caméra (avancée ≤ 2 %).
- **Boucle de fond 2** : le lavis qui fleurit et sèche (front irrégulier, liseré humide), zones décalées.
- **Gestes natifs** : la taille (burin en plein trait, copeau qui monte) ; **les trois passes** (le volume vient passe après passe) ; **le médaillon d'agrandissement** (cercle tracé à la pointe, zone polie puis retaillée en grand, envolée vers une marge sur un arc, trait de rappel, étiquette taillée à l'arrivée) ; **l'épreuve** (la feuille se décolle : le cuivre en miroir devient le papier à l'endroit) ; les états de la plaque (une zone polie et retaillée) ; le coloriage à la main ; la grandeur nature ; la planche terminée.
- **Autorisés** : `#004` tracé (taille), `#174` loupe qui suit la pointe du burin, `#028` recul en zoom régulier, `#027` avancée vers une pièce, `#126` trajet en arc (médaillon), `#025`/`#026` lecture le long de la feuille, `#175` planche fixe, `#143` vue éclatée par médaillons, `#046` coupe du cuivre en miroir à l'épreuve à l'endroit.
- **Interdits** : `#044` fondu, `#045` volet, glissements d'interface, traits de largeur uniforme, gris remplis, couleur opaque, plusieurs directions de lumière.

## 5. Rythme et montage

- Grammaire d'usage : **l'ordre et la durée d'arrivée des informations**. Construis ta propre timeline à partir des faits du client.

| Usage | Ordre des informations | Tenue par couche | Durée |
|---|---|---|---|
| Fiche de musée | titre + nom → détail + terme + note (× N) → où le voir | titre ≥ 2,2 s ; note ≥ caractères ÷ 12 + 1 s ; final ≥ 4 s | 30 à 40 s |
| « Une minute sur… » | question → nom → 2 ou 3 faits → un chiffre → invitation à suivre | chiffre ≥ 2,5 s, seul | 35 à 60 s |
| Figure de manuel | figure → pièces étiquetées une à une → légende | étiquette ≥ caractères ÷ 12 + 1 s | 20 à 45 s |
| Savoir-faire | objet → 2 ou 3 détails de fabrication → atelier | idem | 30 à 45 s |
| Carte ou plan de site | lieu → encarts → légende → infos de visite | encart ≥ 3 s ; légende ≥ 4 s | 30 à 45 s |

- Transitions **d'atelier seulement** : épreuve tirée, papier de soie posé dessus, zone polie et retaillée, nouvelle feuille sur la presse.
- Instruments pincés et secs pendant qu'on taille ; archet ou son tenu seulement quand quelque chose de doux arrive (le lavis).
- **Version courte (8 à 12 s)** : titre et nom (2,2 s), un seul détail avec son terme et sa note (4 s), final tenu 3 s (et non 4) ; couper les autres détails et le chiffre isolé.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `burin.js` (réserve de traits ordonnés + planification, hachure, gravure d'un champ de ton, hachure le long des contours, contour, pointillé, poils), `planche.js` (feuille, texte gravé, écriture, cadre de médaillon), `lavis.js`, `cuivre.js` (plaque, burin, copeau), `figure.js` (n'importe quelle forme SVG → figure gravée : position, lumière, espacement).
- **Techniques clés** :
  ```js
  // loi de gonflement d'une hachure, u de 0 à 1 le long du trait
  const w = wMax * (0.2 + 0.8 * Math.pow(Math.sin(Math.PI * u), 0.7));   // effilée sur les 22 % de chaque bout
  // les familles s'allument par seuils de ton (0 = lumière, 1 = ombre)
  const familles = [ton > 0.14, ton > 0.5, ton > 0.75];
  const pas = hauteurFigure / 180;                                        // espacement relatif à la figure
  ```
  - Contours taillés en plusieurs passes, amincis là où une passe prend le relais de l'autre.
  - Dessine les médaillons **en grand**, puis réduis-les : dessinés petits, ils se figent sous le pixel.
- **Pièges** :
  - Largeur uniforme = stylo : fais enfler les hachures, pince les contours.
  - Formes qui se recouvrent sans occultation : passe les formes de devant comme zones à exclure.
  - Pièces seulement détourées à côté d'un corps hachuré : hachure le long de l'axe de chaque pièce, un noir à chaque jointure.
  - Burin posé dans l'axe du trait : il cache le sillon ; trop de biais : il a l'air de piquer.
  - Copeau en hélice régulière = un ressort : varie l'enroulement.
  - Traits de rappel collés au sujet : ils semblent le traverser ; laisse de l'air.
  - Un long premier trait qui ne se dessine jamais : la sortie anticipée de l'encre doit regarder en avant de la durée du plus long trait.
  - Noms savants : un contrôle automatique de la voix ne les reconnaît pas ; donne-lui une orthographe simple.

## 7. Son

- **Bruitages par matière** (≈ 5 par 10 s ; les hachures sont une texture de micro-grattements, plus dense à chaque passe) : papier (crépitement du décollage, languette qu'on tapote, papier de soie), presse (roulement, choc), **cuivre et acier** (sifflement aigu du burin, tintement du copeau, un tic au lever, pointe qui trace un cercle, frottement du brunissoir), encre et eau (plume, goutte, pinceau humide).
- **Pièce** : un atelier calme (horloge lointaine).
- **Instruments** (au choix) : clavecin, quatuor à cordes, violoncelle ou viole seule, luth, petit orgue ; un petit tintement pour un cercle tracé, un pincé grave à l'atterrissage d'un médaillon.
- **Silence** réel : coupe aussi le ton de pièce, garde au plus un petit son.
- **Voix** : un conservateur ou un naturaliste, posé. Mélodie une octave au-dessus de la voix, musique à mi-niveau sous la parole. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Aucun aplat gris : tout le ton est fait de lignes.
- [ ] Chaque ligne enfle au milieu et s'effile aux deux bouts.
- [ ] Trois familles de hachures au plus, allumées par le ton ; une seule direction de lumière.
- [ ] Le sujet tient dans la cuvette ; étiquettes et médaillons dans les marges, traits de rappel dégagés.
- [ ] La couleur est un lavis transparent sous l'encre, posé après le noir, sur ce qui compte.
- [ ] Lettres taillées, écriture tracée ; rien n'apparaît en fondu.
- [ ] Chaque note reste lisible (caractères ÷ 12 + 1 s) et n'est jamais rognée par une avancée.
- [ ] Rien d'important sous y = 1560 ni à droite de x = 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine (40 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/engraving.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/engraving.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/engraving.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre le sujet ni la planche.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/engraving/STYLE.md`, `DEMO.md`, `demo/engine/burin.js`, `plate.js`, `wash.js`, `copper.js`, `index.js`, `FACTS.md` (modèle de faits sourcés). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, planche verticale, valeurs hex des lavis proposées par Flot Web, numéros du dictionnaire de mouvements, budget de bruitages. Remplacer le contenu de la démo par celui du client n'est qu'un test technique, jamais une façon de livrer.
