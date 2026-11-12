#!/usr/bin/env python3
"""Contrôle de cohérence du plugin : anciens noms, en-têtes des skills, renvois cassés, marqueurs privés.

  python scripts/verifier_plugin.py                 les trois contrôles de base, puis les comptes
  python scripts/verifier_plugin.py --prive         ajoute la recherche de marqueurs interdits dans un dépôt public
  python scripts/verifier_plugin.py --prive --motif "IDENTIFIANT" --motif "Nom Propre"
  python scripts/verifier_plugin.py --detail        liste aussi les renvois résolus ailleurs que dans leur skill

Ce qui est vérifié :
  a. plus aucune occurrence d'un ancien nom de skill ou de fiche (liste ANCIENS_NOMS), hors des fichiers réservés au
     coordinateur (RESERVES), qui sont listés à part sans faire échouer le contrôle ;
  b. chaque skills/<nom>/SKILL.md commence par un en-tête YAML valide, avec `name` égal au nom du dossier et une
     `description` non vide ;
  c. aucun renvoi cassé : tout chemin cité entre accents graves dans un fichier .md et qui ressemble à un fichier du
     plugin (skills/…, references/…, styles/…/STYLE.md, kit/…, scripts/…, gabarits/…, licenses/…, docs/…, ou
     <skill>/…) doit exister. Le chemin est cherché par rapport au fichier, à son skill, à skills/, à la racine, puis
     n'importe où dans le plugin (un renvoi du type « son `references/pipeline.md` » désigne le fichier d'un autre
     skill). Ne sont pas vérifiés : les gabarits à variables (<id>, …, *, {x}, $X), les blocs de code, la
     documentation tierce recopiée (dossiers officiel/, licenses/), les sections « Aperçu » et « Origine » des fiches
     et les lignes qui citent un dépôt d'origine (elles donnent les chemins de ce dépôt, pas ceux du plugin) ;
  d. avec --prive : chemins de poste (C:\\Users\\…, /Users/…, /home/…), liens vers une vidéo en ligne, et tout motif
     passé par --motif (expression régulière, insensible à la casse). Les identifiants à chercher se passent en
     argument : ils ne s'écrivent pas dans ce script.

Code de sortie : 0 si tout est bon, 1 sinon. Bibliothèque standard seulement. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
# les anciens noms sont écrits en deux morceaux pour que ce script ne se signale pas lui-même
ANCIENS_NOMS = ["styles-2-5d-" + "histoire-vraie", "histoire-vraie-" + "tete-ronde"]
RESERVES = ["BACKLOG.md", "NOTICE", "docs/CONVENTIONS.md"]            # réservés au coordinateur : listés, jamais modifiés ici
TEXTE = {".md", ".py", ".json", ".txt", ".sh", ".ps1", ".html", ".js", ".mjs", ".css", ".yml", ".yaml", ".toml", ".svg", ""}
IGNORES = {".git", "node_modules", "__pycache__", "_a-supprimer", "_to_delete"}
# documentation tierce recopiée telle quelle : ses chemins sont ceux de son projet d'origine
TIERS = ["/officiel/", "licenses/"]            # licenses/ cite les chemins des dépôts d'origine
PREFIXES = ("skills/", "references/", "styles/", "kit/", "scripts/", "gabarits/", "licenses/", "docs/")
EXTENSIONS = (".md", ".py", ".json", ".sh", ".txt", ".html", ".js", ".mjs", ".css", ".yml", ".yaml", ".wav", ".mp3", ".png", ".jpg", ".svg", ".woff2")
DANS_UN_SKILL = {"SKILL.md", "references", "styles", "scripts", "kit", "gabarits", "fonds"}
PROVENANCE = re.compile(r"\bcommit\b|\bdépôt\b|^\s*[-*>]*\s*\**Origine", re.I)
VARIABLE = re.compile(r"[<>…*{}$%]|\.\.\.|XXXX|NNNN|####")
PRIVES = [(r"[A-Za-z]:\\+Users\\", "chemin de poste Windows"), (r"(?<![\w.])/(?:c|C)/Users/", "chemin de poste Windows (écriture POSIX)"),
          (r"(?<![\w.])/Users/[A-Za-z]", "chemin de poste macOS"), (r"(?<![\w.])/home/[a-z][\w-]*/", "chemin de poste Linux"),
          (r"youtu\.be/[\w-]{6,}|youtube\.com/(?:watch\?v=|shorts/)[\w-]{6,}|tiktok\.com/@[\w.]+/video/\d+|instagram\.com/(?:reel|p)/[\w-]+", "lien vers une vidéo en ligne")]


def fichiers():
    for f in sorted(RACINE.rglob("*")):
        if f.is_file() and not (set(f.relative_to(RACINE).parts) & IGNORES):
            yield f


def rel(f):
    return f.relative_to(RACINE).as_posix()


def lire(f):
    try:
        return f.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def anciens_noms():
    erreurs, reserves = [], []
    for f in fichiers():
        if f.suffix.lower() not in TEXTE:
            continue
        t = lire(f)
        if t is None:
            continue
        for i, ligne in enumerate(t.splitlines(), 1):
            for nom in ANCIENS_NOMS:
                if nom in ligne:
                    (reserves if rel(f) in RESERVES else erreurs).append(f"{rel(f)}:{i} : ancien nom « {nom} »")
        for nom in ANCIENS_NOMS:
            if nom in rel(f):
                erreurs.append(f"{rel(f)} : ancien nom « {nom} » dans le chemin")
    return erreurs, reserves


def entetes():
    erreurs, noms = [], []
    for d in sorted((RACINE / "skills").iterdir()):
        if not d.is_dir():
            continue
        f = d / "SKILL.md"
        if not f.exists():
            erreurs.append(f"skills/{d.name}/ : pas de SKILL.md")
            continue
        noms.append(d.name)
        t = lire(f) or ""
        if t.startswith("\ufeff"):
            erreurs.append(f"{rel(f)} : marque d'ordre des octets en tête de fichier")
            t = t[1:]
        lignes = t.splitlines()
        if not lignes or lignes[0].strip() != "---":
            erreurs.append(f"{rel(f)} : la première ligne n'est pas « --- »")
            continue
        try:
            fin = next(i for i, l in enumerate(lignes[1:], 1) if l.strip() == "---")
        except StopIteration:
            erreurs.append(f"{rel(f)} : en-tête YAML non fermé")
            continue
        champs = {}
        for i, l in enumerate(lignes[1:fin], 2):
            if not l.strip() or l.lstrip().startswith("#"):
                continue
            m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", l)
            if not m:
                erreurs.append(f"{rel(f)}:{i} : ligne d'en-tête illisible (attendu « clé: valeur » sur une ligne)")
                continue
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                corps = v[1:-1]
                if v[0] == '"' and re.search(r'(?<!\\)"', corps):
                    erreurs.append(f"{rel(f)}:{i} : guillemet double non échappé dans la valeur de « {m.group(1)} »")
                v = corps
            elif v[:1] in "\"'":
                erreurs.append(f"{rel(f)}:{i} : guillemets non fermés dans la valeur de « {m.group(1)} »")
            elif re.search(r":\s", v) or v[:1] in "[{&*!|>%@`":
                erreurs.append(f"{rel(f)}:{i} : la valeur de « {m.group(1)} » doit être entre guillemets (elle contient « : » ou commence par un signe réservé)")
            champs[m.group(1)] = v
        if champs.get("name") != d.name:
            erreurs.append(f"{rel(f)} : name = « {champs.get('name')} », attendu « {d.name} »")
        if not champs.get("description", "").strip():
            erreurs.append(f"{rel(f)} : description absente ou vide")
    return erreurs, noms


def renvois(noms_skills):
    tous = {rel(f) for f in fichiers()}
    dossiers = {p.rsplit("/", 1)[0] + "/" for p in tous if "/" in p}
    dossiers |= {"/".join(d.rstrip("/").split("/")[:k]) + "/" for d in list(dossiers) for k in range(1, d.count("/") + 1)}
    erreurs, ailleurs, vus = [], [], 0
    for f in fichiers():
        if f.suffix.lower() != ".md" or any(t in "/" + rel(f) for t in TIERS) or rel(f) in RESERVES:
            continue
        t = lire(f)
        if t is None:
            continue
        parts = f.relative_to(RACINE).parts
        skill = RACINE / "skills" / parts[1] if len(parts) > 2 and parts[0] == "skills" else None
        dans_bloc = False
        for i, ligne in enumerate(t.splitlines(), 1):
            if f.name == "STYLE.md" and re.match(r"^##\s*(9|10)\.", ligne):
                break                                    # sections « Aperçu » et « Origine » d'une fiche : chemins des dépôts d'origine
            if ligne.lstrip().startswith("```"):
                dans_bloc = not dans_bloc
                continue
            if dans_bloc or PROVENANCE.search(ligne):
                continue                                 # une ligne qui cite un dépôt d'origine donne les chemins de ce dépôt
            for c in re.findall(r"`([^`\n]+)`", ligne):
                c = c.strip().replace("\\", "/")
                if " " in c or VARIABLE.search(c) or "/" not in c or c.startswith(("http", "/", "~", ".")) or "@" in c:
                    continue
                c = c.split("#")[0].rstrip(":,;")
                premier = c.split("/")[0]
                segs = c.split("/")
                if not (c.startswith(PREFIXES) or (premier in noms_skills and len(segs) > 1 and segs[1] in DANS_UN_SKILL)):
                    continue                             # `son/design.json`, `personnages/png/…` : dossiers de l'épisode du client, pas du plugin
                est_dossier = c.endswith("/")
                if not est_dossier and not c.lower().endswith(EXTENSIONS):
                    continue
                vus += 1
                bases = [f.parent] + ([skill] if skill else []) + [RACINE / "skills", RACINE]
                if any(((b / c).is_dir() if est_dossier else (b / c).is_file()) for b in bases):
                    continue
                ensemble = dossiers if est_dossier else tous
                trouve = sorted(p for p in ensemble if p.endswith("/" + c) or p == c)
                if trouve:
                    ailleurs.append(f"{rel(f)}:{i} : `{c}` -> {trouve[0]}" + (f" (et {len(trouve) - 1} autre(s))" if len(trouve) > 1 else ""))
                else:
                    erreurs.append(f"{rel(f)}:{i} : renvoi cassé `{c}`")
    return erreurs, ailleurs, vus


def prives(motifs):
    regles = [(re.compile(m), nom) for m, nom in PRIVES] + [(re.compile(m, re.I), f"motif « {m} »") for m in motifs]
    erreurs, reserves = [], []
    moi = rel(pathlib.Path(__file__).resolve())
    for f in fichiers():
        if f.suffix.lower() not in TEXTE or rel(f) == moi:
            continue
        t = lire(f)
        if t is None:
            continue
        for i, ligne in enumerate(t.splitlines(), 1):
            for rx, nom in regles:
                m = rx.search(ligne)
                if m:
                    (reserves if rel(f) in RESERVES else erreurs).append(f"{rel(f)}:{i} : {nom} : « {ligne.strip()[max(0, m.start() - 30):m.end() + 30]} »")
    return erreurs, reserves


def comptes(noms):
    fiches = {}
    for f in fichiers():
        if f.name == "STYLE.md":
            fiches.setdefault(f.relative_to(RACINE).parts[1], []).append(f.parent.name)
    doublons = {}
    for cat, ids in fiches.items():
        for i in ids:
            doublons.setdefault(i, []).append(cat)
    return fiches, {k: v for k, v in doublons.items() if len(v) > 1}


def main():
    ap = argparse.ArgumentParser(description="Contrôle de cohérence du plugin (anciens noms, en-têtes, renvois, marqueurs privés).")
    ap.add_argument("--prive", action="store_true", help="chercher aussi les marqueurs interdits dans un dépôt public")
    ap.add_argument("--motif", action="append", default=[], help="motif supplémentaire à chercher avec --prive (expression régulière) ; répétable")
    ap.add_argument("--detail", action="store_true", help="lister les renvois résolus ailleurs que dans leur skill")
    a = ap.parse_args()
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    echec = 0

    def bloc(titre, erreurs):
        nonlocal echec
        print(f"\n{titre} : " + ("OK" if not erreurs else f"{len(erreurs)} ERREUR(S)"))
        for e in erreurs:
            print("  - " + e)
        echec += len(erreurs)

    e, reserves = anciens_noms()
    bloc("a. Anciens noms (" + ", ".join(ANCIENS_NOMS) + ")", e)
    if reserves:
        print(f"   Fichiers réservés au coordinateur, non modifiés ({len(reserves)} occurrence(s), à mettre à jour par lui) :")
        for r in reserves:
            print("     · " + r)
    e, noms = entetes()
    bloc(f"b. En-têtes YAML des {len(noms)} SKILL.md (name = nom du dossier, description non vide)", e)
    e, ailleurs, vus = renvois(set(noms))
    bloc(f"c. Renvois entre accents graves ({vus} chemins vérifiés, dont {len(ailleurs)} résolus dans un autre dossier du plugin)", e)
    if a.detail:
        for r in ailleurs:
            print("     · " + r)
    if a.prive:
        e, reserves = prives(a.motif)
        bloc("d. Marqueurs interdits dans un dépôt public" + (f" (+ {len(a.motif)} motif(s) donné(s))" if a.motif else ""), e)
        if reserves:
            print(f"   Dans les fichiers réservés au coordinateur ({len(reserves)}), à vérifier par lui avant de pousser :")
            for r in reserves:
                print("     · " + r)
    fiches, doublons = comptes(noms)
    total = sum(len(v) for v in fiches.values())
    socle = [n for n in noms if n not in fiches]
    print(f"\nComptes sur disque : {len(noms)} skills ({len(socle)} sans fiche de style, {len(fiches)} avec), {total} fiches STYLE.md")
    for cat in sorted(fiches):
        print(f"  {len(fiches[cat]):3d}  {cat}")
    if doublons:
        bloc("Identifiants de style présents dans deux dossiers", [f"{k} : {', '.join(v)}" for k, v in sorted(doublons.items())])
    print("\n" + ("TOUT EST BON" if not echec else f"ÉCHEC : {echec} erreur(s)"))
    return 1 if echec else 0


if __name__ == "__main__":
    sys.exit(main())
