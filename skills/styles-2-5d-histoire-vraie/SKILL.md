---
name: styles-2-5d-histoire-vraie
description: "Catégorie de styles 2.5D : des personnages plats dans des décors 3D éclairés, pour raconter une histoire vraie en vertical (histoire, science, objets étonnants). À utiliser quand le client veut une vidéo racontée avec un personnage dessiné dans un décor en relief, ou cite le format « bonhomme à tête ronde dans un décor de cinéma »."
---

# Styles 2.5D « histoire vraie »

## À quoi sert la catégorie

Raconter **une histoire vraie** en 55 à 70 secondes, avec une seule voix, en mélangeant deux mondes :

- des **personnages volontairement simples**, plats, sans ombrage ;
- des **décors volontairement riches**, en 3D, éclairés comme par une équipe de tournage.

C'est ce contraste qui fait la signature. Le spectateur repart avec un fait qu'il peut répéter à table ; l'animation est le moyen, pas le sujet.

Pourquoi le format ne ressemble pas à de l'animation générée :

1. Les personnages sont simples exprès : personne n'attend de réalisme, rien ne paraît étrange.
2. Les décors sont riches exprès : lumière chaude, vraies matières, profondeur.
3. Chaque plan a une raison : il arrive sur une idée nouvelle du texte, pas sur un minuteur.
4. Une seule voix humaine.
5. Une histoire vraie : les faits se vérifient.

Chaque étape de production protège l'un de ces cinq points.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `histoire-vraie-tete-ronde` | Histoire vraie à tête ronde | Bonshommes plats à tête ronde et gros contour dans des salles 3D éclairées à la bougie et à la fenêtre ; un plan toutes les 2 s. | blender | élevée | pas d'aperçu tiers (à produire) |
| `theatre-de-papier` | Théâtre de papier | Figurines de carton imprimé à marge blanche sur des décors en plans parallèles, éclairées par une rampe de bougies qui projette leurs ombres. | blender | moyenne | extrait d'un film LemoLab (lien seulement) |

Fiches : `styles/<identifiant>/STYLE.md`.

**Voir aussi (fiches portées par une autre catégorie)** : deux autres styles 2.5D à personnages plats servent à cette catégorie. Une seule fiche par style dans tout le plugin : elles ne sont pas dupliquées ici. Pour une histoire vraie dans l'un de ces styles, suivre `references/pipeline.md` de cette catégorie avec la fiche de l'autre.

- `diorama-pixel` (petits personnages en pixel art debout comme des découpes dans une maquette 3D embrumée, vue de haut, netteté en bande) : `styles-jeu-retro/styles/diorama-pixel/STYLE.md`.
- `livre-pop-up` (un vrai livre animé filmé sur un bureau : chaque page qui se dresse est un chapitre, on tourne la page au lieu de couper ; moteur blender, difficulté élevée) : `styles-matieres-3d/styles/livre-pop-up/STYLE.md`. Lire son encadré « Variante histoire vraie » (section 5) : mouvement continu, jeu sobre, sous-titres de 1 à 2 mots. Dans ce style, **le carton reçoit la lumière** et porte son ombre : c'est une exception à la règle « personnages émissifs ».

## Comment choisir

| Le client veut… | Style |
|---|---|
| Une histoire vraie racontée vite, au ton de documentaire malin, format « le saviez-vous » | `histoire-vraie-tete-ronde` |
| Un récit d'aventure, un voyage, une ambiance de jeu vidéo ou de conte | `diorama-pixel` (catégorie `styles-jeu-retro`) |
| Une histoire ancienne, un fait divers d'époque, du théâtre, de l'humour pince-sans-rire | `theatre-de-papier` |
| Une vie ou une histoire en chapitres, un ton tendre ou familial | `livre-pop-up` (catégorie `styles-matieres-3d`) |
| Aucune préférence | `histoire-vraie-tete-ronde` (le plus direct, le mieux documenté) |

Difficulté : `theatre-de-papier` est le plus simple (tout est plat, la lumière vient d'un seul endroit) ; commencer par lui avec un client qui découvre Blender.

Un seul style par vidéo. Une série garde le même style d'un épisode à l'autre.

## Ce qui est commun aux styles de la catégorie

- **Format** : vertical 1080×1920, 30 i/s, rendu à la taille exacte.
- **Personnages plats, décor en relief.** Le personnage ne reçoit jamais un ombrage réaliste (sauf règle propre au style, notée dans sa fiche).
- **Ombre de contact** sous chaque personnage.
- **Objet héros en vrai 3D** : ce dont parle l'histoire n'est jamais un dessin plat.
- **Caméra lente et motivée** : avancée ou travelling avec une raison ; pas de dérive, pas de rotation permanente.
- **Histoire vraie** : chaque affirmation du texte et chaque chiffre à l'écran a sa source.
- **Sous-titres** : 1 à 2 mots à la fois.
- **Jamais** les personnages, les dessins, le texte ou la structure d'une autre chaîne. On étudie la grammaire d'un format, on ne copie pas son contenu.

## Mise en garde : vos sujets, votre dessin

À dire au client dès la première conversation, et à tenir ensuite.

- **Choisir ses propres sujets.** Une histoire déjà racontée par une chaîne du même format n'est pas un sujet : en trouver une autre, avec ses propres sources.
- **Dessiner un personnage original.** Forme de tête, yeux, costume, couleur d'accent : assez différent de tout personnage de chaîne existant pour qu'on ne les confonde pas sur une vignette. Le skill `personnages` et la fiche « ma chaîne » (skill `marque`) servent à ça.
- **Ne jamais reprendre le dessin, les sujets ou la grammaire reconnaissable d'une chaîne existante.** Personnages plats dans un décor éclairé : c'est une technique, libre. Le bonhomme d'une chaîne, ses sujets, son ton, sa façon de cadrer et de sous-titrer, pris ensemble : c'est son identité. Si un spectateur peut croire à un épisode de cette chaîne, c'est trop près.
- Si le client demande « la même chose que telle chaîne », l'agent propose le format et refuse la copie : on analyse la référence comme un format (`references/pipeline.md`, « Analyser une référence »), puis on prend cinq décisions pour un épisode original.
- Le personnage d'exemple du kit, « Galet », est lui aussi à remplacer : une chaîne qui le garderait ressemblerait à toutes celles qui ont pris le kit.

Pourquoi cette insistance : le film d'essai du studio (11/11/2026), qui a servi à écrire le kit, suivait de près le sujet et la grammaire d'une chaîne existante. C'était un choix pour un essai interne ; il n'a pas été publié, il n'est pas fourni, et son compte rendu conclut lui-même qu'une version vendable doit choisir ses propres sujets et un dessin qui s'en distingue.

## Le kit de départ

`kit/` contient des outils prêts à copier dans le dossier d'un épisode (lire `kit/LISEZMOI.md`) : liste de plans en données lue par Blender, bibliothèque de construction (plans émissifs, ombre de contact, lumière motivée, une caméra par plan, clés tenues), boucle de rendu qui reprend après un plantage, re-rendu par plages d'images, planches de revue avec vérification, mixage, assemblage HyperFrames avec sous-titres au mot. Un épisode devient : **un script, une liste de plans, un décor ou deux, un objet héros**.

Tout est en Python (Windows, macOS, Linux). Un exemple neutre de 2 plans tourne tel quel ; ce qui a été essayé et ce qui ne l'a pas été est dit dans `references/pipeline.md`, « Ce qui a été essayé pour de vrai ».

## Ce qui n'est pas encore au niveau

Dit sans détour, d'après le film complet fabriqué par le studio le 11/11/2026 (61,5 s, 36 plans). Le format tient ; ces quatre points le séparent encore d'une vidéo qu'on publierait sans réserve. À dire au client avant de commencer.

| Point faible | Ce qu'on a constaté | Ce qu'on fait en attendant |
|---|---|---|
| **Objet héros complexe à modeler** | Les formes tournées et les boîtes sortent bien (le corps de l'objet : correct). Les formes organiques non (des têtes d'animal sculptées, lisibles de profil mais prises pour un autre animal de face). Écrire de la sculpture en code atteint vite sa limite. | Choisir une histoire dont l'objet est fait de formes simples ; ou prévoir 30 minutes de modelage à la main dans Blender ; ou, avec l'accord du client (cela peut coûter un crédit), un générateur 3D du connecteur. Toujours la planche 6 angles, et un axe de caméra qui montre l'objet sous son meilleur profil. |
| **Décors procéduraux, sans textures réelles** | Les bibliothèques (Poly Haven) étaient désactivées dans le connecteur : aucune texture réelle, aucun HDRI, tout en matières calculées. Le résultat est propre mais pauvre : deux couches de crêtes au lieu de cinq ou six pour un lointain, aplats sombres qui trament en pleine taille. | Activer Poly Haven dans le connecteur avant de commencer (skill `blender`), importer textures et HDRI ; soigner la passe 3. Une bibliothèque de décors réutilisables reste à construire : c'est le plus gros gain de qualité attendu. |
| **Voix de synthèse** | La voix de l'essai est une voix de synthèse provisoire : très régulière (plage dynamique de 2,2 LU), et ses repères de mots étaient décalés de 107 ms par rapport au son. Le format repose sur « une seule voix humaine ». | Faire enregistrer le texte par le client, puis l'aligner au mot. Si synthèse malgré tout : une voix dont il a les droits, le contrôle de l'écart (`outils/ecart_voix.py`), et le dire dans la note de livraison. |
| **Temps de rendu sur carte graphique intégrée** | 7,5 s par image avec les réglages par défaut, 3,6 s après allègement : 1 h 50 pour le film, une dizaine de plantages du pilote (repris automatiquement), pas de rendu en parallèle possible, 10 à 20 minutes par tour de correction. | Profiler avant de lancer, la boucle de reprise du kit, re-rendre par plages. Une carte dédiée changerait l'échelle (estimation, non mesurée : cinq à dix fois plus rapide). Skill `blender`, `references/rendu-long-et-fiable.md`. |

Autres limites, traitées ailleurs : le pantin n'a qu'une vue de face (skill `personnages`, `references/limites-du-pantin.md`) ; aucun enregistrement libre de certains instruments d'époque (règle des instruments virtuels, `references/pipeline.md`, étape 7) ; les temps réels par étape (`references/pipeline.md`, « Temps réels mesurés »).

## Parcours de production

Le déroulé complet est dans `references/pipeline.md` :

1. proposer 5 histoires vraies avec leurs sources, le client choisit ;
2. texte de 150 à 170 mots et `sources.md`, validation ;
3. liste de plans : un plan par idée, 3 à 5 décors ;
4. temps clés en numéros d'image ;
5. décors en 3 passes, objet héros, personnages, ligne de jeu ;
6. voix, temps mot à mot, sous-titres ;
7. son ;
8. assemblage ;
9. revue : planche contact, test téléphone, images pleine taille vérifiées, critique en 9 questions, 3 corrections par tour, chacune en 4 champs.

Le parcours contient les règles tirées du rendu réel du 11/11/2026 : bande des sous-titres (y = 1385 à 1515), sujet dans les 65 % du haut, 1 à 2 bruitages par 10 s, instruments virtuels, objet héros sans double, contrôle de la voix de synthèse, vérification fait par fait, temps réels mesurés.

## Skills à charger avec cette catégorie

- `studio-coeur` **pilote le parcours** (questions au client, validations, porte de livraison, relecteur indépendant). Cette catégorie lui fournit le contenu de chaque étape.
- `blender` : connecteur, décors en 3 passes, objet héros, rendu, export.
- `personnages` : pièces SVG, planche d'expressions, montage en plans, jeu d'acteur.
- `principes-mouvement` : dictionnaire des mouvements (les fiches citent leurs numéros), règles chiffrées.
- `rendu` : assemblage HyperFrames, sous-titres, export.
- `son` : voix, bruitages, musique, −14 LUFS.
- `marque` : la fiche « ma chaîne » du client (personnage récurrent, palette, ton).

## Références

- `references/pipeline.md` : le parcours complet, avec les gabarits de fichiers, les règles du rendu réel et les temps mesurés.
- `kit/LISEZMOI.md` : le kit de départ (ordre des étapes, rôle de chaque fichier, ce qu'on change pour un nouvel épisode).
- `styles/histoire-vraie-tete-ronde/STYLE.md`
- `styles/theatre-de-papier/STYLE.md`
- Fiches voisines : `styles-jeu-retro/styles/diorama-pixel/STYLE.md`, `styles-matieres-3d/styles/livre-pop-up/STYLE.md`

Crédits : voir `licenses/styles-2-5d-histoire-vraie.md` à la racine du plugin.
