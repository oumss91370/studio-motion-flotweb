# Sources libres : où chercher, quelles licences, comment créditer

Une vidéo publiée est un usage commercial (monétisation, vente, promotion), c'est une œuvre modifiée (le son est coupé, superposé, calé) et elle passe par des plateformes qui analysent le son. Chaque fichier doit donc autoriser les trois, et la preuve est **la page du fichier lui-même**, lue le jour du téléchargement.

## Ordre de recherche

1. **La banque CC0 fournie** : `banque-cc0/` (109 sons, index dans `banque-cc0/LISEZMOI.md`). Aucune obligation, redistribuable, déjà mesurée. Elle n'a ni matières, ni instruments, ni musique : `sons-manquants.md` donne, son par son, le plus proche ou l'endroit où chercher.
2. **Freesound** (freesound.org) : filtrer sur la licence « Creative Commons 0 » ; « Attribution » (CC BY) accepté avec crédit. La licence est par son, pas par auteur : lire l'encadré de la page du son.
3. **Kenney** (kenney.nl/assets, rubrique audio) : paquets entiers en CC0, très bons pour les interfaces et les jeux.
4. **Musique** : auteurs qui publient en CC BY sur leur propre site ; bibliothèque audio de YouTube pour une vidéo destinée à YouTube ; la musique fournie par la personne (preuve de ses droits à demander).
5. **Mixkit** (mixkit.co) et **Pixabay** (pixabay.com/sound-effects) : gratuits pour une vidéo commerciale, sans crédit obligatoire, mais **non redistribuables** : voir plus bas.

## Musique : où en trouver une vraie

La banque n'a aucune musique, et les quatre fonds de `fonds/` sont des boucles de repli calculées (utiles, mais pauvres). Pour un film qui compte, chercher une vraie musique, dans cet ordre. Les licences ci-dessous sont celles que ces sites affichaient à notre connaissance ; elles changent, et elles se lisent **sur la page du morceau**, le jour du téléchargement.

| Source | Licence habituelle | Pour quoi | À savoir |
| --- | --- | --- | --- |
| La musique de la personne (composée, achetée, abonnement qu'elle paie) | la sienne | tout | demander la preuve des droits ; un abonnement (Epidemic Sound, Artlist, Uppbeat…) ne couvre que ses propres comptes |
| FreePD (freepd.com) | CC0 | fonds calmes, tension, comédie | aucun crédit obligatoire ; qualité inégale |
| Incompetech, Kevin MacLeod (incompetech.com) | CC BY 4.0 | piano de film muet, cartoon, suspense, jazz | crédit obligatoire dans la description ; morceaux très entendus |
| Scott Buckley (scottbuckley.com.au) | CC BY 4.0 | cinématique, émotion, documentaire | crédit obligatoire |
| Free Music Archive (freemusicarchive.org) | variable par morceau | tous styles | filtrer CC BY ou CC0 ; beaucoup de NC, ND, SA : refusés |
| OpenGameArt (opengameart.org) | variable par fichier | musique « puce », boucles de jeu | filtrer CC0 ou CC BY ; refuser GPL et CC BY-SA |
| Musopen (musopen.org) | domaine public ou CC, par enregistrement | classique, ragtime | l'œuvre ET l'enregistrement doivent être libres |
| Bibliothèque audio de YouTube | licence YouTube | une vidéo publiée sur YouTube | à ne pas réutiliser ailleurs sans relire ses conditions |
| Pixabay Music, Mixkit | licences maison | fond d'une vidéo, à télécharger chez la personne | non redistribuables (voir plus bas) ; certains morceaux Pixabay déclenchent des revendications automatiques : garder la page et la date |

Choisir, puis mesurer : une musique dont la partie forte arrive vite (le film entre sur elle), un tempo qui permet de caler les coupes (`beat-et-drop.md`), pas de voix chantée sous une voix parlée. `trouver-drop.py` et `npx hyperframes@0.9.33 beats` donnent le drop et les temps. Sans réseau : un fond de `fonds/`, annoncé comme tel, et la vraie musique en « reste à faire » dans la note de livraison.

Instruments isolés (une note de piano, un koto) : Freesound en CC0, mots de recherche dans `sons-manquants.md`.

## Tableau des licences

| Licence | Dans une vidéo du studio | Crédit | Peut être copié dans un autre projet, un modèle, un dépôt ? |
| --- | --- | --- | --- |
| CC0 1.0, domaine public | oui | facultatif (on le donne quand même) | oui |
| CC BY 2.0 à 4.0 | oui | **obligatoire** : titre, auteur, lien de la page, licence, « modifié » | oui, avec le crédit |
| Licence Mixkit (effets, musique) | oui | facultatif | **non** |
| Licence Pixabay | oui | facultatif | **non** |
| CC BY-NC | **non** (usage commercial) | | |
| CC BY-ND | **non** (le montage est une modification) | | |
| CC BY-SA | **non** (imposerait la même licence à la vidéo) | | |
| « Usage personnel », « éditorial », « libre de droits » sans texte de licence, extrait d'une vidéo en ligne | **non** | | |
| Deux sources qui se contredisent | **non** : la lecture la plus stricte l'emporte | | |

## Mixkit, Pixabay et autres fichiers non redistribuables

- Ils se téléchargent **chez la personne, pour le projet en cours**, dans `assets/sfx/` ou `assets/musique/` du projet.
- Ils ne sont **jamais** : inclus dans ce plugin, copiés dans un modèle réutilisable, envoyés dans un dépôt public, partagés en fichiers bruts, revendus dans un pack.
- Pixabay bloque les téléchargements automatiques : donner le lien de la page à la personne, qui télécharge elle-même.
- Ne jamais inscrire le son de la vidéo dans un système de revendication de droits (Content ID).
- Les bruitages MP3 livrés avec le skill officiel `media-use` de HyperFrames sont sous licence Pixabay : utilisables dans une vidéo par la CLI, non recopiés ici.

## Vérifier et noter

Pour chaque fichier téléchargé, une ligne dans `audio/sources.json` :

```json
{ "fichier": "assets/sfx/fs-527522-pop.ogg", "titre": "ppop.wav", "auteur": "Narjara",
  "page": "https://freesound.org/people/Narjara/sounds/527522/", "licence": "CC0 1.0",
  "licence_lue_le": "2026-11-11", "modifie": "coupé, niveau ajusté" }
```

- Lire la licence sur la page du son, pas dans un résultat de recherche ni sur un site qui recopie.
- Lire la description : certains auteurs demandent une formule de crédit précise ou interdisent la mise en ligne des fichiers bruts.
- Freesound : l'original demande un compte ; l'aperçu de haute qualité (OGG) est public et suffit pour un bruitage.
- Nommer le fichier avec sa source et son numéro (`fs-527522-pop.ogg`, `kenney-interface-click-001.ogg`) : le crédit se retrouve toujours.
- Un doute : on laisse le fichier de côté. Il existe toujours un autre enregistrement.

## Créditer

`audio/CREDITS.md` dans le projet, et pour tout son CC BY, la même ligne **dans la description de la vidéo** :

```
« Titre » par Auteur (lien de la page), licence CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/), modifié.
```

Les sons CC0 sont crédités par courtoisie dans `CREDITS.md` (pas d'obligation dans la description). Les crédits de la banque fournie sont dans `banque-cc0/LICENSES.md`.

## Contrôler ce qu'on a trouvé

- Mesure : `python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/caler.py" attaque <fichier>` (attaque, pic, fin, durée, crête) ou `npx hyperframes@0.9.33 audio <fichier> --json`.
- Un bon bruitage : attaque nette dans les 50 premières millisecondes (ou à rogner avec `debut_fichier`), queue propre qui finit dans le silence, pas de bruit de fond, pas de parole ni de musique derrière.
- Avec earshot : `earshot rank "<description du son, en anglais>" dossier/ --top 5`, `earshot find <prise longue> "<un seul coup>"` pour découper, `earshot realness <fichier>` pour vérifier qu'il se lit comme un vrai enregistrement (`earshot.md`).
- La chaîne complète fournit un contrôle des licences par script (`officiel/real-sound/scripts/audit.py`, règles dans `officiel/real-sound/references/licences.md`).

Sources : `officiel/real-sound/references/licences.md` (Leon Lin, MIT) ; `banque-cc0/LICENSES.md` (Bart, MIT ; vérifications du 12/10/2026).
