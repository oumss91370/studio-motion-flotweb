#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""note_livraison.py : écrit la note de livraison. Les FAITS sont écrits par le script, pas par l'agent.

Usage :
    python3 note_livraison.py film.mp4 --porte porte.json --relecture relecture/tour-2.md \
        --plan-faible "Plan 6 (14–17 s) : la carte reste presque immobile" \
        [--corrige "ce que la revue a trouvé et qui a été corrigé"] [--non-verifie "ce qui n'a pas pu être vérifié"] \
        [--tour 2] [--accord-client "le client accepte la note 7 en variété, message du 12/03"] [--sortie livraison/]
    python3 note_livraison.py --verifier livraison/note-de-livraison.md

Le script refuse d'écrire une note « LIVRABLE » (code 2) si :
  - la porte de livraison est au rouge, ou son fichier manque ;
  - il n'y a pas de relecture indépendante, ou si une de ses notes est sous 8/10
    (sauf --accord-client "…", recopié tel quel : le client sait ce qu'il reçoit) ;
  - le plan le plus faible n'est pas nommé (--plan-faible). Tout film en a un : le nommer est obligatoire.

La partie « Faits » porte une empreinte : `--verifier` dit si quelqu'un l'a modifiée après coup.
L'agent complète seulement la partie « Notes du réalisateur », sous les faits.

Fichier de relecture attendu (écrit par le relecteur, voir references/relecteur.md) : une ligne par critère,
de la forme « - accroche : 8/10 ». Les 7 critères : accroche, lisibilité, mouvement, variété, composition,
exactitude, son.

Inspiration : deliver.py de huashu-art-motion (alchaincyf, MIT, commit 1468196) pour « les faits sont écrits
par le script, avec une empreinte » ; critique notée « 8+ partout » de claude-motion-design (Howseen AI, MIT,
commit 3d90d34) ; « nommer le plan le plus faible » d'animate (cth9191, MIT, commit 7e5eb56). Réécrit.
"""
import datetime
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

CRITERES = ["accroche", "lisibilite", "mouvement", "variete", "composition", "exactitude", "son"]
SEUIL = 8.0
DEBUT, FIN = "<!-- faits : début (écrit par note_livraison.py, ne pas modifier) -->", "<!-- faits : fin -->"
NOM = "note-de-livraison.md"


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def lire_notes(chemin):
    """{critère: note} lues dans le fichier du relecteur."""
    notes = {}
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        m = re.search(r"(\d+(?:[.,]\d+)?)\s*/\s*10", ligne)
        if not m:
            continue
        for c in CRITERES:
            if c in norm(ligne.split(m.group(0))[0]) and c not in notes:
                notes[c] = float(m.group(1).replace(",", "."))
    return notes


def empreinte(texte):
    return hashlib.sha256(texte.strip().encode("utf-8")).hexdigest()[:16]


def verifier(chemin):
    try:
        texte = Path(chemin).read_text(encoding="utf-8")
    except OSError as e:
        print(f"Note illisible : {e}")
        return 2
    m = re.search(re.escape(DEBUT) + r"\n(.*?)\nEmpreinte des faits : ([0-9a-f]{16})\n" + re.escape(FIN), texte, re.S)
    if not m:
        print("Bloc des faits introuvable : cette note n'a pas été écrite par note_livraison.py.")
        return 2
    if empreinte(m.group(1)) != m.group(2):
        print("LES FAITS ONT ÉTÉ MODIFIÉS après l'écriture de la note. Relancer note_livraison.py.")
        return 2
    print("Faits intacts.")
    return 0


def option(args, nom, defaut=None):
    return args[args.index(nom) + 1] if nom in args else defaut


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 1
    if args[0] == "--verifier":
        return verifier(args[1])

    film = Path(args[0])
    refus = []
    # --- la porte ---
    porte = None
    try:
        porte = json.loads(Path(option(args, "--porte", "")).read_text(encoding="utf-8"))
        if porte.get("film") != film.name:
            refus.append(f"le fichier de porte concerne « {porte.get('film')} », pas « {film.name} » : relancer la porte sur ce film")
        elif porte["bilan"] == "ROUGE":
            refus.append("la porte de livraison est au ROUGE")
    except (OSError, ValueError, KeyError):
        refus.append("fichier --porte absent ou illisible : lancer porte_livraison.py --json porte.json")
    # --- la relecture ---
    relecture, notes = option(args, "--relecture"), {}
    accord = option(args, "--accord-client")
    if not relecture or not Path(relecture).exists():
        refus.append("pas de relecture indépendante (--relecture) : la faire faire par un sous-agent qui n'a pas construit le film")
    else:
        notes = lire_notes(relecture)
        manquants = [c for c in CRITERES if c not in notes]
        if manquants:
            refus.append("relecture incomplète, critères sans note : " + ", ".join(manquants))
        faibles = {c: n for c, n in notes.items() if n < SEUIL}
        if faibles and not accord:
            refus.append("notes sous 8/10 : " + ", ".join(f"{c} {n:g}" for c, n in faibles.items())
                         + ". Corriger les 3 pires défauts et refaire relire, ou --accord-client \"…\" si le client accepte en connaissance de cause")
    # --- le plan le plus faible ---
    faible = option(args, "--plan-faible", "").strip()
    if len(faible) < 12:
        refus.append("plan le plus faible non nommé (--plan-faible \"Plan N (a–b s) : pourquoi\")")
    if not film.exists():
        refus.append(f"film introuvable : {film}")

    if refus:
        print("NOTE NON ÉCRITE, film non livrable :")
        for r in refus:
            print("  - " + r)
        return 2

    info = porte["info"]
    sha = hashlib.sha256(film.read_bytes()).hexdigest()[:16]
    lignes = [
        f"- Film : `{film.name}` (empreinte {sha})",
        f"- Écrit le : {datetime.date.today().isoformat()}, tour de correction n° {option(args, '--tour', '1')}",
        f"- Format : {info['largeur']}×{info['hauteur']}, {info['ips']} i/s, {info['duree']:.1f} s, "
        f"son {'oui' if info['son'] else 'non'}"
        + (f", {porte['volume_lufs']:.1f} LUFS" if porte.get("volume_lufs") is not None else ""),
        f"- Porte de livraison : **FEU {porte['bilan']}**",
    ]
    lignes += [f"  - [{c['feu']}] {c['nom']} : {c['valeur']}" + (f" ({c['detail']})" if c["detail"] else "")
               for c in porte["controles"]]
    lignes.append(f"- Relecture indépendante : `{Path(relecture).name}`, note la plus basse {min(notes.values()):g}/10")
    lignes.append("  - " + ", ".join(f"{c} {notes[c]:g}" for c in CRITERES))
    if accord:
        lignes.append(f"- Livré avec une note sous 8 sur accord du client : {accord}")
    lignes.append(f"- Plan le plus faible : {faible}")
    lignes.append(f"- Corrigé pendant la revue : {option(args, '--corrige', 'rien à signaler')}")
    lignes.append(f"- Non vérifié : {option(args, '--non-verifie', 'rien à signaler')}")
    faits = "\n".join(lignes)

    sortie = Path(option(args, "--sortie", str(film.parent / "livraison")))
    sortie.mkdir(parents=True, exist_ok=True)
    if (sortie / film.name).resolve() != film.resolve():
        shutil.copy2(film, sortie / film.name)
    note = (f"# Note de livraison\n\n## Faits\n\n{DEBUT}\n{faits}\nEmpreinte des faits : {empreinte(faits)}\n{FIN}\n\n"
            "## Notes du réalisateur\n\n"
            "_À compléter par l'agent, en quelques lignes : ce qu'est le film, pourquoi chaque point jaune est acceptable, "
            "les deux autres directions envisagées, ce qu'il changerait avec un tour de plus._\n")
    (sortie / NOM).write_text(note, encoding="utf-8")
    print(f"Note écrite : {sortie / NOM}\nFilm copié : {sortie / film.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
