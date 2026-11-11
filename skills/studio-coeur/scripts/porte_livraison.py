#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""porte_livraison.py : la porte chiffrée par laquelle tout film passe avant d'être montré au client.

Usage :
    python3 porte_livraison.py film.mp4 [--fiche chemin/STYLE.md] [--textes textes.json] [--strict]
                               [--json porte.json] [--format 1080x1920] [--sans-fond]
                               [--autoriser-bleu-violet "raison donnée par le client"]

Elle ne lit que le fichier vidéo fini (et, si on les donne, le relevé des textes et la fiche du style).
Besoin : ffmpeg, ffprobe, numpy.

--fiche : lit le bloc « Réglages des contrôles » de la fiche STYLE.md du style (voir fiche_reglages.py).
Sans l'option : mouvement normal, bleu-violet interdit, texte vivant non, taille mini 50 px.

Sept contrôles peuvent donner un FEU ROUGE (film non livrable) :

  1. Diaporama : « est-ce une suite d'images fixes ? ». On lit 12 images/s à 180 px de large, en gris, bas de
     l'image masqué (sous-titres et interface). Entre deux images voisines, on compte la PART DE PIXELS QUI
     CHANGENT (écart de plus de 6 niveaux sur 255 après un léger flou, ou 4 fois le grain mesuré : un grain qui
     grouille partout ne compte pas), une fois retiré ce qu'explique un mouvement d'ensemble de l'image (glissé,
     zoom, rotation, variation de lumière globale : la poussée de caméra sur une image fixe n'est pas une action).
     Une paire d'images est « vivante » si au moins 0,2 % des pixels changent ainsi.
     Le chiffre jugé est la PART DU TEMPS VIVANT à l'intérieur des plans. Ne comptent pas dans ce temps :
     les coupes franches, et les passages d'une image fixe à une autre (fondu, volet : 1,5 s au plus, immobile
     avant et après, plus de 30 % de l'image changée) : changer d'image n'est pas du mouvement.
         Mouvement : normal  → rouge sous 20 %, jaune sous 35 %
         Mouvement : calme   → rouge sous 10 %, jaune sous 20 %   (seuil abaissé, jamais supprimé)
         Mouvement : vif     → rouge sous 35 %, jaune sous 50 %
     Ce chiffre ne dépend ni du contraste ni de la surface qui bouge (un trait fin qui se dessine compte autant
     qu'un grand aplat qui glisse), contrairement à l'ancienne mesure (différence moyenne de toute l'image).
     Un éclair, une secousse ou un changement de couleur ne sont pas des coupes (voir `coupes()`).
  2. Clignotement : plus de 3 changements brusques de luminance ou de couleur par seconde sur au moins 25 % de
     l'image (risque pour les personnes photosensibles). Lu à 30 images/s sur une grille de 18 × 32 cases ;
     une case « saute » quand sa luminance bouge de 25 niveaux (≈ 10 %) ou sa couleur de 45. Un changement
     compte quand les cases qui sautent dans le même sens dépassent de 25 % de l'image celles qui sautent dans
     l'autre (un motif rayé qui défile ne clignote pas). Un éclair (aller et retour en 0,12 s au plus) compte
     pour un changement. Jaune : exactement 3 par seconde, ou plus de 3 sur 10 à 25 % de l'image.
  3. Écran vide : ≥ 0,3 s de suite où moins de 0,2 % des pixels portent un contour (image presque unie),
     hors première et dernière demi-seconde. Jugé sur les contours, pas sur la couleur.
  4. Bleu-violet « look IA » : pixel de teinte 225–300°, saturation ≥ 0,30 (les très clairs ne comptent que
     s'ils sont vifs, saturation ≥ 0,50) ; une image qui en contient ≥ 30 % est une image bleu-violet ;
     ≥ 30 % du film rouge, ≥ 12 % jaune. Le bleu marine en aplat (≈ 210°) passe. Le rouge devient jaune si la
     fiche dit « Bleu-violet : dérogation », ou si le client l'a demandé : --autoriser-bleu-violet "raison".
  5. Texte hors zone sûre, et 6. temps de lecture insuffisant : par `controle_textes.py`, si --textes est donné.
     Sans relevé, ces deux contrôles sont marqués « NON CONTRÔLÉ » et la note de livraison le dira.

Le volume est le septième : il est mesuré ET jugé par `skills/son/scripts/niveau.py mesurer --json` (la porte
l'appelle, elle ne remesure pas à sa façon). Méthode, la seule du studio :
`ffmpeg -hide_banner -nostats -i film.mp4 -map 0:a:0 -af ebur128=peak=true -f null -`, bloc « Summary »
(I = niveau intégré, Peak = crête vraie). Film avec voix ou musique : −14 LUFS ± 1 et crête ≤ −1 dBTP, sinon
rouge. Film sans voix ni musique : passer --sans-fond ; la cible −14 ne s'applique plus, le feu est JAUNE si
la règle « sans fond » du skill `son` est tenue (à écrire dans la note), rouge sinon.
Le film à passer à la porte est le MP4 LIVRÉ (`*-livre.mp4`, produit par `skills/son/scripts/finaliser.py`),
pas le rendu brut : c'est lui qui a le bon niveau sonore.

Signalés en jaune seulement : image figée plus de 3 s, format ou cadence différents de ceux attendus, pas de
piste son, film court (12 s ou moins : un rouge « diaporama » proche du seuil y devient jaune).

Codes de sortie : 0 vert ou jaune, 2 rouge, 1 fichier illisible ou outil manquant.

Ce que la porte ne voit pas : un film qui bouge mais ne raconte rien, un rythme qui s'essouffle, une image
laide. Une porte verte ne dit pas que le film est bon : la planche contact et le relecteur restent obligatoires.
Limites de la mesure « diaporama » : voir references/controles.md.

Inspiration : film_gate.py de huashu-art-motion (alchaincyf, MIT, commit 1468196) : les portes diaporama,
écran vide et bleu-violet, et les seuils des deux dernières. La mesure du mouvement (part de pixels, part du
temps, retrait du mouvement d'ensemble, passages entre images fixes) et le clignotement sont écrits
pour ce plugin et calés sur ses 12 films d'essai et 7 diaporamas fabriqués ; le volume vient du skill `son`.
Pas d'OpenCV.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import numpy as np
except ImportError:
    print("numpy manquant : pip install numpy")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import controle_textes  # noqa: E402
import fiche_reglages   # noqa: E402

IPS_ANALYSE = 12        # images par seconde lues pour le mouvement
LARGEUR = 180           # largeur d'analyse (une image de 1080 px y perd son grain, pas ses traits de 2 px)
SEUIL_PIXEL = 6.0       # écart (0–255, après flou 3×3) à partir duquel un pixel « change »
FACTEUR_GRAIN = 4.0     # … ou 4 fois l'écart médian de l'image (le grain), si c'est plus,
SEUIL_PIXEL_MAX = 16.0  # … sans dépasser 16 (quand toute l'image change, la médiane n'est plus du grain)
SURFACE_VIVANTE = 0.002 # part de pixels qui changent pour qu'une paire d'images soit « vivante »
TOLERANCE_CALAGE = 0.5  # pixel d'erreur de recalage toléré quand l'image entière bouge (caméra)
PART_HORS_CAMERA = 0.15 # quand l'image entière bouge, ce qui bouge « dedans » doit faire 15 % du changement au moins
SEUILS_MOUVEMENT = {"calme": (0.10, 0.20), "normal": (0.20, 0.35), "vif": (0.35, 0.50)}   # (rouge, jaune)
COUPE_SURFACE = 0.25    # une coupe change au moins un quart de l'image d'un coup
PASSAGE_MAX_S, PASSAGE_CALME_S, PASSAGE_SURFACE = 1.5, 0.25, 0.30
SEUIL_CONTOUR, PART_CONTOUR, VIDE_MIN_S, BORD_S = 24, 0.002, 0.3, 0.5
TEINTE_BV, SAT_BV, VAL_BV, PART_IMAGE_BV = (225, 300), 0.30, (0.06, 0.90), 0.30
SAT_VIF = 0.50          # ajout par rapport à la source : un violet vif et lumineux compte aussi
ROUGE_BV, JAUNE_BV = 0.30, 0.12
FIGE_S = 3.0            # image figée plus longtemps que ça : jaune
COURT_S = 12.0          # film court : 12 s ou moins
CLIGNO_IPS, CLIGNO_GRILLE = 30, (18, 32)
CLIGNO_LUMA, CLIGNO_COULEUR = 25.0, 45.0     # saut de luminance (≈ 10 % de l'échelle) ou de couleur d'une case
CLIGNO_MAX, CLIGNO_SURFACE_ROUGE, CLIGNO_SURFACE_JAUNE = 3, 0.25, 0.10
CLIGNO_ECLAIR_S = 0.12  # aller et retour plus court que ça : un seul changement (un éclair)
CIBLE_LUFS, TOL_LUFS, PLAFOND_DBTP = -14.0, 1.0, -1.0   # repli seulement : le skill `son` porte les vrais seuils


def sonde(chemin):
    """Largeur, hauteur, durée, cadence, présence d'une piste son."""
    j = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate:format=duration",
         "-of", "json", str(chemin)]))
    video = next(s for s in j["streams"] if s["codec_type"] == "video")
    num, den = video["r_frame_rate"].split("/")
    return {"largeur": int(video["width"]), "hauteur": int(video["height"]),
            "duree": float(j["format"]["duration"]), "ips": round(int(num) / max(1, int(den)), 2),
            "son": any(s["codec_type"] == "audio" for s in j["streams"])}


def images(chemin, ips, largeur, hauteur, format_pixel):
    """Lit le film image par image (sans tout charger en mémoire)."""
    canaux = 1 if format_pixel == "gray" else 3
    taille = largeur * hauteur * canaux
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(chemin), "-vf",
                          f"fps={ips},scale={largeur}:{hauteur}:flags=area", "-pix_fmt", format_pixel,
                          "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    while True:
        brut = p.stdout.read(taille)
        if len(brut) < taille:
            break
        forme = (hauteur, largeur) if canaux == 1 else (hauteur, largeur, 3)
        yield np.frombuffer(brut, np.uint8).reshape(forme)
    p.wait()


def plages(drapeaux, ips, duree_min):
    """Suites de True d'au moins duree_min secondes → [(début, fin)] en secondes."""
    sorties, depart = [], None
    for i, v in enumerate(list(drapeaux) + [False]):
        if v and depart is None:
            depart = i
        elif not v and depart is not None:
            if (i - depart) / ips >= duree_min - 1e-9:
                sorties.append((round(depart / ips, 2), round(i / ips, 2)))
            depart = None
    return sorties


# --- Mouvement -------------------------------------------------------------------------------------------

def flou3(a):
    """Moyenne 3×3 : efface le grain d'un pixel, garde un trait."""
    p = np.pad(a, 1, mode="edge")
    return (p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] + p[1:-1, :-2] + p[1:-1, 1:-1] + p[1:-1, 2:]
            + p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:]) / 9


def seuil_pixel(ecart):
    """Écart à partir duquel un pixel « change » : 6 niveaux, ou 4 fois le grain (écart médian), 16 au plus."""
    return min(SEUIL_PIXEL_MAX, max(SEUIL_PIXEL, FACTEUR_GRAIN * float(np.median(ecart))))


def reduire2(a):
    h, w = a.shape[0] // 2 * 2, a.shape[1] // 2 * 2
    return a[:h, :w].reshape(h // 2, 2, w // 2, 2).mean((1, 3))


def gradients(m):
    gx, gy = np.zeros_like(m), np.zeros_like(m)
    gx[:, 1:-1] = (m[:, 2:] - m[:, :-2]) / 2
    gy[1:-1, :] = (m[2:, :] - m[:-2, :]) / 2
    return gx, gy


def deplacer(a, qx, qy):
    """a échantillonnée en (x + qx, y + qy), interpolation bilinéaire, bords répétés."""
    h, w = a.shape
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    x, y = np.clip(x + qx, 0, w - 1.001), np.clip(y + qy, 0, h - 1.001)
    x0, y0 = x.astype(np.int32), y.astype(np.int32)
    fx, fy = x - x0, y - y0
    return (a[y0, x0] * (1 - fx) * (1 - fy) + a[y0, x0 + 1] * fx * (1 - fy)
            + a[y0 + 1, x0] * (1 - fx) * fy + a[y0 + 1, x0 + 1] * fx * fy)


def champ(p, forme):
    """Déplacement d'ensemble (glissé a, b ; zoom s ; rotation r) en chaque pixel d'une image de cette forme."""
    h, w = forme
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    x, y = x - w / 2, y - h / 2
    return p[0] + p[2] * x - p[3] * y, p[1] + p[2] * y + p[3] * x


def mouvement_ensemble(a, b):
    """Cherche le mouvement d'ensemble qui fait passer de l'image a à l'image b (du grossier au fin), et rend
    (a recalée sur b, plus grand déplacement en pixels, gain et décalage de lumière)."""
    niveaux = [(a, b)]
    for _ in range(2):
        niveaux.append((reduire2(niveaux[-1][0]), reduire2(niveaux[-1][1])))
    p = np.zeros(4, np.float64)                       # a, b en pixels du niveau le plus fin ; s, r sans unité
    lumiere = (0.0, 0.0)
    for k in (2, 1, 0):
        ak, bk = niveaux[k]
        ech = 2 ** k
        for _ in range(2):
            qx, qy = champ((p[0] / ech, p[1] / ech, p[2], p[3]), ak.shape)
            ar = deplacer(ak, qx, qy)
            d, m = bk - ar, (bk + ar) / 2
            gx, gy = gradients(m)
            h, w = ak.shape
            y, x = np.mgrid[0:h, 0:w].astype(np.float32)
            x, y = x - w / 2, y - h / 2
            cols = np.stack([gx, gy, gx * x + gy * y, gy * x - gx * y, m - m.mean(), np.ones_like(m)], -1).reshape(-1, 6)
            dv = d.reshape(-1)
            garde = np.ones(len(dv), bool)
            sol = np.zeros(6)
            for _ in range(3):                        # moindres carrés en écartant ce qui bouge pour de bon
                c = cols[garde]
                if len(c) < 60:
                    break
                try:
                    sol = np.linalg.solve(c.T @ c + 1e-3 * np.eye(6), c.T @ dv[garde])
                except np.linalg.LinAlgError:
                    break
                reste = np.abs(dv - cols @ sol)
                garde = reste < max(3.0, 2.5 * float(np.median(reste[garde])))
            p += (sol[0] * ech, sol[1] * ech, sol[2], sol[3])
            lumiere = (float(sol[4]), float(sol[5]))
    qx, qy = champ(p, a.shape)
    ar = deplacer(a, qx, qy)
    ar = ar + lumiere[0] * (ar - ar.mean()) + lumiere[1]
    return ar, float(np.hypot(qx, qy).max()), lumiere


def comparer(a, b):
    """Deux images voisines (déjà floutées) → (part de pixels qui changent, part qui change une fois retiré le
    mouvement d'ensemble, déplacement d'ensemble en pixels)."""
    ecart = np.abs(b - a)
    seuil = seuil_pixel(ecart)
    brut = float((ecart > seuil).mean())
    if brut < SURFACE_VIVANTE / 4:
        return brut, brut, 0.0
    ar, dep, _ = mouvement_ensemble(a, b)
    if dep < 0.03:                                    # rien ne bouge d'un bloc : pas de caméra à retirer
        return brut, brut, dep
    gx, gy = gradients((ar + b) / 2)
    reste = np.abs(b - ar)
    seuil = seuil_pixel(reste)
    local = float((reste > seuil + TOLERANCE_CALAGE * np.hypot(gx, gy)).mean())
    if local < PART_HORS_CAMERA * brut:               # ce qui reste n'est qu'un résidu du recalage
        local = 0.0
    return brut, min(brut, local), dep


def contours(img):
    gx, gy = gradients(img)
    return np.hypot(gx, gy) > 10


def coupes(brut, vues):
    """Coupes franches : un saut isolé (au moins un quart de l'image, trois fois plus que ses deux voisins),
    dont l'image d'après ne revient pas à celle d'avant (sinon c'est un éclair ou une secousse) et dont le
    dessin change (sinon c'est un changement de couleur ou de lumière sur la même image)."""
    n = len(brut)
    coupe = np.zeros(n, bool)
    for i in range(n):
        voisins = max(brut[i - 1] if i else 0.0, brut[i + 1] if i + 1 < n else 0.0)
        if brut[i] < COUPE_SURFACE or brut[i] < 3 * voisins:
            continue
        avant, apres = vues[i], vues[i + 1]
        plus_tard = vues[min(i + 4, len(vues) - 1)]                # un tiers de seconde après
        ecart = np.abs(plus_tard - avant)
        retour = float((ecart > seuil_pixel(ecart)).mean())
        if retour < 0.5 * brut[i]:
            continue                                               # éclair, secousse : l'image d'avant est revenue
        ca, cb = contours(avant), contours(apres)
        commun, total = float((ca & cb).sum()), float((ca | cb).sum())
        if total > 0 and commun / total >= 0.6:
            continue                                               # même dessin : changement de couleur
        coupe[i] = True
    return coupe


def passages(vivante, coupe, vues):
    """Passages d'une image fixe à une autre (fondu, volet, glissé) : une suite de paires vivantes de 1,5 s au
    plus, calme avant et après (0,25 s), et dont l'image d'arrivée diffère de l'image de départ sur plus de
    30 % de sa surface. Rendu : masque des paires concernées."""
    n = len(vivante)
    masque = np.zeros(n, bool)
    calme = int(round(PASSAGE_CALME_S * IPS_ANALYSE))
    i = 0
    while i < n:
        if not vivante[i] or coupe[i]:
            i += 1
            continue
        j = i
        while j < n and vivante[j] and not coupe[j]:
            j += 1                                                 # paires i … j-1
        avant_calme = i == 0 or not vivante[max(0, i - calme):i].any()
        apres_calme = j >= n or not vivante[j:min(n, j + calme)].any()
        if (j - i) / IPS_ANALYSE <= PASSAGE_MAX_S and avant_calme and apres_calme and not (i == 0 and j >= n):
            ecart = np.abs(vues[j] - vues[i])
            if float((ecart > seuil_pixel(ecart)).mean()) >= PASSAGE_SURFACE:
                masque[i:j] = True
        i = j
    return masque


def mesurer_mouvement_et_vides(chemin, info, bande_bas):
    h = int(round(info["hauteur"] * LARGEUR / info["largeur"] / 2) * 2)
    utile = int(h * (1 - bande_bas))                      # on masque le bas (sous-titres, interface)
    bruts, locaux, deps, vides, figees, vues = [], [], [], [], [], []
    for img in images(chemin, IPS_ANALYSE, LARGEUR, h, "gray"):
        zone = img[:utile].astype(np.float32)
        gx, gy = np.abs(np.diff(zone, axis=1))[:-1, :], np.abs(np.diff(zone, axis=0))[:, :-1]
        vides.append((np.hypot(gx, gy) > SEUIL_CONTOUR * 180 / 320).mean() < PART_CONTOUR)
        vue = flou3(zone)
        if vues:
            b, l, d = comparer(vues[-1], vue)
            bruts.append(b)
            locaux.append(l)
            deps.append(d)
        vues.append(vue)
    n = len(bruts)
    if n < IPS_ANALYSE:
        raise ValueError("film trop court ou illisible")
    brut, local = np.array(bruts), np.array(locaux)
    coupe = coupes(brut, vues)
    vivante = (local >= SURFACE_VIVANTE) & ~coupe
    passage = passages(vivante, coupe, vues)
    dans_plan = ~coupe & ~passage
    compte = vivante & dans_plan
    part = float(compte.sum() / max(1, dans_plan.sum()))
    # pire fenêtre de 10 s (un film peut bouger au début et mourir ensuite)
    f = 10 * IPS_ANALYSE
    pire, pire_t = part, 0.0
    if n > f:
        cumul_b, cumul_p = np.concatenate([[0], np.cumsum(compte)]), np.concatenate([[0], np.cumsum(dans_plan)])
        parts = (cumul_b[f:] - cumul_b[:-f]) / np.maximum(1, cumul_p[f:] - cumul_p[:-f])
        pire, pire_t = float(parts.min()), round(int(parts.argmin()) / IPS_ANALYSE, 1)
    # écrans vides : hors bords du film et hors images voisines d'une coupe
    v = np.array(vides)
    ok = np.ones(len(v), bool)
    bord = int(round(BORD_S * IPS_ANALYSE))
    ok[:bord] = False
    ok[len(v) - bord:] = False
    for i in np.where(coupe)[0]:
        ok[i] = False
        ok[min(i + 1, len(v) - 1)] = False
    surfaces = local[compte]
    return {"part_mouvement": round(part, 4), "pire_fenetre_10s": round(pire, 4), "pire_fenetre_debut_s": pire_t,
            "surface_mediane_qui_bouge": round(float(np.median(surfaces)), 4) if len(surfaces) else 0.0,
            "part_temps_image_entiere_en_mouvement": round(float((np.array(deps) >= 0.03).mean()), 3),
            "part_temps_brut": round(float(((brut >= SURFACE_VIVANTE) & dans_plan).sum() / max(1, dans_plan.sum())), 4),
            "coupes": int(coupe.sum()), "coupes_s": [round((i + 1) / IPS_ANALYSE, 2) for i in np.where(coupe)[0]],
            "passages_entre_images_fixes_s": plages(passage, IPS_ANALYSE, 0),
            "ecrans_vides_s": plages(v & ok, IPS_ANALYSE, VIDE_MIN_S),
            "images_figees_s": plages(brut < 0.0002, IPS_ANALYSE, FIGE_S)}


# --- Clignotement ----------------------------------------------------------------------------------------

def changements(signal, seuil):
    """Instants (indices) où un signal fait un saut d'au moins `seuil` dans un sens, entre deux paliers ou deux
    retournements. Rend [(indice de fin du saut, sens)]."""
    sorties = []
    bas = haut = signal[0]
    sens = 0
    for i in range(1, len(signal)):
        v = signal[i]
        if sens >= 0:
            if v > haut:
                haut = v
                if sens == 0 and haut - bas >= seuil:
                    sens = 1
                    sorties.append((i, 1))
            elif haut - v >= seuil:
                sens, bas = -1, v
                sorties.append((i, -1))
            elif sens == 0 and v < bas:
                bas = v
        if sens <= 0:
            if v < bas:
                bas = v
                if sens == 0 and haut - bas >= seuil:
                    sens = -1
                    sorties.append((i, -1))
            elif v - bas >= seuil:
                sens, haut = 1, v
                sorties.append((i, 1))
            elif sens == 0 and v > haut:
                haut = v
    return sorties


def compter_clignotements(nets, part, n_cases):
    """nets : par signal, somme signée des sauts des cases à chaque image. Un changement brusque « de grande
    surface » est une image où les cases qui sautent DANS LE MÊME SENS dépassent de `part` de l'image celles qui
    sautent dans l'autre (un motif rayé qui défile fait monter autant de cases qu'il en fait descendre : il ne
    compte pas). Rend (plus grand nombre de changements dans une seconde, masque des instants au-dessus de 3)."""
    n = len(nets[0])
    eclair = int(round(CLIGNO_ECLAIR_S * CLIGNO_IPS))
    pire, au_dessus = 0, np.zeros(n, bool)
    idx = np.arange(n)
    for net in nets:
        evenements, i = [], 0
        while i < n:
            v = net[i] + (net[i + 1] if i + 1 < n else 0)        # le même saut tombe parfois sur deux images voisines
            if abs(net[i]) >= part * n_cases:
                evenements.append((i, 1 if net[i] > 0 else -1))
            elif abs(v) >= part * n_cases and (net[i] > 0) == (v > 0) and net[i] != 0:
                evenements.append((i, 1 if v > 0 else -1))
                i += 1
            i += 1
        # une même montée (fondu, glissé) fait sauter les cases les unes après les autres : des sauts de même
        # sens à moins de 0,2 s l'un de l'autre ne font qu'un changement
        fusion = []
        for ev in evenements:
            if fusion and ev[1] == fusion[-1][1] and ev[0] - dernier <= int(0.2 * CLIGNO_IPS):
                dernier = ev[0]
                continue
            fusion.append(ev)
            dernier = ev[0]
        evenements = fusion
        marque, k = np.zeros(n + 1, np.int16), 0
        while k < len(evenements):
            marque[evenements[k][0]] = 1
            # éclair : le saut suivant est en sens inverse et arrive vite → les deux ne font qu'un changement
            if (k + 1 < len(evenements) and evenements[k + 1][1] != evenements[k][1]
                    and evenements[k + 1][0] - evenements[k][0] <= eclair):
                k += 2
            else:
                k += 1
        cumul = np.cumsum(marque)
        par_seconde = cumul[idx] - cumul[np.maximum(0, idx - CLIGNO_IPS)]
        pire = max(pire, int(par_seconde.max()))
        au_dessus |= par_seconde > CLIGNO_MAX
    return pire, au_dessus


def mesurer_clignotement(chemin):
    """Changements brusques de luminance ou de couleur, par seconde glissante, sur une grande surface."""
    gl, gh = CLIGNO_GRILLE
    vues = [img.astype(np.float32) for img in images(chemin, CLIGNO_IPS, gl, gh, "rgb24")]
    n, cases = len(vues), gl * gh
    vide = {"clignotement_max_par_s": 0, "clignotement_max_par_s_petite_surface": 0, "clignotement_plages_s": [],
            "clignotement_plages_petite_surface_s": []}
    if n < CLIGNO_IPS // 2:
        return vide
    pile = np.stack(vues).reshape(n, cases, 3)
    r, g, b = pile[..., 0], pile[..., 1], pile[..., 2]
    signaux = [(0.2126 * r + 0.7152 * g + 0.0722 * b, CLIGNO_LUMA), (r - g, CLIGNO_COULEUR), (b - (r + g) / 2, CLIGNO_COULEUR)]
    nets = []
    for signal, seuil in signaux:
        net = np.zeros(n, np.int32)
        for c in np.where(signal.max(0) - signal.min(0) >= seuil)[0]:
            for i, sens in changements(signal[:, c], seuil):
                net[i] += sens
        nets.append(net)
    k_rouge, m_rouge = compter_clignotements(nets, CLIGNO_SURFACE_ROUGE, cases)
    k_jaune, m_jaune = compter_clignotements(nets, CLIGNO_SURFACE_JAUNE, cases)
    return {"clignotement_max_par_s": k_rouge, "clignotement_max_par_s_petite_surface": k_jaune,
            "clignotement_plages_s": plages(m_rouge, CLIGNO_IPS, 0),
            "clignotement_plages_petite_surface_s": plages(m_jaune, CLIGNO_IPS, 0)}


def mesurer_bleu_violet(chemin, info):
    larg, ips = 160, 2
    h = max(2, int(round(info["hauteur"] * larg / info["largeur"] / 2)) * 2)
    drapeaux = []
    for img in images(chemin, ips, larg, h, "rgb24"):
        f = img.astype(np.float32) / 255
        r, g, b = f[..., 0], f[..., 1], f[..., 2]
        maxi, mini = f.max(-1), f.min(-1)
        ecart = maxi - mini + 1e-6
        sat = ecart / (maxi + 1e-6)
        teinte = np.where(maxi == r, ((g - b) / ecart) % 6, np.where(maxi == g, (b - r) / ecart + 2, (r - g) / ecart + 4)) * 60
        # trop sombre = noir, pas violet ; très clair ET peu saturé = lilas pâle, toléré ; vif = compté
        masque = ((teinte >= TEINTE_BV[0]) & (teinte <= TEINTE_BV[1]) & (sat >= SAT_BV)
                  & (maxi >= VAL_BV[0]) & ((maxi <= VAL_BV[1]) | (sat >= SAT_VIF)))
        drapeaux.append(masque.mean() >= PART_IMAGE_BV)
    part = float(np.mean(drapeaux)) if drapeaux else 0.0
    return {"part_bleu_violet": round(part, 3), "plages_bleu_violet_s": plages(drapeaux, ips, 1.0)}


def mesurer_volume(chemin, sans_fond):
    """Volume du film, mesuré et jugé par `skills/son/scripts/niveau.py mesurer --json` (la seule mesure du
    studio : `ffmpeg -af ebur128=peak=true`, bloc « Summary », lignes I, LRA, Peak). Rend
    {feu, lufs, crete_dbtp, lra, remarques, source}, ou None si rien n'est mesurable.
    Si le skill `son` n'est pas installé à côté, la même commande ffmpeg est lancée ici, avec un jugement
    réduit (cible ±1 LU et crête ≤ −1 dBTP ; sans fond : jaune)."""
    niveau = Path(__file__).resolve().parents[2] / "son" / "scripts" / "niveau.py"
    if niveau.is_file():
        r = subprocess.run([sys.executable, str(niveau), "mesurer", str(chemin), "--json"] + (["--sans-fond"] if sans_fond else []),
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8"))
        try:
            j = json.loads(r.stdout[r.stdout.index("{"):])
            return {"feu": j["feu"].upper(), "lufs": j["lufs"], "crete_dbtp": j["crete_dbtp"], "lra": j.get("lra"),
                    "remarques": j.get("remarques", []), "source": "son/scripts/niveau.py"}
        except (ValueError, KeyError):
            return None                                   # niveau.py n'a rien pu mesurer (piste vide)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(chemin), "-map", "0:a:0", "-af",
                        "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    bloc = r.stderr[r.stderr.rfind("Summary:"):] if "Summary:" in r.stderr else ""
    i = re.search(r"\bI:\s*(-?[\d.]+)\s*LUFS", bloc)
    tp = re.search(r"Peak:\s*(-?[\d.]+)\s*dBFS", bloc)
    lra = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", bloc)
    if not i or not tp or float(i.group(1)) <= -70:
        return None
    lufs, crete = float(i.group(1)), float(tp.group(1))
    remarques, feu = ["skill `son` introuvable à côté de ce skill : jugement réduit (cible et crête seulement)"], "VERT"
    if crete > PLAFOND_DBTP + 0.05:
        feu = "ROUGE"
        remarques.append(f"crête {crete:.1f} dBTP au-dessus du plafond {PLAFOND_DBTP:g}")
    if sans_fond:
        feu = "ROUGE" if feu == "ROUGE" or lufs > CIBLE_LUFS + TOL_LUFS else "JAUNE"
        remarques.append("film sans voix ni musique : la cible ne s'applique pas, à écrire dans la note de livraison")
    elif abs(lufs - CIBLE_LUFS) > TOL_LUFS:
        feu = "ROUGE"
        remarques.append(f"{lufs - CIBLE_LUFS:+.1f} LU par rapport à {CIBLE_LUFS:g} LUFS (tolérance ±{TOL_LUFS:g})")
    return {"feu": feu, "lufs": lufs, "crete_dbtp": crete, "lra": float(lra.group(1)) if lra else None,
            "remarques": remarques, "source": "ffmpeg ebur128=peak=true (repli)"}


def option(args, nom, defaut=None):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else defaut


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 1
    film = Path(args[0])
    reglages, avertissements = fiche_reglages.option_fiche(args)
    try:
        info = sonde(film)
        vertical = info["hauteur"] > info["largeur"]
        mesures = mesurer_mouvement_et_vides(film, info, 0.19 if vertical else 0.12)
        mesures.update(mesurer_clignotement(film))
        mesures.update(mesurer_bleu_violet(film, info))
    except (OSError, subprocess.CalledProcessError, StopIteration, ValueError) as e:
        print(f"Film illisible, ou ffmpeg / ffprobe absent : {e}")
        return 1

    controles = []                                         # {nom, feu, valeur, detail}
    def ajouter(nom, feu, valeur, detail=""):
        controles.append({"nom": nom, "feu": feu, "valeur": valeur, "detail": detail})

    court = info["duree"] <= COURT_S + 1e-6
    # 1. diaporama
    p = mesures["part_mouvement"]
    rouge, jaune = SEUILS_MOUVEMENT[reglages["mouvement"]]
    feu = "ROUGE" if p < rouge else "JAUNE" if p < jaune else "VERT"
    adouci = feu == "ROUGE" and court and p >= rouge / 2
    if adouci:
        feu = "JAUNE"
    detail = ""
    if feu != "VERT":
        detail = (f"part du temps où quelque chose bouge dans les plans ; mouvement « {reglages['mouvement']} » : "
                  f"rouge < {rouge:.0%}, jaune < {jaune:.0%}. ")
        if info["duree"] > 10.5:
            detail += f"Pire fenêtre de 10 s : {mesures['pire_fenetre_10s']:.0%} à partir de {mesures['pire_fenetre_debut_s']} s. "
        if mesures["passages_entre_images_fixes_s"]:
            detail += f"{len(mesures['passages_entre_images_fixes_s'])} passage(s) d'une image fixe à une autre non compté(s). "
        if mesures["part_temps_brut"] - p > 0.15:
            detail += (f"L'image entière bouge {mesures['part_temps_brut']:.0%} du temps (caméra, zoom) mais rien "
                       "ne bouge dedans : une poussée de caméra sur une image fixe n'est pas une action. ")
        if adouci:
            detail += f"Film de {COURT_S:g} s ou moins et chiffre proche du seuil : rouge ramené à jaune. "
        detail += "Donner une action à chaque plan (pas un fondu de plus), faire vivre le fond"
    ajouter("diaporama (temps où ça bouge dans les plans)", feu, f"{p:.0%}", detail)
    # 2. clignotement
    k, k_petit = mesures["clignotement_max_par_s"], mesures.get("clignotement_max_par_s_petite_surface", 0)
    if k > CLIGNO_MAX:
        ajouter("clignotement (photosensibilité)", "ROUGE", f"{k} par seconde",
                f"plus de {CLIGNO_MAX} changements brusques par seconde sur {CLIGNO_SURFACE_ROUGE:.0%} de l'image ou plus, à "
                + ", ".join(f"{a}–{b} s" for a, b in mesures["clignotement_plages_s"][:6])
                + " : espacer les éclairs et les changements de couleur, ou réduire leur surface")
    elif k == CLIGNO_MAX or k_petit > CLIGNO_MAX:
        ajouter("clignotement (photosensibilité)", "JAUNE", f"{max(k, k_petit)} par seconde",
                (f"{k_petit} changements brusques par seconde sur {CLIGNO_SURFACE_JAUNE:.0%} à {CLIGNO_SURFACE_ROUGE:.0%} de l'image, à "
                 + ", ".join(f"{a}–{b} s" for a, b in mesures["clignotement_plages_petite_surface_s"][:6])
                 if k_petit > CLIGNO_MAX else f"exactement {CLIGNO_MAX} par seconde sur une grande surface : à la limite")
                + " : aller voir")
    else:
        ajouter("clignotement (photosensibilité)", "VERT", f"{k} par seconde")
    # 3. écrans vides
    vides = mesures["ecrans_vides_s"]
    ajouter("écrans vides ≥ 0,3 s", "ROUGE" if vides else "VERT", len(vides),
            "à " + ", ".join(f"{a}–{b} s" for a, b in vides) if vides else "")
    # 4. bleu-violet
    bv = mesures["part_bleu_violet"]
    raison = option(args, "--autoriser-bleu-violet")
    if not raison and reglages["bleu_violet"] == "dérogation":
        raison = "dérogation écrite dans la fiche du style"
    feu = "ROUGE" if bv >= ROUGE_BV else "JAUNE" if bv >= JAUNE_BV else "VERT"
    detail = ""
    if feu != "VERT":
        detail = "plages : " + ", ".join(f"{a}–{b} s" for a, b in mesures["plages_bleu_violet_s"])
        if feu == "ROUGE" and raison:
            feu, detail = "JAUNE", detail + f" ; autorisé : {raison}"
    ajouter("palette bleu-violet « look IA »", feu, f"{bv:.0%}", detail)
    # 5 et 6. textes
    chemin_textes = option(args, "--textes")
    if chemin_textes:
        try:
            donnees = json.loads(Path(chemin_textes).read_text(encoding="utf-8"))
            res, rouges, jaunes = controle_textes.controler(donnees, "--strict" in args, reglages)
            hors = [r for r in res if any("zone sûre" in x and "non contrôlée" not in x for x in r["pourquoi"])]
            lents = [r for r in res if any("temps de lecture" in x or "sous-titre" in x for x in r["pourquoi"])]
            petits = [r for r in res if any("px de haut" in x for x in r["pourquoi"])]
            ajouter("texte hors zone sûre", "ROUGE" if hors else "VERT", len(hors),
                    " ; ".join(f"{r['id']} ({r['debut']} s)" for r in hors))
            ajouter("temps de lecture", "ROUGE" if lents else "VERT", len(lents),
                    " ; ".join(f"{r['id']} ({r['debut']} s)" for r in lents))
            if petits:
                ajouter(f"texte sous {reglages['taille_mini']} px", "JAUNE", len(petits),
                        " ; ".join(f"{r['id']}" for r in petits))
            if donnees.get("canvas_sans_texte_declare"):
                ajouter("texte dessiné dans un canvas", "JAUNE", "non relevé",
                        "le relevé automatique ne lit pas un canvas : compléter textes.json à la main "
                        "(gabarits/textes-canvas.json) ou écrire dans la note qu'il n'y a pas de texte dedans")
        except (OSError, ValueError, KeyError) as e:
            ajouter("textes (zone sûre, temps de lecture)", "NON CONTRÔLÉ", "-", f"relevé illisible : {e}")
    else:
        ajouter("textes (zone sûre, temps de lecture)", "NON CONTRÔLÉ", "-",
                "aucun relevé --textes : lancer relever_textes.py, ou écrire dans la note que le film n'a aucun texte")
    # Volume : mesuré et jugé par le skill `son`
    sans_fond = "--sans-fond" in args or "--sans-voix-ni-musique" in args
    volume = mesurer_volume(film, sans_fond) if info["son"] else None
    lufs = volume["lufs"] if volume else None
    if not info["son"]:
        ajouter("son", "JAUNE", "aucune piste", "un film muet paraît inachevé : voir le skill `son`")
    elif volume is None:
        ajouter("volume", "JAUNE", "non mesuré", "piste son vide ou illisible")
    else:
        ajouter("volume" + (" (film sans voix ni musique)" if sans_fond else ""), volume["feu"],
                f"{lufs:.1f} LUFS, crête {volume['crete_dbtp']:.1f} dBTP", " ".join(volume["remarques"]))
    # Jaunes d'information
    if mesures["images_figees_s"]:
        ajouter("image figée > 3 s", "JAUNE", len(mesures["images_figees_s"]),
                "à " + ", ".join(f"{a}–{b} s" for a, b in mesures["images_figees_s"]) + " : seule la tenue finale peut être immobile")
    attendu = option(args, "--format", "1080x1920")
    if f"{info['largeur']}x{info['hauteur']}" != attendu:
        ajouter("format", "JAUNE", f"{info['largeur']}x{info['hauteur']}", f"attendu {attendu}")
    if abs(info["ips"] - 30) > 0.1:
        ajouter("cadence", "JAUNE", f"{info['ips']} i/s", "30 i/s attendues, sauf si la fiche du style dit autre chose")
    if court:
        ajouter("film court", "JAUNE", f"{info['duree']:.1f} s",
                f"{COURT_S:g} s ou moins : peu d'images pour juger le mouvement, regarder la planche de près")
    for a in avertissements:
        ajouter("fiche du style", "JAUNE", "-", a)

    feux = [c["feu"] for c in controles]
    bilan = "ROUGE" if "ROUGE" in feux else "JAUNE" if ("JAUNE" in feux or "NON CONTRÔLÉ" in feux) else "VERT"
    print(f"{film.name} : {info['largeur']}x{info['hauteur']}, {info['ips']} i/s, {info['duree']:.1f} s, "
          f"{mesures['coupes']} coupe(s), son {'oui' if info['son'] else 'non'}"
          + (f", {lufs:.1f} LUFS" if lufs is not None else ""))
    print("  " + fiche_reglages.resume(reglages))
    for c in controles:
        print(f"  [{c['feu']:12}] {c['nom']} : {c['valeur']}" + (f"  → {c['detail']}" if c["detail"] else ""))
    print({"ROUGE": "FEU ROUGE : film non livrable. Corriger, re-rendre, relancer la porte.",
           "JAUNE": "FEU JAUNE : livrable après avoir regardé chaque point jaune et écrit pourquoi il est acceptable.",
           "VERT": "FEU VERT : la porte est passée. Reste la planche contact et le relecteur indépendant."}[bilan])
    sortie = option(args, "--json")
    if sortie:
        Path(sortie).write_text(json.dumps({"film": film.name, "info": info, "volume_lufs": lufs,
                                            "crete_dbtp": volume["crete_dbtp"] if volume else None,
                                            "volume": volume, "sans_fond": sans_fond,
                                            "reglages": {k: v for k, v in reglages.items() if k != "lus"},
                                            "mesures": mesures, "controles": controles, "bilan": bilan,
                                            "bleu_violet_autorise": raison},
                                           ensure_ascii=False, indent=2), encoding="utf-8")
    return 2 if bilan == "ROUGE" else 0


if __name__ == "__main__":
    sys.exit(main())
