---
name: styles-cinema
description: "Catégorie de styles « Cinéma » du studio motion (film muet des années 1920, found footage liminal au caméscope) et bibliothèque de 98 looks rapides inspirés de l'histoire du cinéma et des arts graphiques. À utiliser quand le client veut une vidéo « comme un vieux film », « comme une cassette retrouvée », ou demande un look précis d'époque sans passer par un style complet."
---

# Styles Cinéma (catégorie 8)

Deux styles complets où **le support raconte** (la pellicule projetée, la cassette de caméscope), et une réserve de 98 looks courts pour aller vite.

Le skill `studio-coeur` pilote le parcours. `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, export) et `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) s'appliquent. Les deux styles d'ici ont une règle sonore à part, écrite dans leur fiche : le film muet n'a **aucun** bruitage (un instrument joue tout), le found footage n'a **aucune** musique.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `film-muet-1920` | Film muet des années 1920 | Dessin à l'encre et lavis d'argent projeté en salle : image 4:3 qui scintille, cartons à la place des voix, un pianiste | hyperframes (canvas + passe WebGL) ; personnages 2.5D, Blender possible | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/silent-film.mp4) (LemoLab, CC BY 4.0) |
| `found-footage-liminal` | Found footage liminal | Cassette de caméscope retrouvée dans des espaces vides sans fin sous néons ; des règles au lieu de monstres | blender (qualité) ou three (léger) + hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/backrooms.mp4) (LemoLab, CC BY 4.0) |

Et : **`references/98-looks.md`**, 98 prompts de style courts (look en une ligne + prompt), classés en 8 familles.

## Comment choisir

- **Un gag visuel, une réaction en chaîne, une histoire sans paroles, une archive d'entreprise à rhabiller** : `film-muet-1920`.
- **Un malaise doux, un lieu vide, des consignes qui dérapent, un « tape retrouvée »** : `found-footage-liminal`. À réserver aux comptes qui assument un ton inquiétant ; jamais pour une marque rassurante.
- **Le client cite une époque, une technique ou « un film dans ce genre »** et le délai est court : cherche dans `references/98-looks.md`. Repères :
  - noir et blanc d'époque : looks 01, 05, 09, 16, 21, 26, 66, 84, 86 ;
  - affiches et estampes : 02, 11, 15, 22, 25, 31, 43, 54 ;
  - peinture : 12, 14, 39, 45, 48, 51, 53, 62, 65, 89, 93 ;
  - dessin et gravure : 03, 08, 10, 13, 20, 23, 36, 50, 59, 64, 82 ;
  - objets et supports (album, carte postale, livre, écran) : 19, 28, 41, 56, 67, 69, 86, 88, 91, 94 ;
  - grands espaces 3D : 32, 38, 49, 58, 70, 80, 90, 96, 98 ;
  - nuit et néon : 40, 75, 78, 97.
- Un look rapide n'a ni moteur ni liste de contrôle : pour une vidéo importante, ou si le look plaît et doit resservir, monte-le en style complet avec le client (voir « mon style » dans `studio-coeur`).

## Règles communes à la catégorie

1. **La grammaire, jamais l'œuvre.** Aucun titre de film, nom de réalisateur, d'acteur, de studio, de personnage ou de récompense dans la vidéo, sa description ou ses mots-clés. On ne rejoue pas un gag, un plan ou une mélodie existants. Les mots de folklore d'Internet associés au genre « liminal » (nom du lieu, numéros de « niveaux », noms d'entités) sont eux aussi proscrits : tout ce qui apparaît à l'écran est original.
2. **Le support a ses défauts, et pas ceux d'un autre.** Pellicule : scintillement, flottement, rayures, poussières, brûlures. Cassette : bavure de couleur, bande de commutation, déchirure de suivi, bruit dans les sombres. On ne met jamais de rayures sur une cassette ni de lignes vidéo sur une pellicule.
3. **Les défauts changent à chaque image, le jeu non.** Le dessin ou la caméra peuvent être échantillonnés bas (16 poses par seconde pour le muet) ; les défauts du support tournent à la cadence de sortie.
4. **L'image dans l'image.** Les deux styles sont en 4:3 d'origine. En 9:16, on ne recadre pas : on garde une fenêtre et on **habille le reste avec le lieu de projection** (la salle, le téléviseur, l'écran du caméscope). Chaque fiche donne sa mise en page.
5. **Le texte fait partie du monde** : cartons peints, sous-titres codés de télévision, affichettes punaisées. Pas de sous-titres modernes posés par-dessus, sauf demande du client.
6. **Zone sûre 9:16** : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945.
7. **Le grain lourd coûte cher à l'encodage** : vérifie le poids du fichier ; ajoute le grain à l'encodage plutôt que dans la page quand c'est possible.

## Pour produire

1. Lis la fiche `styles/<identifiant>/STYLE.md`, ou le look choisi dans `references/98-looks.md`.
2. L'histoire vient du sujet du client, jamais de la démo d'origine (au moins 4 différences sur 6 : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin).
3. Rends une image de style 1080×1920 **à travers toute la chaîne** (dessin + passe du support) et fais-la valider avant d'animer. Pour `found-footage-liminal` et pour les looks rapides marqués `3D`, ouvre le skill `blender` (connexion au connecteur MCP, rendu vertical, envoi vers HyperFrames).
4. Liste de contrôle de la fiche, puis porte de livraison de `studio-coeur`. Pour un look rapide : applique au moins les contrôles communs et fais relire par un regard neuf.

## Crédits

Sources, commits et licences : `licenses/styles-cinema.md` à la racine du plugin.
