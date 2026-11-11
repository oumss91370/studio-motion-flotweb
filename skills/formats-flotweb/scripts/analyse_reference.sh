#!/usr/bin/env bash
# Analyse complète d'une vidéo de référence avec les outils HyperFrames + ffmpeg.
# Écrit par Flot Web.
# Version épinglée : toutes les commandes passent par `npx -y hyperframes@0.9.33` (règle du skill `rendu`).
# `hyperframes measure` (probe, cuts, events, frames, look) et `hyperframes beats <fichier> --json` existent bien en
# 0.9.33 (vérifié par `--help` et par un essai réel le 11/11 ; détail : skill `rendu`, references/cli.md).
# Le script détecte quand même `measure` : s'il ne répond pas (pas de réseau au premier appel, autre version, Chrome
# ou FFmpeg absent), il fait les mêmes relevés avec ffmpeg et ffprobe seuls (repli), sans carte des évènements ni
# relevé du look, qui restent alors à faire à l'œil (references/mesurer-une-reference.md).
# Usage : analyse_reference.sh <video.mp4> <dossier_sortie> [dossier_de_travail]
#   dossier_de_travail : dossier d'où la commande est lancée (défaut : le dossier de sortie ; rien n'y est installé)
# Produit dans <dossier_sortie> :
#   probe.json, cuts.json, events.json (+ images), frames_0.5s/ (planche toutes les 0,5 s),
#   strips/ (images consécutives autour de chaque événement ; en repli : autour de chaque coupe), beats.json, look.json,
#   (en repli : events.json et look.json valent {} et le fichier REPLI.txt dit ce qui manque)
#   scenes_ffmpeg.txt (2e détecteur de coupes, pour les fondus que `cuts` rate),
#   plans/ (une image pleine résolution au milieu de chaque plan), audio16k.wav
set -euo pipefail
V="$(realpath "$1")"; OUT="$(realpath -m "$2")"
mkdir -p "$OUT"/plans
HF="${3:-$OUT}"
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_NO_UPDATE_CHECK=1 HYPERFRAMES_SKIP_SKILLS=1
HFV="hyperframes@0.9.33"
hf(){ (cd "$HF" && npx -y "$HFV" "$@") 2>/dev/null | sed -n '/^{/,$p'; }
# `measure` répond-il ? (le premier appel télécharge la CLI épinglée si elle n'est pas en cache)
# Forcer le repli (essai, machine sans réseau ni cache) : ANALYSE_SANS_MEASURE=1 analyse_reference.sh …
if [ "${ANALYSE_SANS_MEASURE:-0}" != 1 ] && (cd "$HF" && npx -y "$HFV" measure --help) >/dev/null 2>&1; then MEASURE=1; else MEASURE=0; fi

if [ "$MEASURE" = 1 ]; then
  echo "1/8 probe";   hf measure probe "$V" > "$OUT/probe.json"
  echo "2/8 coupes";  hf measure cuts "$V" > "$OUT/cuts.json"
else
  echo "$HFV measure indisponible : relevés faits avec ffmpeg (repli)"
  printf '%s\n' "Analyse faite en repli (ffmpeg seul) : pas de carte des évènements (events.json vide), pas de relevé du look (look.json vide)." \
    "Bandes d'images prises autour des coupes, pas autour des évènements. Compléter à l'œil : references/mesurer-une-reference.md." > "$OUT/REPLI.txt"
  echo "1/8 probe (ffprobe)"
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_frames:format=duration -of json "$V" \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); s=d["streams"][0]; n,q=s["r_frame_rate"].split("/"); print(json.dumps({"duration": float(d["format"]["duration"]), "width": s["width"], "height": s["height"], "fps": round(float(n)/float(q), 3), "source": "ffprobe"}))' \
    > "$OUT/probe.json"
  echo "2/8 coupes franches (ffmpeg, seuil 0,30)"
  ffmpeg -hide_banner -i "$V" -vf "select='gt(scene,0.30)',showinfo" -an -f null - 2>&1 \
    | { grep -o 'pts_time:[0-9.]*' || true; } | cut -d: -f2 \
    | python3 -c 'import json,sys; print(json.dumps({"cuts": [{"t": float(x)} for x in sys.stdin.read().split()], "source": "ffmpeg scene 0.30"}))' \
    > "$OUT/cuts.json"
fi
echo "3/8 coupes ffmpeg (fondus, coupes douces)"
ffmpeg -hide_banner -i "$V" -vf "select='gt(scene,0.18)',showinfo" -an -f null - 2>&1 \
  | { grep -o 'pts_time:[0-9.]*' || true; } | cut -d: -f2 > "$OUT/scenes_ffmpeg.txt" || true
if [ "$MEASURE" = 1 ]; then
  echo "4/8 événements + son"; hf measure events "$V" --map --out "$OUT/events" > "$OUT/events.json"
  echo "5/8 planches toutes les 0,5 s"; hf measure frames "$V" --every 0.5 --width 270 --out "$OUT/frames_0.5s" > /dev/null
  echo "6/8 bandes autour des événements"; hf measure frames "$V" --events --max 16 --width 270 --out "$OUT/strips" > /dev/null
else
  echo "4/8 événements : non relevés en repli"; echo '{}' > "$OUT/events.json"
  echo "5/8 planches toutes les 0,5 s (ffmpeg)"; mkdir -p "$OUT/frames_0.5s"
  ffmpeg -v error -y -i "$V" -vf "fps=2,scale=270:-2" "$OUT/frames_0.5s/f_%04d.png"
  echo "6/8 bandes de 16 images autour de chaque coupe (ffmpeg)"; mkdir -p "$OUT/strips"
  python3 - "$OUT" "$V" <<'PY'
import json, subprocess, sys
out, v = sys.argv[1], sys.argv[2]
fps = json.load(open(f"{out}/probe.json")).get("fps") or 30
for i, c in enumerate(json.load(open(f"{out}/cuts.json"))["cuts"][:40]):
    debut = max(0.0, c["t"] - 8 / fps)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{debut:.3f}", "-i", v, "-frames:v", "16",
                    "-vf", "scale=270:-2", f"{out}/strips/C{i+1:02d}_{c['t']:.2f}s_%02d.png"])
PY
fi
echo "7/8 rythme et look"
if [ "${ANALYSE_SANS_MEASURE:-0}" = 1 ]; then echo '{}' > "$OUT/beats.json"; else hf beats "$V" --json > "$OUT/beats.json" || echo '{}' > "$OUT/beats.json"; fi
[ -s "$OUT/beats.json" ] || echo '{}' > "$OUT/beats.json"
if [ "$MEASURE" = 1 ]; then hf measure look "$V" > "$OUT/look.json"; else echo '{}' > "$OUT/look.json"; fi
echo "8/8 une image pleine résolution par plan"
python3 - "$OUT" "$V" <<'PY'
import json, subprocess, sys
out, v = sys.argv[1], sys.argv[2]
cuts = json.load(open(f"{out}/cuts.json"))
extra = [float(x) for x in open(f"{out}/scenes_ffmpeg.txt").read().split()] if open(f"{out}/scenes_ffmpeg.txt").read().strip() else []
dur = json.load(open(f"{out}/probe.json"))["duration"]
b = sorted(set([0.0] + [c["t"] for c in cuts.get("cuts", [])] + [round(x, 2) for x in extra] + [dur]))
# fusionner les bornes à moins de 0,25 s
m = [b[0]]
for x in b[1:]:
    if x - m[-1] >= 0.25: m.append(x)
shots = list(zip(m[:-1], m[1:]))
json.dump([{"id": f"P{i+1:02d}", "start": round(a, 3), "end": round(e, 3), "seconds": round(e - a, 3)} for i, (a, e) in enumerate(shots)],
          open(f"{out}/plans.json", "w"), indent=1, ensure_ascii=False)
for i, (a, e) in enumerate(shots):
    for tag, t in (("a", a + 0.05), ("m", (a + e) / 2), ("z", max(a, e - 0.07))):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", v, "-frames:v", "1", f"{out}/plans/P{i+1:02d}_{tag}.png"])
print(len(shots), "plans")
PY
ffmpeg -v error -y -i "$V" -ac 1 -ar 16000 "$OUT/audio16k.wav" || true
echo "Fini : $OUT"
