# earshot : des oreilles pour l'agent

earshot (Leon Lin, MIT, version 0.4.1) écoute un fichier son ou la bande son d'une vidéo et rend des mesures et des verdicts : ce que c'est, quand ça se passe, si c'est calé sur l'image, à quel niveau, si ça se lit comme un vrai enregistrement. Tout tourne sur la machine, sur le processeur ; aucun son ne quitte l'ordinateur (sauf la commande facultative `llm`, à ne jamais lancer sans accord explicite).

Texte complet, en anglais : `officiel/earshot/SKILL.md`. Ce fichier en est le résumé pour le studio.

## Faut-il l'installer ?

| | Sans earshot | Avec earshot |
| --- | --- | --- |
| Niveau, crête, attaques, calage approximatif | oui (`niveau.py`, `caler.py`, `hyperframes audio`) | oui, plus précis |
| Écart son / image par événement, en millisecondes | à la main | `timeline --cues` + correction automatique (`recaler.py`) |
| Choisir le meilleur son parmi 20 candidats | non | `rank`, `match`, `find` |
| Vrai enregistrement ou synthèse ? | non | `realness` |
| Planche visuelle (images, spectre, événements) | non | `sheet` |

Il demande Python 3.10 ou plus, environ 2 Go de disque (PyTorch pour processeur et deux modèles) et une machine avec 8 Go de mémoire. Le proposer à la personne dès qu'elle produit régulièrement ; ne pas l'imposer pour une première vidéo.

## Installation (une fois)

Avec `uv` (le plus simple ; installer `uv` d'après sa documentation officielle) :

```bash
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch        # télécharge les modèles et vérifie l'installation
```

Sans `uv` :

```bash
git clone https://github.com/Leonxlnx/earshot
cd earshot
python3 -m venv .venv
.venv/bin/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu    # Windows : .venv\Scripts\python
.venv/bin/python -m pip install -e ".[mcp]"
.venv/bin/python -m earshot doctor --fetch
```

- La version validée par le studio est le commit `4ac3d2a` (0.4.1, 06/11/2026). Pour l'installer exactement : ajouter `@4ac3d2a` à l'adresse git.
- Windows : `python` ouvre parfois le Microsoft Store ; utiliser `py -3` ou le chemin complet de l'environnement. Poser `HF_HUB_DISABLE_SYMLINKS_WARNING=1` pour éviter un avertissement sans importance.
- Machine partagée ou modeste : `EARSHOT_THREADS=2` (ou `--threads 2`).
- Chaque commande recharge les modèles (20 à 40 s). Pour plusieurs écoutes de suite : le serveur MCP (`earshot mcp --warm`, à déclarer dans le client : voir le texte officiel) ou un seul script Python (`from earshot import api`). Une écoute complète d'une vidéo de 90 s prend quelques minutes sur un processeur ordinaire : la lancer en tâche de fond.

## Les cinq usages

**1. Choisir un son**

```bash
earshot rank "a soft felt mallet hit on a wooden block" assets/sfx/candidats/ --top 5
earshot find prise-longue.ogg "a single clean mallet hit" --top 3        # découpes prêtes : début et fin en secondes
earshot describe choix.ogg --start 1.12 --end 1.48                        # ce que c'est vraiment
earshot realness choix.ogg --start 1.12 --end 1.48                        # vrai enregistrement ou synthèse
earshot ab a.ogg b.ogg --query "a crisp fast air whoosh"                  # départager deux candidats
```

Décrire **le son**, en anglais, pas son usage : source + matière + action + caractère (« a heavy wooden door slamming in a small room », pas « un son pour le logo »). Une découpe marquée `head cut` ou `tail cut` commence ou finit au milieu d'un son : ne pas l'utiliser telle quelle.

**2. Relire un mix ou un film**

```bash
earshot timeline renders/essai.mp4 --cues audio/cues.json --json --out audio/ecoute.json
earshot sheet renders/essai.mp4 -o audio/ecoute.png --cues audio/cues.json
earshot critique renders/essai.mp4
earshot measure renders/essai.mp4
```

- `timeline` : la transcription d'écoute (événements, niveaux, sections, coupes de l'image, calage par événement). `offset_ms` = son moins image ; négatif = en avance. Ne tenir compte du calage que s'il est nettement meilleur que le hasard (champ `chance`).
- `sheet` : une planche PNG à **ouvrir** : marqueurs verts (calé à une image près), orange (moins de 100 ms), rouges (aucun son). Trous, empilements et retards s'y voient d'un coup d'œil.
- `critique` : un barème comparé à 7 films de lancement professionnels. **Indicatif** pour le studio : ses consignes « un son sur chaque coupe » ou « finir sur un logo » ne valent pas pour une histoire racontée ou un explicatif. Garder ses mesures (silences, stéréo, graves, crêtes) et arbitrer avec les règles du studio.
- Les coupes de l'image sont détectées par différence d'images : fiable pour les coupes franches, pas pour les fondus ni pour le mouvement dans un plan. Pour de l'animation, toujours passer `--cues`.

**3. Comparer avant et après** : `earshot ab avant.wav apres.wav --query "<description>"`, puis `timeline` de nouveau. Une chose à la fois.

**4. Fabriquer un son en code** (`earshot forge`) et **5. banque de sons calculés** (`earshot sfx`, `earshot kit`) : repli seulement, voir `synthese-repli.md`. Ces sons obtiennent facilement de bons scores auprès des modèles d'earshot : cela dit que le modèle est satisfait, pas que le son vaut un enregistrement.

## Corriger le calage automatiquement

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/recaler.py" audio/ecoute.json audio/placements.json --out audio/placements_recales.json
```

Pour chaque événement dont le son arrive avant l'image (au-delà de 10 ms, la précision de la mesure) ou plus de 75 ms après, le script déplace le son (pas l'image) pour viser +8 ms. earshot, lui, tolère jusqu'à 45 ms d'avance : le studio est plus strict (jamais avant l'image). Il ne déplace que les sons à attaque ; whoosh et montées sont signalés (à caler sur leur pic ou leur fin) ; un écart de plus de 150 ms ou une absence de son est signalé, jamais corrigé (le son trouvé n'est peut-être pas le bon). Reporter les nouveaux `t` dans les `data-start`, rendre, réécouter : au moins deux tours.

## Lire les chiffres

| Chiffre | Ce que c'est | Confiance |
| --- | --- | --- |
| LUFS, dBTP, LRA, ms, Hz | mesures | exactes : s'en servir pour les niveaux |
| `z` (match, rank, find) | à quel point une description ressort parmi quelques centaines | 3 ou plus : net ; 2,5 à 3 : plausible ; 2 à 2,5 : faible ; moins de 2 : non |
| `p_real`, verdict | vrai ou produit professionnellement / synthétisé | indice fort, pas une preuve ; comparer les verdicts, pas les valeurs brutes entre fichiers de longueurs différentes |
| `offset_ms`, `chance` | écart son / image ; ce que donneraient des coupes au hasard | fiable s'il est bien au-dessus du hasard |
| statut de `critique` | position dans la plage de 7 films de référence | une plage, pas une cible |
| similarité cosinus | brute | jamais une probabilité |

## Limites à dire quand elles comptent

- Le goût n'est pas mesuré : earshot dit ce qu'est un son et comment il se mesure, pas s'il est beau ni juste pour l'histoire. La personne décide ; on lui donne les mesures et une courte liste.
- Pas de reconnaissance de la parole : il sait qu'on parle, pas ce qui est dit.
- Les sons très courts (moins de 0,5 s) sont mal étiquetés : un étiquetage incertain est neutre, seul un étiquetage franchement autre (parole, musique, moteur) est un signal d'alarme.
- Un son synthétique propre et professionnel se lit aussi comme « synthétisé » : `realness` entend comment ça sonne, pas d'où ça vient.
- Licence et provenance ne s'entendent pas : earshot ne peut pas les vérifier (`sources-libres.md`).
