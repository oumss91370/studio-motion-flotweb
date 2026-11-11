# Actualités filmées des années 1920

## 1. Identité
- **Nom** : Actualités filmées 1920. Identifiant : `actualites-1920`.
- **Inspiration** : les actualités sonores de la fin des années 1920 (rituel du générique au projecteur et au globe, speaker enjoué, une histoire par lieu, pirouette finale), le journal qui tournoie vers l'objectif, les orchestres de danse « hot ». Grammaire seulement : jamais le nom, le logo, le globe, la police ou la fanfare d'un vrai journal filmé.
- **Principe** : c'est un style de montage. Le look vient de la façon dont de **vraies archives** sont rangées, coupées, légendées et portées par le son. Image au format 1,37:1 dans une fenêtre de projection ; objets d'information filmés (journaux, pages de magazine, télégrammes, cartes, disques) ; une voix qui parle par-dessus tout, par exclamations courtes ; un orchestre qui fait le montage et qui sait s'arrêter net pour la chute.
- **Pour quels sujets** : histoire d'une mode ou d'une époque, anniversaire d'une marque ou d'une ville, origine d'un objet du quotidien, anecdote historique drôle.
- **Ne marche pas pour** : catastrophes et deuils (le ton guilleret est faux), sujet sans archives libres de droits, actualité récente. Ce n'est pas un film muet dessiné, ni un documentaire « filtre vintage » (pas d'interviews, pas de lents travellings sur photo, pas de bandeaux modernes).

## 2. Palette, typographie, matières
- **Noir et blanc argent chaud**, sans aucun accent de couleur ni voile sépia. Texte crème `#f3eee4` / `#d6cfc0` sur presque noir `rgba(12,11,10,.8)`, cadre crème de 2 px. Lettrage du générique en dégradé argent `#fff → #d9d4ca | #9e978a → #efebe2` avec cassure « métal » au milieu et contour noir (0,12 em).
- **Polices libres (OFL)** : Limelight (générique, cartons, titre de fin, 104 à 118 px) ; Oswald 600 en capitales espacées (cartons « LIEU · DATE ») ; sans demi-gras pour les sous-titres.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Limelight ; Oswald : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/limelight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Deux couches** : la couche image (archives, imprimés, cartes) reçoit le look pellicule ; la couche texte (cartons, étiquettes, sous-titres) reste nette et stable. Les marques au crayon gras appartiennent à l'image et tremblent avec elle.
- **Étalonnage de base** de chaque source : niveaux de gris → étirement par percentiles (0,6 % → noir, 99,6 % → blanc) → légère courbe en S → sortie 14 à 238. **Un seul réglage par plan**, jamais par image (sinon l'image pompe).
- **Look projection** (couche image seulement) : teinte argent chaud, vignette, scintillement ±3,5 % par image (faible amplitude : ne jamais dépasser ±5 %, c'est une variation de tout le cadre), flottement de fenêtre ±1,6 px / ±2,2 px, 0 à 3 rayures verticales qui vivent 9 images, 0 à 4 poussières d'une image. Le grain s'ajoute à l'encodage, pas dans la page.

## 3. Composition 9:16
- **Fenêtre de projection** : 1,37:1 en pleine largeur utile, soit ≈ 1000×730, coins arrondis de 20 px, centrée vers y 760 ; noir pur autour. Rien n'est jamais dessiné hors de la fenêtre, sauf les sous-titres et le carton de lieu.
- **Carton de lieu** : au-dessus de la fenêtre, entre y 180 et y 330, boîte sombre à cadre crème, « LIEU · DATE » (34 px minimum, capitales espacées) sur une ligne ; il se déroule de gauche à droite en 0,22 s.
- **Sous-titres** : sous la fenêtre, entre y 1180 et y 1480, deux lignes maximum, 46 à 54 px, contour noir épais. Bande sombre continue derrière (elle ne clignote pas entre deux répliques espacées de moins d'1 s).
- **Imprimés** (journal, page) : ils peuvent déborder de la fenêtre en hauteur pour être lisibles ; recadrer sur le pli utile.
- Zones d'interface : rien d'important au-dessus de y 160, sous y 1560, ni à droite de x 945.
- **16:9** : fenêtre 1480×1080 centrée dans 1920×1080, carton de lieu en haut à gauche de la fenêtre, sous-titres en bas de la fenêtre.

## 4. Ce qui bouge
- **Action principale** : le journal qui tournoie et claque. Il grandit en `u^2,3`, sa rotation s'amortit en `(1−u)^1,25` sur 2,5 tours, trois copies fantômes à 18 ms d'écart servent de flou, puis une secousse verticale amortie (16 px) et un rebond de 3 % à l'impact, poussée, et coup de zoom sur le temps suivant.
- **Boucles de fond** : (1) scintillement, flottement de fenêtre, rayures et poussières ; (2) poussée lente sur chaque image fixe (une image fixe a toujours un mouvement qui a un but).
- **Autorisés** : #188 fermeture à l'iris, #045 volet (diagonal, bord clair de 6 px), #021 retournement sur l'axe vertical, #138 store vénitien (12 lames), #140 page qui tourne, #137 poussée d'un panneau, #040 arrêt sur image avec secousse, #144 écran partagé à 2 ou 4, #025 panoramique sur un imprimé large, #048 L-cut. **Chaque transition une seule fois**, comme ponctuation.
- **Interdits** : #044 fondu enchaîné entre deux histoires, #043 panoramique filé moderne, flou de zoom, faux mouvement de caméra de plus de ~6 % sur une archive filmée (elle a déjà sa caméra).

## 5. Rythme et montage
- **L'orchestre est l'horloge** : tempo de danse 190 à 220 BPM ; chaque coupe, chaque atterrissage et chaque étiquette tombe sur un temps, la plupart des coupes sur une barre de mesure. Si un disque d'époque joue, couper sur son propre temps (le mesurer).
- **Une histoire = un lieu + un type de matériel + une phrase de voix.** Les histoires raccourcissent vers la fin (2 à 3 mesures → 1 mesure → quelques temps), puis une chute tenue.
- Durées : plan d'archive 1 à 2,5 s ; imprimé ou document 2,5 à 4 s (il faut le lire) ; comparaison ≥ 2,5 s ; jamais d'image figée plus d'1 s sans rien qui bouge.
- La voix peut déborder de 0,3 à 0,5 s sur la coupe ; un nouvel état musical peut commencer un temps avant son image.
- **Version courte (8 à 12 s)** : le journal qui tournoie et claque (2 s), deux plans d'archive, un imprimé tenu 2,5 s ; pas de générique ni de carton de fin.

## 6. Recette technique
- **Moteur** : HyperFrames. Archives en séquences d'images **à la cadence d'origine de l'archive** (24 i/s le plus souvent : c'est une vraie raison de garder 24, on ne réinvente pas les images d'un film d'époque), affichées par `Math.floor((t − t0) * 24)` dans un écouteur `hf-seek` (rendu déterministe) ; le film, lui, reste à 30 i/s, et tout ce qui est dessiné (cartons, étiquettes, journal) bouge à chaque image, ou en `<video class="clip">` si le plan n'est pas retraité. Cartons et étiquettes en HTML ; look pellicule sur un `<canvas>` posé au-dessus de la couche image.
- **Aléatoire à graine** pour scintillement, rayures et poussières (aucun `Math.random()` nu).
```js
window.addEventListener("hf-seek", (e) => {
  const t = e.detail.time, f = Math.floor(t * 24);
  dessinerImage(t);            // archive, imprimé ou carte
  lookProjection(ctx, f);      // scintillement, flottement, rayures : fonctions de f
});
```
- **Archives** : agrandissement ≤ 2,5× ; chaîne ffmpeg `hqdn3d=4:3:6:5` → `lanczos` → `unsharp=5:5:0.55` → étalonnage de base. Couper à l'intérieur des claquettes d'archive et des flashs blancs ; retirer filigranes et logos d'archive.
- **Soulignement de document** : positions exactes des mots d'après les boîtes OCR du scan ; trait de mine tendre tracé mot par mot.
- **Générique dessiné en code** : rayons, deux projecteurs, globe filaire, titre ; inventer son propre nom et son emblème (celui de la fiche « ma chaîne »).
- **Pièges** : un iris en `destination-in` laisse des coins transparents qui virent au gris, peindre du noir derrière ; les pages de journaux portent des articles sans rapport, parfois choquants, recadrer sur le pli ; ne jamais générer de fausses « archives ».

## 7. Son
- **Speaker** : voix masculine claire et énergique, débit rapide, 6 à 12 mots par phrase, exclamations et questions. Traitement « piste optique 1930 » : passe-haut 260 Hz, passe-bas 3,7 kHz, +4 dB de présence vers 2 kHz, légère saturation, compression 4:1.
- **Orchestre** (original) : tuba sur 1 et 3, banjo sur les quatre temps, trombones sur la figure de charleston, caisse claire à contretemps, trompette bouchée ; fanfare de cuivres pour le générique ; arrêt net avec un seul accord pour la chute.
- **Disque d'époque** possible si l'enregistrement est dans le domaine public (vérifier aussi la composition) : craquement, pose et levée de l'aiguille.
- **Bruitages** (budget du skill `son`) : claquement d'arc, souffle du journal qui tourne, claque du papier, obturateur par photo, crissement du crayon gras. Lit continu : ronron de projecteur du début à la fin.
- Voix ≈ 12 dB au-dessus de la musique ; deux silences (arrêt net avant le retournement, projecteur seul avant la chute) ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Toutes les sources sont de vraies archives dont la licence est écrite dans `SOURCES.md` (domaine public, CC0 ou CC BY) ; aucune image générée, colorisée ou « restaurée par IA ».
- [ ] Un seul réglage de niveaux par plan ; pas de pompage de luminosité.
- [ ] Chaque transition d'époque n'apparaît qu'une fois.
- [ ] Les coupes tombent sur les temps de l'orchestre (écart mesuré < 1 image).
- [ ] Carton de lieu lisible : tenu au moins (lettres ÷ 15 + 1,5) s une fois complet.
- [ ] La description du catalogue de chaque film a été lue : le plan montre bien ce que la voix affirme.
- [ ] Sous-titres sur deux lignes au plus, hors zones d'interface.
- [ ] Le générique porte le nom et l'emblème du client, rien d'un vrai journal filmé.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/newsreel.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/newsreel.jpg
- Crédit : « Knock-Knee Alert », LemoLab, CC BY 4.0. Archives et imprimés de tiers (domaine public et licences propres) : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/newsreel/STYLE.md`, `style.json`, `demo/` (`sceneLogo()`, `filmLook()`, `tools/prep.py`, `audio/mix.py`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mise en page 9:16, HyperFrames, budget de bruitages. Sources et droits : `references/materiel-et-droits.md`.
