#!/usr/bin/env python3
"""Contrôle automatique d'un rendu (ou d'une référence) :
  1. images figées : toute suite d'images sans mouvement plus longue que --hold secondes ;
  2. plans : coupes détectées, énergie de mouvement par plan ;
  3. plans trop semblables : chaque plan doit être différent des autres (décor + cadrage) ;
  4. (option --ref) même découpage et même énergie que la référence, plan par plan.
Usage : python3 controle_rendu.py notre.mp4 [--ref reference.mp4] [--hold 0.5] [--allow 3.2-4.0,...] [--out rapport.json]
Sortie : rapport JSON + résumé lisible ; code de sortie 1 si un défaut bloquant est trouvé.
"""
import argparse, json, subprocess, sys
import numpy as np

W, H = 108, 192


def frames(path):
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=avg_frame_rate",
                        "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
    n, d = (p.split("/") + ["1"])[:2]
    fps = float(n) / float(d or 1)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"scale={W}:{H}:flags=area,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    return a, fps


def analyse(path, hold, allow):
    a, fps = frames(path)
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))  # différence moyenne entre images voisines (0-255)
    # coupes : différence forte et isolée
    med = np.median(d) + 1e-6
    cuts = [i + 1 for i in range(len(d)) if d[i] > max(18, 6 * med) and d[i] >= d[max(0, i - 1):i + 2].max()]
    bounds = [0] + cuts + [len(a)]
    shots = []
    for s, e in zip(bounds[:-1], bounds[1:]):
        if e - s < 3:
            continue
        seg = d[s:e - 1]
        shots.append({"start": round(s / fps, 3), "end": round(e / fps, 3), "seconds": round((e - s) / fps, 2),
                      "energie_moy": round(float(seg.mean()), 3), "energie_min": round(float(seg.min()), 3),
                      "mid": (s + e) // 2})
    # images figées (seuil : moins de 0,08 niveau de gris en moyenne = rien ne bouge)
    still = d < 0.08
    frozen, i = [], 0
    while i < len(still):
        if still[i]:
            j = i
            while j < len(still) and still[j]:
                j += 1
            t0, t1 = i / fps, (j + 1) / fps
            if t1 - t0 >= hold and not any(a0 <= t0 and t1 <= a1 for a0, a1 in allow):
                frozen.append([round(t0, 2), round(t1, 2)])
            i = j
        else:
            i += 1
    # plans trop semblables (corrélation des images du milieu, réduites)
    sims = []
    mids = [a[s["mid"]].ravel() for s in shots]
    mids = [(m - m.mean()) / (m.std() + 1e-6) for m in mids]
    for x in range(len(mids)):
        for y in range(x + 1, len(mids)):
            c = float((mids[x] * mids[y]).mean())
            if c > 0.90:
                sims.append({"plans": [x + 1, y + 1], "t": [shots[x]["start"], shots[y]["start"]], "correlation": round(c, 3)})
    for s in shots:
        s.pop("mid")
    return {"video": path, "fps": fps, "duree": round(len(a) / fps, 2), "nb_plans": len(shots), "plans": shots,
            "images_figees": frozen, "plans_semblables": sims}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--ref"); ap.add_argument("--hold", type=float, default=0.5)
    ap.add_argument("--allow", default="", help="plages tenues voulues, ex. 3.2-4.0,10-10.6")
    ap.add_argument("--out", default="controle_rendu.json")
    o = ap.parse_args()
    allow = [tuple(map(float, x.split("-"))) for x in o.allow.split(",") if x]
    r = {"notre": analyse(o.video, o.hold, allow)}
    bad = bool(r["notre"]["images_figees"] or r["notre"]["plans_semblables"])
    if o.ref:
        ref = analyse(o.ref, 99, [])
        r["reference"] = {k: ref[k] for k in ("duree", "nb_plans", "plans")}
        comp = []
        for i, (p, q) in enumerate(zip(ref["plans"], r["notre"]["plans"])):
            comp.append({"plan": i + 1, "ref": [p["start"], p["end"]], "notre": [q["start"], q["end"]],
                         "ecart_debut_s": round(q["start"] - p["start"], 2),
                         "energie_ref": p["energie_moy"], "energie_notre": q["energie_moy"],
                         "ratio_energie": round(q["energie_moy"] / (p["energie_moy"] + 1e-6), 2)})
        r["comparaison"] = comp
        if ref["nb_plans"] != r["notre"]["nb_plans"]:
            bad = True
        if any(abs(c["ecart_debut_s"]) > 0.1 or not 0.5 <= c["ratio_energie"] <= 2 for c in comp):
            bad = True
    json.dump(r, open(o.out, "w"), indent=1, ensure_ascii=False)
    n = r["notre"]
    print(f"{n['video']} : {n['duree']} s, {n['nb_plans']} plans")
    print("Images figées >", o.hold, "s :", n["images_figees"] or "aucune")
    print("Plans trop semblables :", n["plans_semblables"] or "aucun")
    if o.ref:
        print(f"Référence : {r['reference']['nb_plans']} plans / nous : {n['nb_plans']}")
        for c in r["comparaison"]:
            flag = "" if abs(c["ecart_debut_s"]) <= 0.1 and 0.5 <= c["ratio_energie"] <= 2 else "  <-- à corriger"
            print(f"  P{c['plan']:02d} ref {c['ref']} nous {c['notre']} énergie x{c['ratio_energie']}{flag}")
    print("RÉSULTAT :", "À CORRIGER" if bad else "OK")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
