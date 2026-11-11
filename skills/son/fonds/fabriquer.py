#!/usr/bin/env python3
"""Fabrique les fonds sonores de repli du studio (aucun échantillon, aucun téléchargement).

  PYTHONDONTWRITEBYTECODE=1 python3 fabriquer.py [--dossier <sortie>] [--seulement nappe-calme,tension] [--wav]

Chaque fond est calculé avec le moteur de repli `../scripts/sfx/` (whaleyxbt/claude-motion, MIT, non modifié) :
oscillateurs, bruit filtré et réverbération calculée. Les fonds sont BOUCLABLES : tout ce qui dépasse la fin est
reporté au début (écriture circulaire), et la réverbération est calculée sur deux tours dont on garde le second.
Niveau : un gain constant vers -18 LUFS (mesure BS.1770 du moteur). Sortie : OGG Vorbis (et WAV avec --wav).
Même graine = même fichier. Compter une à deux minutes pour les quatre (Python pur).
"""
import sys
sys.dont_write_bytecode = True
import argparse, math, os, random, struct, subprocess, wave
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "scripts"))
from sfx import dsp
from sfx.synth import SR, bandnoise, blip, click, pad
from sfx.loudness import integrated_lufs, true_peak

CIBLE_LUFS = -18.0


class Boucle:
    """Tampon stéréo circulaire : ce qui dépasse la fin revient au début, donc la boucle est sans couture."""

    def __init__(self, duree):
        self.n = int(round(duree * SR))
        self.g = [0.0] * self.n
        self.d = [0.0] * self.n

    def poser(self, t, mono, gain=1.0, pan=0.0):
        gl, gr = dsp.pan_gains(pan)
        self.stereo(t, [v * gl for v in mono], [v * gr for v in mono], gain)

    def stereo(self, t, gauche, droite, gain=1.0):
        n, i0 = self.n, int(round(t * SR)) % self.n
        for k, (a, b) in enumerate(zip(gauche, droite)):
            i = (i0 + k) % n
            self.g[i] += a * gain
            self.d[i] += b * gain

    def reverberer(self, part=0.3, taille=0.8, amorti=0.5):
        """Ajoute une réverbération en régime établi (deux tours calculés, second gardé)."""
        mono = [(a + b) * 0.5 for a, b in zip(self.g, self.d)]
        wl, wr = dsp.reverb(mono + mono, size=taille, damp=amorti)
        n = self.n
        self.g = [a + part * w for a, w in zip(self.g, wl[n:])]
        self.d = [b + part * w for b, w in zip(self.d, wr[n:])]


def fenetre(x, montee, descente):
    """Enveloppe en cosinus : montée et descente en secondes."""
    n, a, b = len(x), int(montee * SR), int(descente * SR)
    out = list(x)
    for i in range(min(a, n)):
        out[i] *= 0.5 - 0.5 * math.cos(math.pi * i / a)
    for i in range(min(b, n)):
        out[n - 1 - i] *= 0.5 - 0.5 * math.cos(math.pi * i / b)
    return out


def accord(boucle, t, duree, freqs, gain, fondu=2.0, desaccord=0.6):
    """Un accord tenu (nappe du moteur), fondu d'entrée et de sortie, posé en boucle."""
    g, d = pad(duree + fondu, [(0, freqs)], detune=desaccord, tremolo=0.0)
    boucle.stereo(t, fenetre(g, fondu, fondu), fenetre(d, fondu, fondu), gain)


# Notes (Hz). Registre médium : un fond tout en graves ne s'entend pas sur un téléphone (règle 10).
DO3, RE3, MI3, FA3, SOL3, LA3, SI3 = 130.81, 146.83, 164.81, 174.61, 196.00, 220.00, 246.94
DO4, RE4, MI4, FA4, SOL4, LA4, SI4, DO5, MI5, SOL5 = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 659.26, 783.99


def nappe_calme():
    """Nappe lente, 4 accords de 5 s (la mineur 7, fa majeur 7, do majeur, sol), sans pulsation. 20 s."""
    b = Boucle(20.0)
    suite = [[LA3, DO4, MI4, SOL4], [FA3, LA3, DO4, MI4], [DO4, MI4, SOL4, DO5], [SOL3, SI3, RE4, SOL4]]
    for k, f in enumerate(suite):
        accord(b, k * 5.0 - 1.0, 5.0, f, 0.2)
        accord(b, k * 5.0 - 1.0, 5.0, [f[-1] * 2], 0.03, desaccord=1.1)     # un fil aigu, très bas
    n = b.n                                                               # un peu d'air (souffle 1 à 3 kHz), sinon la nappe sonne « orgue »
    air = bandnoise(n, lambda k: 1800 + 900 * math.sin(2 * math.pi * k / n), q=0.6)
    b.poser(0.0, [v * (0.6 + 0.4 * math.sin(2 * math.pi * 2 * k / n)) for k, v in enumerate(air)], 0.012)
    b.reverberer(0.35, 0.85, 0.55)
    return b


def pulsation_legere():
    """Pulsation douce à 100 battements par minute (un temps = 0,6 s), 8 mesures de 4 temps = 19,2 s."""
    temps = 0.6
    b = Boucle(32 * temps)
    for k, f in enumerate([[DO4, MI4, SOL4], [LA3, DO4, MI4]]):          # do majeur puis la mineur, 4 mesures chacun
        accord(b, k * 16 * temps - 0.75, 16 * temps, f, 0.11, fondu=1.5)
    basses = [DO3, DO3, DO3, SOL3, LA3, LA3, LA3, MI3]                     # une par mesure
    for mesure in range(8):
        for t in range(4):
            i = mesure * 4 + t
            b.poser(i * temps, blip(basses[mesure] * 2, 0.4, 0.09), 0.30 if t == 0 else 0.17)
            b.poser(i * temps + temps / 2, click(3200, 0.03), 0.035, pan=0.25 if i % 2 else -0.25)
        motif = [MI4, SOL4, DO5, SOL4] if mesure < 4 else [MI4, LA4, DO5, LA4]
        for t, f in enumerate(motif):
            b.poser((mesure * 4 + t) * temps + temps / 2, blip(f, 0.5, 0.14), 0.07, pan=0.3 - 0.2 * t)
    b.reverberer(0.22, 0.6, 0.5)
    return b


def tension():
    """Bourdon sombre : la et si bémol qui frottent, souffle qui enfle toutes les 10 s, tic d'horloge. 20 s."""
    b = Boucle(20.0)
    for t0 in (0.0, 10.0):
        accord(b, t0 - 1.5, 10.0, [LA3, LA3 * 1.5, LA4], 0.16, fondu=3.0, desaccord=0.9)
        accord(b, t0 + 3.5, 5.0, [233.08, 466.16], 0.075, fondu=2.5, desaccord=1.4)       # si bémol : le frottement
        n = int(10.0 * SR)
        souffle = bandnoise(n, lambda k: 500 + 900 * math.sin(math.pi * k / n) ** 2, q=0.7)
        b.poser(t0, [v * math.sin(math.pi * k / n) ** 2 for k, v in enumerate(souffle)], 0.05)
    for s in range(20):
        b.poser(s * 1.0, click(2300 if s % 2 else 1900, 0.04), 0.05, pan=-0.15 if s % 2 else 0.15)
    for s in range(0, 20, 5):                                               # battement sourd, deux coups
        b.poser(s + 0.0, blip(LA3 / 2, 0.45, 0.10), 0.34)
        b.poser(s + 0.32, blip(LA3 / 2, 0.45, 0.10), 0.22)
    b.reverberer(0.4, 0.9, 0.35)
    return b


def retro_puce():
    """Musique « puce » : arpèges d'ondes carrées à 120 battements par minute (un temps = 0,5 s), 8 mesures = 16 s."""
    temps = 0.5
    b = Boucle(32 * temps)
    grille = [([DO4, MI4, SOL4, DO5], DO3), ([SOL3, SI3, RE4, SOL4], SOL3 / 2),
              ([LA3, DO4, MI4, LA4], LA3 / 2), ([FA3, LA3, DO4, FA4], FA3 / 2)]      # 2 mesures chacun

    def note(freq, duree, largeur, chute):
        n = int(duree * SR)
        onde = dsp.pulse(freq, n, largeur)
        return dsp.fade([v * math.exp(-k / (chute * SR)) for k, v in enumerate(onde)], 48, 240)

    for bloc, (notes, basse) in enumerate(grille):
        for pas in range(32):                                              # doubles croches : 4 par temps
            t = (bloc * 8) * temps + pas * temps / 4
            f = notes[(pas * 3) % 4] * (2 if pas % 8 >= 4 else 1)
            b.poser(t, note(f, 0.11, 0.25, 0.05), 0.085, pan=0.35 if pas % 2 else -0.35)
        for pas in range(16):                                              # croches de basse
            t = (bloc * 8) * temps + pas * temps / 2
            b.poser(t, note(basse * 2, 0.2, 0.5, 0.09), 0.12 if pas % 2 == 0 else 0.07)
        for pas in range(16):                                              # bruit en guise de charleston
            t = (bloc * 8) * temps + pas * temps / 2
            n = int((0.09 if pas % 4 == 2 else 0.03) * SR)
            bruit = [random.uniform(-1, 1) * math.exp(-k / (0.25 * n)) for k in range(n)]
            b.poser(t, bruit, 0.06 if pas % 4 == 2 else 0.03)
    melodie = [(0, MI5, 1), (1, SOL5, 1), (2, MI5, 2), (4, RE4 * 2, 1), (5, SOL5, 1), (6, RE4 * 2, 2),
               (8, DO5, 1), (9, MI5, 1), (10, LA4 * 2, 2), (12, LA4, 1), (13, DO5, 1), (14, FA4 * 2, 2)]
    for depart, f, longueur in melodie:                                    # en temps, sur les mesures 1 à 4 puis 5 à 8
        for tour in (0, 16):
            b.poser((depart + tour) * temps, note(f, longueur * temps * 0.9, 0.5, 0.35), 0.075)
    b.g, b.d = dsp.crush(b.g, bits=7, hold=3), dsp.crush(b.d, bits=7, hold=3)   # grain « console »
    return b


FONDS = {
    "nappe-calme": (nappe_calme, 21),
    "pulsation-legere": (pulsation_legere, 22),
    "tension": (tension, 23),
    "retro-puce": (retro_puce, 24),
}


def ecrire(nom, b, dossier, garder_wav):
    lufs = integrated_lufs(b.g, b.d)
    gain = 10 ** ((CIBLE_LUFS - lufs) / 20)
    g, d = [v * gain for v in b.g], [v * gain for v in b.d]
    crete = max(true_peak(g), true_peak(d))
    if crete > 0.7:                                                        # garde : jamais au-dessus de -3 dBTP
        g, d = [v * 0.7 / crete for v in g], [v * 0.7 / crete for v in d]
    wav = os.path.join(dossier, nom + ".wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        trames = bytearray()
        for a, c in zip(g, d):
            trames += struct.pack("<hh", int(max(-1, min(1, a)) * 32767), int(max(-1, min(1, c)) * 32767))
        w.writeframes(bytes(trames))
    saut = max(abs(g[0] - g[-1]), abs(d[0] - d[-1]))
    pente = max(max(abs(g[i + 1] - g[i]) for i in range(len(g) - 1)), 1e-9)
    ogg = os.path.join(dossier, nom + ".ogg")
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-c:a", "libvorbis", "-q:a", "6", ogg], capture_output=True, text=True)
    if r.returncode != 0:
        print("  OGG non écrit (ffmpeg) :", r.stderr.strip()[-200:]); garder_wav = True
    if not garder_wav:
        os.remove(wav)
    print(f"{nom} : {len(g) / SR:.2f} s, {integrated_lufs(g, d):.1f} LUFS, crête {20 * math.log10(max(true_peak(g), true_peak(d))):.1f} dBTP, "
          f"saut à la couture {saut:.4f} (plus grand saut du fichier {pente:.4f})")


def main():
    ap = argparse.ArgumentParser(description="Fabriquer les fonds sonores de repli.")
    ap.add_argument("--dossier", default=ICI); ap.add_argument("--seulement", default="")
    ap.add_argument("--wav", action="store_true", help="garder aussi le WAV")
    o = ap.parse_args()
    os.makedirs(o.dossier, exist_ok=True)
    voulus = [s for s in o.seulement.split(",") if s] or list(FONDS)
    for nom in voulus:
        if nom not in FONDS:
            sys.exit(f"Fond inconnu : {nom} (choix : {', '.join(FONDS)})")
        fabrique, graine = FONDS[nom]
        random.seed(graine)
        ecrire(nom, fabrique(), o.dossier, o.wav)


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    main()
