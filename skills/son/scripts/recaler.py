#!/usr/bin/env python3
"""Recaler les bruitages d'après l'écoute earshot.
Entrées :
  ecoute.json     : `earshot timeline video.mp4 --cues cues.json --json --out ecoute.json`
  placements.json : liste [{"id": "<id du cue>", "t": <début du son en s>, ...autres champs libres}]
Règle du studio : attaque sur l'impact, +8 ms, jamais avant. Un son mesuré avant son image (au-delà de
--avance-toleree, 10 ms par défaut : la précision de la mesure) ou plus de 75 ms après est recalé à +8 ms. Seuls les sons à attaque (hit, click, pop, key, land, snap, tick, tock, knock, drop)
sont déplacés automatiquement ; whoosh / riser / swell sont signalés (ils se calent sur leur sommet ou leur fin).
Un écart > 150 ms ou « no sound » est signalé, jamais corrigé (le son trouvé n'est peut-être pas le bon).
Sortie : placements_recales.json + rapport à l'écran.
Usage : python3 recaler.py ecoute.json placements.json [--out placements_recales.json] [--cible 8]
"""
import sys
sys.dont_write_bytecode = True
import argparse, json

ATTAQUE = {"hit", "click", "clic", "pop", "bip", "blip", "pose", "key", "land", "snap", "tick", "tic", "tock", "knock", "drop",
           "bell", "ding", "impact", "coup", "choc"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ecoute"); ap.add_argument("placements")
    ap.add_argument("--out", default="placements_recales.json"); ap.add_argument("--cible", type=float, default=8.0)
    ap.add_argument("--avance-toleree", type=float, default=10.0, help="ms d'avance admises (précision de la mesure)")
    o = ap.parse_args()
    r = json.load(open(o.ecoute))
    items = ((r.get("sync") or {}).get("cues") or {}).get("items") or []
    if not items:
        raise SystemExit("Pas de calage par événement dans ecoute.json : relancer earshot timeline avec --cues.")
    pl = json.load(open(o.placements))
    par_id = {}
    for p in pl:
        par_id.setdefault(p.get("id"), []).append(p)
    corriges, signales = 0, []
    for it in items:
        cid, off, kind = it.get("id"), it.get("offset_ms"), (it.get("kind") or "").lower()
        if off is None or it.get("status") in ("no sound", "off"):
            signales.append(f"{it['t']:.3f}s {cid or kind} : aucun son ne répond"); continue
        if -o.avance_toleree <= off <= 75:
            continue
        if abs(off) > 150:
            signales.append(f"{it['t']:.3f}s {cid or kind} : écart {off:+.0f} ms (trop grand, vérifier à l'œil sur la planche)"); continue
        if kind and kind not in ATTAQUE:
            signales.append(f"{it['t']:.3f}s {cid} ({kind}) : écart {off:+.0f} ms, caler le sommet/la fin à la main"); continue
        cibles = par_id.get(cid) or []
        if not cibles:
            signales.append(f"{it['t']:.3f}s {cid} : écart {off:+.0f} ms mais aucun placement avec cet id"); continue
        d = (o.cible - off) / 1000.0
        for p in cibles:
            p["t"] = round(p["t"] + d, 4); p["recale_ms"] = round(d * 1000, 1)
        corriges += 1
        print(f"recalé {cid} : {off:+.0f} ms -> {o.cible:+.0f} ms (décalage {d*1000:+.0f} ms)")
    json.dump(pl, open(o.out, "w"), indent=1, ensure_ascii=False)
    st = r["sync"]["cues"].get("stats", {})
    print(f"\n{corriges} son(s) recalé(s) ; écart médian avant : {st.get('median_abs_offset_ms')} ms ; sans son : {len(st.get('no_sound', []))}")
    for s in signales:
        print("À VOIR :", s)
    print("Écrit :", o.out, "-> remixer puis relancer earshot timeline (au moins 2 tours).")


if __name__ == "__main__":
    main()
