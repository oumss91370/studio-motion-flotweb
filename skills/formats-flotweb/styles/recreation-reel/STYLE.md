# Recréation du motion design d'un reel

Format de méthode (le look vient de la vidéo de référence) : on **mesure** un reel existant, on écrit un **cahier de recréation chiffré**, on le reconstruit, puis on **prouve** la ressemblance image par image.

> **Avec le skill `reproduire-reel`.** Cette fiche tient le cahier plan par plan, la reconstruction et le contrôle du rythme du film fini. La **mesure de la référence** (découpage vérifié à l'image, lecture continue de toutes les images, zoom et mesure au pixel du trait, des couleurs, de l'ombrage, des sous-titres), la **fiche de style chiffrée**, le **contrôle chiffré** « référence / nous / écart » et la **critique indépendante des plans de test** sont dans `skills/reproduire-reel/` : commence par lui dès que le client veut le *rendu* d'un reel (personnages dessinés, 2.5D, 3D), pas seulement son rythme. Ses scripts ne sont pas recopiés ici.

## 1. Identité
- **Nom** : Recréation de reel. Identifiant : `recreation-reel`.
- **Inspiration** : le reel que le client envoie (« refais-moi ça », « même accroche », « mêmes animations »).
- **Principe** : **calquer la forme, pas l'œuvre.** On reprend exactement le rythme, l'accroche, la grammaire d'animation, les transitions, les mouvements de caméra, la mise en page et le niveau de finition. On **remplace** les textes, marques, logos, personnages, visages, voix et musique par ceux du client (ou un équivalent neutre).
- **Deux modes** : **recréation** (une référence existe : les six étapes ci-dessous) ; **création** (pas de référence : on saute l'analyse, on définit l'identité de mouvement de la vidéo avec le skill `principes-mouvement`, puis on écrit le même cahier chiffré et on suit les mêmes contrôles).
- **Pour quels sujets** : reprendre une structure qui marche pour sa propre niche, apprendre d'un reel très réussi, décliner un format vu ailleurs avec ses propres contenus.
- **Ne marche pas pour** : republier la vidéo d'un autre, reprendre son personnage ou son logo, copier son texte. Une référence filmée avec des personnes réelles ne se « recrée » pas en motion design : on en garde le rythme et la structure seulement.
- **Ce que la fiche « ma chaîne » fournit** : les textes de remplacement (ou le sujet, pour les écrire), le logo, les personnages, la voix, la musique autorisée, la palette quand elle doit remplacer celle de la référence.

## 2. Palette, typographie, matières
- **Tout vient de la mesure**, rien du souvenir :
  - **Couleurs** : 3 à 6 codes hex relevés à la pipette sur des images pleine résolution, chacun avec son rôle (fond, accent, texte, alerte).
  - **Typographie** : famille (grotesque grasse, serif condensée, manuscrite…), graisse, interlettrage, contour, ombre ; **taille et position mesurées sur l'encre** (boîte du texte, hauteur de capitale, nombre de lignes). On prend la police libre la plus proche, ou celle de la chaîne.
  - **Matières** : grain, flou, ombres de contact, reflets ; pour la 3D : matière (mate, métal, verre, plastique), éclairage (lumière principale chaude, contre-jour froid), profondeur de champ.
- **Décision du client** : garder la palette de la référence (pour apprendre le format) ou passer à celle de sa chaîne (pour publier). Par défaut pour une publication : sa palette, en gardant les **rapports** de contraste et de saturation mesurés.
- **Interdits de matière** : logo, mascotte ou personnage protégé d'un autre créateur, même redessiné.
- **Police de repli** : selon la famille relevée sur la référence : Inter ou Montserrat (grotesque), Oswald ou League Gothic (condensée), Playfair Display ou EB Garamond (serif), Nunito (ronde ou manuscrite), JetBrains Mono (chasse fixe). Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : chercher la police libre la plus proche sur `@fontsource/<nom>` (vérifier par `npm view @fontsource/<nom> version`) ; sinon « à vérifier ».

## 3. Composition 9:16
- **Le projet reprend la taille et la cadence de la référence**, ramenées à 1080×1920 (une référence en 720×1280 se met à l'échelle ×1,5 ; mesures multipliées d'autant).
- **Positions et tailles notées à l'état final** (la mise en page avant animation), en pixels du 1080×1920.
- **Zones d'interface** : rien d'important au-dessus de y 160, sous y 1560, à droite de x 945. Si la référence y place un élément clé, on le ramène dans la zone utile et on le note comme écart voulu.
- Le texte d'interface de l'application visible autour de la vidéo d'origine **n'est pas dans la vidéo** : on ne le reproduit pas.
- **Couverture** : sur l'image de l'accroche.

## 4. Ce qui bouge
- **Action principale** : chaque animation de la référence, refaite avec **sa propriété, ses valeurs de départ et d'arrivée, sa durée, sa courbe et son instant de départ mesurés** (début, durée, dépassement, courbe la plus proche).
- **Boucles de fond** : relever dans la référence **ce qui bouge en permanence** (particules, grain, dérive, respiration) et le refaire ; relever aussi **ce qui ne bouge jamais** (fond, cadre).
- **Animation sur toutes les images** : aucune image figée plus de 0,5 s, sauf une tenue voulue et notée dans le cahier (et alors : respiration, dérive de caméra, particules ou grain vivant).
- **Chaque plan est différent** : nouveau cadrage, nouveau décor ou nouvel élément à chaque coupe ; jamais deux plans identiques.
- **Transitions relevées par leur type exact et leur durée en images** : coupe sèche, flash blanc, filé avec flou, zoom traversant, masque, raccord de forme, fondu. **La transition est la sortie du plan** : pas d'animation de sortie avant elle.
- **Caméra** : zoom (de combien de %), panoramique (pixels par seconde), tremblement (amplitude, fréquence), coup de zoom sur le temps fort.
- **Autorisés** : tout mouvement **mesuré dans la référence**, noté avec son numéro du dictionnaire `principes-mouvement` dans le cahier.
- **Interdits** : toute valeur devinée ; « dynamique », « percutant », « fluide » sans chiffres ; courbe linéaire mécanique là où la référence a une anticipation ou un dépassement ; plan inventé.

## 5. Rythme et montage
- **Même nombre de plans que la référence, chaque coupe à ±0,1 s** (±3 images).
- **L'accroche (0 à 3 s) se relève image par image, sans exception** : ce qui bouge, apparaît, flashe, zoome ; premier mot, premier son, premier mouvement de caméra, à quelle image.
- Noter si les coupes tombent sur les temps de la musique ; relever la structure (accroche / promesse / développement / chute / appel à l'action), le plan le plus court et le plus long, les motifs qui reviennent.
- **Deux validations du client** : après le **cahier de recréation** (avant de construire), et après le **rendu contrôlé** (avant toute publication).

## 6. Recette technique
- **Moteur** : HyperFrames pour tout le motion design. La 3D légère en Three.js dans la composition (`hf-seek`) ; **Blender par le connecteur `blender`** pour les modèles et les passes exigeantes (verre, matières complexes), intégrées en séquence d'images avec transparence.

**Étape 1, récupérer la référence.** Le client fournit le fichier. Garder l'original intact.

**Étape 2, analyser (en continu + image par image).** `scripts/analyse_reference.sh ref.mp4 analyse/` puis lecture à l'œil (`references/mesurer-une-reference.md` §2) ; pour vérifier chaque coupe à l'image, lire toutes les images d'un plan et mesurer au pixel ce qui fait le style : skill `reproduire-reel`, étapes 2 à 6. Ici : coupes (deux détecteurs : coupes franches, et fondus), carte des évènements avec le son, rythme, look ; planches toutes les 0,5 s, bandes d'images natives autour de chaque évènement, trois images pleine résolution par plan. Écrire **une fiche par plan, sans exception** :
```
## P03 · 2,633–4,100 s (44 images) · entrée : filé de 6 images
Cadrage : plan serré centré, sujet à 62 % de la hauteur, fond en dégradé radial #1B1F3A → #07080F
Éléments : titre (grotesque 900, 148 px, #FFD23F, contour 6 px), objet 3D (Ø 520 px)
Animations : titre échelle 0,2 → 1, rotation −12° → 0, 0,43 s, retour avec dépassement, à 2,700 s ; puis respiration 1 → 1,04
Caméra : coup de zoom 100 → 108 % sur le temps fort à 3,40 s (6 images)
Sortie : flash blanc de 3 images à 4,033 s
Son : souffle à 2,62 s ; impact grave à 3,40 s ; voix 2,75–3,90 s
Toujours vivant : poussières qui montent (≈ 40 px/s), grain fin
```

**Étape 3, écrire le cahier de recréation.** Un document chiffré, plan par plan, qui permettrait à quelqu'un **qui ne voit pas la référence** de reconstruire la vidéo. **Chaque adjectif devient un nombre.** Il contient : format ; **ce qu'on garde / ce qu'on remplace** ; identité (couleurs, polices, courbes signature, interdits) ; **l'accroche image par image** (tableau image / temps / ce qui se passe / son) ; chaque plan (cadrage, éléments à l'état final en px, une ligne par animation, ce qui reste vivant, 3D, transition de sortie, son, **ce qui doit être vrai sur l'image du milieu**) ; le son global ; les **critères d'acceptation**. Instants en secondes à 3 décimales et en numéro d'image. Tenues voulues listées. Textes du client complets et déjà validés. → **Validation du client.**

**Étape 4, reconstruire.** Une sous-composition par plan, placée à l'instant mesuré (durée du plan + chevauchement de la transition).
```js
// d'abord la mise en page à l'état final (CSS statique), vérifiée par une capture au milieu du plan ; puis :
tl.fromTo("#titre", {scale: 0.2, rotation: -12}, {scale: 1, rotation: 0, duration: 0.43, ease: "back.out(2.2)"}, 2.700);
tl.to("#cam", {scale: 1.08, duration: 0.2, ease: "expo.out"}, 3.400);                        // coup de zoom sur le temps
tl.fromTo("#flash", {opacity: 0}, {opacity: 1, duration: 0.05, yoyo: true, repeat: 1}, 4.033);   // la transition EST la sortie
```
  - Particules et dérives à **graine fixe**, répétitions **finies**.
  - 3D en Three.js : fonction pure du temps, fond transparent (sinon un fond noir cache le décor), bibliothèque embarquée (pas de réseau au rendu). 3D Blender : **regarder la scène après chaque modification** (outil de vue du skill `blender`) : objet qui flotte, intersection, face manquante, échelle, ce que la caméra cache.
  - Son : skill `son` ; voix du client ; **jamais la musique de la référence** : une piste autorisée de même tempo et de même énergie.

**Étape 5, contrôler, corriger, recommencer.** Dans l'ordre, sans rien livrer tant qu'un point échoue :
  1. Contrôles du moteur (skill `rendu`) sans erreur ; captures de revue regardées.
  2. `python3 scripts/controle_rendu.py brouillon.mp4 --ref ref.mp4 --allow <tenues>` sur un rendu **sans grain** : aucune image figée, aucun couple de plans semblables, même nombre de plans, coupes à ±0,1 s, **énergie de mouvement entre ×0,5 et ×2** de la référence, plan par plan.
  3. Vidéo **côte à côte** référence | nous ; les pires instants regardés en grand. Les textes et personnages étant remplacés, on ne vise pas l'identité des pixels : on juge le contenu manquant, les instants de mouvement et les courbes.
  4. Courbes de l'accroche comparées : même début (±1 image), même durée (±10 %), même courbe. Look par plan (luminosité, contraste, saturation, chaleur) proche.
  5. Image par image : toutes les images de l'accroche ; 6 images avant et après chaque coupe ; planche à 0,5 s ; recadrages pleine résolution des textes, visages et objets 3D.
  6. Son : boucle d'écoute du skill `son`. 7. Lecture en continu avec le son.
  Écrire le **compte rendu de revue** : par plan, verdict, mesures clés, écarts restants et leur raison.

**Étape 6, livrer.** La vidéo, la planche référence | nous, le compte rendu en cinq lignes ; puis la porte de livraison du skill `studio-coeur`.

- **Pièges** : une planche à 1 image par seconde rate les flashs et les plans de 2 à 5 images ; confondre un zoom rapide avec une coupe ; croire un détecteur de coupes sans regarder les images (un film peut être un quasi plan-séquence relié par des fondus et des déplacements de caméra : skill `reproduire-reel`, étape 2) ; grain ajouté avant les contrôles (il cache les images figées) ; cadence variable de la référence ; fond noir derrière la 3D (transparence oubliée).

## 7. Son
- Relever dans la référence : la voix (mots horodatés), la musique (tempo, montée, temps fort), **chaque bruitage avec son instant et l'action qu'il accompagne**.
- Refaire **avec nos sons**, calés sur **nos** instants d'animation : vrais enregistrements d'abord, budget et écoute du skill `son`. La densité de bruitages de la référence est une indication, pas une obligation.
- Jamais la piste musicale ni la voix de la référence. −14 LUFS, dynamique conservée.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
**Réalisme et finition, pour chaque plan** :
- [ ] Rien ne flotte : objets posés, ombres de contact, échelles cohérentes ; lumière venant du même côté que les reflets et les ombres.
- [ ] Aucun texte qui déborde, coupé, illisible ou dans une zone d'interface (durée à l'écran ≥ 0,5 s + 0,3 s par mot).
- [ ] Aucune image noire, aucun clignotement involontaire, aucun crénelage.
- [ ] Chaque plan apporte un nouveau cadrage, décor ou élément ; tout bouge à chaque image, sauf tenue voulue.

**Fidélité** :
- [ ] Même nombre de plans, coupes à ±0,1 s, énergie entre ×0,5 et ×2 (script de contrôle au vert).
- [ ] Courbes de l'accroche identiques aux mesures.
- [ ] Aucune valeur du cahier n'est devinée.

**Droits** :
- [ ] Textes, logo, personnages, voix et musique sont ceux du client ; rien de protégé d'un autre créateur.
- [ ] Le client a validé le cahier avant la construction, et le rendu avant toute publication.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Format maison Flot Web : pas d'aperçu de tiers (et l'on ne montre jamais la référence d'un autre créateur en vitrine). Aperçu à produire : la planche « avant / après » d'une recréation faite sur un reel du client lui-même.

## 10. Origine
- Source : skill de recréation de reel du plugin Flot Web (protocole d'analyse, modèle de cahier, reconstruction, contrôles) et ses deux scripts (`scripts/analyse_reference.sh`, `scripts/controle_rendu.py`, écrits par Flot Web), **rendus génériques** : toute référence aux séries, comptes, voix, dossiers et outils de publication d'origine a été retirée ; le format lit la fiche « ma chaîne » du client.
- Outils : HyperFrames (heygen-com, Apache 2.0) par le skill `rendu` ; three.js (MIT) ; principes de mouvement du mode création : skill `principes-mouvement`.
- Adaptations : validations confiées au client, Blender par le connecteur `blender`, −14 LUFS.
