#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_storyboard.py : contrôle mécanique d'un storyboard AVANT d'écrire la moindre ligne d'animation.

Usage :
    python3 lint_storyboard.py storyboard.md [--fiche chemin/STYLE.md] [--script script.txt] [--sans-demo]

--fiche : lit le bloc « Réglages des contrôles » de la fiche du style (voir fiche_reglages.py) :
  - « Couleurs max » : nombre de couleurs de la palette au-delà duquel le lint passe au jaune (6 sans fiche) ;
  - « Caméra : fixe » : un film sans mouvement de caméra n'est plus signalé (c'est la règle du style) ; c'est
    au contraire un mouvement de caméra qui est signalé en jaune ;
  - « Bleu-violet : dérogation » : une couleur bleu-violet de la palette donne un jaune au lieu d'un rouge ;
  - « Mouvement : calme » : un plan de 8 à 12 s est accepté en jaune s'il contient au moins deux évènements datés.

Feu rouge = interdit de construire. Feu jaune = à regarder, on peut continuer si on sait pourquoi.
Codes de sortie : 0 (vert ou jaune), 1 (au moins un rouge), 2 (fichier illisible ou tableau introuvable).
Bibliothèque standard seulement.

Le storyboard suit le gabarit `gabarits/storyboard.md` :
  - le verrou, avant le tableau : lignes « Style : », « Palette : », « Personnage : », « Format : »
    (et « Bleu-violet autorisé : <raison> » seulement si le client l'a demandé ; « Ouverture en texte :
    <ce que dit la fiche> » seulement si le style ouvre sur une ligne de texte) ;
  - un tableau « Écart avec la démo » de 6 lignes, dernière colonne oui / non ;
  - le tableau des plans : N° | Temps | À l'écran | Ce qui se passe | Caméra | Texte à l'écran | Son | Rôle.

Accroche : elle doit être comprise avant 3 s. Si le premier plan dure plus de 3 s (style à plans longs), la
règle est tenue par un ÉVÈNEMENT DATÉ avant 3 s dans sa case « Ce qui se passe », écrit « à 1,5 s : … »
(temps du film) : « à 1,2 s : le néon s'allume ; à 4 s : la serveuse pose la tasse ». Sans évènement daté
avant 3 s : rouge.

Inspiration : storyboard_lint.py de huashu-art-motion (alchaincyf, MIT, commit 1468196) pour l'idée et
la plupart des règles ; règle « 4 points sur 6 diffèrent de la démo » de lemo-opuscar (LemoLab, MIT,
commit 9eb7739, DIRECTOR.md §11) ; « 5 mots à l'écran » de motion-graphics-skills (Charlie Hills, MIT,
commit 229022e). Réécrit en entier pour le français et le format vertical ; aucun code copié.
"""
import colorsys
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fiche_reglages  # noqa: E402

ROUGE, JAUNE = "ROUGE", "JAUNE"

# --- Vocabulaire -----------------------------------------------------------------------------------
# « À l'écran » : s'il ne reste rien une fois ces mots retirés, la case ne nomme aucun objet concret.
ABSTRAITS = """titre sous-titre soustitre texte textes mot mots phrase liste puces puce point points etiquette
etiquettes legende carte cartes fond arriere-plan arriereplan couleur degrade icone icones pictogramme logo
ecran image visuel element elements contenu information infos schema illustration animation effet forme formes
particules lumiere ligne lignes fleche fleches bloc blocs cadre slogan citation conclusion resume concept idee
message chiffre nombre""".split()
# Cases qui décrivent un écran vide.
VIDES = re.compile(r"ecran (noir|blanc|vide)|fond (noir|blanc|uni|vide)|plan vide|noir complet|rien")
# « Ce qui se passe » : verbes passe-partout qui ne décrivent aucune action.
FAIBLES = """apparait apparaissent apparaitre apparition s'affiche s'affichent affichage affiche arrive arrivent
fondu fade entre entrent entree est sont reste restent presente presentation montre montrent illustre
explique liste enumere defile s'anime anime animation transition visible""".split()
MOTS_OUTILS = """le la les l un une des du de d et ou a au aux en sur sous dans avec par pour qui que se s y
puis ensuite tout tous toute toutes son sa ses leur leurs ce cette ces un deux trois plusieurs petit
grand gros doucement lentement progressivement peu""".split()
# Plan « à dominante texte » : l'objet principal est du texte.
TEXTE_DOMINANT = re.compile(r"\b(titre|texte|mot|mots|phrase|liste|puces|citation|slogan|carton)\b")
# Mouvements de caméra qui vont « vers l'intérieur ».
POUSSEES = ("pousse", "zoom avant", "zoom in", "avance", "travelling avant", "dolly in", "punch")
FIXES = ("fixe", "aucun", "statique", "-", "")
ROLES_OBLIGATOIRES = ("accroche", "rebondissement", "chute")
POINTS_DEMO = 6          # structure, ouverture, plan signature, trajet caméra, forme de la musique, fin
MIN_DIFFERENTS = 4


def norm(s):
    """Minuscules sans accents, pour comparer des mots."""
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").replace("’", "'")


def mots(s):
    return [m for m in re.split(r"[^a-z0-9'\-]+", norm(s)) if m]


def cellule_vide(s):
    return norm(s).strip(" -—–/") in ("", "aucun", "aucune", "rien", "non")


def secondes(txt):
    """« 2,5 », « 2.5 s » ou « 0:12,5 » → secondes."""
    txt = txt.strip().lower().rstrip("s").strip().replace(",", ".")
    if ":" in txt:
        m, s = txt.split(":", 1)
        return int(m) * 60 + float(s)
    return float(txt)


def lire_temps(cell):
    """« 0-2,5 », « 2.5 – 6 », « 0:00 → 0:03 » → (début, fin) en secondes, ou None."""
    morceaux = re.split(r"\s*(?:-|–|—|→|>|à)\s*", cell.strip())
    if len(morceaux) != 2:
        return None
    try:
        a, b = secondes(morceaux[0]), secondes(morceaux[1])
    except ValueError:
        return None
    return (a, b) if b > a else None


def evenements_dates(cell):
    """Temps (secondes du film) des évènements écrits « à 1,5 s : … » dans une case « Ce qui se passe »."""
    return [float(x.replace(",", ".")) for x in re.findall(r"(?:^|[\s;,.(])(?:a|vers)\s+(\d+(?:[.,]\d+)?)\s*s\b", norm(cell))]


def bleu_violet(hexa):
    """Teinte 225–300° et saturation ≥ 0,30 : la zone « look IA » (même définition que la porte de livraison)."""
    h = hexa.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    teinte, sat, val = colorsys.rgb_to_hsv(r, g, b)
    return 225 <= teinte * 360 <= 300 and sat >= 0.30 and val >= 0.06 and (val <= 0.90 or sat >= 0.50)


def lire_tableaux(texte):
    """Tous les tableaux markdown hors blocs de code : liste de (ligne_de_départ, en-têtes, lignes)."""
    tableaux, courant, dans_code = [], None, False
    for n, ligne in enumerate(texte.splitlines(), 1):
        if ligne.strip().startswith("```"):
            dans_code = not dans_code
            continue
        if not dans_code and ligne.strip().startswith("|"):
            cases = [c.strip() for c in ligne.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cases):
                continue                       # ligne de séparation | --- | --- |
            if courant is None:
                courant = (n, cases, [])
                tableaux.append(courant)
            else:
                courant[2].append((n, cases))
        else:
            courant = None
    return tableaux


def colonne(entetes, *indices):
    """Position de la première colonne dont l'en-tête contient un des mots donnés."""
    for i, e in enumerate(entetes):
        if any(k in norm(e) for k in indices):
            return i
    return None


def lire_verrou(texte):
    verrou = {}
    for ligne in texte.splitlines():
        m = re.match(r"^\s*[-*]?\s*\**\s*(Style|Palette|Personnage|Format|Bleu-violet autorisé|Ouverture en texte)\s*\**\s*:\s*\**\s*(.+?)\s*$",
                     ligne, re.I)
        if m and m.group(2).strip(" _.…"):
            verrou.setdefault(norm(m.group(1)), m.group(2))
    return verrou


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    sans_demo = "--sans-demo" in args
    reglages, avertissements = fiche_reglages.option_fiche(args)
    couleurs_max, camera_fixe = reglages["couleurs_max"], reglages["camera"] == "fixe"
    script = None
    if "--script" in args:
        script = Path(args[args.index("--script") + 1]).read_text(encoding="utf-8")
    try:
        texte = Path(args[0]).read_text(encoding="utf-8")
    except OSError as e:
        print(f"Illisible : {e}")
        return 2

    alertes = []                                # (feu, plan, message)
    def alerte(feu, ou, msg):
        alertes.append((feu, ou, msg))
    for a in avertissements:
        alerte(JAUNE, "fiche", a)

    # --- 1. Le verrou : un style, une palette, un choix de personnage, un format ---------------------
    verrou = lire_verrou(texte)
    for cle in ("style", "palette", "personnage", "format"):
        if cle not in verrou:
            alerte(ROUGE, "verrou", f"ligne « {cle.capitalize()} : » absente ou vide avant le tableau des plans")
    couleurs = re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", verrou.get("palette", ""))
    if "palette" in verrou:
        if len(couleurs) < 3:
            alerte(ROUGE, "verrou", f"la palette doit donner 3 à {couleurs_max} couleurs en hex (#RRGGBB)")
        if len(couleurs) > couleurs_max:
            alerte(JAUNE, "verrou", f"{len(couleurs)} couleurs : au-delà de {couleurs_max}"
                                    + (" (maximum de la fiche du style)" if "couleurs max" in reglages["lus"] else "")
                                    + ", le film ressemble à un collage")
        fautives = [c for c in couleurs if bleu_violet(c)]
        if fautives:
            if "bleu-violet autorise" in verrou:
                alerte(JAUNE, "verrou", f"bleu-violet autorisé ({verrou['bleu-violet autorise']}) : {' '.join(fautives)}")
            elif reglages["bleu_violet"] == "dérogation":
                alerte(JAUNE, "verrou", f"bleu-violet : dérogation de la fiche du style : {' '.join(fautives)}")
            else:
                alerte(ROUGE, "verrou", f"couleur(s) bleu-violet « look IA » : {' '.join(fautives)} "
                                        "(teinte 225–300°). Changer, ou écrire « Bleu-violet autorisé : raison » si le client l'exige")

    # --- 2. Trouver les deux tableaux ---------------------------------------------------------------
    plans_tab = demo_tab = None
    for depart, entetes, lignes in lire_tableaux(texte):
        if colonne(entetes, "ecran") is not None and colonne(entetes, "passe") is not None and plans_tab is None:
            plans_tab = (entetes, lignes)
        elif colonne(entetes, "demo") is not None and colonne(entetes, "different") is not None and demo_tab is None:
            demo_tab = (entetes, lignes)
    if plans_tab is None:
        print("Tableau des plans introuvable (colonnes « À l'écran » et « Ce qui se passe » attendues).")
        return 2

    # --- 3. Écart avec la démo : au moins 4 points sur 6 différents ---------------------------------
    if demo_tab is None:
        if not sans_demo:
            alerte(ROUGE, "démo", "tableau « Écart avec la démo » absent (6 lignes). "
                                  "Passer --sans-demo seulement si le style n'a aucune démo")
    else:
        e, lignes = demo_tab
        c = colonne(e, "different")
        oui = sum(1 for _, cases in lignes if c < len(cases) and norm(cases[c]).startswith("oui"))
        if len(lignes) < POINTS_DEMO:
            alerte(ROUGE, "démo", f"{len(lignes)} ligne(s) sur {POINTS_DEMO} : structure, ouverture, plan signature, "
                                  "trajet caméra, forme de la musique, fin")
        if oui < MIN_DIFFERENTS:
            alerte(ROUGE, "démo", f"seulement {oui} point(s) différent(s) de la démo : il en faut au moins "
                                  f"{MIN_DIFFERENTS} sur {POINTS_DEMO}. Repenser ceux qui se ressemblent")

    # --- 4. Les plans, ligne par ligne --------------------------------------------------------------
    e, lignes = plans_tab
    ci = {k: colonne(e, *v) for k, v in {
        "temps": ("temps", "duree"), "objet": ("ecran",), "action": ("passe",), "camera": ("camera",),
        "texte": ("texte",), "son": ("son",), "role": ("role",)}.items()}
    plans = []
    for n, cases in lignes:
        def case(k):
            i = ci[k]
            return cases[i] if i is not None and i < len(cases) else ""
        plans.append({"ligne": n, "nom": f"plan {len(plans) + 1}", "temps": lire_temps(case("temps")),
                      "objet": case("objet"), "action": case("action"), "camera": norm(case("camera")).strip(),
                      "texte": "" if cellule_vide(case("texte")) else case("texte").strip("«»\"“” "),
                      "son": case("son"), "role": norm(case("role"))})
    if not plans:
        print("Le tableau des plans est vide.")
        return 2

    for p in plans:
        # 4a. un objet concret à l'écran
        reste = [m for m in mots(p["objet"]) if m not in ABSTRAITS and m not in MOTS_OUTILS and not m.isdigit()]
        if cellule_vide(p["objet"]) or VIDES.search(norm(p["objet"])):
            alerte(ROUGE, p["nom"], "« À l'écran » décrit un écran vide : chaque plan montre le héros ou l'objet du film")
        elif not reste:
            alerte(ROUGE, p["nom"], f"« À l'écran » ne nomme aucun objet concret ({p['objet']!r}) : "
                                    "écrire la chose qu'on voit, pas « un titre » ou « une liste »")
        # 4b. une vraie action
        reste = [m for m in mots(p["action"]) if m not in FAIBLES and m not in MOTS_OUTILS and not m.isdigit()]
        if cellule_vide(p["action"]) or not reste:
            alerte(ROUGE, p["nom"], f"« Ce qui se passe » n'a pas de verbe d'action ({p['action']!r}) : "
                                    "« apparaît », « s'affiche », « fondu » ne comptent pas")
        # 4c. texte à l'écran court
        nb = len(p["texte"].split())
        if nb > 7:
            alerte(ROUGE, p["nom"], f"{nb} mots à l'écran : 5 au mieux, 7 au plus")
        elif nb > 5:
            alerte(JAUNE, p["nom"], f"{nb} mots à l'écran : viser 5")
        p["dominante_texte"] = bool(TEXTE_DOMINANT.search(norm(p["objet"]))) or nb >= 6
        # 4d. durée du plan
        if p["temps"] is None:
            alerte(ROUGE, p["nom"], "colonne « Temps » illisible : écrire « début-fin » en secondes (ex. 2,5-6)")
        else:
            d = p["temps"][1] - p["temps"][0]
            dedans = [t for t in evenements_dates(p["action"]) if p["temps"][0] - 1e-6 <= t <= p["temps"][1] + 1e-6]
            if 8 < d <= 12 and reglages["mouvement"] == "calme" and len(dedans) >= 2:
                alerte(JAUNE, p["nom"], f"{d:.1f} s : plan long accepté (style calme, {len(dedans)} évènements datés dans le plan)")
            elif d > 8:
                alerte(ROUGE, p["nom"], f"{d:.1f} s : un plan de plus de 8 s est un écran figé, le couper en deux actions"
                                        + (" (style calme : jusqu'à 12 s avec au moins deux évènements datés « à 3 s : … »)"
                                           if reglages["mouvement"] == "calme" else ""))
            elif d > 6:
                alerte(JAUNE, p["nom"], f"{d:.1f} s : au-delà de 6 s il faut du nouveau à l'intérieur du plan")
            elif d < 1:
                alerte(JAUNE, p["nom"], f"{d:.1f} s : trop court pour être compris, sauf rafale voulue")
        # 4e. chiffres à l'écran présents dans le script
        if script is not None:
            for chiffre in re.findall(r"\d+(?:[.,]\d+)?", p["texte"]):
                if chiffre not in script and chiffre.replace(",", ".") not in script.replace(",", "."):
                    alerte(ROUGE, p["nom"], f"le chiffre « {chiffre} » est à l'écran mais pas dans le script : "
                                            "aucun chiffre sans source")

    # --- 5. Le tableau dans son ensemble ------------------------------------------------------------
    premier, dernier = plans[0], plans[-1]
    if premier["dominante_texte"]:
        if "ouverture en texte" in verrou:
            alerte(JAUNE, premier["nom"], f"le film s'ouvre sur du texte, comme le veut son style ({verrou['ouverture en texte']}) : "
                                          "cette ligne doit poser l'enjeu et il doit lui arriver quelque chose avant 3 s "
                                          "(elle se tape, se barre, se coupe, se transforme), pas un titre posé")
        else:
            alerte(ROUGE, premier["nom"], "le film s'ouvre sur du texte : les 3 premières secondes montrent une petite "
                                          "scène concrète, pas un titre. Si la fiche du style ouvre sur une ligne de texte "
                                          "(démo produit, typographie), l'écrire dans le verrou : « Ouverture en texte : <ce que dit la fiche> »")
    if dernier["dominante_texte"]:
        alerte(JAUNE, dernier["nom"], "le film finit sur un carton de texte : finir sur une action du héros ou de l'objet, "
                                      "le texte posé dans l'image")
    part = sum(p["dominante_texte"] for p in plans) / len(plans)
    if part > 0.30:
        alerte(ROUGE, "ensemble", f"{part:.0%} de plans à dominante texte (30 % au plus) : c'est un diaporama")

    # rôles : accroche avant 3 s, un rebondissement, une chute
    for role in ROLES_OBLIGATOIRES:
        if not any(role in p["role"] for p in plans):
            alerte(ROUGE, "ensemble", f"aucun plan n'a le rôle « {role} » dans la colonne Rôle")
    accroche = next((p for p in plans if "accroche" in p["role"]), None)
    if accroche and accroche["temps"]:
        if accroche is not premier or accroche["temps"][0] > 0.01:
            alerte(ROUGE, accroche["nom"], "l'accroche doit être le premier plan et commencer à 0 s")
        elif accroche["temps"][1] > 3.0 and len(plans) > 1:
            tot = [t for t in evenements_dates(accroche["action"]) if t < 3.0]
            if not tot:
                alerte(ROUGE, accroche["nom"], f"l'accroche dure jusqu'à {accroche['temps'][1]:.1f} s : elle doit être "
                                               "comprise avant 3 s. Raccourcir le plan, ou dater dans « Ce qui se passe » "
                                               "l'évènement qui accroche (« à 1,5 s : … », avant 3 s)")
    chute = next((p for p in reversed(plans) if "chute" in p["role"]), None)
    if chute and plans.index(chute) < len(plans) - 2:
        alerte(JAUNE, chute["nom"], "la chute est loin de la fin : elle se place dans les deux derniers plans")

    # caméra : pas trois fois le même mouvement, pas trois poussées d'affilée, pas un film tout fixe
    for i in range(len(plans) - 2):
        trio = [plans[i + k]["camera"] for k in range(3)]
        if trio[0] == trio[1] == trio[2] and trio[0] not in FIXES:
            alerte(JAUNE, plans[i + 2]["nom"], f"trois plans de suite avec la même caméra (« {trio[0]} »)")
        elif all(any(k in c for k in POUSSEES) for c in trio):
            alerte(JAUNE, plans[i + 2]["nom"], "trois poussées vers l'intérieur d'affilée : alterner avec un recul ou un plan fixe")
    if camera_fixe:
        mobiles = [p["nom"] for p in plans if p["camera"] not in FIXES and "coupe" not in p["camera"]]
        if mobiles:
            alerte(JAUNE, "ensemble", "la fiche du style dit « Caméra : fixe » mais la caméra bouge : " + ", ".join(mobiles))
    elif all(p["camera"] in FIXES for p in plans):
        alerte(JAUNE, "ensemble", "aucun mouvement de caméra dans tout le film (si c'est la règle du style, sa fiche "
                                  "le dit par « Caméra : fixe » : passer --fiche)")

    # temps : les plans se suivent sans trou ni chevauchement
    datés = [p for p in plans if p["temps"]]
    for a, b in zip(datés, datés[1:]):
        if abs(b["temps"][0] - a["temps"][1]) > 0.05:
            alerte(JAUNE, b["nom"], f"commence à {b['temps'][0]:g} s alors que le plan précédent finit à {a['temps'][1]:g} s")
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*s\b", verrou.get("format", ""))
    if m and datés and abs(datés[-1]["temps"][1] - float(m.group(1).replace(",", "."))) > 0.5:
        alerte(JAUNE, "ensemble", f"le dernier plan finit à {datés[-1]['temps'][1]:g} s mais le format annonce {m.group(1)} s")
    if ci["son"] is not None and all(cellule_vide(p["son"]) for p in plans):
        alerte(JAUNE, "ensemble", "colonne « Son » vide partout : noter au moins le silence avant la chute et le son de la chute")

    # --- 6. Rapport -------------------------------------------------------------------------------
    rouges = [a for a in alertes if a[0] == ROUGE]
    jaunes = [a for a in alertes if a[0] == JAUNE]
    duree = datés[-1]["temps"][1] if datés else 0
    print(f"Storyboard : {len(plans)} plans, {duree:g} s, {len(couleurs)} couleurs")
    print("  " + fiche_reglages.resume(reglages))
    for feu, ou, msg in rouges + jaunes:
        print(f"  [{feu}] {ou} : {msg}")
    if rouges:
        print(f"FEU ROUGE : {len(rouges)} point(s) bloquant(s). Corriger le storyboard, relancer, puis seulement construire.")
        return 1
    print(f"FEU {'JAUNE' if jaunes else 'VERT'} : on peut montrer le storyboard au client"
          + (f" ({len(jaunes)} point(s) à regarder)." if jaunes else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
