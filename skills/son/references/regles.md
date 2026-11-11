# Les règles du son, en détail

Règles du studio, établies à partir de corrections répétées sur de vraies vidéos et des normes mesurées par earshot sur des films professionnels (`officiel/real-sound/references/sound-design.md`). Les chiffres sont des repères vérifiables, pas des goûts.

## Liste des événements (`audio/cues.json`)

C'est le contrat entre l'image et le son : chaque son se pose sur un instant calculé par le code de la vidéo.

```json
{
  "fps": 30,
  "total": 540,
  "events": [
    { "f": 0,   "kind": "hit",    "id": "accroche:titre:1", "weight": 1.2 },
    { "f": 63,  "kind": "pop",    "id": "pop:carte:1", "pan": -0.3 },
    { "f": 72,  "kind": "pop",    "id": "pop:carte:2" },
    { "f": 135, "kind": "whoosh", "id": "whoosh:transition:1", "dur": 14 },
    { "f": 240, "kind": "riser",  "id": "montee:revelation:1", "dur": 54 },
    { "f": 240, "kind": "hit",    "id": "impact:revelation:1", "weight": 1.5 }
  ]
}
```

- `f` : numéro d'image (peut être fractionnaire) = secondes × images par seconde. `kind` : `tick`, `key`, `click`, `pop`, `snap`, `land`, `hit`, `drop`, `whoosh`, `riser`, `swell`, `bell`, ou un mot à soi. `id` : `action:objet:numéro`, stable d'une version à l'autre. `weight` 0 à 2 (1 = normal), `pan` −1 à 1 (position à l'écran), `dur` en images pour whoosh et montées.
- Ce format est celui que lisent earshot et la chaîne complète (`officiel/real-sound/templates/cues.json`).
- **Où poser l'instant** : un impact sur l'image du contact ; une apparition à 50 % de son trajet ; un whoosh sur le pic de vitesse du mouvement ; une montée sur l'image du coup qu'elle prépare ; un son de logo sur l'image où le nom devient lisible.
- Dans HyperFrames, exporter ces instants depuis les constantes de la timeline (les mêmes nombres que ceux passés à `tl.to(..., position)`), par un petit script du projet ou à la lecture de `npx hyperframes@0.9.33 timeline --json`. Si un plan change de durée, la liste est régénérée, jamais retouchée à la main.

`audio/plan.json` (entrée de `caler.py`) reprend ces événements en secondes, avec le fichier choisi :

```json
[
  { "id": "pop:carte:1", "t": 2.100, "fichier": "assets/sfx/pop-a.ogg", "type": "pop", "gain_db": -8 },
  { "id": "impact:revelation:1", "t": 8.000, "fichier": "assets/sfx/impact.ogg", "type": "impact", "gain_db": -4 }
]
```

## Carte « image → son »

| À l'image | Son | Calé sur |
| --- | --- | --- |
| Mouvement continu (dérive, grain, rotation, défilement, texte qui s'écrit en continu) | rien : la musique le porte | |
| Coupe franche | rien (8 à 9 fois sur 10) | |
| Clic, appui | un seul clic réel pour tout le film, même prise et même niveau (exception à la rotation des prises) ; relâchement environ 85 ms après | l'image de l'appui |
| Frappe au clavier | un vrai clavier découpé ; 12 touches par seconde au plus ; au-delà de 25 caractères par seconde, une touche par mot ; la musique baisse de 6 à 10 dB | chaque caractère sonorisé |
| Carte, pastille, badge qui apparaît | un pop ou un tic doux, qui monte le long d'une série | 50 % du trajet |
| Bascule, verrouillage, valeur finale d'un compteur | un loquet, un clic net | l'image du contact |
| Grand mouvement de caméra, balayage, zoom (2 à 3 par film) | un souffle réel | le pic de vitesse |
| Tension avant la révélation | la montée de la musique, ou une montée réelle qui finit 30 à 250 ms avant le coup | le coup |
| Révélation, moment fort | le **drop** de la musique, plus un seul impact réel si besoin | l'image |
| Logo, signature | la musique s'arrête sur une barre de mesure ou se filtre, 0,2 à 0,7 s de quasi-silence, **une** note douce dans la tonalité, queue jusqu'au silence | l'image où le nom se lit |
| Personnage qui marche, pose, saisit | bruitage de la matière (pas, tissu, objet), discret | l'image du contact |
| Lieu (extérieur, pièce, machine) | une ambiance continue, très basse, qui change avec le lieu | le plan |

## Budget

- **Environ 5 bruitages « conçus » par 10 s** ; plage normale 3 à 8. Seul le maximum (8) est une faute pour `budget.py` ; sous 3, le film est « calme » : permis, à condition que l'accroche et le moment fort aient leur son. L'ambiance et la musique ne comptent pas ; une rafale de frappe au clavier compte pour un.
- Vidéo de 30 s : 12 à 18 bruitages au total, dont 2 à 3 whoosh, un seul gros impact, une seule grande montée.
- Répartition : dense là où l'image est dense et la voix absente, rare sous la voix et après le moment fort.
- Vérification : `scripts/budget.py`. Si le budget déborde, l'ordre de retrait est : sons des coupes, sons des petits mouvements, doublons d'un même geste, puis les sons masqués par la voix.
- Un film « haut de gamme, calme » : une poignée de coups doux ; retirer tout ce qui paraît fort ou déplacé.

## Palette et variation

- Une famille de matières par vidéo, choisie au brief d'après le style (papier et crayon pour un style dessiné, plastique et verre pour une interface, bois et pierre pour un conte…). Un son hors palette se remarque plus qu'un son absent.
- Action répétée : 2 à 4 prises en rotation, jamais la même deux fois de suite ; ±1 à 2 dB ; ±0,5 demi-ton au plus (au-delà, le timbre change). **Exception : le clic d'interface**, qui garde la même prise et le même niveau dans tout le film ; `budget.py` l'accepte et signale au contraire plusieurs clics différents.
- Série qui progresse (3 cartes, 5 étapes) : la hauteur monte de 1 à 3 demi-tons par élément et se résout sur le dernier.
- Tous les sons à hauteur (tintements, notes, pops accordés) dans la tonalité de la musique.

## Niveaux

| Élément | Repère |
| --- | --- |
| Film entier, avec voix ou musique | −14 LUFS intégrés (±1 sur le MP4) ; plage dynamique (LRA) de 5 à 9 LU pour un film monté sur une musique, 7 ou plus pour une histoire racontée |
| Film entier, sans voix ni musique | pas de cible LUFS : voir « Niveau final » plus bas |
| Crête | −1,5 dBTP sur le fichier maître WAV ; −1 dBTP ou moins après encodage AAC |
| Voix | l'élément le plus fort et le plus stable ; chaque phrase au même niveau |
| Musique sous une voix | environ 11 dB sous la voix (9 à 14) ; `data-volume` de départ 0,14 à 0,25 |
| Musique seule | pleine, mais baissée de 6 à 12 dB pendant 0,3 à 0,5 s avant un impact ou le drop, et ramenée sur le coup |
| Bruitage | 3 à 10 dB au-dessus du fond à cet instant (mesurer le fond la seconde d'avant) |
| Ambiance | 25 à 30 dB sous la voix entre les phrases |
| Moment le plus fort | sur le drop ou la révélation, entre 30 et 60 % du film ; le logo 8 à 20 dB dessous |

Pourquoi −14 LUFS : c'est le niveau auquel Instagram, TikTok et YouTube ramènent ce qu'on leur envoie. Plus fort, la plateforme baisse (et la dynamique sacrifiée est perdue) ; nettement plus bas, la vidéo paraît faible à côté des autres.

Pourquoi un gain constant : une normalisation dynamique (un `loudnorm` en une passe, un limiteur qui travaille en permanence) remonte les silences voulus et aplatit le moment fort. On mesure, on applique un seul gain, on ne limite que les crêtes qui dépasseraient.

## Niveau final

Le niveau du film se règle **après le rendu**, par `scripts/finaliser.py` (étape 7 du skill). Dans la composition, le mixeur de HyperFrames plafonne la crête à −1 dBTP : monter les `data-volume` s'arrête vers −19,5 LUFS (mesuré : ambiance passée de 6 à 11, aucun gain).

**Mesure.** Une seule méthode, décrite en tête de `scripts/niveau.py` : `ffmpeg -i <fichier> -map 0:a:0 -af ebur128=peak=true -f null -`, lignes `I:` (LUFS), `LRA:` et `Peak:` (crête vraie) du résumé, sur le MP4 livré. `loudnorm=print_format=json` ne sert pas de mesure : sur un film de 10 s, son `input_i` s'écarte jusqu'à 0,8 LU (pixel-8-bits : −15,3 contre −16,0 ; un calcul BS.1770 indépendant donne −16,01).

**Film avec voix ou musique.** −14 LUFS ±1 et crête à −1 dBTP au plus sur le MP4 (maître WAV : ±0,5 et −1,5 dBTP). Un gain constant ; un limiteur seulement sur les crêtes, et pas plus de 6 dB retirés. Le plafond annoncé est tenu en crête vraie : limiteur à 192 kHz, mesure du fichier écrit, nouveau passage si besoin ; puis nouvelle mesure après l'AAC, qui déplace les crêtes (jusqu'à +1,7 dB mesuré sur un mix écrasé).

**Film sans voix ni musique** (option `--sans-fond` de `niveau.py` et de `finaliser.py`). La cible −14 LUFS n'a pas de sens pour quelques coups dans du silence : le niveau intégré ne compte que les moments sonores, et il faudrait écraser les coups ou remonter le silence pour l'atteindre. Règle :

1. un seul gain constant, aucun limiteur, aucune normalisation dynamique ;
2. la crête du bruitage le plus fort entre −3 et −1 dBTP sur le MP4 (la référence est la crête : c'est aussi là que culminent les coups d'un film à −14 LUFS) ;
3. jamais au-dessus de −14 LUFS : avec des bruitages denses, le gain s'arrête à −14 et la crête peut rester sous −3 ;
4. le fond entre les bruitages (plancher : 10e centile des fenêtres de 50 ms) au moins 20 dB sous le passage le plus fort : un ton de pièce monté pour gonfler le chiffre est du souffle ;
5. le film sort en **jaune**, et la note de livraison dit « film sans voix ni musique : niveau réglé sur la crête (x dBTP), y LUFS ».

Une ambiance de lieu continue et voulue forte (pluie, foule, atelier) tient lieu de fond : profil par défaut. Un ton de pièce, non.

**Ce que disent les essais** (12 films de test de 9 à 10 s, HyperFrames 0.9.33 ; mesuré, non écouté) :

| Film (rendu) | Parcours | Résultat sur le MP4 livré | Limiteur | Plancher | Facteur de crête des coups |
| --- | --- | --- | --- | --- | --- |
| isométrique trait fin, −26,2 LUFS, crête −5,2 | défaut (6 dB au plus) | −18,5 LUFS, −1,4 dBTP : rouge, trop bas | 5,4 dB, 3 % du temps | +9,7 dB | −3,3 dB |
| | `--forcer` | −14,2 LUFS, −1,4 dBTP | 12,8 dB, 34 % du temps | +17,0 dB (−12,1 dBFS) | 11,0 → 3,9 dB |
| | `--fond` nappe calme | −14,1 LUFS, −1,6 dBTP : vert | 1,6 dB, 0,5 % | fond voulu | 11,0 → 10,7 dB |
| typo suisse, −25,9 LUFS, crête −1,3 | `--forcer` | −14,2 LUFS, −1,4 dBTP | 17,4 dB, 14 % du temps | +14,1 dB | 15,4 → 6,6 dB |
| | `--sans-fond` | −26,1 LUFS, −1,5 dBTP : jaune | aucun | inchangé | inchangé |
| | `--fond` nappe calme | −14,0 LUFS, −1,6 dBTP : vert | 1,7 dB, 0,5 % | fond voulu | 15,4 → 13,2 dB |
| cartoon années 50, −25,6 LUFS | `--forcer` | −14,2 LUFS, −1,1 dBTP | 13,2 dB, 19 % du temps | +15,0 dB | 16,1 → 4,7 dB |
| démo produit, −23,9 LUFS | `--sans-fond` | −23,5 LUFS, −1,5 dBTP : jaune | aucun | silence | inchangé |
| pixel 8 bits, −16,0 LUFS, crête −5,0 | `--sans-fond` | −14,0 LUFS, −3,0 dBTP : jaune | aucun | silence | inchangé |
| pop trame (avec ambiance), −19,1 LUFS | défaut | −14,1 LUFS, −1,3 dBTP : vert | 5,5 dB, 2 % du temps | +5,4 dB | 14,1 → 8,6 dB |

Lecture : forcer −14 LUFS sur des coups isolés retire 13 à 17 dB aux crêtes et remonte d'autant tout ce qui se trouve entre les coups. À l'écoute, il faut s'attendre à des coups aplatis et durs (leur facteur de crête tombe sous 7 dB), à un souffle de fond nettement audible (un ton de pièce parti de −29 à −34 dBFS finit entre −12 et −20 dBFS) et à du pompage (le fond baisse à chaque coup puis remonte, le limiteur agissant 14 à 34 % du temps). Avec un fond musical, le même film atteint −14 LUFS en ne limitant que 1 à 3 dB pendant moins de 1 % du temps : c'est la bonne voie. Ces effets sont déduits des mesures ; personne n'a écouté.

## Calage

| Type de son | Ce qui se cale | Tolérance |
| --- | --- | --- |
| Coup, clic, pop, bip, pose, touche, tintement | l'attaque sur l'image de l'événement, +8 ms | au placement : +8 ms exactement, jamais avant ; au contrôle du rendu : de 0 à +75 ms (10 ms d'avance tolérées, c'est la précision de la mesure) |
| Whoosh, souffle | le pic sur le pic de vitesse | ±1 image |
| Montée | la fin, 30 à 250 ms avant le coup (100 ms par défaut) | |
| Drop de la musique | le premier temps fort sur l'image de la révélation | ±1 image |

- **Règle du studio : attaque sur l'impact, +8 ms, jamais avant.** La lumière arrive avant le son : un son en avance choque bien plus vite qu'un son en léger retard. Dans le doute, une image après, jamais une image avant. Ce qui commence avant l'image, ce sont seulement les sons lents (whoosh, montée), dont le pic ou la fin est calé, pas le début.
- Presque tous les fichiers ont leur pic après leur début : placer par le début du fichier est l'erreur la plus fréquente. `scripts/caler.py attaque` ou `npx hyperframes@0.9.33 audio <fichier> --place-at <instant>` donnent la mesure.
- Un mouvement qui doit tomber sur un coup de la musique démarre 40 à 190 ms avant ; le coup lui-même est un changement instantané (pas un adoucissement).

## Silence, début et fin

- Les 0,5 premières secondes : l'accroche a un son (un coup net ou l'entrée de la musique), sans masquer le premier mot.
- Un vrai silence (ou la musique filtrée, baissée de 12 dB ou plus) de 0,2 à 0,7 s avant le moment fort.
- Fin : fondu de la musique de 1 à 1,5 s sur une barre de mesure, ou dernière note qui s'éteint ; jamais de coupe nette, jamais de son après la dernière image.

## Signes d'un son « bon marché » (à chercher à la relecture)

Le même whoosh partout ; un son sur chaque coupe ; des bips et tintements synthétiques sans cause ; une montée générique devant un moment qui ne la mérite pas ; des bruitages plus forts que la voix ; une musique en boucle visible (reprise audible) ; un fond tout en graves inaudible sur téléphone ; un clic différent à chaque appui ; une fin coupée net.

## Sources

- earshot et real-sound, Leon Lin, MIT (budget « environ 5 effets conçus par 10 s », niveaux par rapport au fond, tolérance de calage, carte image → son des films de lancement, signes bon marché).
- claude-remotion-skill (haidrrrry, MIT, commit `1dcbe5e`) donne « le son 2 à 3 images avant l'impact » : le studio ne retient cette avance que pour le **début** des sons qui s'établissent lentement (souffles, montées), dont le pic ou la fin se cale sur l'image ; pour les coups, la tolérance mesurée par earshot prévaut (jamais avant l'image).
- Herk Edit Kit (Nate Herk, MIT, commit `10511e5`) : musique environ 11 dB sous la voix, −14 LUFS mesurés sur le MP4 final.
- HyperFrames (HeyGen, Apache 2.0) : `sound.md` (pic une image après l'image, 3 à 6 dB au-dessus du fond, rotation des prises), `film.md` (mouvement 40 à 190 ms avant un coup).
- claude-motion (whaleyxbt, MIT) : « accentuer, ne pas commenter », une tonalité, un seul impact et une seule grande montée par vidéo.
