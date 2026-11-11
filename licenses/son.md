# Crédits du skill `son`

## earshot et real-sound — Leon Lin — MIT

- Dépôt : https://github.com/Leonxlnx/earshot, version 0.4.1, commit `4ac3d2a` (06/11/2026). © 2026 Leon Lin.
- Texte de la licence : `skills/son/references/officiel/LICENSE-earshot.txt`.
- `skills/son/references/officiel/earshot/` et `skills/son/references/officiel/real-sound/` : copies non modifiées de `skills/earshot/` et `skills/real-sound/` (documentation, scripts, modèles).
- `skills/son/SKILL.md`, `references/regles.md`, `references/earshot.md`, `references/chaine-complete.md`, `references/sources-libres.md` : résumés et adaptations en français par Flot Web (budget d'environ 5 effets par 10 s, tolérance de calage −45 / +75 ms, niveaux par rapport au fond, tableau des licences, carte image → son).
- `skills/son/scripts/recaler.py` : écrit par Flot Web, lit la sortie de `earshot timeline`.
- Le paquet Python earshot et ses modèles ne sont pas redistribués : ils s'installent chez le client.

## claude-motion — whaleyxbt — MIT

- Dépôt : https://github.com/whaleyxbt/claude-motion, commit `6f80380` (08/11/2026). © 2026 whaleyxbt.
- `skills/son/scripts/sfx/` (`__init__.py`, `__main__.py`, `synth.py`, `mix.py`, `loudness.py`, `dsp.py`) : copie non modifiée du dossier `sfx/` (moteur de bruitages synthétisés, Python standard). Licence : `skills/son/scripts/sfx/LICENSE`.
- Non repris : l'exemple `sfx/cues/effort.py` et toute la partie Remotion du dépôt.
- `skills/son/references/synthese-repli.md` et `scripts/exemples/` : écrits par Flot Web d'après le skill `sound-design` de ce dépôt.

## motion-graphics — Bart — MIT (code), CC0 1.0 (sons)

- Dépôt : https://github.com/Barty-Bart/motion-graphics, commit `3d83d98` (13/10/2026). © 2026 Bart. Licence du code : `skills/son/banque-cc0/LICENSE-code-MIT.txt`.
- `skills/son/banque-cc0/` : copie non modifiée de `skills/sound-effects/sfx/` (109 fichiers OGG, `manifest.json`) et de `skills/sound-effects/LICENSES.md`.
- Tous les sons sont sous CC0 1.0 : paquets Kenney (kenney.nl : Interface Sounds, UI Audio, Digital Audio, Impact Sounds, Sci-fi Sounds) et sons Freesound vérifiés CC0 par Bart le 12/10/2026. Auteur et page d'origine de chaque fichier : `skills/son/banque-cc0/LICENSES.md`.
- La méthode de passe son du skill d'origine est créditée par son auteur à Vox (@Voxyz_ai).
- Aucun fichier Mixkit n'est inclus (le manifeste n'en garde que des adresses).

## claude-motion-design — Howseen AI (Raphaël Aubry) — MIT

- Dépôt : https://github.com/howseen-ai/claude-motion-design, commit `3d90d34` (02/10/2026). © 2026 Howseen AI (Raphaël Aubry).
- Repris sous forme de règles réécrites (aucun fichier copié) dans `skills/son/references/beat-et-drop.md` et `scripts/trouver-drop.py` : carte des temps, drop trouvé par l'énergie et posé sur le moment visuel clé, repères de tempo, placement d'un bruitage par son pic mesuré, impulsions de caméra après le drop, décalage maximal des entrées pour s'accrocher à un coup.

## HyperFrames — HeyGen — Apache 2.0

- Dépôt : https://github.com/heygen-com/hyperframes, version 0.9.33, commit `ffb13c3`, Copyright 2026 HeyGen, Inc. Voir `licenses/rendu.md`.
- Repris sous forme de règles réécrites : `sound.md` (pic une image après l'image, 3 à 6 dB au-dessus du fond, rotation des prises), `film.md` (« On music »), `types/music.md`, commandes `audio`, `beats`, `normalize-audio`.

## Autres sources de règles (aucun fichier copié)

- Herk Edit Kit (Nate Herk), https://github.com/nateherkai/hyperframes-student-kit, commit `10511e5`, © 2026 Nate Herk, MIT pour le kit d'origine et « Herk Edit Kit Use Permission » pour les ajouts « pipeline » dont vient cette règle (`docs/EDITING-PLAYBOOK.md` ; texte dans `licenses/textes/Herk-Edit-Kit-Use-Permission.txt`) : musique environ 11 dB sous la voix, −14 LUFS et crête mesurés sur le MP4 final.
- claude-remotion-skill (haidrrrry), https://github.com/haidrrrry/claude-remotion-skill, commit `1dcbe5e`, © 2025 haidrrrry, MIT (aucun code Remotion repris) : avance du son de 2 à 3 images, discutée dans `references/regles.md`.

## Écrit par Flot Web

`skills/son/SKILL.md`, `skills/son/references/*.md` (hors `officiel/`), `skills/son/banque-cc0/LISEZMOI.md`, `skills/son/scripts/_audio.py`, `caler.py`, `budget.py`, `niveau.py`, `trouver-drop.py`, `recaler.py`, `scripts/exemples/`.

## Ce qui n'est jamais embarqué

Fichiers audio à licence non redistribuable : Mixkit, Pixabay (dont les bruitages MP3 du skill officiel `media-use` de HyperFrames), Sonniss, bibliothèque audio de YouTube, tout son sous CC BY-NC, ND ou SA. Ils peuvent servir dans une vidéo quand leur licence le permet, téléchargés chez le client pour son projet.

## Fonds sonores de repli (`skills/son/fonds/`)

Les quatre boucles `nappe-calme.ogg`, `pulsation-legere.ogg`, `tension.ogg` et `retro-puce.ogg` sont créées par le studio (Flot Web, 2026) avec `fabriquer.py`, qui pilote le moteur de synthèse `scripts/sfx` de whaleyxbt/claude-motion (MIT, commit `6f80380`, non modifié). Elles sont libres d'usage dans les vidéos du client. Aucun enregistrement tiers n'y entre.
