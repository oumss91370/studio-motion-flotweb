# Reel face caméra (montage de ses propres rushes)

## 1. Identité
- **Nom** : Reel face caméra. Identifiant : `reel-face-cam`.
- **Inspiration** : le reel « expert qui parle » très monté : accroche en trois secondes, alternance du visage et d'images d'illustration, sous-titres mot à mot, musique discrète. Les chiffres ci-dessous ont été mesurés par l'auteur de la source sur ses 27 reels les plus vus : ce sont un point de départ, pas une loi ; la demande du client passe avant.
- **Principe** : le client se filme en train de parler, donne le fichier, et l'agent coupe, sous-titre, trouve ou fabrique les images d'illustration, construit les animations, mixe et se contrôle. Le montage doit raconter l'histoire de celui qui parle par l'image, le rythme et le son.
- **La première porte** : « dans les 3 premières secondes, quelqu'un est-il convaincu qu'il doit regarder jusqu'au bout ? » Une raison précise de rester, et sa récompense **dans** la vidéo. Les effets, le volume d'images et la finition viennent après ce test.
- **Pour quels sujets** : conseil, méthode, actu d'une niche, démonstration d'outil, publicité courte, short tiré d'une vidéo longue.
- **Ne marche pas pour** : un rush sans accroche ni appel à l'action (un enregistrement brut plafonne le montage : écrire l'accroche avant de filmer), une vidéo sans parole. La viralité est une ambition, jamais une promesse.
- **Variante légère (« reel brut »)** : ni images d'illustration ni musique ; on coupe reprises, bégaiements et air mort ; un mot à l'écran à la fois, petit, en bas au milieu, calé sur le mot exact.

## 2. Palette, typographie, matières
- **Couleurs et polices** : celles de la fiche « ma chaîne » (skill `marque`). À défaut : sous-titres en **Montserrat ExtraBold, capitales, 62 à 64 px**, avec un accent en serif gras (Abril Fatface) sur 5 à 20 % des groupes, pour les mots doux ; **jamais deux groupes en serif de suite**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place d'Abril Fatface ; Montserrat : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/abril-fatface` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Couleur dans les sous-titres** : sur 25 à 45 % des groupes, le groupe entier seulement : rouge pour la mauvaise façon ou une perte, sarcelle pour le concept ou le mot-clé, vert pour l'action ou la récompense (à remplacer par les trois tons de la chaîne en gardant les trois rôles).
- **Un seul look pour tout le reel** : chaque sous-titre dans **la même boîte sombre avec un fin liseré clair**, pour se lire sur du noir, du blanc et des images. Mélanger sous-titres en boîte et sous-titres nus fait bon marché. Une boîte sombre sans liseré disparaît sur fond sombre.
- **Matières** : le visage du client (recadré depuis la source native), de vraies images qui bougent, des enregistrements d'écran, des interfaces animées. Chaque plan bouge.
- **Logos** : jamais inventés, approchés ou redessinés de mémoire. Uniquement le fichier fourni par le client ou celui du site officiel de la marque (garder l'adresse et le fichier d'origine). Sans fichier vérifié : le nom de la marque en texte.

## 3. Composition 9:16
- **Zone sûre du texte** : x 90 à 930, y 200 à 1560 (la source allait jusqu'à y 1600 ; la table du plugin, `rendu/references/zones-interface.md`, interdit le bas à partir de y 1560 et le haut jusqu'à y 160). Étiquettes jamais au-dessus de y 160.
- **Trois mises en page, chaque changement est une coupe franche** :
  - **Partagé** : image d'illustration en haut (y 0 à 880), le client en bas. 30 à 42 % du reel.
  - **Illustration plein cadre** : 50 à 55 %.
  - **Gros plan serré** sur le client pour les pivots, l'insistance et l'appel à l'action : 5 à 15 %.
- Le client est à l'écran environ 45 % du temps et jamais absent plus de ~3,5 s.
- **La première image** est un écran partagé avec l'outil ou la marque du sujet en haut : elle est la vignette et doit avoir un sens tout de suite.
- **Position des sous-titres** : sur la jointure en écran partagé ; sur le haut du torse en gros plan (pas la mâchoire) ; dans une zone dégagée quand le plan est un texte à lire. **Jamais sur la bouche ou le menton**, surtout dans la première seconde, quand le spectateur décide si la personne à l'écran est réelle. Un sous-titre qui traverse une coupe passe à l'emplacement du nouveau plan sur l'image de la coupe.
- **16:9 sur demande** : une seconde composition avec son propre cadrage et ses propres placements ; un recadrage central n'est pas une seconde composition.

## 4. Ce qui bouge
- **Action principale** : l'image d'illustration qui change sur le nom qu'elle illustre (**un visuel par groupe nominal**, calé sur le mot prononcé, à 2 images près, avec au plus 0,15 s d'avance voulue).
- **Boucles de fond** : (1) poussée lente dans chaque plan (aucune image figée) ; (2) le visage et les gestes du client.
- **Ordre de préférence des images d'illustration** : 1) vraies images de la chose nommée ; 2) vrai enregistrement d'écran du site ou de l'appli, zoomé sur la partie dont on parle, curseur visible ; 3) interface animée refaite (frappe, lignes qui se cochent, compteur qui monte), **étiquetée « exemple »** ; 4) vidéo générée (les métaphores concrètes marchent ; « personne devant un ordinateur » fait banque d'images) ; 5) courts recadrages surlignés d'une vraie page (moins d'1 s). **La vidéo bat l'image fixe, toujours** ; une image fixe avec un zoom n'est pas une image d'illustration.
- Chaque graphique tenu fait une **action avec un résultat** (une clé s'enclenche et un projet démarre, des critères deviennent des coches). Pas de carton qui se pose et se fige.
- **Autorisés** : #041 coupe sautée, #046 coupe sèche, #028 poussée lente, #080 surlignage sur le mot dit, #185 insert, #189 plan de coupe, #144 écran partagé, #007 compteur, #006 frappe dans une interface (jamais pour un titre).
- **Interdits** : animation « pop » sur les sous-titres (ils se remplacent sec) ; même flottement appliqué à tous les objets ; fond vidéo dupliqué et flouté pour remplir le vertical ; tampon « STOP », flash ou effet de 0,3 s systématiques en ouverture ; transition choisie par rotation d'un plan à l'autre ; interface minuscule flottant dans du vide (zoomer jusqu'à remplir le panneau).

## 5. Rythme et montage
- La parole démarre dans les 0,1 s ; le fichier finit juste après le dernier mot. Ni carton d'intro ni carton de fin.
- Plans de 1,1 à 1,4 s en moyenne, aucun au-delà de ~2,8 s. La première coupe tombe à 0,6 à 1,0 s, sur le premier mot chargé. Chaque élément d'une liste a son plan. Le repère « un événement toutes les 1 à 2 s » est un diagnostic, pas un métronome : une action qui se développe mérite une tenue plus longue.
- **Histoire** : 1) accroche (une affirmation ou un ordre qui nomme l'outil ou la personne) ; 2) une ligne de crédibilité ; 3) s'il y a une liste, montrer tous les éléments tôt, floutés, en **boucle ouverte** ; 4) chaque élément : carton de section, définition en une ligne, deux ou trois visuels littéraux, gros plan sur la phrase clé ; 5) résolution qui rappelle le visuel de l'accroche ; 6) appel à l'action : montrer la ressource d'abord, puis gros plan avec le mot-clé à commenter.
- **Boucles ouvertes** : les noter (question honnête du spectateur, objet planté, instant de pose, rappels, instant de fermeture, phrase dite qui la ferme). Une boucle principale et au plus une secondaire en même temps. Fermer la leçon promise **avant** l'appel à l'action.
- **Trois ouvertures différentes**, construites avec les mêmes vraies paroles, comparées sur les 3 premières secondes (clarté du sujet, curiosité, compréhension sans le son, tenue de la promesse) ; noter la raison du choix, qui n'est pas « l'effet le plus fort ».
- **Maquette animée basse définition** avec la voix et un son brut **avant** de soigner les matières.
- **Sous-titres** : groupes de 1 à 3 mots, coupés aux frontières de sens ; remplacement sec ; ils apparaissent 2 images avant le premier mot.
- Ne pas redire trois fois la même chose (voix, sous-titre, titre) : le graphique montre l'exemple, la relation, la preuve ou la conséquence.

## 6. Recette technique
- **Moteur** : HyperFrames. Étape préalable : la fiche `derushage-silences-rates`.
- **Structure** : la vidéo du client en `<video class="clip" muted>` dans un conteneur qu'on anime (on anime l'enveloppe, pas la vidéo) + une piste `<audio>` séparée ; les mises en page sont des états du conteneur changés par `tl.set` (coupe franche) ; images d'illustration en clips ; sous-titres générés depuis la transcription recalée.
```js
// mises en page par coupe franche, calées sur les mots
tl.set("#client", {top: 880, height: 1040, scale: 1}, mot("automatiser").debut - 2 / 30);   // partagé
tl.set("#illu1", {opacity: 1}, mot("automatiser").debut - 2 / 30);
// sous-titres : un seul groupe visible, remplacement sec
groupes.forEach(g => { tl.set(g.el, {opacity: 1, visibility: "visible"}, g.debut - 2 / 30);
                       tl.set(g.el, {opacity: 0, visibility: "hidden"}, g.fin); });
```
- Animer les transformations (`x`, `y`, `scale`), jamais `top` ou `left` en continu. Lier chaque apparition à **son** mot, jamais à un décalage arbitraire `index * 0.4`.
- **Registre des images d'illustration** : un fichier qui note, pour chaque scène, sa provenance, son empreinte et l'intervalle utilisé. **Chaque scène une seule fois par reel** ; un autre recadrage, une autre vitesse ou un autre étalonnage n'en font pas une nouvelle scène.
- **Contraste** : mesurer les pixels derrière chaque sous-titre. Jamais de blanc sur clair.
- **Pièges** : une page web entière réduite à la taille du téléphone est illisible (recadrer sur la phrase) ; ne jamais cliquer « Accepter » sur une fenêtre de cookies pendant un enregistrement d'écran ; les vidéos générées changent souvent d'angle vers 2,5 à 3 s et leur texte devient du charabia (garder les premières secondes continues) ; ne jamais montrer d'identifiants réels ; ne jamais inventer un chiffre, un résultat ou un test réussi pour décorer une affirmation ; ne jamais fabriquer un appel à l'action que le client n'a pas dit.

## 7. Son
- **Musique choisie à l'humeur** : rythme plus sombre et assuré pour les affirmations et l'actu, ambiance douce pour les méthodes. Elle reste **environ 11 dB sous la voix** (plage de travail 9 à 14 dB) et baisse encore sous la parole. Les 1 à 2 premières secondes sont souvent plus calmes, le rythme tombant sur la deuxième phrase.
- **Les bruitages suivent des actions visibles**, pas chaque coupe (budget du skill `son`, environ 5 par 10 s) : souffle d'air doux sur un vrai déplacement, tape amortie quand un logo se pose, clic sec pour une petite interface, papier pour un document, un ton chaud et court pour une coche. Éviter lasers, « plops » descendants, gazouillis de science-fiction, souffle sur chaque coupe. Varier les fichiers pour les éléments répétés. Caler le **pic** du son sur l'impact visuel, pas le début du fichier.
- Si le client dit que la musique est trop forte : baisser son gain **par rapport à la voix** et vérifier l'écart après normalisation.
- Chaque phrase de voix au même niveau. **−14 LUFS, crête ≤ −1,5 dBTP, mesurés sur le MP4 final stéréo** (un fichier mono lit 3 dB plus bas). Ne jamais fondre le dernier mot.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Les 3 premières secondes : sujet clair sans le son, raison précise de rester, promesse tenue plus loin ; contrôle image par image des 2,5 premières secondes (rien sur la bouche).
- [ ] Trois ouvertures ont été comparées et le choix est motivé par écrit.
- [ ] Bandes de 10 images de chaque côté de chaque coupe : pas de panneau vide d'une image, pas de sous-titre qui clignote sur le mauvais plan.
- [ ] Contraste mesuré derrière chaque sous-titre ; une seule boîte pour tout le reel ; texte dans x 90 à 930, hors zones d'interface.
- [ ] Chaque plan bouge ; chaque scène d'illustration n'apparaît qu'une fois (registre à jour).
- [ ] Chaque logo vient d'un fichier vérifié ; les interfaces refaites sont étiquetées « exemple ».
- [ ] Le client n'est jamais absent plus de ~3,5 s ; la leçon est donnée avant l'appel à l'action.
- [ ] Rendu final retranscrit et comparé au brut à chaque raccord ; −14 LUFS et crête mesurés sur le fichier livré.
- Méthode à garder : **chaque remarque du client devient une règle** écrite dans la fiche « ma chaîne », pour ne jamais la redonner deux fois. Et la relecture du client reste la dernière porte.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 3
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Pas d'aperçu libre de droits : les vidéos vitrines du dépôt d'origine sont à droits réservés et portent la marque de leur auteur ; on ne les reprend pas. Aperçu Flot Web à produire.

## 10. Origine
- Dépôt : nateherkai/hyperframes-student-kit (« Herk Edit Kit »), commit `10511e5`. Fichiers : `.claude/skills/short-form-edit/SKILL.md` (+ `references/quality-gates.md`, `curiosity-and-entertainment.md`), `docs/EDITING-PLAYBOOK.md`, `docs/SHORT-FORM.md`.
- Licence : MIT (© 2026 Nate Herk) ; ajouts « pipeline » (dont ce flux court) sous la permission d'usage du kit, **à conserver** : « Herk Edit Kit Use Permission. Copyright 2026 the contributors to this teaching kit. » (texte complet dans `licenses/styles-montage-documentaire.md`).
- Adaptations Flot Web : français, niveau sonore unifié à −14 LUFS (la source hésite entre −16 et −14), zones d'interface du plugin, moteur HyperFrames à jour (les copies HyperFrames de la source sont ignorées), marque de l'auteur et noms de styles de tiers retirés, services payants de la source non imposés.
