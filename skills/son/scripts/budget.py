#!/usr/bin/env python3
"""Contrôle du budget de bruitages (Python standard).

  python3 budget.py placements.json --duree 30 [--max 8] [--cible 5] [--whoosh 3]

placements.json : liste [{"id": ..., "t": <s>, "type": "pop", "fichier": "..."}] (sortie de caler.py ou liste écrite
à la main). Ambiances et musique (type ambiance, musique, bed) ne comptent pas.
Règles contrôlées (code de sortie 1 si l'une est dépassée) :
  - au plus 8 bruitages par tranche de 10 s et en moyenne (cible environ 5) ; le MAXIMUM seul est une faute.
    Sous 3 par 10 s, le film est « calme » : c'est permis, le script le dit sans refuser ;
  - 3 whoosh au plus par vidéo ;
  - jamais la même prise deux fois de suite pour une même action (pop, impact, whoosh, pas…), SAUF le clic :
    un clic d'interface garde la même prise et le même niveau dans tout le film (règle 4 du skill), et le
    script signale au contraire un film qui utilise plusieurs clics différents (remarque, pas une faute) ;
  - pas de mitraillette (écart minimal 80 ms entre deux sons du même type, hors frappe au clavier).
"""
import sys
sys.dont_write_bytecode = True
import argparse, json

HORS_BUDGET = {"ambiance", "musique", "bed", "music", "voix"}
WHOOSH = {"whoosh", "swish", "transition", "passage", "woosh"}
CLAVIER = {"key", "touche", "typing", "frappe"}
CLIC = {"click", "clic", "toggle", "bascule"}          # une seule prise pour tout le film
MINI = 3                                               # sous ce nombre par 10 s : film calme (permis)


def fr(v):
    return f"{v:.1f}".replace(".", ",")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("placements"); ap.add_argument("--duree", type=float, required=True)
    ap.add_argument("--cible", type=float, default=5); ap.add_argument("--max", type=int, default=8)
    ap.add_argument("--whoosh", type=int, default=3)
    o = ap.parse_args()
    pl = [p for p in json.load(open(o.placements, encoding="utf-8")) if str(p.get("type", "")).lower() not in HORS_BUDGET]
    for p in pl:
        p["_t"] = float(p.get("t_evenement", p["t"])); p["_type"] = str(p.get("type", "?")).lower()
    pl.sort(key=lambda p: p["_t"])
    pb = []
    # la frappe au clavier compte pour un seul bruitage par rafale (sons à moins de 0,4 s l'un de l'autre)
    comptes, dernier_clavier = [], None
    for p in pl:
        if p["_type"] in CLAVIER:
            if dernier_clavier is not None and p["_t"] - dernier_clavier < 0.4:
                dernier_clavier = p["_t"]; continue
            dernier_clavier = p["_t"]
        comptes.append(p["_t"])
    n = len(comptes)
    moy = n / o.duree * 10 if o.duree else 0
    print(f"{n} bruitages sur {o.duree:g} s = {fr(moy)} par 10 s (cible environ {o.cible:g} ; maximum {o.max} ; sous {MINI} : film calme, permis)")
    t0 = 0.0
    while t0 < max(o.duree - 5, 0.01):
        k = sum(1 for t in comptes if t0 <= t < t0 + 10)
        etat = "trop chargé" if k > o.max else ""
        if etat:
            pb.append(f"{t0:.0f}-{t0 + 10:.0f} s : {k} bruitages (maximum {o.max}) : retirer d'abord les sons des coupes et des petits mouvements")
        print(f"  {t0:5.1f} à {min(t0 + 10, o.duree):5.1f} s : {k} {etat}")
        t0 += 5
    if moy > o.max:
        pb.append(f"moyenne {fr(moy)} par 10 s au-dessus de {o.max}")
    nw = sum(1 for p in pl if p["_type"] in WHOOSH)
    print(f"whoosh / transitions sonorisées : {nw} ({o.whoosh} au plus par vidéo)")
    if nw > o.whoosh:
        pb.append(f"{nw} whoosh : n'en garder que {o.whoosh}, sur les vrais grands mouvements")
    par_type = {}
    for p in pl:
        par_type.setdefault(p["_type"], []).append(p)
    for typ, liste in par_type.items():
        for a, b in zip(liste, liste[1:]):
            if a.get("fichier") and a.get("fichier") == b.get("fichier") and a.get("debut_fichier") == b.get("debut_fichier") and typ not in CLAVIER and typ not in CLIC:
                pb.append(f"{typ} : même prise deux fois de suite ({a.get('fichier')}) à {a['_t']:.2f} s et {b['_t']:.2f} s : alterner 2 à 4 prises")
                break
    for a, b in zip(pl, pl[1:]):
        if b["_t"] - a["_t"] < 0.08 and a["_type"] == b["_type"] and a["_type"] not in CLAVIER:
            pb.append(f"mitraillette : deux « {a['_type']} » à {a['_t']:.3f} s et {b['_t']:.3f} s (moins de 80 ms)")
    avoir = []
    clics = sorted({p.get("fichier") for p in pl if p["_type"] in CLIC and p.get("fichier")})
    if len(clics) > 1:
        avoir.append(f"{len(clics)} clics différents ({', '.join(clics)}) : un clic d'interface garde la même prise et le même niveau dans tout le film")
    if n and moy < MINI:
        avoir.append(f"{fr(moy)} par 10 s, sous la plage habituelle ({MINI} à {o.max}) : permis pour un film calme ; vérifier que l'accroche et le moment fort ont bien leur son")
    if n == 0:
        avoir.append("aucun bruitage : voulu (film muet, musique seule) ?")
    if avoir:
        print("\nÀ VOIR (pas une faute) :"); [print(" -", x) for x in avoir]
    if pb:
        print("\nÀ CORRIGER :"); [print(" -", x) for x in pb]; sys.exit(1)
    print(f"\nMaximum respecté ({fr(moy)} par 10 s pour {o.max} au plus)" + (" ; film calme." if n and moy < MINI else "."))


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    main()
