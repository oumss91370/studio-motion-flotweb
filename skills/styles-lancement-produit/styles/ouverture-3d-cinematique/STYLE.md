# Ouverture 3D cinématique

## 1. Identité
- **Nom** : Ouverture 3D cinématique. Identifiant : `ouverture-3d-cinematique`.
- **Inspiration** : les génériques d'ouverture de films et de documentaires : une caméra qui avance dans un décor éclairé et finit sur une question ou un titre.
- **Principe** : les 3 premières secondes décident si l'on regarde. On construit une **courte ouverture de 8 à 15 secondes** : une caméra qui se déplace dans **un seul monde 3D éclairé**, où les objets du sujet deviennent des enseignes, des écrans ou des affiches, et qui se termine sur **la phrase** du client.
- **Pour quels sujets** : ouverture d'une vidéo de lancement, d'un explicatif ou d'un documentaire court ; bande-annonce ; question d'accroche (« Pourquoi tous les logos se ressemblent-ils ? »).
- **Ne marche pas pour** : une vidéo entière (c'est une ouverture), un sujet sans phrase forte, un client qui n'a pas ses fichiers de logos.
- **Barre de qualité** : « renversant, ou ce n'est pas fini ». Si les 3 premières secondes n'arrêteraient pas ton propre pouce, les refaire avant de construire la suite.

## 2. Palette, typographie, matières
- **Le monde** : un seul décor qui colle à l'histoire. Par défaut : **rue sous la pluie, la nuit**. Autres : bureau vide, table de travail à 5 h du matin, scène de théâtre, entrepôt, quai.
- **Palette de nuit** : fond bleu nuit très sombre mais **jamais noir pur** (`#0B0B0F` à `#10121A`), sol mouillé réfléchissant, enseignes lumineuses aux couleurs réelles des objets, **un seul accent** (celui de la fiche « ma chaîne ») pour le mot clé du titre.
- **Titre** : gras, condensé (Barlow Condensed 800, Anton ou Oswald 700, libres), blanc, mot clé en accent.
- **Matières** : bâtiments simples à peu de facettes, sol mouillé, pluie fine, halo doux sur les enseignes : **subtil, jamais brûlé**.
- **Enseignes** : le fichier du logo ou de l'image est appliqué sur un panneau lumineux. **Les logos viennent des vrais fichiers fournis, jamais redessinés de mémoire**, et ils **remplissent leur panneau** (un logo petit dans une grande boîte fait faux).
- **Cartes et images, pas des lignes** : une seule barre ou ligne qui traverse l'écran se lit comme statique ; chaque plan utilise des cartes, de vraies images ou des objets qui bougent en profondeur.
- **Grilles symétriques** : panneaux de même taille, écarts égaux ; une disposition bancale se lit comme une erreur.
- **Police de repli** : Inter pour les textes ajoutés dans HyperFrames ; Montserrat (800) pour une enseigne. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : la police de la marque : fichier fourni par le client ; à vérifier. Dans Blender, la police est un fichier `.ttf` chargé dans la scène.

## 3. Composition 9:16
- **Une rue en perspective centrale** convient au vertical : point de fuite vers y 800, façades et enseignes qui montent de chaque côté. Étager les enseignes en hauteur (y 250 à y 1100).
- **Titre** : dans le dernier tiers du temps, en bas à gauche de la zone utile : x 80, entre y 1080 et y 1480, 2 à 4 lignes de 110 à 150 px. **Le sol sous le titre reste assez sombre** pour qu'aucun reflet ne traverse les lettres ; rien de réfléchi derrière le titre.
- **Petits libellés** (dates, légendes) : **au moins deux fois plus gros que ce qu'on croit nécessaire** ; 34 px minimum.
- Chaque enseigne lisible à la taille d'un téléphone. Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : rue plus large, titre en bas à gauche.

## 4. Ce qui bouge
- **Action principale** : **un seul travelling avant, lent et régulier, légèrement montant**, qui passe devant les enseignes. Ni secousse, ni tour sur soi.
- **Boucles de fond** : (1) la pluie (à graine fixe) ; (2) le léger scintillement des enseignes et des reflets au sol.
- **Le titre** se pose dans le dernier tiers : révélation par masque ou montée courte, puis tenue.
- **Autorisés** : #027 travelling avant, #031 légère montée de grue, #176 traversée de décor, #016 parallaxe (naturelle en 3D), #005 révélation par masque du titre, #105 flou d'arrière-plan, #033 bascule de mise au point vers le titre.
- **Interdits** : #034 caméra à la main qui tremble, #030 orbites et #170 tonneaux, #023 parasites décoratifs, halo brûlé, plusieurs décors, logos redessinés.

## 5. Rythme et montage
- **8 à 15 secondes**, un seul plan.
- Seconde 0 à 1 : l'image ressemble déjà à un film, pas à un diaporama (l'image 0 est la vignette : décor éclairé, jamais du noir).
- Tiers 1 et 2 : la caméra avance, deux à cinq enseignes passent, chacune lisible ≥ 1 s.
- Dernier tiers : le titre se pose et tient ≥ (lettres ÷ 15 + 1,5) s.
- Sortie : coupe sèche vers la suite de la vidéo, ou fondu court sur un temps de la musique.

## 6. Recette technique
- **Moteur** : **Blender** par le connecteur `blender` quand la qualité compte (sol mouillé, reflets, halo, flou de profondeur : c'est ce qui fait « film »). Décor en trois passes (volumes → lumière → détails), caméra sur une trajectoire droite, rendu en séquence d'images 1080×1920 ; titre et sons ajoutés dans HyperFrames. **Three.js** dans HyperFrames pour une version légère.
- **Version Three.js** (extrait) :
```js
// une enseigne : le fichier fourni devient la texture d'un panneau lumineux
const tex = new THREE.TextureLoader().load("assets/logo-client.png");
const enseigne = new THREE.Mesh(new THREE.PlaneGeometry(3, 1.7),
  new THREE.MeshBasicMaterial({map: tex, toneMapped: false}));
// pluie à graine fixe : jamais Math.random au moment du rendu
const alea = graine(42);
// caméra : une seule fonction du temps
window.addEventListener("hf-seek", (e) => {
  const u = e.detail.time / DUREE, k = u * u * (3 - 2 * u);
  camera.position.set(0, 1.6 + 0.9 * k, 18 - 22 * k);
  pluie.position.y = -((e.detail.time * 9) % 12);
  composer.render();
});
```
- Version de Three.js **épinglée et embarquée** ; rien chargé depuis internet au rendu.
- **Halo** : seuil haut, force faible ; vérifier qu'aucune enseigne ne devient une tache blanche.
- **Contrôle** : captures à 1 s, au milieu et à la dernière seconde : chaque enseigne lisible à la taille d'un téléphone, rien de réfléchi derrière le titre, chaque logo conforme à son fichier.
- **Pièges** : halo sur fond clair qui explose ; sol trop réfléchissant sous le titre ; rendu logiciel lent sans carte graphique (prévenir le client de la durée) ; aléatoire non fixé = pluie différente à chaque rendu.

## 7. Son
- **Le son n'est pas optionnel** : une ouverture muette paraît inachevée.
- Structure : un lit grave, **un coup à chaque nouveau plan ou enseigne importante**, une levée sur la dernière ligne.
- Ambiance du monde : pluie douce, ville lointaine ; entrée en fondu sur la première seconde.
- La source propose d'écrire la musique en code ; ici : **vrais enregistrements d'abord** (pluie, ambiance, impact), synthèse en repli (skill `son`). Budget : 3 à 6 bruitages sur toute l'ouverture.
- −14 LUFS avec le reste de la vidéo.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] La première seconde ressemble déjà à un film ; l'image 0 n'est pas noire.
- [ ] Un seul monde, un seul mouvement de caméra, sans secousse ni rotation.
- [ ] Chaque enseigne vient d'un fichier fourni, remplit son panneau et se lit sur un téléphone.
- [ ] Le titre est lisible : sol sombre dessous, aucun reflet derrière les lettres.
- [ ] Libellés ≥ 34 px ; titre tenu assez longtemps.
- [ ] Halo subtil : aucune zone brûlée (contrôle sur 3 images).
- [ ] Le son est présent : lit, coups, levée finale.
- [ ] Zones d'interface respectées ; rendu reproductible (même pluie à chaque rendu).

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu
- Aucun aperçu fourni dans le dépôt d'origine pour ce style. Aperçu Flot Web à produire (c'est un bon candidat de vitrine).

## 10. Origine
- Dépôt : charlie947/motion-graphics-skills, commit `229022e`. Fichier : `skills/title-sequence-3d/SKILL.md`.
- Licence : MIT (© 2026 Charlie Hills).
- Adaptations Flot Web : français, Blender en moteur de qualité (la source est en Three.js), composition 9:16, vrais enregistrements d'abord.
