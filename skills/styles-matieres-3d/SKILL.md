---
name: styles-matieres-3d
description: "Catégorie de styles « Matières et 3D » du studio motion (briques jouet, livre pop-up, maquette tilt-shift, île low-poly, produit en verre, diorama Memphis, survol de bureau, isométrique au trait fin, pâte à modeler, mosaïque). À utiliser quand le client veut une vidéo en 3D, en maquette, en volume ou dans une matière reconnaissable (plastique, papier, verre, argile, pierre), ou dit « 3D », « maquette », « isométrique », « stop-motion », « pâte à modeler »."
---

# Styles Matières et 3D (catégorie 9)

Dix styles où **la matière est le sujet** : on doit croire qu'on pourrait toucher l'image. Huit sont en vraie 3D, deux sont dessinés en 2D (isométrique au trait, mosaïque).

Le skill `studio-coeur` pilote le parcours. `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, export) et `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) s'appliquent. Dans cette catégorie, **le bruitage suit la matière** : chaque fiche donne les sons de son matériau.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `briques-jouet` | Briques jouet | Stop-motion de briques en plastique filmé en macro sur un vrai bureau | **blender** (three possible) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/brick-toy.mp4) (LemoLab, CC BY 4.0) |
| `livre-pop-up` | Livre pop-up | Un livre animé sur un bureau : acteurs en papier découpé devant des décors qui se déplient ; conte, ou histoire vraie en chapitres | **blender** ou three | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/paper-popup.mp4) (LemoLab, CC BY 4.0) |
| `maquette-tilt-shift` | Maquette tilt-shift | Un lieu réaliste vu de haut, bande de netteté et accéléré : le monde devient une maquette | **blender** (three possible) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/tilt-shift.mp4) (LemoLab, CC BY 4.0) |
| `ile-low-poly` | Île low-poly isométrique | Petit monde à facettes en vue orthographique ; chaque pièce arrive avec un rebond et une note | **three** (blender possible) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/lowpoly-island.mp4) (LemoLab, CC BY 4.0) |
| `verre-produit` | Produit en verre | Objet en verre clair et dépoli dans un studio noir : balayages de lumière, dispersion, vue éclatée | **blender** (three possible) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/glass-product.mp4) (LemoLab, CC BY 4.0) |
| `diorama-memphis` | Diorama Memphis | Un lieu en maquette aux couleurs plates, contours encre, ombres violettes dures, mille petits mouvements | **three** (blender possible) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/memphis-diorama.mp4) (LemoLab et Eian, CC BY 4.0) |
| `survol-bureau` | Survol de bureau | Écrans d'applis imprimés en cartes papier sur un bureau ensoleillé, petits personnages en voxels, un seul plan | **three** ou blender | élevée | affiche seulement (voir la fiche) |
| `isometrique-trait-fin` | Isométrique au trait fin | Objets en isométrie 2:1 dessinés en traits fins gris sur blanc, un seul accent sombre | **hyperframes** (2D) | facile | image dans la fiche (animate, MIT) |
| `pate-a-modeler` | Pâte à modeler | Stop-motion d'argile : marionnette bosselée, empreintes de doigts, 12 poses par seconde | **blender** (obligatoire) | moyenne | pas de vidéo publiée (voir la fiche) |
| `mosaique` | Mosaïque | Tesselles de pierre qui suivent les contours ; les pierres ne bougent pas, la couleur circule | **hyperframes** (2D) | moyenne | pas d'aperçu isolé (voir la fiche) |

## Comment choisir

- **Montrer un produit haut de gamme, ce qu'il a dedans, ce qu'il fait d'invisible** : `verre-produit`.
- **Expliquer un produit, un matériel, une infrastructure, sobrement** : `isometrique-trait-fin` (le plus rapide à faire).
- **Raconter une construction, un échec qui devient des pièces de rechange, un projet d'équipe** : `briques-jouet`.
- **Une histoire pour enfants, des étapes en chapitres, une vie racontée page par page, un objet réel qui entre dans le récit** : `livre-pop-up`.
- **Un système vu d'en haut (ville, port, logistique), puis un détail humain** : `maquette-tilt-shift`.
- **Une croissance pièce par pièce, un réseau qui s'allume, une journée en accéléré** : `ile-low-poly`.
- **Un lieu qu'on regarde vivre (quartier, saisons, carte de couverture), sans personnage** : `diorama-memphis`.
- **Le trajet d'une donnée ou d'une tâche entre plusieurs applis** : `survol-bureau`.
- **Un petit personnage attachant, une mascotte, une carte de vœux** : `pate-a-modeler`.
- **Un sujet patrimonial, culinaire ou méditerranéen, un logo en pierre** : `mosaique`.

Débutant : `isometrique-trait-fin`, puis `ile-low-poly`.

**Fiches d'ici qui servent aussi à d'autres catégories** (une seule fiche par style dans tout le plugin) : `livre-pop-up` sert à `styles-2-5d` (encadré « Variante histoire vraie » de la fiche) et à `styles-papier-impression` ; `isometrique-trait-fin` sert à `styles-explicatif-infographie` et à `styles-lancement-produit`.

**Voir aussi (fiches portées par une autre catégorie)** :

- `diorama-pixel` (maquette 3D embrumée à petits personnages en pixel art) : `styles-jeu-retro/styles/diorama-pixel/STYLE.md` ;
- `theatre-de-papier` (figurines de carton devant des décors en plans parallèles, éclairées à la bougie) : `styles-2-5d/styles/theatre-de-papier/STYLE.md` ;
- `vue-eclatee` et `donnees-en-objets` (vrai produit démonté, statistiques en objets filmés en studio) : `styles-montage-documentaire/styles/<identifiant>/STYLE.md`.

## Blender ou Three.js : ce qui change

Règle du studio : **Blender (connecteur MCP `blender`) dès que la qualité l'exige ; Three.js pour le léger ; HyperFrames assemble dans tous les cas** (titres, sous-titres, son, export). Chaque fiche 3D redit le choix pour son style et ce qui lui est propre. L'installation, la connexion, le rendu vertical et l'envoi vers HyperFrames sont décrits dans le skill `blender` : ouvre-le avant toute voie Blender.

| | Blender | Three.js |
|---|---|---|
| Ce qu'il faut chez le client | Blender 4.2 ou plus, le connecteur MCP `blender` actif, une carte graphique de préférence | rien de plus qu'HyperFrames (navigateur) |
| Comment on travaille | l'agent écrit du Python exécuté dans Blender (`execute_blender_code`), regarde le résultat (`look` : vue caméra, planche d'angles, bande d'images), importe textures, ciels et modèles libres (`search_assets` / `import_asset`) | une page HTML avec une scène three.js dont l'état est calculé depuis le temps, pilotée image par image par HyperFrames |
| Lumière et matières | lancer de rayons (Cycles) : reflets, réfractions, caustiques, ombres douces, occlusion, profondeur de champ **vrais** ; EEVEE pour aller plus vite | approximations temps réel : il faut écrire ou régler soi-même occlusion ambiante, profondeur de champ, lueur ; verre et reflets limités |
| Physique | corps rigides, tissu, particules, précalculés | à écrire à la main et à précalculer |
| Temps de rendu | lent (secondes à minutes par image) ; on valide sur des images fixes avant de lancer le film | rapide (≈ temps réel par sous-image) |
| Sortie | suite d'images PNG ou vidéo, **posée comme fond** d'une composition HyperFrames | canvas WebGL vivant dans la composition, piloté par `hf-seek` |
| Retouche | changer un détail = relancer le rendu de la plage concernée | changer un détail = relancer l'export |
| Texte à l'écran | le texte « dans le monde » (enseigne, carte imprimée) se rend dans Blender ; sous-titres et titres par-dessus, en HTML | tout peut rester dans la page |
| Risque | rendu trop réaliste, qui perd le caractère du style ; durées de rendu sous-estimées | rendu « image de synthèse propre » : plat, crénelé, sans contact au sol |

**Méthode commune aux deux** :

1. Construis en **unités réelles** (mètres, ou millimètres pour un produit) : la lumière, les ombres et la profondeur de champ se comportent alors comme en vrai.
2. **Images fixes d'abord** : 4 à 6 images aux temps forts, basse résolution, peu d'échantillons. Vérifie l'exposition, le contact au sol, la lisibilité du sujet à taille de vignette, le cadrage 9:16. Seulement ensuite, le rendu complet.
3. **Tout est déterministe** : simulations précalculées, hasard à graine, aucun état gardé d'une image à l'autre. La même image rendue deux fois est identique.
4. **L'occlusion ambiante n'est pas une option** : c'est elle qui assoit les objets (joints entre briques, dessous des toits, contact des pieds).
5. **Suréchantillonne** (rendu 2× puis réduction) en Three.js : les arêtes fines scintillent sinon.
6. **Courbe de tons neutre** : les courbes « filmiques » décalent les couleurs franches du papier, du plastique et des accents.
7. Images fixes des personnages « en deux » si le style est un stop-motion (15 poses par seconde à 30 i/s, 12 à 24 i/s) ; la caméra reste fluide.

```html
<!-- Three.js dans HyperFrames -->
<canvas id="gl" width="1080" height="1920"></canvas>
<script type="module">
  function renderAt(t) { majScene(t); renderer.render(scene, camera); }
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(0);
</script>

<!-- Blender dans HyperFrames : la suite d'images rendue devient la vidéo de fond ;
     titres et sous-titres se posent par-dessus (voir le skill rendu) -->
```

**Timeline à enregistrer.** Un film dessiné par `hf-seek` doit quand même enregistrer une timeline, même vide, après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire le contrôle qui détecte un film figé. Recette complète : skill `rendu`, section « Film en canvas piloté par `hf-seek` » (vérifiée en rendu réel le 11/11/2026).

## Règles communes à la catégorie

1. **Aucune marque** : ni nom, ni logo, ni silhouette reconnaissable d'un jouet, d'un téléphone, d'un casque ou d'une appli. Les objets sont inventés ; les interfaces sont celles du client ou des interfaces génériques.
2. **Zone sûre 9:16** : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Sujet à au moins 1/3 de la hauteur aux moments clés.
3. **Le vertical se recompose** : on ne recadre pas un plan horizontal. Une table, un bureau ou une île se cadrent en plongée plus forte, sujet au tiers bas ou au centre, profondeur vers le haut.
4. **Modèles, textures et ciels importés** : seulement sous licence libre (domaine public CC0 de préférence), notés dans les crédits du film avec leur source.

## Pour produire

1. Lis la fiche `styles/<identifiant>/STYLE.md` (figée : look, couleur, typo, mouvement, son, pièges).
2. L'histoire vient du sujet du client, jamais de la démo d'origine (au moins 4 différences sur 6 : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin).
3. Vérifie le moteur disponible chez le client (Blender et son connecteur répondent-ils ?). Sans Blender, prends la voie Three.js de la fiche, ou propose un style voisin en 2D.
4. Images fixes validées, puis rendu, puis liste de contrôle de la fiche et porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-matieres-3d.md` à la racine du plugin.
