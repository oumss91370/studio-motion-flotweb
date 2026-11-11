# Histoire 2D interactive (la communauté vote la suite)

## 1. Identité
- **Nom** : Histoire 2D interactive. Identifiant : `histoire-2d-interactive`.
- **Inspiration** : les séries d'histoires à suspense des réseaux, en motion design 2D, où chaque épisode se termine sur un choix laissé au public.
- **Principe** : une histoire en plusieurs épisodes, racontée par une voix off, dessinée en **2D à plat avec des contours d'encre**, où le spectateur est mis à la place du héros. **Chaque épisode finit sur un vote entre deux options**, et l'épisode suivant s'ouvre sur la conséquence du choix gagnant.
- **Pour quels sujets** : survie, mystère, enquête, science-fiction, aventure ; mais aussi une histoire d'entreprise ou une fiction pédagogique « dont tu es le héros ».
- **Ne marche pas pour** : une vidéo isolée sans suite, un client qui ne peut pas publier régulièrement (le vote demande une suite), un sujet sans enjeu.
- **Ce que la fiche « ma chaîne » fournit** : le genre et le ton, la **formule d'ouverture** de la chaîne, les **personnages récurrents** (un narrateur, un personnage qui revient d'une histoire à l'autre), les voix, la palette, la durée, ce que la chaîne ne fait jamais.
- **Avant toute image** : la bible de la série et les scripts de tous les épisodes (`references/serie-a-votes.md`).

## 2. Palette, typographie, matières
- **Palette cohérente par histoire**, tirée de la fiche « ma chaîne ». Exemple par défaut, nuit : ciel `#0F1B2D` → `#1F3554`, silhouettes `#0A0F18`, lumière chaude `#FFB454`, froid `#7FD1E8`, danger `#E5484D`, texte `#F5F1E6`.
- **Contours d'encre** (trait d'environ 4 px, sombre) sur tous les éléments.
- **Décors détaillés, jamais vides** : nuages en couches qui défilent, étoiles qui scintillent, lune avec halo, lumières à l'horizon ; intérieurs avec plafond, luminaires et faisceaux, mobilier en perspective, **objets du quotidien** (tasse, papiers, écrans avec du texte), voyants qui clignotent.
- **Sous-titres** : manuscrits (police de type Patrick Hand, libre), blancs, sur 1 ou 2 lignes, pour le style dessiné ; pour un style plus plat, sans gras avec **mots-clés colorés à sens fixe** (rouge = danger, jaune = personnages et objets, bleu clair = froid, ambre = feu).
- **Affichage en haut** : heure, compteurs (ce qui reste, combien de personnes).
- **Grain léger et vignette ajoutés au montage**, pas dans le dessin.
- **Personnages** : du skill `personnages` ; **apparence conforme à ce qu'ils sont** (âge, métier) ; le héros peut parler par bulles de texte plutôt que par une voix.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Patrick Hand. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/patrick-hand` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).

## 3. Composition 9:16
- **Sous-titres** : en bas par défaut, **y 1400 à 1430** ; **remontés quand le sujet du plan est dessous** (par exemple dans le ciel, vers y 860). La position est décidée **par sous-titre**, selon son instant de début, jamais par plan : un sous-titre ne saute pas de place en cours d'affichage. **Jamais sur le sujet du plan.**
- **Affichage** : en haut à gauche, x 60 à 420, y 200 à 340.
- **Le vote** : deux cartes empilées entre y 620 et y 1250, numérotées 1 et 2, chaque option en une vraie phrase de 44 à 56 px ; tenu au moins 3 s.
- **Le décor va jusqu'aux bords** ; rien d'important au-dessus de y 160, sous y 1560, à droite de x 945.
- **Géographie lisible** : si la scène est confuse, faire un plan large ou une vue du dessus.
- **Couverture** : surtitre espacé, titre sur deux lignes (blanc puis couleur) avec ombre, pastille de question, la scène forte au centre ; **rien derrière le titre** ; l'important dans le centre 3:4.

## 4. Ce qui bouge
- **Action principale** : **un évènement dans chaque plan**, entre sa première et sa dernière image, puis **la réaction** du personnage. Jamais un personnage immobile avec juste un zoom.
- **Boucles de fond** : (1) la vie du décor : neige, flammes, nuages, voyants, souffle ; (2) la caméra qui dérive. Rien n'est jamais figé.
- **Règles de jeu** :
  1. **Cause puis réaction, en séquence**, jamais superposées ; la réaction a son temps.
  2. **Les visages jouent** : ils ne sautent jamais d'une expression à l'autre. Un changement d'émotion se joue : anticipation plissée → la nouvelle expression arrive à sa pleine taille → petit rebond ; **les yeux mènent, les mains arrivent en dernier**.
  3. Anticipation avant chaque grand mouvement, écrasement et étirement, accélération et décélération, arcs, suivi d'élan, pas de gestes jumeaux, poses poussées.
  4. **Un personnage se retourne par vues clés dessinées** (face, trois quarts, profil, dos) en 0,2 à 0,35 s, jamais par une fausse 3D.
  5. **Une transition à chaque raccord** : fondu au noir, flash, coupe dans l'action, raccord de forme, mouvement de caméra qui continue ; et **le son fait la transition au moins deux fois** (il arrive avant ou reste après l'image).
  6. **Au moins quatre mouvements de caméra différents par épisode, et un plan signature.**
- **Autorisés** : #121 anticipation, #122 suivi d'élan, #011 écrasement et étirement, #016 parallaxe des couches, #027 poussée, #025 panoramique, #042 raccord de forme, #047 et #048 son en avance ou en retard, #187 fondu au noir, #183 plan d'ensemble, #184 très gros plan, #099 silhouette, #024 secousse.
- **Interdits** : personnage figé, expression qui saute, deux actions superposées, rotation en fausse 3D, objet qui flotte, plan repris d'une ouverture précédente.

## 5. Rythme et montage
- **Durée** : celle de la fiche « ma chaîne » (souvent 1 min 45 à 1 min 55) ; environ 2,3 mots par seconde ; 8 à 10 s de silences et de plans muets.
- **Structure d'un épisode** : ouverture à la deuxième personne, situation claire en 3 s, **avec des plans neufs** → une information nouvelle → un retournement → le plan signature → **deux vrais silences avant le moment fort** → la fin en suspens → **le vote**.
- **Pas de bruitage fort dans les premières secondes.**
- **Alterner rapide et tenu** ; une vraie respiration.
- **Storyboard en planches d'images, très garni** : une vingtaine de plans pour deux minutes, planches de 10. Pour chaque plan : ce qu'on voit, **l'évènement**, la réaction, la caméra, la voix, et **les lectures** (ce que le spectateur doit comprendre, dans l'ordre, une à la fois). Rendu avec **le vrai code de dessin**, pas une maquette. Le client valide les planches.
- **Sous-titre** : au moins 1,8 s, et la durée de la réplique + 0,6 s.
- **Élément choc** : jamais montré en entier au premier épisode (indices, puis partiel, puis complet).
- **Version courte (8 à 12 s)** : c'est une bande-annonce, pas un épisode : la situation posée en 3 s, un évènement et sa réaction, puis **une** carte de vote tenue 3 s ; couper l'information nouvelle, le retournement, les plans muets et la seconde carte. Accroche avant 3 s : l'évènement du premier plan.

## 6. Recette technique
- **Moteur** : HyperFrames ; scène en **SVG 1080×1920 où chaque image est une fonction pure du temps**, redessinée depuis `hf-seek`. Personnages montés et joués avec le skill `personnages` (vues, mains, objets tenus, émotions jouées).
```js
function rendre(t) {
  const p = planA(t), u = (t - p.debut) / p.duree;
  scene.innerHTML = p.decor(u, t)                                   // décor complet, toujours vivant
    + heros({x: 540, y: 1180, vue: tourner(t, p.t0, p.t1, "face", "profil"),
             emotion: emotions(t, [[p.debut, "calme"], [p.evenement + 0.25, "effraye"]]),   // la réaction APRÈS la cause
             tient: "radio"});
  sousTitre.setAttribute("y", positionSousTitre(repliqueA(t)));     // décidée par sous-titre, pas par plan
}
window.addEventListener("hf-seek", e => rendre(e.detail.time));
```
- **Interdit de dessiner de tête** : chaque décor, objet, lumière et cadrage vient d'une image de référence regardée en grand, ou d'un épisode précédent de la série. Si une vidéo de référence existe : inventaire écrit de chaque plan (décor, objets, lumières, textes à l'écran, pose, cadrage, style, sons), voir `references/mesurer-une-reference.md`.
- **Toute nouvelle émotion, vue ou accessoire** se vérifie d'abord sur une planche du personnage, **pour chaque vue**, avant d'être utilisée.
- **Quatre contrôles, dans l'ordre, sans en sauter** : (a) analyse de la référence ; (b) comparaison référence / nous, plan par plan ; (c) planche finale ; (d) vidéo rendue. On ne passe pas au suivant tant qu'un défaut reste.
- **Contrôle « ouverture neuve »** (dès le deuxième épisode) : planche côte à côte des 15 premières secondes de l'épisode précédent et de celles du nouveau ; aucun plan ne partage le même décor et le même cadrage.
- **Voix** : une génération par réplique ; nombres écrits en lettres ; ne jamais relancer « pour réessayer ». Effets de voix selon le personnage (masque, radio, voix abîmée) par filtres ; exemple radio : `highpass=f=300,lowpass=f=3200,equalizer=f=1500:t=q:w=1:g=5,acompressor=threshold=-20dB:ratio=4`.
- **Rendu** : par moitiés reprenables ; grain et vignette **après** les contrôles de mouvement.

## 7. Son
- **Trois couches** : ambiance, bruitages des actions importantes (de la bonne matière), nappes de tension aux moments forts. **Vrais enregistrements d'abord** (skill `son`) ; budget d'environ 5 bruitages par 10 s.
- **Le fond nettement plus bas que la voix** : environ 25 à 30 dB dessous entre les répliques (le mesurer et l'afficher à chaque mix), baisse douce sous la voix.
- **Garder la dynamique** : un seul gain global vers la cible + un limiteur de crête ; **jamais de normalisation qui écrase** ; écart de volume d'au moins 7 à 8 unités.
- **Deux vrais silences** (fonds coupés) avant le moment fort ; le premier son après le silence est l'un des plus importants.
- **Pas de musique, sauf demande** (ou si la fiche « ma chaîne » en prévoit une). −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
**Cohérence physique, sur chaque plan (planche ET vidéo)** :
- [ ] **Orientation et trajectoires** justes : un véhicule suit sa route, rien ne bouge de travers.
- [ ] **Accessoires bien portés dans toutes les vues** (face, trois quarts, profil, dos) ; les objets tenus restent dans la bonne main.
- [ ] **Rien ne flotte** ; échelles cohérentes selon la distance.
- [ ] **Géographie constante** d'un plan à l'autre ; **continuité** de l'heure, des compteurs, de l'éclairage, de la météo.
- [ ] Sous-titres jamais sur le sujet, jamais dans une zone d'interface.

**Récit et série** :
- [ ] Un évènement et une réaction dans chaque plan ; rien de figé.
- [ ] Ouverture neuve par rapport à l'épisode précédent (comparaison aux mêmes instants : 0,5 / 2,5 / 5 / 7 / 10 / 12 s).
- [ ] Le vote : deux vraies phrases, chacune avec un risque, lisibles 3 s ; la suite existe pour les deux ; les votes sont comptés et montrés au client avant d'écrire la suite.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu
- Format maison Flot Web : pas d'aperçu de tiers. Aperçu à produire avec le plugin.

## 10. Origine
- Source : format de production « histoire interactive en 2D » et skill d'écriture d'histoire du plugin Flot Web, **rendus génériques** : toute référence à la série, à ses histoires, à ses personnages, à sa formule d'ouverture propre, à ses comptes, à ses voix, à ses dossiers et à ses outils de publication a été retirée ; le format lit la fiche « ma chaîne » du client.
- Principes de jeu d'acteur : voir le skill `personnages` (ClaudeAnimationBase, MIT) ; direction : lemo-opuscar DIRECTOR.md (LemoLab, MIT) ; méthode d'écriture : Superpowers (Jesse Vincent, MIT).
- Adaptations : moteur HyperFrames (`hf-seek`), palette par défaut neutre, −14 LUFS.
