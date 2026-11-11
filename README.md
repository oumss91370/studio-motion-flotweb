# studio-motion-flotweb

Version 0.1.0 · plugin pour Claude Code et Claude Desktop · par Flot Web

## Ce que fait le plugin

Ce plugin transforme votre assistant en studio de motion design : vous décrivez un sujet, il vous pose quelques questions à choix, puis il fabrique une vidéo verticale entièrement en code.
Il s'appuie sur un socle de 8 skills (l'installation, le parcours, la marque, le mouvement, le rendu, le son, la 3D, les personnages) et sur 13 catégories de styles prêtes à l'emploi.
Chaque vidéo passe par trois validations de votre part et par des contrôles mesurés avant d'être livrée.

## Ce qu'il vous faut

| Élément | Pour quoi faire | Obligatoire ? |
|---|---|---|
| Claude Code ou Claude Desktop | faire tourner le plugin | oui |
| Node.js 22 ou plus | la commande `hyperframes`, qui rend les vidéos | oui |
| FFmpeg et FFprobe (version 6 ou plus) | encodage, son, contrôle du fichier final | oui |
| Python 3 (3.9 ou plus) avec `numpy` | scripts de contrôle du studio | oui pour les contrôles |
| Blender 4.2 ou plus, et son connecteur `blender` | styles en 3D et en 2.5D | seulement pour ces styles |

Vous n'avez pas à tout installer seul. Demandez à l'assistant « installe ce qu'il faut pour le studio » : il suit ces deux guides, une commande à la fois, avec votre accord.

- Rendu (Node.js, FFmpeg, HyperFrames, sur Windows, macOS et Linux) : `skills/rendu/references/installation.md`
- 3D (Blender, l'outil `uv`, le connecteur) : `skills/blender/references/installation.md`

Aucun compte n'est nécessaire pour créer et rendre une vidéo sur votre machine.

## Installer le plugin dans Claude Code

Il faut Claude Code et `git` installé sur votre machine. Le dépôt est public pendant la phase de test : aucun compte n'est nécessaire.

Dans Claude Code, tapez ces deux commandes l'une après l'autre :

```
/plugin marketplace add oumss91370/studio-motion-flotweb
/plugin install studio-motion-flotweb@flotweb
```

Puis redémarrez Claude Code. Les mêmes commandes depuis un terminal :

```
claude plugin marketplace add oumss91370/studio-motion-flotweb
claude plugin install studio-motion-flotweb@flotweb
```

Pour vérifier : tapez `/plugin` dans Claude Code, le plugin `studio-motion-flotweb` doit apparaître comme installé. Ensuite, dites simplement : « vérifie l'installation du studio », puis « fais-moi une vidéo ».

Mettre à jour plus tard : `/plugin marketplace update flotweb`, puis redémarrez. Désinstaller : `/plugin uninstall studio-motion-flotweb@flotweb`.

Sans GitHub : décompressez l'archive du plugin dans un dossier, puis `/plugin marketplace add <chemin du dossier>` et `/plugin install studio-motion-flotweb@flotweb`.

## Première utilisation

À la première utilisation, le plugin vérifie votre machine et vous propose d'installer ce qui manque (skill `installation`) : Node, FFmpeg, HyperFrames et Python pour toutes les vidéos ; Blender et son connecteur pour les styles 3D et 2.5D. Rien n'est installé sans votre accord. Vous pouvez relancer la vérification à tout moment en demandant « vérifie l'installation du studio ».

## Le parcours type d'une vidéo

Le skill `studio-coeur` conduit tout. Dites simplement « fais-moi une vidéo sur… ».

1. **Votre fiche « ma chaîne ».** L'assistant la lit (niche, public, ton, couleurs, typographie, personnages). Si elle n'existe pas, il la construit avec vous, une question à la fois.
2. **Les questions.** Quatre au plus, à choix. Il vous propose 4 ou 5 thèmes tirés de votre niche (ou 4 ou 5 histoires), vous choisissez ; puis le public, le format, le style.
3. **L'histoire.** Il propose trois structures, en recommande une, écrit le script et note la source de chaque fait. **Validation n° 1.**
4. **Le look.** Il fabrique 3 ou 4 images de votre histoire avec le vrai code de la vidéo. Vous critiquez chaque image, il refait ce qui ne va pas, et on recommence jusqu'à ce que ça vous aille. **Validation n° 2.** Aucune vidéo n'est lancée avant.
5. **Le storyboard.** Une image par plan, sur une planche numérotée. Vous dites oui ou non case par case. **Validation n° 3.** Rien n'est animé avant.
6. **La construction.** Animation des cases validées, puis le son sur la même ligne de temps.
7. **La revue.** Contrôles automatiques (mouvement, écran vide, zones sûres, temps de lecture), planches d'images regardées, visionnage avec le son, puis un relecteur indépendant qui note sept critères sur 10. Il faut 8 ou plus partout. Trois corrections par tour, trois tours au plus.
8. **La livraison.** La vidéo, les chiffres de la revue, le plan le plus faible et pourquoi, ce qui n'a pas pu être vérifié, et la liste des éléments tiers avec leur licence.

Vos retours ouvrent un nouveau tour : l'assistant ne change que ce que vous demandez.

## Les 8 skills du socle

| Skill | À quoi il sert |
|---|---|
| `installation` | Première utilisation : vérifie la machine, installe ce qui manque avec votre accord, fait un essai réel |
| `studio-coeur` | Chef d'orchestre : questions, histoire, look, storyboard, construction, revue, livraison |
| `marque` | Votre fiche « ma chaîne » : niche, public, ton, palette, typographie, personnages |
| `principes-mouvement` | Dictionnaire de 192 mouvements numérotés, principes d'animation, règles chiffrées, caméra |
| `rendu` | HyperFrames (HTML + GSAP rendu en MP4) : installation, commandes, sous-titres, exports |
| `son` | Bruitages, ambiance, musique, mixage, niveau final, écoute mesurée |
| `blender` | Décors et objets en 3D, pilotés par le connecteur `blender` |
| `personnages` | Personnages 2D en pièces, planches d'expressions, jeu d'acteur |

## Les 13 catégories de styles

Nombre de fiches de style (`STYLE.md`) présentes dans le plugin, comptées sur disque le 11/11/2026 : 130 au total.

| N° | Catégorie | Skill | Fiches |
|---|---|---|---|
| 1 | Peinture et dessin | `styles-peinture-dessin` | 20 |
| 2 | Encre et Asie | `styles-encre-asie` | 8 |
| 3 | Papier et impression | `styles-papier-impression` | 9 |
| 4 | Graphique et typo | `styles-graphique-typo` | 15 |
| 5 | Explicatif et infographie | `styles-explicatif-infographie` | 17 |
| 6 | Cartoon | `styles-cartoon` | 6 |
| 7 | Jeu vidéo et rétro | `styles-jeu-retro` | 7 |
| 8 | Cinéma | `styles-cinema` | 2 |
| 9 | Matières et 3D | `styles-matieres-3d` | 10 |
| 10 | Montage et documentaire | `styles-montage-documentaire` | 20 |
| 11 | Lancement de produit et SaaS | `styles-lancement-produit` | 9 |
| 12 | Formats Flot Web | `formats-flotweb` | 5 |
| 13 | 2.5D « histoire vraie » | `styles-2-5d-histoire-vraie` | 2 (plus 2 fiches partagées avec d'autres catégories) |

En plus des fiches : la catégorie Cinéma contient une bibliothèque de 98 looks rapides, et la catégorie Explicatif un recueil de 16 effets. Une fiche, `livre-pop-up`, existe pour l'instant dans deux catégories (9 et 13).

Chaque fiche décrit le style de la même façon : identité, palette et typographie, composition verticale, ce qui bouge, rythme, recette technique, son, liste de contrôle, aperçu, origine.

## Les règles du studio

1. Format par défaut : vertical 9:16, 1080×1920, 30 images par seconde.
2. Rien d'important dans les zones d'interface des applications : 160 px en haut, 360 px en bas, 135 px à droite.
3. Moteur : HyperFrames pour la 2D et l'assemblage, Blender pour la 3D et la 2.5D, Three.js pour le léger. Jamais Remotion.
4. Son final à −14 LUFS, mesuré sur le fichier livré.
5. De vrais enregistrements d'abord, environ 5 bruitages par 10 secondes ; la synthèse seulement en repli.
6. Aucune animation avant que vous ayez validé le storyboard.
7. Le style est figé, l'histoire est libre : un seul style et une seule palette par vidéo, et jamais une copie de la démo du style.
8. Chaque chiffre et chaque fait à l'écran a une source notée.
9. « Fini » veut dire mesuré, regardé et relu par un relecteur indépendant, qui n'a pas fabriqué la vidéo.
10. Rien de protégé : pas de personnage, de logo, de marque ou de musique qui ne vous appartient pas. « Style Ghibli » ou « style Pixar » sont des inspirations, jamais une affiliation.

## État du plugin

Soyons francs : c'est une version 0.2.0, pas encore une version de vente.

- Les 8 skills du socle et les 130 fiches de style sont **écrits** et relus entre eux.
- **12 styles sur 130 ont été vérifiés par un rendu réel** (un par catégorie, HyperFrames 0.9.33, le 11/11/2026) ; leur fiche le dit en section 10. Les 118 autres sont écrits d'après leurs sources, avec des mises en page verticales adaptées de sources souvent pensées en 16:9 : attendez-vous à des ajustements.
- Les contrôles de livraison, le réglage du niveau sonore et le rendu ont été corrigés d'après ces 12 rendus et essayés sur de vrais fichiers. Aucun film n'a encore été refait de bout en bout avec la version corrigée.
- **Aucun style Blender n'a été rendu à travers le plugin.** Le format 2.5D a fait l'objet d'un prototype réel ; son kit de départ n'a tourné que sur un exemple réduit, et ses personnages sont en cours de refonte.
- Beaucoup de fiches décrivent un moteur de dessin (trame, trait, papier, pixel…) que l'assistant écrit lui-même d'après la fiche : ce code n'est pas fourni. La liste est dans `docs/code-de-depart-manquant.md`.
- Les outils du connecteur Flot Studio cités dans le paramétrage ne sont pas encore livrés. En attendant, votre fiche « ma chaîne » est un fichier dans votre dossier.
- Il n'y a pas encore de galerie d'aperçus.
- La licence du plugin n'est pas décidée (voir `LICENSE`, provisoire).

Dites à l'assistant ce qui ne va pas sur vos premières vidéos : il corrige et le note.

## Crédits et licences

Ce plugin reprend et adapte le travail de nombreux auteurs (HyperFrames, des skills et des bibliothèques de styles sous licence libre, une banque de sons du domaine public). La liste complète, avec auteurs, dépôts, versions, licences et ce qui est repris, est dans le fichier `NOTICE`. Le détail par skill est dans `licenses/`, et les textes des licences dans `licenses/textes/`.

Les marques citées appartiennent à leurs propriétaires. Ce plugin n'est pas un produit officiel de HeyGen, de la fondation Blender ni d'aucun auteur cité, et n'y est pas affilié.
