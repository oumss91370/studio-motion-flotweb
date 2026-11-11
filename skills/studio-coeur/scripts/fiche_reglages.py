#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fiche_reglages.py : lit le bloc « Réglages des contrôles » d'une fiche STYLE.md.

Chaque fiche de style porte, à la fin de sa section 8, ce bloc (format exact) :

    **Réglages des contrôles**
    - Mouvement : calme | normal | vif
    - Caméra : fixe | mobile
    - Couleurs max : <nombre>
    - Bleu-violet : interdit | dérogation
    - Texte vivant : non | oui
    - Taille mini du texte : <px>

Les scripts de contrôle (`porte_livraison.py`, `controle_textes.py`, `lint_storyboard.py`,
`relever_textes.py`) le lisent par l'option `--fiche <chemin/STYLE.md>`. Sans l'option, ou pour une ligne
absente, ils gardent les valeurs par défaut : normal, mobile, 6, interdit, non, 50.

Usage direct (pour voir ce qu'un contrôle lira) :
    python3 fiche_reglages.py chemin/STYLE.md

Bibliothèque standard seulement. Écrit pour ce plugin.
"""
import re
import sys
import unicodedata
from pathlib import Path

DEFAUTS = {"mouvement": "normal", "camera": "mobile", "couleurs_max": 6, "bleu_violet": "interdit",
           "texte_vivant": False, "taille_mini": 50}


def _norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip(" *_`.")


def lire_reglages(chemin):
    """Renvoie (réglages, avertissements). `chemin` vide ou None : les valeurs par défaut, sans avertissement.

    Les réglages portent aussi `source` (chemin lu, ou None) et `lus` (noms des lignes trouvées dans la fiche)."""
    r = dict(DEFAUTS, source=None, lus=[])
    if not chemin:
        return r, []
    alertes = []
    try:
        texte = Path(chemin).read_text(encoding="utf-8")
    except OSError as e:
        return r, [f"fiche illisible ({e}) : valeurs par défaut"]
    r["source"] = str(chemin)
    m = re.search(r"R[ée]glages des contr[ôo]les", texte, re.I)
    if not m:
        return r, [f"{chemin} n'a pas de bloc « Réglages des contrôles » : valeurs par défaut"]
    for ligne in texte[m.end():].splitlines()[1:]:
        if not ligne.strip():
            if r["lus"]:
                break                                   # fin du bloc : première ligne vide après les puces
            continue
        mm = re.match(r"^\s*[-*]\s*([^:]+?)\s*:\s*(.+?)\s*$", ligne)
        if not mm:
            break
        cle, brut = _norm(mm.group(1)), mm.group(2)
        val = _norm(brut)
        mot = val.split()[0] if val.split() else ""
        nombre = re.search(r"\d+", val)
        if cle == "mouvement":
            if mot in ("calme", "normal", "vif"):
                r["mouvement"] = mot
            else:
                alertes.append(f"Mouvement : {brut!r} n'est pas calme, normal ou vif (gardé : normal)")
        elif cle == "camera":
            if mot in ("fixe", "mobile"):
                r["camera"] = mot
            else:
                alertes.append(f"Caméra : {brut!r} n'est pas fixe ou mobile (gardé : mobile)")
        elif cle == "couleurs max":
            if nombre:
                r["couleurs_max"] = int(nombre.group(0))
            else:
                alertes.append(f"Couleurs max : {brut!r} n'est pas un nombre (gardé : 6)")
        elif cle == "bleu-violet":
            if mot.startswith("derog"):
                r["bleu_violet"] = "dérogation"
            elif mot.startswith("interdit"):
                r["bleu_violet"] = "interdit"
            else:
                alertes.append(f"Bleu-violet : {brut!r} n'est pas interdit ou dérogation (gardé : interdit)")
        elif cle == "texte vivant":
            if mot in ("oui", "non"):
                r["texte_vivant"] = mot == "oui"
            else:
                alertes.append(f"Texte vivant : {brut!r} n'est pas oui ou non (gardé : non)")
        elif cle == "taille mini du texte":
            if nombre:
                r["taille_mini"] = int(nombre.group(0))
            else:
                alertes.append(f"Taille mini du texte : {brut!r} n'est pas un nombre (gardé : 50)")
        else:
            continue                                    # ligne inconnue : ignorée, sans arrêter la lecture
        r["lus"].append(cle)
    if not r["lus"]:
        alertes.append(f"{chemin} : bloc « Réglages des contrôles » vide : valeurs par défaut")
    return r, alertes


def resume(r):
    """Une ligne lisible, à imprimer en tête des contrôles."""
    origine = f"fiche {Path(r['source']).parent.name}" if r["source"] and r["lus"] else "valeurs par défaut"
    return (f"Réglages ({origine}) : mouvement {r['mouvement']}, caméra {r['camera']}, {r['couleurs_max']} couleurs "
            f"au plus, bleu-violet {r['bleu_violet']}, texte vivant {'oui' if r['texte_vivant'] else 'non'}, "
            f"texte de {r['taille_mini']} px au moins")


def option_fiche(args):
    """Lit `--fiche chemin` dans une liste d'arguments. Renvoie (réglages, avertissements)."""
    chemin = args[args.index("--fiche") + 1] if "--fiche" in args and args.index("--fiche") + 1 < len(args) else None
    return lire_reglages(chemin)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(2)
    reglages, avertissements = lire_reglages(sys.argv[1])
    print(resume(reglages))
    for a in avertissements:
        print("  [À VOIR] " + a)
    sys.exit(1 if avertissements else 0)
