# La chaîne complète (« real-sound »)

Pour un film soigné : une bande son construite uniquement à partir de vrais enregistrements sous licence, placée sur les images de la liste d'événements par un mixeur déterministe, contrôlée par des mesures, critiquée sous cinq angles, corrigée, masterisée à −14 LUFS, créditée et posée sur l'image. Le code choisit, coupe, place, règle, égalise et masterise ; il ne fabrique aucun son.

Texte complet, scripts, modèles de fichiers et consignes pour sous-agents, en anglais : `officiel/real-sound/` (Leon Lin, MIT, non modifié). Ce fichier en est le plan en français.

## Prérequis

- earshot installé (`earshot.md`) : son Python fournit numpy, scipy, soundfile, dont les scripts ont besoin. Dans les commandes ci-dessous, `PY` est ce Python (environnement d'earshot) et `RS` le dossier `${CLAUDE_PLUGIN_ROOT}/skills/son/references/officiel/real-sound`.
- Lancer les scripts avec l'option `-I` de Python (mode isolé : un fichier téléchargé ne peut pas se faire passer pour un module).
- Les fichiers de travail vivent dans le projet vidéo : `audio/` (brief, sons, conception) et `out/` (rendus, contrôles).

## Les étapes

| Étape | Qui | Produit | Condition pour passer |
| --- | --- | --- | --- |
| 0. Liste des événements | agent principal | `out/cues.json` | instants calculés depuis le code de l'image |
| 1. Brief | agent principal | `audio/SOUND_BRIEF.md` (modèle : `templates/SOUND_BRIEF.md`) | chaque événement a un besoin, ou « rien » |
| 2. Recherche de sons, par catégorie | sous-agents | `audio/assets/<catégorie>/`, fiches | chaque fichier mesuré ; `earshot realness` = réel sur la découpe utilisée |
| 3. Contrôle des licences | un contrôleur | `audit.json` | `audit.py` sort avec le code 0 |
| 4. Montage de la musique | un superviseur | `audio/design/music.json` | grille vérifiée, drop sur la révélation, raccords propres |
| 5. Conception par catégorie | sous-agents | `audio/design/<catégorie>.json` | rendu seul + contrôle propres |
| 6. Assemblage | agent principal | bande son, pistes séparées, rapport, trace | niveau final ±0,5 LU, crête ≤ −1,5 dBTP |
| 7. Contrôle et écoute | agent principal | `out/qa/qa.json`, écoute earshot | aucun échec |
| 8. Critique, 5 angles, en lecture seule | 5 critiques | problèmes classés + corrections testées | |
| 9. Correction | **un seul** correcteur | la conception corrigée | aucun recul au contrôle |
| 10. Master, crédits, pose sur l'image | agent principal | `CREDITS.md`, texte de description, le film | crédits code 0, décalage 0 |

Les cinq angles de critique : calage (`critic_sync.md`), bords et clics (`critic_edges.md`), masquage (`critic_masking.md`), équilibre tonal (`critic_tonal.md`), regard du réalisateur (`critic_director.md`). Chaque critique teste ses corrections dans son propre dossier (`variant.py`) et rend des opérations exactes avec les chiffres avant → après ; le correcteur unique les fusionne.

## Commandes principales

```bash
# mesurer les enregistrements trouvés
PY -I RS/scripts/analyze.py audio/assets/ui/* --png out/audio-review/ui --out out/audio-review/ui.json
# contrôle des licences et des fichiers
PY -I RS/scripts/audit.py --root . --report out/qa/mix_report.json
# grille et montage de la musique à la mesure
PY -I RS/scripts/arrange.py audio/assets/music/<piste> --film-bpm 120 --arc audio/arc.json --out out/audio-review/music/arrange.json
# rendre la conception (le master à -14 LUFS est fait par master.py)
PY -I RS/scripts/mix.py --root . --design audio/sounddesign.json --cues out/cues.json --trace out/qa/adds.json
# contrôles reliés à chaque placement, puis écoute
PY -I RS/scripts/qa.py --layers
PY -I RS/scripts/qa.py --listen --realness --video out/film.mp4
# crédits et pose sur l'image (l'image est copiée sans réencodage)
PY -I RS/scripts/credits.py --root . --design audio/sounddesign.json --audit audio/assets/manifests/audit.json
node RS/scripts/mux.mjs --video out/film.mp4 --audio out/audio/soundtrack.wav --out out/film_sound.mp4
```

Chaque script (sauf `licences.py`, un module) affiche son aide avec `--help`.

## Ce que le studio change par rapport au texte d'origine

| Sujet | Texte d'origine | Studio |
| --- | --- | --- |
| Niveau | −14 LUFS, crête 0,77 linéaire (réglage par défaut de `master.py`) | identique pour un film avec voix ou musique ; sans voix ni musique, règle « sans fond » de `regles.md` ; dans tous les cas le MP4 livré se contrôle avec `niveau.py mesurer` |
| Calage des coups | tolérance de −45 à +75 ms autour de l'image | plus strict : attaque sur l'impact, +8 ms, jamais avant (10 ms d'avance tolérées à la mesure) |
| Budget | environ 5 effets conçus par 10 s | identique ; le contrôle `qa.py --layers` (densité) fait foi, `budget.py` sert au parcours simple |
| Référence de critique | 7 films de lancement professionnels | indicative hors films de lancement : garder les mesures, arbitrer avec `regles.md` |
| Synthèse | « le code ne fabrique aucun son » | même principe ; la synthèse de repli (`synthese-repli.md`) se fait hors de cette chaîne, et se signale |
| Sources | Freesound, Mixkit, bibliothèques d'auteurs | idem, plus la banque CC0 du skill ; fichiers Mixkit et Pixabay jamais gardés hors du projet (`sources-libres.md`) |
| Moteur d'image | tout moteur, exemples avec « Cinetic » | HyperFrames : la bande son finale entre comme une seule balise `<audio id="bande-son" class="clip" data-start="0" data-volume="1">` avant le rendu, ou par `mux.mjs` après |
| Sous-agents | consignes prêtes dans `templates/prompts/` | à utiliser si le client permet des sous-agents ; sinon l'agent principal joue les rôles l'un après l'autre, le critique après une pause et une relecture à neuf |

## Quand la choisir

Film de lancement, film de marque, court animé où la musique doit être montée à la mesure, ou toute vidéo pour laquelle la personne dit « le son doit être irréprochable ». Pour un court vertical ordinaire, le parcours simple du skill suffit et prend dix fois moins de temps.

## Dépannage

`officiel/real-sound/references/troubleshooting.md` (erreurs et corrections), `design-format.md` (toutes les clés du fichier de conception), `process.md` (rôles, seuils et leur origine).
