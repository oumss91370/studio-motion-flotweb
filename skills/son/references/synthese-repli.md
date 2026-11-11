# Synthèse en repli

La synthèse (des sons calculés, sans aucun enregistrement) ne vient qu'**après** la recherche de vrais enregistrements. Elle a deux avantages (aucune licence, aucun téléchargement, même résultat à chaque rendu) et un défaut : des bips, des tintements et des souffles calculés s'entendent vite comme « faits par une machine ».

## Quand elle est admise

| Situation | Décision |
| --- | --- |
| La banque CC0 et les sources libres ont un son qui convient | enregistrement réel, toujours |
| Pas de réseau, et la banque CC0 n'a pas ce son | synthèse, annoncée dans la note de livraison |
| Style où le son synthétique est le sujet (jeu rétro, interface futuriste, pixel art) | synthèse assumée : c'est la palette du style |
| Fond continu discret pour porter le niveau quand il n'y a pas de musique | synthèse acceptable (nappe très basse) |
| Voix, pas, objets, matières, ambiances de lieu | **jamais** en synthèse |

Dans le doute : un enregistrement moyen vaut mieux qu'une synthèse propre. Au-delà d'un tiers de sons synthétiques dans un film qui n'est pas d'un style « machine », revoir la recherche de sons.

## Le moteur `scripts/sfx/`

Moteur de whaleyxbt/claude-motion (MIT, commit `6f80380`), copié sans modification : Python standard seulement, 48 kHz stéréo, aucun échantillon. Il place les sons sur les instants d'un fichier JSON et règle le niveau final à −14 LUFS avec une crête à −2 dBFS au plus.

| Fichier | Rôle |
| --- | --- |
| `sfx/synth.py` | générateurs : chacun renvoie un son mono |
| `sfx/mix.py` | `Mix` : placer dans le temps, panoramique, niveau final, écriture du WAV |
| `sfx/loudness.py` | mesure du niveau intégré (norme BS.1770) et de la crête vraie |
| `sfx/dsp.py` | filtres, oscillateurs, réverbération calculée, pour des sons plus longs |
| `exemples/repli_synthese.py`, `exemples/timeline-exemple.json` | exemple complet du studio |

Générateurs (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="${CLAUDE_PLUGIN_ROOT}/skills/son/scripts" python3 -m sfx --list`, depuis n'importe quel dossier) :

| Générateur | Pour |
| --- | --- |
| `click(freq, dur)` | clic d'interface, cran |
| `key()` | une frappe de clavier (`mix.typing(début, fin, caractères)` pour une saisie) |
| `blip(freq)` | note douce : un mot ou un élément qui se pose |
| `pop(f0, f1)` | pastille, badge qui apparaît ; monter `f0` le long d'une série |
| `chime(freqs)` | accord de cloche : arrivée, réussite |
| `whoosh(dur, f0, f1, peak)` | souffle ; `peak` (0 à 1) = position du pic dans la durée |
| `riser(dur)` | montée ; doit finir juste avant le coup ; une seule par vidéo |
| `impact(dur)` | impact grave du moment fort ; un seul par vidéo |
| `scratch(dur)` | crayon sur papier : un trait qui se dessine |
| `pad(durée, accords, volume)` | nappe de fond stéréo ; `envelope(points)` pour la baisser |

## Écrire une feuille de sons

```python
from sfx.synth import pop, whoosh, impact

TARGET_LUFS = -14.0
SEED = 11

def score(mix, tl):                       # tl = le JSON de la timeline de la vidéo
    for i, t in enumerate(tl["cartes"]):
        mix.put(t, pop(700 + i * 120, 380), 0.22, pan=-0.3 + i * 0.3)
    mix.put(tl["revelation"] + 0.008, impact(1.2), 0.32)
```

Depuis le dossier du projet vidéo (on n'entre jamais dans le plugin, et on n'y écrit rien : `PYTHONDONTWRITEBYTECODE=1` empêche Python d'y créer des dossiers `__pycache__`) :

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="${CLAUDE_PLUGIN_ROOT}/skills/son/scripts" \
  python3 -m sfx audio/sons.py --timeline audio/timeline.json --out assets/sfx/repli.wav
```

- Le fichier de timeline contient au moins `"duration"` (secondes) et les instants nommés de la vidéo ; **ce sont les mêmes nombres que ceux du code de l'image**. `mix.put(t, …)` prend toujours son instant dans `tl`, jamais un nombre tapé.
- Gains : moment fort 0,25 à 0,35 ; sons d'appui 0,08 à 0,2 ; nappe environ 0,03 à 0,05, baissée d'environ 65 % sous le moment fort.
- Panoramique selon la position à l'écran (−1 gauche, +1 droite), modéré en vertical (±0,3).
- Une seule tonalité pour tous les sons à hauteur ; la hauteur monte avec la progression et se résout sur le moment fort.
- Calage (règle du studio : attaque sur l'impact, +8 ms, jamais avant) : `pop`, `click`, `impact` ont leur attaque au début (poser à l'instant + 8 ms) ; `whoosh` a son pic à `peak × durée` (poser à `instant − peak × durée`) ; `riser` culmine à sa fin (poser pour finir 100 ms avant le coup).
- Le budget reste le même : environ 5 bruitages par 10 s. La gratuité des sons calculés pousse à en mettre partout : ne pas le faire.
- Si le moteur annonce un niveau inférieur à la cible (« too sparse »), le mix est fait de coups isolés : ajouter une nappe ou des queues plus longues, ne pas forcer. Le moteur règle le niveau de **son** fichier ; le niveau du film se règle quand même après le rendu (`finaliser.py`, étape 7 du skill).
- Besoin d'un fond tout fait : `../fonds/` contient quatre fonds bouclables fabriqués avec ce moteur (`fonds/LISEZMOI.md`), et `fonds/fabriquer.py` montre comment écrire une boucle sans couture.
- Le fichier produit entre dans la composition comme une seule balise `<audio id="sfx-repli" class="clip" src="assets/sfx/repli.wav" data-start="0" data-volume="1">`. Mélangé à une musique réelle, le niveau final se règle sur l'ensemble (`niveau.py`).
- Le calcul est en Python pur : compter quelques secondes pour 10 s de son, plus pour une nappe longue.

## Synthèse plus proche du réel : earshot

earshot fournit une banque de sons calculés mieux mesurés (`earshot sfx`, `earshot kit`) et un atelier pour fabriquer un son en le comparant à de vrais enregistrements (`earshot forge`). Ce ne sont pas des enregistrements : même statut de repli. Voir `earshot.md` et `officiel/earshot/SKILL.md` (boucles 4 et 5).

## Contrôle

`PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/niveau.py" mesurer assets/sfx/repli.wav`, puis les contrôles habituels sur le rendu (étape 6 du skill). Avec earshot, `earshot realness` dira « synthétisé » : c'est attendu ; l'information va dans la note de livraison (« bruitages synthétisés : pops et impact »).
