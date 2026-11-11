# Sons demandés par les fiches et absents de la banque

La banque `banque-cc0/` est faite pour l'interface et l'explication : clics, pops, souffles, montées, impacts, signaux, trois tons de pièce. Elle n'a **ni matières** (tasse, pas, papier, bois, tissu, liquide), **ni instruments**, **ni musique**. Les fiches de style (section 7) en demandent souvent. Cette table dit quoi faire pour chaque son réclamé pendant les douze rendus de test.

Ordre de décision, toujours le même :

1. **Chercher le vrai son** (colonne « À chercher ») dès qu'il y a du réseau : c'est la seule réponse juste pour une matière. Licence lue sur la page, notée dans `audio/sources.json` (`sources-libres.md`).
2. **Sinon le plus proche de la banque** : un pis-aller, choisi d'après le nom et la durée du fichier, **jamais écouté**. Le mesurer (`caler.py attaque`), le poser bas (−8 à −14 dB), et écrire dans la note de livraison « son de remplacement : … ».
3. **Sinon une recette de synthèse**, seulement pour ce qui n'est pas une matière (note d'instrument, mécanisme régulier, souffle) ou pour un style où la synthèse est la palette. Voix, pas, objets et liquides ne se synthétisent pas (`synthese-repli.md`).
4. **Sinon rien.** Un son absent se remarque moins qu'un son hors palette (règle 4).

## Table

| Son demandé (fiche) | Le plus proche dans la banque | Recette de synthèse | À chercher (où, avec quels mots) |
| --- | --- | --- | --- |
| Tasse posée, porcelaine (dîner américain) | `ding/kenney-interface-glass-002.ogg` (0,12 s) pour le tintement, sur `impact/kenney-impact-impactsoft-heavy-000.ogg` très bas pour le contact | non (matière) | Kenney « Impact Sounds » (CC0) : fichiers `impactPlate`, `impactGlass` ; Freesound, CC0 : « cup saucer », « mug set down », « ceramic clink » |
| Chaise qui racle, qui grince | aucun de proche ; à défaut ne rien mettre | non | Kenney « RPG Audio » (CC0) : `creak` ; Freesound, CC0 : « chair scrape », « chair creak wood » |
| Store qui se lève | `transition/kenney-interface-scroll-001.ogg` (1,0 s), pic calé sur le milieu du mouvement | `rouleau(durée)` ci-dessous (souffle grave) | Freesound, CC0 : « roller blind », « window shade », « venetian blinds up » |
| Pas (carrelage, parquet, trottoir) | aucun ; ne pas remplacer par des impacts | non | Kenney « Impact Sounds » (CC0) : `footstep_wood`, `footstep_concrete`, `footstep_carpet` ; Freesound, CC0 : « footsteps tile indoor » |
| Versement d'un liquide (cartoon) | `pop/fs-447910-plop.ogg` (0,24 s) pour la dernière goutte seulement | non | Freesound, CC0 : « pouring coffee cup », « pour water glass » |
| Carton, panneau qui tombe (cartoon) | `impact/fs745291.ogg` (0,29 s) ou `pop/kenney-interface-drop-002.ogg` | non | Kenney « Impact Sounds » : `impactPlank`, `impactWood` ; Freesound, CC0 : « cardboard drop », « sign flip » |
| Frottoir sur le papier (estampe) | `transition/fs-816262-broomstick-whoosh-3-quiet-okm1.ogg` (0,41 s), très bas | `scratch(durée)` du moteur (crayon sur papier), gain 0,15 à 0,2 | Freesound, CC0 : « paper rubbing », « hand rub paper », « baren » |
| Rouleau encreur (estampe) | `transition/kenney-interface-scroll-002.ogg` (1,0 s) | `rouleau(durée)` ci-dessous | Freesound, CC0 : « brayer », « ink roller », « paint roller » |
| Sceau, tampon (estampe) | `impact/kenney-impact-impactsoft-heavy-001.ogg` (0,57 s), −10 dB | `click(700, 0.08)` (clic grave et mat), gain 0,3 | Freesound, CC0 : « rubber stamp », « stamp paper desk » |
| Bois (bloc posé, planche, coup de maillet) | `impact/fs524817.ogg` ou `tick/fs384187.ogg` pour un petit choc sec | non | Kenney « Impact Sounds » : `impactWood`, `impactPlank` ; Freesound, CC0 : « wood block », « wood knock » |
| Instruments japonais (koto, shamisen, flûte) | `ding/fs-349504-triangle-open-04.ogg` pour une ponctuation, rien pour une mélodie | non : une imitation calculée sonne faux | Freesound, CC0 ou CC BY : « koto single note », « shakuhachi phrase », « shamisen » ; sinon une musique CC BY (`sources-libres.md`) |
| Piano (film muet, cartoon) | aucun | `piano(fréquence)` ci-dessous, note par note depuis la timeline ; à annoncer comme synthèse | Notes isolées : Freesound, CC0 : « piano single note » ; morceaux : musiques de film muet en CC BY ou CC0 (`sources-libres.md`, « Musique ») |
| Projecteur de cinéma (film muet) | `glitch/kenney-sci-computernoise-000.ogg` (4 s) très bas : ronronnement de machine, sans le cliquetis | `projecteur(durée, 18)` ci-dessous (un cliquetis par image + souffle) | Freesound, CC0 : « film projector », « 16mm projector loop », « super 8 projector » |
| Triangle, clochette (cartoon) | `ding/fs-349504-triangle-open-04.ogg`, `ding/fs-571513-soft-notifications-bell-ding-d.ogg` | `chime([523.25, 783.99], 1.5, 0.5)` | inutile : la banque suffit |
| Musique de puce (pixel 8 bits) | aucune musique ; bruitages : `ui-blip/`, `riser/kenney-digital-powerup*.ogg` | fond `fonds/retro-puce.ogg` (boucle de 16 s à 120 battements par minute) | OpenGameArt (filtre CC0), musiques « chiptune » ; licence lue sur la page |
| Musique d'accompagnement (cartoon, dîner, lancement) | aucune | fonds `fonds/nappe-calme.ogg`, `pulsation-legere.ogg`, `tension.ogg` (repli, pas de mélodie) | `sources-libres.md`, « Musique » |
| Ambiance de lieu (café, rue, atelier) | `ambience/` : trois tons de pièce à −35 LUFS, à laisser à `data-volume` 1 au plus | non | Freesound, CC0 : « diner ambience », « cafe morning », « workshop room tone » |

Les paquets Kenney cités (kenney.nl/assets, rubrique audio) sont publiés en CC0 ; leur contenu exact est à vérifier au téléchargement. Les mots de recherche sont en anglais parce que les banques le sont.

## Recettes de synthèse (repli annoncé)

À mettre dans la feuille de sons du projet (`audio/sons.py`, voir `synthese-repli.md`). Les fonctions ont été essayées avec le moteur `scripts/sfx` le 11/11/2026 (elles s'exécutent ; feuille d'essai rendue à −18,0 LUFS) ; leur ressemblance avec le vrai son n'a pas été écoutée.

```python
import math
from sfx.synth import SR, bandnoise, blip, click, scratch, chime


def piano(freq, duree=1.2):
    """Note de piano de repli : attaque franche, harmoniques, deux « cordes » un peu désaccordées."""
    a, b = blip(freq, duree, 0.38), blip(freq * 1.003, duree, 0.30)
    c = blip(freq * 2, duree, 0.16)
    return [x * 0.6 + y * 0.4 + z * 0.25 for x, y, z in zip(a, b, c)]


def projecteur(duree, images_par_s=18):
    """Projecteur de cinéma : un cliquetis par image et un souffle de moteur."""
    n = int(duree * SR)
    out = [v * 0.25 for v in bandnoise(n, lambda k: 900, q=0.5)]
    tic, i = click(1100, 0.03), 0.0
    while i < n:
        for k, v in enumerate(tic):
            if int(i) + k < n:
                out[int(i) + k] += v * 0.8
        i += SR / images_par_s
    return out


def rouleau(duree):
    """Rouleau encreur, store qui glisse : souffle grave qui enfle puis retombe (pic au milieu)."""
    n = int(duree * SR)
    bruit = bandnoise(n, lambda k: 350 + 500 * math.sin(math.pi * k / n), q=0.5)
    return [v * math.sin(math.pi * k / n) ** 1.5 for k, v in enumerate(bruit)]


def score(mix, tl):
    for i, f in enumerate([261.63, 329.63, 392.00, 523.25]):          # accord de do roulé, attaque + 8 ms
        mix.put(tl["accord"] + 0.008 + i * 0.09, piano(f), 0.25)
    mix.put(tl["debut"], projecteur(tl["duration"]), 0.06)             # fond de projecteur, très bas
    mix.put(tl["frottoir"], scratch(1.2), 0.18)
    mix.put(tl["store"] - 0.5, rouleau(1.0), 0.22)                     # pic (milieu du son) sur le milieu du mouvement
    mix.put(tl["sceau"] + 0.008, click(700, 0.08), 0.30)
```

Fréquences des notes (tempérament égal, la = 440 Hz) : do 261,63 ; ré 293,66 ; mi 329,63 ; fa 349,23 ; sol 392,00 ; la 440,00 ; si 493,88 ; l'octave au-dessus double la fréquence.

## Quand une fiche demande un son introuvable

Le dire dans la note de livraison, avec ce qui a été fait à la place (« tasse : tintement de verre de la banque, à remplacer par un vrai enregistrement »). Si le même son manque pour plusieurs films, il vaut la peine de le télécharger une fois avec sa licence et de le garder dans les fichiers de la personne (pas dans le plugin, sauf CC0).
