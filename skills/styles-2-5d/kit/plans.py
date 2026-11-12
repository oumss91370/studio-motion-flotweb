"""La liste de plans en données : la seule source des bornes du film.

Lue par Blender (bl_film.py), par les rendus de contrôle, la revue et l'assemblage : la liste de plans
et l'animation ne peuvent donc pas diverger. Lancé seul, ce fichier vérifie les bornes puis écrit
`plans.md` (la liste lisible) et `son/reperes.json` (les événements sonores, en numéros d'image).

  python outils/plans.py

Bornes en NUMÉROS D'IMAGE (30 i/s, image 0 = première image) : `a` incluse, `b` exclue.
Caler chaque `a` sur le début du mot qui ouvre l'idée du plan : image = round(début du mot en s × 30).

EXEMPLE NEUTRE À REMPLACER : deux plans, un personnage, un objet, un décor. Aucun fait réel.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R

IPS = R.IPS
TOTAL = 90          # nombre d'images du film (ici 3 s)

P = [
    dict(id=1, a=0, b=45,
         mots="Sur l'établi, une sonnette.",
         decor="ATELIER jour",
         cam="plan moyen, avancée lente vers l'établi (on situe le personnage et l'objet)",
         perso="Galet : yeux neutres, puis regard vers la sonnette",
         objet="sonnette posée sur l'établi",
         son="",
         jeu="pensée : et si j'appuyais ? Regard de côté 8, anticipation 14, bras levé 18, tenue jusqu'à 45"),
    dict(id=2, a=45, b=90,
         mots="Un doigt dessus, et elle tinte.",
         decor="ATELIER jour",
         cam="gros plan fixe sur la sonnette, légère plongée (on montre ce que fait l'objet)",
         perso="aucun",
         objet="sonnette : le bouton s'enfonce, la cloche vibre",
         son="tintement de sonnette à 56",
         jeu="bouton : anticipation 52, enfoncé 56 (contact, son), remonté 62 ; la cloche vibre jusqu'à 80, puis tenue"),
]

# Temps clés : chaque moment important, en numéros d'image. Une correction se dit « déplacer le contact à 56 ».
TEMPS_CLES = [
    (0, "PLAN 01 : image d'accroche, Galet et la sonnette"),
    (18, "Galet lève le bras"),
    (45, "COUPE vers PLAN 02"),
    (56, "le bouton touche le fond : tintement"),
    (89, "dernière image"),
]

# Événements sonores : seulement ce qui est physique. (identifiant, image du contact, description)
REPERES = [
    ("tintement", 56, "tintement de sonnette, attaque sur l'image 56"),
]

PLANS = {p["id"]: p for p in P}


def plan_de(image):
    """Le plan qui contient cette image."""
    return next(p for p in P if p["a"] <= image < p["b"])


def verifier():
    """Bornes jointives, durées, budget de bruitages. Renvoie (erreurs, remarques)."""
    err, rem = [], []
    if P[0]["a"] != 0:
        err.append("le premier plan doit commencer à l'image 0")
    for p, q in zip(P, P[1:]):
        if p["b"] != q["a"]:
            err.append(f"plans {p['id']} et {q['id']} : bornes non jointives ({p['b']} puis {q['a']})")
    if P[-1]["b"] != TOTAL:
        err.append(f"le dernier plan finit à {P[-1]['b']}, TOTAL vaut {TOTAL}")
    for p in P:
        d = (p["b"] - p["a"]) / IPS
        if p["b"] <= p["a"]:
            err.append(f"plan {p['id']} : durée nulle ou négative")
        elif d > 3.0:
            rem.append(f"plan {p['id']} : {d:.2f} s, plus de 3 s (une idée nouvelle le justifie-t-elle ?)")
        elif d < 1.3:
            rem.append(f"plan {p['id']} : {d:.2f} s, très court (tient-il en trois mots ?)")
    for i, f, _ in REPERES:
        if not 0 <= f < TOTAL:
            err.append(f"repère sonore « {i} » hors du film (image {f})")
    par10 = len(REPERES) / (TOTAL / IPS) * 10
    lo, hi = R.BRUITAGES_PAR_10S
    if TOTAL / IPS >= 20 and not lo <= par10 <= hi:
        rem.append(f"{par10:.1f} bruitages par 10 s (histoire narrée : {lo:g} à {hi:g})")
    return err, rem


def ecrire():
    L = ["# Liste de plans", "",
         f"{len(P)} plans, {TOTAL} images à {IPS} i/s ({TOTAL / IPS:.2f} s). Durée moyenne : {TOTAL / IPS / len(P):.2f} s.",
         "Les numéros d'image sont ceux de la vidéo (image 0 = première image). Bornes : début inclus, fin exclue.",
         "Source des données : `outils/plans.py` (lu par Blender). Ne pas modifier ce fichier à la main : il est réécrit.", ""]
    for p in P:
        L += [f"## Plan {p['id']:02d} — images {p['a']}–{p['b']} ({(p['b'] - p['a']) / IPS:.2f} s)",
              f"- **Mots** : « {p['mots']} »",
              f"- **Décor** : {p['decor']}",
              f"- **Caméra** : {p['cam']}",
              f"- **Personnage** : {p['perso']}",
              f"- **Objet héros** : {p['objet'] or '—'}",
              f"- **Son** : {p['son'] or 'aucun (rien de physique)'}",
              f"- **Ligne de jeu** : {p['jeu']}", ""]
    L += ["## Temps clés (numéros d'image)", "", "| Image | Temps | Événement |", "|---|---|---|"]
    L += [f"| {f} | {f / IPS:.2f} s | {e} |" for f, e in TEMPS_CLES]
    (R.RACINE / "plans.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    R.SON.mkdir(parents=True, exist_ok=True)
    (R.SON / "reperes.json").write_text(json.dumps(
        [{"id": i, "image": f, "t": round(f / IPS, 3), "son": s} for i, f, s in REPERES], ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    err, rem = verifier()
    for r in rem:
        print("remarque :", r)
    if err:
        for e in err:
            print("ERREUR :", e)
        raise SystemExit(1)
    ecrire()
    print(f"plans.md et son/reperes.json écrits : {len(P)} plans, {TOTAL} images, {len(REPERES)} repère(s) sonore(s)")
