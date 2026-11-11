---
name: styles-lancement-produit
description: "Catégorie de styles « Lancement de produit et SaaS » du studio motion : vidéo de lancement (narrée mot à mot, en 7 temps, forme continue sur la musique, teaser haute énergie), démonstration de logiciel (démo épurée, film produit SaaS, parcours en plan-séquence), ouverture 3D cinématique et export en reel vertical. À utiliser quand le client lance ou présente un produit, une offre, une appli ou un logiciel, ou dit « vidéo de lancement », « teaser », « démo », « vidéo de page d'accueil », « promo de mon produit »."
---

# Styles Lancement de produit et SaaS (catégorie 11)

Neuf fiches pour vendre **une chose**, avec de vraies preuves. Leur point commun : un film de produit défend une seule affirmation, montre le vrai produit, et ne ment sur rien.

Le skill `studio-coeur` pilote le parcours. `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, export), `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s), `marque` (fiche « ma chaîne » : couleurs, polices, logo, ton) et `blender` (ouverture 3D) s'appliquent.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `lancement-7-temps` | Lancement en 7 temps | Une phrase découpée en fragments, de vraies preuves, le produit qui travaille, un nombre sourcé, l'appel à l'action | hyperframes | facile | à produire |
| `lancement-narre-mot-a-mot` | Lancement narré mot à mot | La voix d'abord ; chaque révélation tombe sur son mot ; deux registres (sombre pour l'argument, clair pour le produit) | hyperframes | élevée | à produire (film d'origine non réutilisable) |
| `forme-continue-sur-la-musique` | Forme continue sur la musique | Une seule forme jamais coupée, pilotée par un curseur, tout calé sur la musique | hyperframes | élevée | à produire (films d'origine non réutilisables) |
| `teaser-haute-energie` | Teaser haute énergie | 12 à 20 s, quelque chose à chaque temps, une forme porte l'œil d'une scène à l'autre | hyperframes (+ canvas / three) | moyenne | [GIF](https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-high-energy.gif) (Bart, MIT) |
| `demo-produit-epuree` | Démo produit épurée | Fond clair, une ligne à la fois, l'interface reconstruite et filmée de près ; la caméra fait le montage | hyperframes | moyenne | [GIF](https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-default.gif) (Bart, MIT) |
| `film-produit-saas` | Film produit SaaS | 45 à 75 s : une chaîne où chaque étape produit la suivante, écrans reconstruits depuis les captures, muet d'abord | hyperframes | élevée | à produire |
| `parcours-plan-sequence` | Parcours en plan-séquence | Un héros (une bille) traverse les étapes du produit, la caméra ne coupe jamais, recul final sur tout le parcours | hyperframes (fonction pure du temps) | élevée | [GIF](https://github.com/Barty-Bart/motion-graphics/blob/main/docs/explainer-engaging.gif) (Bart, MIT) |
| `ouverture-3d-cinematique` | Ouverture 3D cinématique | 8 à 15 s : une caméra avance dans un décor éclairé (rue de nuit, enseignes) et finit sur la phrase | blender (qualité) ou three + hyperframes | élevée | à produire |
| `export-reel-vertical` | Export en reel vertical | Une vidéo large posée dans un cadre 9:16 sous une accroche de deux lignes, encodée comme les applis l'attendent | ffmpeg (ou hyperframes) | facile | à produire |

## Comment choisir

| Le client veut… | Style conseillé | Sinon |
|---|---|---|
| Annoncer un lancement, simplement, avec des preuves | `lancement-7-temps` | `lancement-narre-mot-a-mot` s'il veut une voix |
| Un film de lancement avec voix off | `lancement-narre-mot-a-mot` | |
| Un film de lancement sans voix, très « design » | `forme-continue-sur-la-musique` | `teaser-haute-energie` si 15 s suffisent |
| Créer l'attente, 15 secondes, de l'énergie | `teaser-haute-energie` | `ouverture-3d-cinematique` pour une question d'accroche |
| Montrer ce que fait son logiciel, calmement | `demo-produit-epuree` | `film-produit-saas` s'il veut tout le parcours et a des captures |
| Montrer tout le parcours d'un logiciel à plusieurs écrans | `film-produit-saas` | |
| Faire comprendre un fonctionnement en 3 à 6 étapes, en boucle | `parcours-plan-sequence` | |
| Une ouverture qui arrête le pouce avant une vidéo | `ouverture-3d-cinematique` | scène 1 de `teaser-haute-energie` |
| Publier en vertical une démo faite en large | `export-reel-vertical` | recomposer avec la section 9:16 de la fiche d'origine |

Trois questions suffisent pour trancher : **avec ou sans voix ?** (voix → narré ; sans → les autres) · **exciter ou expliquer ?** (exciter → teaser, forme continue, ouverture 3D ; expliquer → démo, film SaaS, parcours) · **quelle durée ?** (≤ 20 s → teaser, parcours, ouverture ; 30 à 60 s → 7 temps, narré, forme continue, démo ; 45 à 75 s → film SaaS).

Débutant : `lancement-7-temps`. On peut combiner : `ouverture-3d-cinematique` (8 s) puis `lancement-7-temps`.

**Voir aussi (fiches portées par une autre catégorie)** : ces fiches donnent un look, pas un déroulé de lancement ; on les combine avec la structure d'une fiche d'ici.

- `keynote-produit` (un écran, une chose ; la vraie capture du produit en grand) et `keynote-sombre` (scène noire, interface dessinée, un seul accent) : `styles-explicatif-infographie/styles/keynote-produit/STYLE.md`, `styles-explicatif-infographie/styles/keynote-sombre/STYLE.md` ;
- `typo-cinetique` (le mot comme acteur : accroche, phrase choc, chiffre) : `styles-graphique-typo/styles/typo-cinetique/STYLE.md` ;
- `isometrique-trait-fin` (un objet au trait gris fin, pour un matériel ou une infrastructure) et `verre-produit` (produit en verre dans un studio noir) : `styles-matieres-3d/styles/<identifiant>/STYLE.md` ;
- `screencast-vivant` (tutoriel de logiciel pas à pas) : `styles-explicatif-infographie/styles/screencast-vivant/STYLE.md`.

## Règles communes à la catégorie

1. **Une affirmation, un film.** Elle tient en sept mots, se dit à voix haute, et tombe dans les 10 premières secondes (les 3 premières en vertical court). Détail : `references/script-de-lancement.md`.
2. **Rien d'inventé.** Ni chiffre, ni prix, ni date, ni « places restantes », ni avis, ni témoignage, ni résultat, ni client. Chaque nombre vient de la liste approuvée par le client, avec sa source. Les données d'exemple à l'intérieur d'une interface sont permises si elles sont crédibles et, au besoin, étiquetées « données d'exemple ».
3. **Logos et visages réels seulement depuis les fichiers du client**, avec son accord ; sinon le nom en texte. Les logos de clients se montrent un par un, jamais en rangée « ils nous font confiance ».
4. **Les couleurs sont celles de la marque** (fiche « ma chaîne »), jamais une palette par défaut. Un seul accent. Dérivation : `references/etalonnage.md` §10.
5. **La frappe n'existe que dans un champ de saisie.** Jamais un titre en machine à écrire.
6. **Interdits par défaut** : rebonds, lueurs, particules décoratives, dégradés sur le texte ou sur les éléments d'interface, fond bleu-violet, temps mort, tout ce qui ressemble à un modèle tout fait.
7. **Ressorts à très faible dépassement** ; la caméra et le texte ne dépassent pas. Les sorties sont plus rapides que les entrées.
8. **Lisible sans le son, sur un téléphone.** Mot ou nombre héros ≥ 120 px ; libellés ≥ 34 px ; état final tenu ≥ 1,2 s ; appel à l'action tenu ≥ 3 s.
9. **Zone sûre 9:16** : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Les sources sont pensées en 16:9 : la section 3 de chaque fiche donne la composition verticale. Calculer chaque poussée de caméra contre ces limites.
10. **L'image 0 est la vignette** : jamais du noir, jamais un logo seul.
11. **Le réalisateur décide et rend compte** : noter chaque décision créative et les lister à la livraison, avec ce qui est réel et ce qui est illustratif, et ce qui a été **mesuré** ou réellement **écouté** pour le son.
12. **Anti-copie** : les films d'exemple des dépôts sources appartiennent à leurs auteurs ou à leurs clients ; on ne les montre pas, on n'en reprend ni plan, ni texte, ni marque.

## Références de la catégorie

| Fichier | Contenu |
|---|---|
| `references/script-de-lancement.md` | l'angle en sept mots, l'arc, écrire pour l'oreille, la liste des chiffres approuvés, ce que le client fournit |
| `references/camera-et-curseur.md` | montage caméra à deux nœuds, rotation, poussée, point fixe, profondeur, mise au point, curseur accessoire, clic en trois couches, budget contre les bords |
| `references/etalonnage.md` | les deux registres de fond, aurore, verre, grain / vignette / balayages, piège des modes de fusion, palette dérivée de la marque |
| `references/son-et-mastering.md` | caler sur la voix ou sur la musique, table des repères, loi du volume, grave et silence, mastering en deux passes, vérification dans le fichier livré |

## Fiches

`styles/<identifiant>/STYLE.md`, dix sections fixes. Crédits et licences : `licenses/styles-lancement-produit.md` à la racine du plugin.
