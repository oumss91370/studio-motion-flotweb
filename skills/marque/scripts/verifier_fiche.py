#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verifier_fiche.py : la fiche « ma chaîne » est-elle assez complète pour faire une vidéo, et sa palette tient-elle ?

Usage :
    python3 verifier_fiche.py ma-chaine.md

Contrôles :
  - rubriques indispensables remplies : niche, public, ton, palette (fond, texte, accent), typographie, format ;
    les autres rubriques vides sont seulement listées ;
  - palette : couleurs en hex ; aucune dans la zone bleu-violet « look IA » (teinte 225–300°, saturation ≥ 0,30),
    sauf ligne « Bleu-violet autorisé : oui, <raison> » ;
  - contraste du texte sur le fond ≥ 4,5 (sinon illisible sur téléphone), de l'accent sur le fond ≥ 3 ;
  - combien de valeurs sont des « choix de l'agent » encore à confirmer par le client.

Les lignes de la section « Journal » (historique des changements) ne sont pas des rubriques : elles sont comptées
à part et ne sont jamais jugées « vides » ou « remplies ».

Codes de sortie : 0 fiche utilisable, 1 il manque de l'indispensable ou la palette ne tient pas, 2 fichier illisible.
Bibliothèque standard seulement.

Inspiration : brand-intake de motion-graphics-skills (Charlie Hills, MIT, commit 229022e) pour « ne jamais combler
un trou par une supposition » ; zone bleu-violet de film_gate.py, huashu-art-motion (alchaincyf, MIT, commit 1468196).
Contraste : formule publique WCAG 2. Écrit pour ce plugin.
"""
import colorsys
import re
import sys
import unicodedata
from pathlib import Path

INDISPENSABLES = ["sujet de la chaine", "promesse en une phrase", "qui regarde", "trois mots", "fond", "texte",
                  "accent", "police des titres", "police du texte", "format", "duree habituelle"]
HEX = re.compile(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip()


def rgb(hexa):
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def bleu_violet(hexa):
    teinte, sat, val = colorsys.rgb_to_hsv(*rgb(hexa))
    return 225 <= teinte * 360 <= 300 and sat >= 0.30 and val >= 0.06 and (val <= 0.90 or sat >= 0.50)


def luminance(hexa):
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb(hexa)]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contraste(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def vide(valeur):
    return norm(valeur) in ("", "a completer", "?", "-", "aaaa-mm-jj")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    try:
        texte = Path(sys.argv[1]).read_text(encoding="utf-8")
    except OSError as e:
        print(f"Fiche illisible : {e}")
        return 2
    fiche, journal, dans_journal = {}, 0, False
    for ligne in texte.splitlines():
        titre = re.match(r"^\s*#+\s*(.+?)\s*$", ligne)
        if titre:                                   # le journal est un historique, pas une rubrique à remplir
            dans_journal = norm(titre.group(1)).lstrip("0123456789. ").startswith("journal")
            continue
        if dans_journal:
            journal += bool(re.match(r"^\s*-\s*\S", ligne))
            continue
        m = re.match(r"^\s*-\s*([^:]+?)\s*:\s*(.*)$", ligne)
        if m:
            fiche.setdefault(norm(m.group(1)), m.group(2).strip())
    if not fiche:
        print("Aucune ligne « - clé : valeur » : ce n'est pas une fiche « ma chaîne ».")
        return 2

    bloquant, a_voir = [], []
    manquants = [k for k in INDISPENSABLES if vide(fiche.get(k, ""))]
    if manquants:
        bloquant.append("indispensable manquant : " + ", ".join(manquants))
    autres = [k for k, v in fiche.items() if vide(v) and k not in INDISPENSABLES and k != "mise a jour"]
    if autres:
        a_voir.append("encore vide : " + ", ".join(autres))

    couleurs = {}
    for role in ("fond", "surface", "texte", "texte secondaire", "accent", "accent 2"):
        m = HEX.search(fiche.get(role, ""))
        if m:
            couleurs[role] = m.group(0)
        elif not vide(fiche.get(role, "")):
            bloquant.append(f"« {role} » n'est pas une couleur hex (#RRGGBB) : {fiche[role]!r}")
    autorise = norm(fiche.get("bleu-violet autorise", "non")).startswith("oui")
    fautives = [f"{r} {c}" for r, c in couleurs.items() if bleu_violet(c)]
    if fautives:
        (a_voir if autorise else bloquant).append(
            "bleu-violet « look IA » : " + ", ".join(fautives)
            + (" (autorisé par le client)" if autorise else " : proposer une autre teinte, ou noter « Bleu-violet autorisé : oui, raison »"))
    if "fond" in couleurs and "texte" in couleurs:
        c = contraste(couleurs["fond"], couleurs["texte"])
        if c < 4.5:
            bloquant.append(f"contraste texte / fond {c:.1f} : il faut 4,5 au moins")
    if "fond" in couleurs and "accent" in couleurs:
        c = contraste(couleurs["fond"], couleurs["accent"])
        if c < 3:
            a_voir.append(f"contraste accent / fond {c:.1f} : sous 3, l'accent se voit mal ; ne pas l'utiliser pour du texte")
    choix = [k for k, v in fiche.items() if "choix de l'agent" in v.lower()]
    if choix:
        a_voir.append("choix de l'agent à faire confirmer : " + ", ".join(choix))

    remplies = sum(1 for v in fiche.values() if not vide(v))
    print(f"Fiche « ma chaîne » : {remplies} lignes remplies sur {len(fiche)}, {len(couleurs)} couleurs"
          + (f", {journal} ligne(s) au journal" if journal else ""))
    for b in bloquant:
        print("  [BLOQUANT] " + b)
    for a in a_voir:
        print("  [À VOIR]   " + a)
    print("Fiche utilisable pour une vidéo." if not bloquant else "Fiche à compléter avant de lancer une vidéo.")
    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main())
