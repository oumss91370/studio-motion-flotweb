#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""controle_textes.py : chaque texte du film est-il dans la zone sûre, et reste-t-il assez longtemps pour être lu ?

Usage :
    python3 controle_textes.py textes.json [--fiche chemin/STYLE.md] [--strict] [--json resultat.json]

`textes.json` est le relevé des textes du film : produit par `relever_textes.py` (film en HTML), ou rempli à la
main d'après `gabarits/textes-canvas.json` (film dessiné dans un canvas) :

    {
      "largeur": 1080, "hauteur": 1920,
      "textes": [
        {"id": "accroche", "texte": "3 € par jour", "debut": 0.4, "fin": 2.6,
         "x0": 120, "y0": 520, "x1": 900, "y1": 700, "taille_px": 96},
        {"id": "st-01", "texte": "et personne ne le voit", "debut": 2.7, "fin": 4.0,
         "x0": 140, "y0": 1380, "x1": 880, "y1": 1470, "sous_titre": true},
        {"id": "enseigne", "texte": "BOULANGERIE", "debut": 5, "fin": 5.6,
         "x0": 0, "y0": 300, "x1": 400, "y1": 380, "passage": true},
        {"id": "carton", "texte": "PAF !", "debut": 6.1, "fin": 7.0,
         "x0": 200, "y0": 600, "x1": 800, "y1": 820, "taille_px": 180, "vivant": true}
      ]
    }

  - debut / fin : secondes pendant lesquelles le texte est ENTIER et lisible à l'écran (animation d'entrée finie).
  - x0, y0, x1, y1 : la boîte de ses lettres, en pixels dans l'image finale (pour un texte qui dérive ou tremble :
    la boîte qui contient toutes ses positions).
  - "sous_titre": true : sous-titre calé sur la voix (règle propre : ≥ 0,7 s et ≤ 17 caractères/s).
  - "passage": true : texte de décor que le spectateur n'a pas à lire (enseigne, étiquette balayée) : listé, pas jugé.
    Ne jamais marquer ainsi un texte dont le film a besoin.
  - "vivant": true : texte qui tremble ou flotte par style (onomatopée, carton de film muet).
  - Le même "id" peut revenir plusieurs fois (le texte part puis revient, ou la caméra le déplace) : la zone sûre
    est jugée sur chaque présence, le temps de lecture sur la plus longue.

Règles :
  1. Zone sûre. Vertical 1080×1920 : rien d'important dans les 160 px du haut, les 360 px du bas, les 135 px
     de droite (interface des applications) ni à moins de 60 px du bord gauche. Autres formats : marge de 5 %.
     (Mêmes valeurs que la table de référence : skills/rendu/references/zones-interface.md.)
  2. Temps de lecture. Par défaut (vidéo courte) : 1 s + 0,25 s par mot au-delà de 3, et 2 s au moins pour le
     dernier texte du film. Avec --strict (explicatif posé) : caractères ÷ 15 + 1,5 s, jamais moins de 1,5 s.
     Texte vivant (`"vivant": true`, ou fiche « Texte vivant : oui ») de 1 ou 2 mots : 0,8 s suffisent (une
     onomatopée se saisit d'un coup) ; au-delà de 2 mots, la règle normale s'applique sans rabais.
  3. Taille : un texte plus petit que la taille mini (pour 1080 de large) est signalé en jaune. Taille mini :
     ligne « Taille mini du texte » de la fiche du style (--fiche), sinon 50 px.

Codes de sortie : 0 tout passe (ou jaune), 1 au moins un rouge, 2 fichier illisible ou sans texte
(« non contrôlé » n'est pas « réussi »).

Inspiration : readcheck.mjs de lemo-opuscar (LemoLab, MIT, commit 9eb7739) pour le principe, la règle
stricte et « passage » ; règle courte de claude-motion (whaleyxbt, MIT, commit 6f80380) ; règle des
sous-titres de claude-motion-design (Howseen AI, MIT, commit 3d90d34) ; zone sûre : conventions du plugin.
Réécrit en entier (l'original pilote un navigateur ; celui-ci lit un relevé).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fiche_reglages  # noqa: E402

TENUE_VIVANT_COURT = 0.8      # secondes : texte vivant de 1 ou 2 mots


def zone_sure(largeur, hauteur):
    """Boîte (x0, y0, x1, y1) où un texte peut se poser."""
    if hauteur > largeur:                                   # vertical : mesures données pour 1080×1920
        kx, ky = largeur / 1080, hauteur / 1920
        return (60 * kx, 160 * ky, largeur - 135 * kx, hauteur - 360 * ky)
    return (0.05 * largeur, 0.05 * hauteur, 0.95 * largeur, 0.95 * hauteur)


def duree_requise(texte, strict, dernier, vivant=False):
    mots = len(texte.split())
    if strict:
        lettres = sum(1 for c in texte if not c.isspace())
        besoin = max(1.5, lettres / 15 + 1.5)
    else:
        besoin = 1.0 + 0.25 * max(0, mots - 3)
    if vivant and mots <= 2:
        besoin = TENUE_VIVANT_COURT
    return max(besoin, 2.0) if dernier else besoin


def controler(donnees, strict=False, reglages=None):
    """Renvoie (lignes de résultat, nombre de rouges, nombre de jaunes).

    `reglages` : ce que rend `fiche_reglages.lire_reglages` (taille mini, texte vivant) ; None = valeurs par défaut."""
    reglages = reglages or fiche_reglages.DEFAUTS
    taille_mini, tout_vivant = reglages["taille_mini"], reglages["texte_vivant"]
    L, H = donnees.get("largeur", 1080), donnees.get("hauteur", 1920)
    zx0, zy0, zx1, zy1 = zone_sure(L, H)
    textes = donnees.get("textes", [])
    a_lire = [t for t in textes if not t.get("passage") and not t.get("sous_titre")]
    dernier = max(a_lire, key=lambda t: t["fin"]) if a_lire else None
    # un même id relevé plusieurs fois : le temps de lecture se juge sur sa plus longue présence
    plus_longue = {}
    for t in textes:
        cle = str(t.get("id", "?"))
        if cle not in plus_longue or t["fin"] - t["debut"] > plus_longue[cle]["fin"] - plus_longue[cle]["debut"]:
            plus_longue[cle] = t
    resultats, rouges, jaunes = [], 0, 0
    for t in textes:
        cle = str(t.get("id", "?"))
        r = {"id": cle, "texte": t["texte"], "debut": t["debut"], "feu": "VERT", "pourquoi": []}
        if t.get("passage"):
            r["feu"] = "PASSAGE"
            resultats.append(r)
            continue
        # 1. zone sûre
        if all(k in t for k in ("x0", "y0", "x1", "y1")):
            depasse = []
            if t["y0"] < zy0: depasse.append(f"haut ({zy0 - t['y0']:.0f} px dans la zone d'interface)")
            if t["y1"] > zy1: depasse.append(f"bas ({t['y1'] - zy1:.0f} px)")
            if t["x1"] > zx1: depasse.append(f"droite ({t['x1'] - zx1:.0f} px)")
            if t["x0"] < zx0: depasse.append(f"gauche ({zx0 - t['x0']:.0f} px)")
            if depasse:
                r["feu"] = "ROUGE"
                r["pourquoi"].append("hors zone sûre : " + ", ".join(depasse))
        else:
            r["feu"] = "JAUNE"
            r["pourquoi"].append("pas de boîte (x0, y0, x1, y1) : zone sûre non contrôlée")
        # 2. temps de lecture
        tenu = t["fin"] - t["debut"]
        if t.get("sous_titre"):
            lettres = sum(1 for c in t["texte"] if not c.isspace())
            if tenu < 0.7 or lettres / max(tenu, 0.01) > 17:
                r["feu"] = "ROUGE"
                r["pourquoi"].append(f"sous-titre trop rapide : {tenu:.2f} s, {lettres / max(tenu, 0.01):.0f} car./s "
                                     "(0,7 s au moins, 17 car./s au plus)")
        elif plus_longue[cle] is not t:
            r["pourquoi"].append(f"autre présence du même texte ({tenu:.2f} s) : lecture jugée sur la plus longue")
        else:
            vivant = bool(t.get("vivant")) or tout_vivant
            besoin = duree_requise(t["texte"], strict, t is dernier or plus_longue.get(str(dernier.get("id", "?"))) is t
                                   if dernier else False, vivant)
            if tenu < besoin - 1e-6:
                r["feu"] = "ROUGE"
                r["pourquoi"].append(f"temps de lecture : tenu {tenu:.2f} s, il faut {besoin:.2f} s "
                                     + ("(texte vivant) " if vivant else "")
                                     + "(tenir plus longtemps ou mettre moins de mots)")
        # 3. taille
        taille = t.get("taille_px")
        if taille is not None and taille * 1080 / L < taille_mini and r["feu"] == "VERT":
            r["feu"] = "JAUNE"
            r["pourquoi"].append(f"{taille} px de haut : sous {taille_mini} px "
                                 + ("(taille mini de la fiche du style)" if reglages.get("source") and "taille mini du texte" in reglages.get("lus", [])
                                    else "c'est difficile à lire sur un téléphone"))
        rouges += r["feu"] == "ROUGE"
        jaunes += r["feu"] == "JAUNE"
        resultats.append(r)
    return resultats, rouges, jaunes


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    try:
        donnees = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"NON CONTRÔLÉ : {args[0]} illisible ({e}). Ce n'est pas un succès.")
        return 2
    if not donnees.get("textes"):
        print("NON CONTRÔLÉ : le relevé ne contient aucun texte. Si le film n'a vraiment aucun texte, le dire dans la note de livraison.")
        return 2
    reglages, avertissements = fiche_reglages.option_fiche(args)
    print(fiche_reglages.resume(reglages))
    for a in avertissements:
        print("  [À VOIR] " + a)
    if donnees.get("canvas_sans_texte_declare"):
        print("  [À VOIR] le film a un canvas et le relevé automatique n'y lit rien : si du texte y est dessiné, "
              "l'ajouter à la main (gabarits/textes-canvas.json)")
    resultats, rouges, jaunes = controler(donnees, "--strict" in args, reglages)
    for r in resultats:
        print(f"  [{r['feu']:7}] {r['id']:<14} à {r['debut']:>5.2f} s  {r['texte'][:32]!r}"
              + ("  → " + " ; ".join(r["pourquoi"]) if r["pourquoi"] else ""))
    if "--json" in args:
        Path(args[args.index("--json") + 1]).write_text(
            json.dumps({"rouges": rouges, "jaunes": jaunes, "textes": resultats}, ensure_ascii=False, indent=2),
            encoding="utf-8")
    print(f"TEXTES : {'FEU ROUGE' if rouges else 'FEU JAUNE' if jaunes else 'FEU VERT'} "
          f"({len(resultats)} textes, {rouges} rouge(s), {jaunes} jaune(s))")
    return 1 if rouges else 0


if __name__ == "__main__":
    sys.exit(main())
