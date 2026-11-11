# Caler le film sur la musique : temps, mesures, drop

Méthode reprise de claude-motion-design (Howseen AI, MIT, commit `3d90d34`) et des références HyperFrames (`film.md`, `types/music.md`), adaptée au vertical court.

## Principe

Quand il n'y a pas de voix, **la musique est l'horloge** : chaque scène commence sur un temps, et le **drop** (l'instant où la musique s'ouvre : entrée de la basse et de la batterie, saut net d'énergie) tombe sur le moment visuel clé (révélation, logo, chiffre). Quand il y a une voix, la voix est l'horloge et la musique s'y plie.

## 1. Choisir la musique par son tempo

| Tempo | Caractère |
| --- | --- |
| 60 à 80 BPM | posé, solennel |
| 90 à 110 BPM | fluide, récit |
| 115 à 125 BPM | net, élégant, produit |
| plus de 125 BPM | énergie, annonce |

Chercher une musique par son caractère et son tempo, pas par son sujet (« pulsation tendue qui monte vers un drop lumineux, 120 BPM »). Une musique dont le début est une longue montée calme vide une vidéo courte : partir d'une section plus forte.

## 2. Trouver le drop par l'énergie

Ne jamais se fier à une grille de temps automatique pour le drop (elle peut être décalée de deux temps).

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/trouver-drop.py" assets/musique.mp3 --bpm 120 --drop-film 8.0
```

Le script mesure l'énergie (bande entière et graves) par demi-seconde, cherche le plus grand saut durable, l'affine à 25 ms près, et donne les attributs à poser sur la balise de la musique pour que le drop tombe à l'instant voulu du film :

- drop de la musique **plus tard** que le moment fort du film : la musique entre en cours de route (`data-media-start`) ;
- drop **plus tôt** : la musique commence après le début du film (`data-start`) ; prévoir une ambiance ou un silence voulu avant.

Un saut inférieur à 3 dB : cette musique n'a probablement pas de drop ; caler alors le moment fort sur un début de section.

Compléments avec la CLI :

```bash
npx hyperframes@0.9.33 beats assets/musique.mp3 --json                              # bpm, beatTimes
npx hyperframes@0.9.33 audio assets/musique.mp3 --only sections,onsets,moments --json   # sections, coups
```

`beats` n'est fiable que sur les passages rythmés ; sur une musique calme il invente un métronome, souvent au double du tempo (lire `bpmConfidence`). Là, couper sur les changements de phrase et d'énergie (`sections`).

## 3. Écrire la carte des temps (`audio/BEATMAP.md`)

```
Musique : <titre>, 120 BPM → un temps = 0,500 s ; une mesure = 2,000 s
Drop de la musique : 16,010 s → placé à 8,000 s du film (data-media-start = 8,010)

| Scène        | Début (s) | Temps | Mesure | Ce qui se passe          |
| accroche     | 0,000     | 1     | 1      | titre déjà à l'écran     |
| problème     | 2,000     | 5     | 2      | 3 cartes, un pop chacune |
| tension      | 6,000     | 13    | 4      | montée, image qui se vide |
| RÉVÉLATION   | 8,000     | 17    | 5      | DROP + impact            |
| preuve       | 10,000    | 21    | 6      | …                        |
| signature    | 14,000    | 29    | 8      | dernière note, fondu     |
```

- Durée d'un temps = 60 / BPM ; chaque scène commence sur un temps, les scènes importantes sur un début de mesure.
- Rien d'immobile plus d'une seconde.
- Le moment fort entre 30 et 60 % de la durée.
- Les durées des scènes dans le code sont **dérivées** de cette carte (constantes `TEMPS = 60 / BPM`), pas l'inverse.

## 4. Régler le mouvement autour des coups

- Un mouvement qui doit **arriver** sur un coup démarre 40 à 190 ms avant ; une **réaction** à un coup démarre 0 à 45 ms après.
- Le coup lui-même est un changement instantané (`tl.set`), pas un adoucissement : adoucir un coup le tue.
- Les petites entrées peuvent se décaler de 0,10 s au plus, les révélations de 0,15 s au plus, pour s'accrocher à un coup de la musique. Au-delà, c'est la carte des temps qu'il faut revoir.
- Petites impulsions de caméra sur les temps après le drop : échelle +1,2 % par temps, +3 % par début de mesure, retour amorti. Jamais avant le drop.
- Un mot à lire reste au moins un temps. Un même traitement visuel lasse après 6 s environ.
- Ne pas couper sur chaque temps : les coupes suivent le mouvement, les temps forts portent les moments forts.

## 5. Monter la musique

- Baisser la musique de 6 à 12 dB pendant 0,3 à 0,5 s avant le drop (enveloppe `data-automation`), et la ramener sur le coup : le drop paraît plus grand sans monter le niveau.
- Entrée : fondu de 0,4 s si la musique entre en cours de route. Sortie : fondu de 1 à 1,5 s **sur une barre de mesure**, sous la signature.
- Musique plus courte que le film : la boucler sur un nombre entier de mesures, raccord sur un temps fort, jamais au milieu d'une phrase.
- Sous une voix : la musique environ 11 dB sous la voix, baissée par enveloppe sur chaque phrase et relevée dans les pauses de plus d'une seconde.
- Montage fin d'une musique à la mesure près (changer sa structure, déplacer son drop) : chaîne complète, `officiel/real-sound/scripts/arrange.py` (`chaine-complete.md`).

## 6. Vérifier sur le rendu

```bash
npx hyperframes@0.9.33 audio renders/essai.mp4 --range 7,9 --only onsets
npx hyperframes@0.9.33 snapshot --at 7.93,8.0,8.07
```

Le coup le plus fort de la plage doit être à moins d'une image (33 ms) de l'image de la révélation, et la capture à cet instant doit montrer la révélation déjà là. Avec earshot : `earshot timeline renders/essai.mp4 --cues audio/cues.json` donne l'écart en millisecondes.

## Liste de contrôle

- [ ] BPM mesuré, durée d'un temps écrite dans le code.
- [ ] Drop trouvé par l'énergie, pas par la grille ; saut d'au moins 3 dB.
- [ ] Drop à moins d'une image du moment fort, vérifié sur le rendu.
- [ ] Chaque scène commence sur un temps ; rien d'immobile plus d'une seconde.
- [ ] Musique baissée avant le drop, fondu final sur une barre de mesure.
- [ ] Licence de la musique lue et notée ; crédit prêt pour la description.
