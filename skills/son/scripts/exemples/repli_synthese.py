"""Exemple de bande son de repli, entièrement synthétisée (aucun fichier son, aucune licence).

À n'utiliser que si aucun vrai enregistrement ne convient (voir SKILL.md, étape 3).
Tous les instants viennent de la timeline de la vidéo (timeline-exemple.json), jamais d'un nombre tapé à la main.

Lancer depuis le dossier du projet vidéo, sans entrer dans le plugin (S = dossier scripts/ du skill son) :
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$S" python3 -m sfx "$S/exemples/repli_synthese.py" \
        --timeline "$S/exemples/timeline-exemple.json" --out assets/sfx/repli.wav

Moteur : sfx/ de whaleyxbt/claude-motion (MIT, commit 6f80380), Python standard.
"""
from sfx.synth import envelope, impact, pad, pop, riser, whoosh

TARGET_LUFS = -14.0   # cible du studio
SEED = 11             # même graine = même rendu

LA_MINEUR = [220.00, 261.63, 329.63]   # une seule tonalité pour tous les sons à hauteur


def score(mix, tl):
    # 1. Fond discret sous tout le film : c'est lui qui permet d'atteindre -14 LUFS sans écraser les coups.
    volume = envelope([(0, 0.0), (0.4, 1.0), (tl["revelation"] - 0.4, 1.0), (tl["revelation"] - 0.05, 0.35),
                       (tl["revelation"] + 0.3, 1.0), (tl["duration"] - 1.2, 1.0), (tl["duration"], 0.0)])
    gauche, droite = pad(tl["duration"], [(0, LA_MINEUR)], volume=volume)
    mix.put_stereo(0, gauche, droite, 0.05)

    # 2. Trois cartes qui arrivent : un pop par carte, la hauteur monte, léger panoramique.
    for i, t in enumerate(tl["cartes"]):
        mix.put(t, pop(700 + i * 120, 380), 0.22, pan=-0.3 + i * 0.3)

    # 3. Une seule transition sonorisée : le pic du whoosh (peak=0.6 de sa durée) tombe sur l'instant.
    d = 0.45
    mix.put(tl["transition"] - 0.6 * d, whoosh(d, 500, 2600, peak=0.6), 0.12)

    # 4. Montée qui finit 100 ms avant la révélation, puis l'unique impact du film sur l'image + 8 ms.
    d = tl["revelation"] - 0.1 - tl["montee_debut"]
    mix.put(tl["montee_debut"], riser(d), 0.10)
    mix.put(tl["revelation"] + 0.008, impact(1.2), 0.32)
    # Budget : 3 pops + 1 whoosh + 1 montée + 1 impact = 6 bruitages sur 12 s, soit 5 par 10 s.
