# Code de départ manquant : fichiers cités par les fiches et absents du plugin

État au 11/11/2026, produit par un script qui lit la section 6 des 130 fiches `STYLE.md` et cherche chaque nom de fichier dans le plugin (hors copies de tiers).

- **61 fiches sur 130** nomment des fichiers de code que le plugin ne fournit pas ; **167 noms distincts**.
- Dans chaque fiche, la ligne « Structure » dit maintenant que ces fichiers sont **à écrire par l'agent, d'après la description** : aucun n'est annoncé comme fourni.
- Les noms sont ceux des dépôts d'origine, traduits : deux fiches qui citent `papier.js` ne parlent pas du même code. Le compte par nom dit donc combien de fiches attendent une brique de ce genre, pas qu'un seul fichier les servirait toutes. La première table, par famille, est celle qui sert à décider.
- Les 69 autres fiches décrivent leur moteur sans nommer de fichier (styles en HTML et GSAP, styles Blender ou Three.js) : elles ne sont pas dans ce compte, mais n'ont pas davantage de code de départ.

## 1. Par famille de moteur (à lire pour choisir quoi fournir en vrai)

| Rang | Famille | Fiches qui en dépendent | Fichiers cités (noms distincts) |
|---|---|---|---|
| 1 | Assemblage du film (scènes, chronologie, boucle `hf-seek`) | 50 | 22 : `film.js`, `scenes.js`, `timeline.js`, `scene.js`, `main.js`, `moteur.js`, `page.js`, `chronologie.js`, `compo.js`, `distribution.js`, `epoques.js`, `histoire.js`, `horloge.js`, `jeu.js` … |
| 2 | Personnages et pantins (rig, poses, visages) | 29 | 18 : `figure.js`, `persos.js`, `heros.js`, `rig.js`, `mascotte.js`, `personnages.js`, `portraits.js`, `poses.js`, `sprites.js`, `coulisses.js`, `figures.js`, `levres.js`, `pantins.js`, `perso.js` … |
| 3 | Décors et motifs | 28 | 21 : `motifs.js`, `accessoires.js`, `decors.js`, `formes.js`, `decor.js`, `mondes.js`, `ampoules.js`, `arrivee.js`, `composants.js`, `deco.js`, `eau.js`, `environnement.js`, `fenetre.js`, `icones.js` … |
| 4 | Trait et outil (encre, plume, craie, feutre, burin, couteau) | 23 | 18 : `encre.js`, `traits.js`, `craie.js`, `toon.js`, `trace.js`, `burin.js`, `cellulo.js`, `ciseaux.js`, `ciseler.js`, `couteau.js`, `dessiner.js`, `encrer.js`, `feutre.js`, `peindre.js` … |
| 5 | Papier et matière (grain, feuille, textures) | 21 | 14 : `papier.js`, `feuille.js`, `tableau.js`, `cuivre.js`, `grain.js`, `materiaux.js`, `matieres.js`, `papier.glsl`, `planche.js`, `plaque.js`, `salle.js`, `table.js`, `textures.js`, `verre.js` |
| 6 | Isométrie et géométrie (projection, faces, grille) | 20 | 18 : `camera.js`, `grille.js`, `iso.js`, `monde.js`, `kit.js`, `couleurs.js`, `energie.js`, `faces.js`, `geo.js`, `graphique.js`, `holo.js`, `infographie.js`, `lieu.js`, `maths.js` … |
| 7 | Lettrage et texte (cartons, bulles, étiquettes, sous-titres) | 20 | 19 : `interface.js`, `affichage.js`, `lettrage.js`, `texte.js`, `affiche.js`, `banderole.js`, `bulles.js`, `cartons.js`, `ecriture.js`, `enseigne.js`, `etiquettes.js`, `incrustation.js`, `inscriptions.js`, `legende.js` … |
| 8 | Trame et impression (points, blocs, repérage) | 14 | 11 : `imprimer.glsl`, `lavis.js`, `ombres.js`, `trame.js`, `compose.glsl`, `couleur.js`, `impression.js`, `pli.js`, `pont.js`, `soie.js`, `trames.js` |
| 9 | Passe finale (pellicule, tube, cassette, lumière) | 13 | 13 : `post.js`, `lumiere.js`, `pellicule.js`, `ambiance.js`, `cassette.js`, `effets.js`, `filtre.js`, `lumiere.glsl`, `miroirs.js`, `neon.js`, `onde.js`, `redessin.js`, `tube.js` |
| 10 | Pixel (primitives, palette forcée, police bitmap) | 6 | 7 : `police.js`, `palette.js`, `art.js`, `palettes.js`, `pixel.js`, `px.js`, `term.js` |
| 11 | Données du film (fichiers JSON) | 6 | 6 : `contenu.json`, `donnees.json`, `evenements.json`, `modele.json`, `timeline.json`, `voix.json` |

Lecture : l'assemblage du film est demandé partout, mais c'est le plus court à écrire (la recette existe dans le skill `rendu`, « Film en canvas piloté par `hf-seek` »). Les familles qui coûtent du temps à chaque film, et où un vrai moteur fourni changerait le résultat, sont le trait, le papier, la trame et l'impression, la passe finale, le pixel.

## 2. Ce que les rendus réels du 11/11/2026 ont déjà écrit (base possible pour un moteur fourni)

Ces morceaux ont tourné dans un film rendu. L'essentiel est recopié dans la section 6 de la fiche, comme « extrait vérifié ». Les projets complets sont dans le dossier des essais (hors plugin).

| Brique | Fiche | Ce qui existe | Familles servies |
|---|---|---|---|
| Impression bloc par bloc (masque diagonal, repérage, veines, manques) | `estampe-japonaise` | un fichier d'environ 230 lignes, canvas 2D | trame et impression, papier |
| Redessin à l'encre et tirage pellicule (un fragment shader WebGL2) | `film-muet-1920` | contours, 5 paliers, hachures, grain, rayures, poussières, sépia, iris | passe finale, trait |
| Police bitmap 5×7 avec accents français, palette forcée, tramage | `pixel-8-bits` | 22 lettres dans le film ; 14 capitales accentuées ajoutées et vues sur capture | pixel |
| Projection isométrique, dalles, ressort sans état | `isometrique-trait-fin` | un fichier d'environ 160 lignes, canvas 2D | isométrie |
| Pièces de personnage en SVG avec trait à manques et couleur décalée | `cartoon-annees-50` | script d'assemblage et gabarit de scène | personnages, trait |
| Trame de points fixe à l'écran, cerne et aplat, étoile éclatée | `pop-trame` | un fichier d'environ 190 lignes, canvas 2D | trame et impression |
| Compteur et barres pilotés par un objet relais | `graphique-anime` | SVG et GSAP | isométrie et géométrie (graphiques) |
| Texte découpé par `SplitText` après chargement des polices | `typo-suisse` | HTML et GSAP | lettrage |
| Sous-titres en blocs dans une scène de `compositions/` | `info-sous-titres` | deux scènes et un `timeline.json` | lettrage, assemblage |
| Pan de lumière à bord net, ombre portée de silhouette | `lumiere-diner-americain` | un fichier d'environ 220 lignes, canvas 2D | passe finale (lumière) |

## 3. Par nom de fichier, du plus cité au moins cité

| Fichier | Fiches | Lesquelles | Rôle décrit (première fiche qui le précise) |
|---|---|---|---|
| `film.js` | 23 | affiche-serigraphie, cartoon-annees-50, circuit-imprime, collage-enquete, donnees-crayon, generique-espion-60, graphique-anime, hologramme-hud, infographie-isometrique, keynote-sombre, livre-isometrique, maths-animees, micro-jeux, pictogrammes, pixel-rpg-16-bits, plan-bleu, presentateur, recit-dessine, science-a-plat, screencast-vivant, tableau-blanc-a-la-main, tableau-noir-craie, terminal-ascii | timeline, caméras, balayages |
| `scenes.js` | 14 | affiche-serigraphie, carnet-de-croquis, craie-grasse-album, encre-hachures, isometrique-trait-fin, jeu-tele-rythmique, papier-decoupe-collage, papier-decoupe-satirique, papiers-decoupes-matisse, pixel-8-bits, pixel-rpg-16-bits, pop-trame, risographie, tuyau-caoutchouc-1930 | un lieu = des pièces d'encre dans l'ordre d'impression |
| `papier.js` | 9 | craie-grasse-album, dossier-trame, generique-espion-60, papier-decoupe-collage, papier-decoupe-rouge, papier-decoupe-satirique, papiers-decoupes-matisse, plan-bleu, trait-continu | grain ancré |
| `camera.js` | 7 | art-deco, collage-enquete, keynote-sombre, science-a-plat, tableau-blanc, tableau-blanc-a-la-main, trait-continu | caméra à sténopé pour un vrai point de fuite |
| `timeline.js` | 7 | craie-grasse-album, film-muet-1920, huile-couteau, micro-jeux, risographie, tableau-blanc, tuyau-caoutchouc-1930 | une feuille de repères qui pilote image **et** musique |
| `scene.js` | 6 | aquarelle-carnet, keynote-sombre, lanterne-papier, ombres-chinoises, screencast-vivant, vitrail | plans, bandes de lavis, placement, annotations |
| `figure.js` | 5 | bonshommes-trait-epais, estampe-japonaise, film-muet-1920, gravure-cuivre, lavis-encre | capsules |
| `persos.js` | 5 | cartoon-annees-50, jeu-tele-rythmique, micro-jeux, sitcom-sf, tuyau-caoutchouc-1930 | présentateur, mains gantées, produit |
| `encre.js` | 4 | encre-hachures, film-muet-1920, trait-continu, tuyau-caoutchouc-1930 | trait tremblé, tracé progressif |
| `main.js` | 4 | aquarelle-carnet, estampe-japonaise, tableau-blanc-a-la-main, tableau-noir-craie | caméra, brume, sous-titres |
| `moteur.js` | 4 | aquarelle-carnet, donnees-crayon, pictogrammes, plan-de-metro | hasard à graine, bruit, touches, lavis, mise en cache |
| `motifs.js` | 4 | lanterne-papier, papier-decoupe-collage, papier-decoupe-rouge, pois-infinis | rayures, pois, vichy, bois |
| `accessoires.js` | 3 | carnet-de-croquis, encre-hachures, isometrique-trait-fin | crayon, gomme, fiche, ruban, tampon, coche |
| `decors.js` | 3 | anime-cellulo-80, huile-couteau, tuyau-caoutchouc-1930 | plaques couleur + émissive, reflets mouillés |
| `feuille.js` | 3 | gravure-sur-bois, lanterne-papier, plan-bleu | transition du décollage |
| `formes.js` | 3 | comics-cosmique, papiers-decoupes-matisse, science-a-plat | la géométrie, dessinée deux fois |
| `grille.js` | 3 | jeu-tele-rythmique, pois-infinis, typo-suisse | `a(mesure, temps |
| `heros.js` | 3 | carnet-de-croquis, encre-hachures, pixel-8-bits |  |
| `interface.js` | 3 | keynote-sombre, pixel-rpg-16-bits, screencast-vivant | les composants |
| `iso.js` | 3 | infographie-isometrique, isometrique-trait-fin, livre-isometrique | projection, caméra, file d'attente triée par profondeur, primitives : boîte, prisme, cylindre, cône, toit, sphère, pl… |
| `monde.js` | 3 | infographie-isometrique, recit-dessine, science-a-plat | le lieu, plus grand que le plan le plus large |
| `police.js` | 3 | circuit-imprime, pixel-8-bits, pixel-rpg-16-bits |  |
| `post.js` | 3 | anime-cellulo-80, circuit-imprime, lanterne-papier | passe finale |
| `rig.js` | 3 | craie-grasse-album, ombres-chinoises, papier-decoupe-rouge | pièces qui s'occultent, membres en tubes |
| `traits.js` | 3 | carnet-de-croquis, collage-enquete, maths-animees | encre, graphite, tracé progressif, position de la pointe |
| `affichage.js` | 2 | hologramme-hud, micro-jeux | plaque, cadre de visée, trait de rappel, texte qui défile, carte, pastille, loupe, sous-titre |
| `contenu.json` | 2 | cartoon-annees-50, hologramme-hud | textes et couleurs du client |
| `craie.js` | 2 | craie-grasse-album, tableau-noir-craie | rubans effilés, hachures avec débord, texte |
| `decor.js` | 2 | neon-vaporwave, papier-decoupe-satirique | mur, soleil, montagnes, grille |
| `imprimer.glsl` | 2 | gravure-sur-bois, risographie | tirage ou bloc |
| `kit.js` | 2 | jeu-tele-rythmique, livre-isometrique | contour, ombre dure, motifs, éclat, verdict, bandeau, carton |
| `lavis.js` | 2 | croquis-urbain, gravure-cuivre | lavis, réserve, taches, feuillage |
| `lettrage.js` | 2 | carnet-de-croquis, comics-cosmique | lettre à lettre, surligneur, soulignement |
| `lumiere.js` | 2 | keynote-sombre, papier-decoupe-rouge | carte de lumière de nuit, pièces en contre-jour, halo, rayons, motif projeté |
| `mascotte.js` | 2 | dossier-trame, screencast-vivant | rig + visages |
| `mondes.js` | 2 | encre-hachures, sitcom-sf | feuille, bois, monde sombre, iris |
| `ombres.js` | 2 | comics-cosmique, trait-continu | croissant noir + hachures |
| `page.js` | 2 | carnet-de-croquis, comics-cosmique | page en cache, depuis un hasard à graine |
| `palette.js` | 2 | pixel-8-bits, science-a-plat | palettes, couleur la plus proche |
| `pellicule.js` | 2 | film-muet-1920, tuyau-caoutchouc-1930 | tirage + dégâts, avec masque de couleur facultatif |
| `personnages.js` | 2 | croquis-urbain, papier-decoupe-collage | squelette simple, poses |
| `portraits.js` | 2 | pixel-rpg-16-bits, pop-trame | grille à 4 jeux de couleurs |
| `poses.js` | 2 | bonshommes-trait-epais, illustration-plate | 4 poses par danse : points clés dans le repère de la figure, origine aux pieds |
| `sprites.js` | 2 | pixel-8-bits, pixel-rpg-16-bits | sprites depuis des tableaux de chaînes |
| `tableau.js` | 2 | tableau-blanc, tableau-blanc-a-la-main | encre en multiplication, texture sèche, effaceurs, reflet, accessoires |
| `texte.js` | 2 | dossier-trame, papier-decoupe-rouge | lettres séparées + chute |
| `toon.js` | 2 | cartoon-annees-50, sitcom-sf | forme dans le style, rubans d'encre, plans, texte à deux plaques, flèche de notice, ornements, décalage global |
| `trace.js` | 2 | plan-bleu, trait-continu | caméra, perspective cavalière, tracés progressifs, solides remplis de « papier », hachures, cotes, bulles, texte |
| `trame.js` | 2 | dossier-trame, pop-trame | cercles en un seul tracé, champs de densité |
| `affiche.js` | 1 | affiche-serigraphie | gabarit, passages partiels, plans flottants, talon de billet, choix d'encre par contraste |
| `ambiance.js` | 1 | science-a-plat | étoiles, particules à graine |
| `ampoules.js` | 1 | art-deco | texte → enseigne, ordre d'allumage |
| `arrivee.js` | 1 | croquis-urbain | champ : à quel instant la couleur atteint chaque point, depuis des sources |
| `art.js` | 1 | terminal-ascii | scènes en niveaux de gris dessinées en code pour le « négatif » |
| `banderole.js` | 1 | vitrail |  |
| `bulles.js` | 1 | pop-trame | bulle de pensée, cartouche, étoile éclatée |
| `burin.js` | 1 | gravure-cuivre | réserve de traits ordonnés + planification, hachure, gravure d'un champ de ton, hachure le long des contours, contour… |
| `cartons.js` | 1 | film-muet-1920 | intertitres, bordures, iris, salle |
| `cassette.js` | 1 | neon-vaporwave | passe finale |
| `cellulo.js` | 1 | anime-cellulo-80 | formes, ombrage automatique, rubans |
| `chronologie.js` | 1 | plan-de-metro | phases de tracé, caméra en fonction du temps, repères sonores |
| `ciseaux.js` | 1 | papiers-decoupes-matisse | contour → segments droits décalés |
| `ciseler.js` | 1 | ombres-chinoises | pièces, découpes, bibliothèque de motifs, texture de cuir, rivets |
| `compo.js` | 1 | vitrail | compositeur |
| `composants.js` | 1 | circuit-imprime | empreintes : pastilles, sérigraphie, zone d'isolement, chemins de conduction |
| `compose.glsl` | 1 | craie-grasse-album | cire, lavis, relief |
| `couleur.js` | 1 | carnet-de-croquis | aplat décalé, hachure dans une découpe, gribouillis |
| `couleurs.js` | 1 | maths-animees | le tableau grandeur → couleur |
| `coulisses.js` | 1 | ombres-chinoises | silhouettes à liseré chaud, flamme, fumée |
| `couteau.js` | 1 | huile-couteau | types de touches : couteau, brosse, tache, ligne ; lots statiques et touches mobiles |
| `cuivre.js` | 1 | gravure-cuivre | plaque, burin, copeau |
| `deco.js` | 1 | art-deco | dégradé d'or, trait signature, aérographe, motifs |
| `dessiner.js` | 1 | risographie | densités d'encre, surimpression, halo de réserve, membres |
| `distribution.js` | 1 | presentateur | qui, où, à quelle échelle, quelle pose, à quel instant |
| `donnees.json` | 1 | graphique-anime | valeurs **exactes** du client, unité, source, indication « réel » ou « exemple » |
| `eau.js` | 1 | estampe-japonaise |  |
| `ecriture.js` | 1 | croquis-urbain |  |
| `effets.js` | 1 | anime-cellulo-80 | pluie, lignes de vitesse, reflets |
| `encrer.js` | 1 | pop-trame | une seule fonction « cerne + aplat » |
| `energie.js` | 1 | comics-cosmique | bulles, flux |
| `enseigne.js` | 1 | neon-vaporwave | lettres en traits + clignotement à graine |
| `environnement.js` | 1 | illustration-plate | oscillations amorties |
| `epoques.js` | 1 | pixel-8-bits | résolution, palette et effets d'écran par époque |
| `etiquettes.js` | 1 | papier-decoupe-collage | année, légende, écriture progressive |
| `evenements.json` | 1 | jeu-tele-rythmique | exporté pour la musique et les bruitages |
| `faces.js` | 1 | isometrique-trait-fin | dessin et texte inscrits dans une face |
| `fenetre.js` | 1 | vitrail | lancettes, rose, bordures, mur |
| `feutre.js` | 1 | tableau-blanc | formes dessinées à la main : ligne, courbe, arc, cercle, rectangle, flèche, pointillés, hachures ; texte en ordre d'é… |
| `figures.js` | 1 | huile-couteau | marche, bras, accessoires en touches à graines fixes |
| `filtre.js` | 1 | gravure-sur-bois | image ou relief → tailles |
| `geo.js` | 1 | circuit-imprime | routage à 0°, 45°, 90° par des points de passage, longueur d'arc, sous-chemin |
| `grain.js` | 1 | tableau-noir-craie | tuile de grain, dépôt |
| `graphique.js` | 1 | graphique-anime | échelle linéaire et son inverse, graduations en 1, 2, 2,5 ou 5 × 10ⁿ, grille, barres, courbe, chandeliers, annotation… |
| `histoire.js` | 1 | recit-dessine | minutage des poses par phrase |
| `holo.js` | 1 | hologramme-hud | projection, scan, vue éclatée, faces, lueur, socle |
| `horloge.js` | 1 | presentateur | la source de temps unique : voix, sous-titres, année affichée |
| `icones.js` | 1 | cartoon-annees-50 |  |
| `impression.js` | 1 | estampe-japonaise | papier, veines, frottoir, mouchetis, blocs, dégradé essuyé, traits gravés, masques d'impression, cartouche, sceaux : … |
| `incrustation.js` | 1 | neon-vaporwave |  |
| `infographie.js` | 1 | infographie-isometrique | épingle, médaillon, ligne de coupe, hachures, anneau, grille d'icônes, personnage |
| `inscriptions.js` | 1 | lavis-encre |  |
| `jeu.js` | 1 | illustration-plate | minutage image par image |
| `legende.js` | 1 | dossier-trame |  |
| `lettres.js` | 1 | generique-espion-60 | contours des glyphes re-découpés |
| `levres.js` | 1 | sitcom-sf | enveloppes de la voix |
| `lieu.js` | 1 | livre-isometrique | sol, marquages, bâtiments en coupe |
| `lumiere.glsl` | 1 | ombres-chinoises | lampes × transmission × toile, vue miroir, halo, fondu chaud |
| `materiaux.js` | 1 | collage-enquete | trame, bord déchiré, adhésif, bande d'étiquette, fiche |
| `maths.js` | 1 | maths-animees | mise en page des formules par jetons, écriture, transformation par identifiant de terme |
| `matieres.js` | 1 | micro-jeux | shaders |
| `miroirs.js` | 1 | pois-infinis | projection en perspective |
| `modele.json` | 1 | hologramme-hud | pièces : arêtes, axe de montage, pièces internes, points d'ancrage ; normalisé au chargement pour que les caméras mar… |
| `nature.js` | 1 | estampe-japonaise |  |
| `neon.js` | 1 | neon-vaporwave | tube lumineux |
| `niveaux.js` | 1 | circuit-imprime | cartes emboîtées |
| `onde.js` | 1 | pois-infinis |  |
| `page.glsl` | 1 | croquis-urbain |  |
| `page.html` | 1 | dossier-trame | scènes à fenêtres de temps |
| `palettes.js` | 1 | anime-cellulo-80 | modèles de couleurs |
| `pantins.js` | 1 | generique-espion-60 | silhouettes articulées, poses, cycles |
| `papier.glsl` | 1 | lavis-encre | papier, diffusion, bord, fleur |
| `paysage.js` | 1 | lavis-encre | montagnes, textures de roche, pins, roseaux, ronds |
| `peindre.js` | 1 | encre-hachures | aplat + textures découpées + contour |
| `perso.js` | 1 | papier-decoupe-satirique | pièces, pivots, états d'expression |
| `personnage.js` | 1 | recit-dessine | poses, expressions, bouches, clignements |
| `pinceau.js` | 1 | lavis-encre | coups, poils, coups chargés, masses, taches |
| `pixel.js` | 1 | pixel-8-bits | primitives : point, rectangle, ligne de Bresenham, ellipse, polygone, tramage, halo tramé |
| `planche.js` | 1 | gravure-cuivre | feuille, texte gravé, écriture, cadre de médaillon |
| `plans.js` | 1 | lanterne-papier | chaque plan : construction, mise à jour, étalonnage |
| `plaque.js` | 1 | huile-couteau | illustration de référence → touches du grossier au fin, confinées par groupe de formes |
| `plateau.js` | 1 | micro-jeux |  |
| `pli.js` | 1 | papier-decoupe-rouge | plier, couper, déplier |
| `plume.js` | 1 | croquis-urbain | trait avec tremblé, dépassement, manques, tracé progressif ; enregistre **l'instant de dessin de chaque pixel** |
| `pont.js` | 1 | papier-decoupe-collage | métamorphose de forme dans une fenêtre déchirée |
| `px.js` | 1 | pixel-rpg-16-bits | image indexée, palettes et tables de chaque profondeur, tramage, mosaïque |
| `rayons.js` | 1 | bonshommes-trait-epais |  |
| `redessin.js` | 1 | film-muet-1920 | passe d'encrage |
| `rendu.js` | 1 | circuit-imprime | dessine une carte pour une caméra `{x, y, zoom, rotation}` |
| `reperes.js` | 1 | maths-animees | axes, quadrillage, courbe, lignes de rappel |
| `reseau.js` | 1 | plan-de-metro | stations : position en G, nom, niveau ; lignes : liste de stations, couleur, mode ; eau ; liaisons à pied |
| `ressort.js` | 1 | isometrique-trait-fin |  |
| `rosace.js` | 1 | papier-decoupe-rouge | un secteur × 8 |
| `salle.js` | 1 | tableau-noir-craie | ardoises, cadre, rigole, horloge, mur, lignes peintes |
| `sceau.js` | 1 | lavis-encre |  |
| `scene-*.html` | 1 | typo-suisse | une règle par scène |
| `sculpts.js` | 1 | gravure-sur-bois | petits reliefs pour les gros plans |
| `soie.js` | 1 | affiche-serigraphie |  |
| `sous-titres.js` | 1 | trait-continu |  |
| `sujets.js` | 1 | aquarelle-carnet | générateurs de plantes et d'objets en coordonnées locales, racine en 0,0 |
| `table.js` | 1 | collage-enquete | position de chaque document dans le monde |
| `tailler.js` | 1 | gravure-sur-bois | forme taillée avec halo et hachures qui suivent la forme, trait le long d'un tracé, hachures de zone, coups de pointe… |
| `tampon.js` | 1 | dossier-trame |  |
| `tempo.js` | 1 | bonshommes-trait-epais |  |
| `term.js` | 1 | terminal-ascii | atlas de caractères, dessin de la grille, échelles de densité, image → cellules |
| `tete.js` | 1 | anime-cellulo-80 | tête 3 vues × expressions |
| `tetes.js` | 1 | film-muet-1920 |  |
| `textures.js` | 1 | encre-hachures | hachure, croisée, crayon, pointillé, grain |
| `timeline.json` | 1 | info-sous-titres |  |
| `titres.js` | 1 | art-deco | barre de titre, chiffres, cadran, horloge, plaque de sous-titre |
| `traceur.js` | 1 | maths-animees | point, valeur affichée |
| `trames.js` | 1 | comics-cosmique | motifs de points |
| `tube.js` | 1 | terminal-ascii | traitement cathodique |
| `verre.js` | 1 | vitrail | pièces, textures, plomb, grisaille, losanges |
| `voix.json` | 1 | recit-dessine | volume de la voix image par image, calculé hors ligne |
| `vol.js` | 1 | keynote-sombre | trajectoires courbes, destinations typées |
| `volets.js` | 1 | dossier-trame |  |
| `vues.js` | 1 | estampe-japonaise | chaque estampe en blocs mis en cache + ce qui se peint à chaque image |

## 4. Scripts des dépôts d'origine

Les fichiers `prep.py`, `render.py`, `music.py`, `voice.py`, `paper.py`, `foley_lib.py`, `claylib.py` et les `demo/*.js` n'apparaissent que dans les sections 9 et 10 des fiches (aperçu, origine), comme références de source avec leur commit. Ils ne sont pas dans le plugin et ne doivent pas être lancés ; aucune recette de la section 6 ne s'appuie sur eux.

## 5. Refaire ce relevé

Le script de relevé est dans le dossier des essais (`_corrections-fiches/scripts_cites.py` et `doc_manquant.py`) ; il n'est pas livré dans le plugin. Règle appliquée : tout nom de fichier entre accents graves dans la section 6, hors blocs de code, dont le nom n'existe nulle part sous `skills/` (les copies de tiers `references/officiel/`, `references/motion-prompt/`, `scripts/sfx/` et `banque-cc0/` ne comptent pas).
