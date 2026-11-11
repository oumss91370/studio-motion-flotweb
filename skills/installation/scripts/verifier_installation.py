#!/usr/bin/env python3
"""verifier_installation.py : dit ce qui est installé, ce qui manque, et la commande pour l'installer.

Usage :
    python3 verifier_installation.py [--json etat.json] [--projet DOSSIER]

Ne télécharge rien et n'installe rien : il regarde, puis affiche les commandes à lancer selon le système
(Windows, macOS, Linux). Code de sortie : 0 si tout l'indispensable est là, 1 sinon.
Trois niveaux :
  INDISPENSABLE  sans lui, aucune vidéo ne sort ni ne passe les contrôles (Python, Node, FFmpeg, HyperFrames, numpy).
  3D             nécessaire pour les styles 3D et 2.5D (Blender, uv, connecteur MCP for Blender).
  CONFORT        améliore les contrôles (Playwright, faster-whisper, earshot).
Three.js n'a rien à installer : il se charge dans la page du film (npm ou copie dans assets/vendor/).
"""
import json, os, platform, re, shutil, subprocess, sys
sys.dont_write_bytecode = True

SYS = {"Windows": "windows", "Darwin": "macos"}.get(platform.system(), "linux")
HF = "0.9.33"

def lance(cmd, delai=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=delai, shell=isinstance(cmd, str))
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return 1, str(e)

def version(txt, motif=r"(\d+\.\d+(?:\.\d+)?)"):
    m = re.search(motif, txt or "")
    return m.group(1) if m else None

def tuple_v(v):
    return tuple(int(x) for x in v.split(".")) if v else (0,)

def trouve_blender():
    p = shutil.which("blender")
    if p:
        return p
    cand = []
    if SYS == "windows":
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"), os.environ.get("ProgramFiles(x86)", "")):
            d = os.path.join(base, "Blender Foundation") if base else ""
            if d and os.path.isdir(d):
                for n in sorted(os.listdir(d), reverse=True):
                    cand.append(os.path.join(d, n, "blender.exe"))
    elif SYS == "macos":
        cand.append("/Applications/Blender.app/Contents/MacOS/Blender")
    else:
        cand += ["/usr/bin/blender", "/snap/bin/blender", os.path.expanduser("~/blender/blender")]
    for c in cand:
        if os.path.isfile(c):
            return c
    return None

def module(nom):
    c, _ = lance([sys.executable, "-c", f"import {nom}"])
    return c == 0

COMMANDES = {
    "node": {
        "windows": "winget install OpenJS.NodeJS.LTS",
        "macos": "brew install node",
        "linux": "sudo apt-get install -y nodejs npm   (ou nvm : https://github.com/nvm-sh/nvm)",
    },
    "ffmpeg": {
        "windows": "winget install Gyan.FFmpeg",
        "macos": "brew install ffmpeg",
        "linux": "sudo apt-get install -y ffmpeg",
    },
    "hyperframes": {s: f"npx -y hyperframes@{HF} --version   puis   npx -y hyperframes@{HF} browser ensure"
                    for s in ("windows", "macos", "linux")},
    "blender": {
        "windows": "winget install BlenderFoundation.Blender",
        "macos": "brew install --cask blender",
        "linux": "sudo snap install blender --classic   (ou https://www.blender.org/download/)",
    },
    "uv": {
        "windows": "winget install astral-sh.uv",
        "macos": "brew install uv",
        "linux": "curl -LsSf https://astral.sh/uv/install.sh | sh",
    },
    "connecteur": {s: "uvx mcp-for-blender setup   puis   claude mcp add -s user blender -- uvx mcp-for-blender"
                   for s in ("windows", "macos", "linux")},
    "numpy": {s: f'"{sys.executable}" -m pip install numpy' for s in ("windows", "macos", "linux")},
    "playwright": {s: f'"{sys.executable}" -m pip install playwright   puis   "{sys.executable}" -m playwright install chromium'
                   for s in ("windows", "macos", "linux")},
    "faster_whisper": {s: f'"{sys.executable}" -m pip install faster-whisper' for s in ("windows", "macos", "linux")},
    "earshot": {s: "voir skills/son/references/earshot.md (installation avec uv, environ 2 Go de modèles)"
                for s in ("windows", "macos", "linux")},
}

def controles():
    out = []
    def ajoute(cle, nom, niveau, ok, detail, aide=None):
        out.append({"cle": cle, "nom": nom, "niveau": niveau, "ok": bool(ok), "detail": detail,
                    "commande": None if ok else COMMANDES.get(cle, {}).get(SYS), "aide": aide})

    # INDISPENSABLE
    v = version(platform.python_version())
    ajoute("python", "Python 3.10 ou plus", "INDISPENSABLE", tuple_v(v) >= (3, 10), f"Python {v}",
           "https://www.python.org/downloads/")
    c, t = lance("node --version")
    v = version(t)
    ajoute("node", "Node.js 20 ou plus (avec npx)", "INDISPENSABLE", c == 0 and tuple_v(v) >= (20,) and shutil.which("npx"),
           f"Node {v}" if v else "absent", "skills/rendu/references/installation.md")
    for outil in ("ffmpeg", "ffprobe"):
        c, t = lance(f"{outil} -version")
        if outil == "ffmpeg":
            ok_ff, v_ff = c == 0, version(t)
        else:
            ok_ff = ok_ff and c == 0
    ajoute("ffmpeg", "FFmpeg et ffprobe", "INDISPENSABLE", ok_ff, f"FFmpeg {v_ff}" if ok_ff else "absent ou incomplet",
           "skills/rendu/references/installation.md")
    if shutil.which("npx"):
        c, t = lance(f"npx --offline hyperframes@{HF} --version", 90)
        if c != 0:
            c, t = lance(f"npx -y hyperframes@{HF} --version", 240)
        v = version(t)
        ajoute("hyperframes", f"HyperFrames {HF}", "INDISPENSABLE", c == 0 and v == HF,
               f"HyperFrames {v}" if v else "pas encore téléchargé (ou pas de réseau)",
               "skills/rendu/references/installation.md")
    else:
        ajoute("hyperframes", f"HyperFrames {HF}", "INDISPENSABLE", False, "npx absent : installer Node d'abord")

    ajoute("numpy", "numpy (porte de livraison)", "INDISPENSABLE", module("numpy"), "présent" if module("numpy") else "absent")

    # 3D
    b = trouve_blender()
    vb = None
    if b:
        c, t = lance([b, "--version"])
        vb = version(t)
    ajoute("blender", "Blender 4.2 ou plus", "3D", b and tuple_v(vb) >= (4, 2), f"Blender {vb} ({b})" if b else "absent",
           "skills/blender/references/installation.md")
    c, t = lance("uv --version")
    ajoute("uv", "uv (lance le connecteur Blender)", "3D", c == 0, f"uv {version(t)}" if c == 0 else "absent",
           "skills/blender/references/installation.md")
    conn, detail = False, "non déclaré dans Claude Code"
    if shutil.which("claude"):
        c, t = lance("claude mcp list", 60)
        if c == 0 and re.search(r"blender", t, re.I):
            conn, detail = True, "déclaré dans Claude Code (penser à démarrer le serveur dans Blender : volet N > onglet du connecteur)"
    else:
        detail = "commande `claude` introuvable ici : vérifier à la main dans la liste des connecteurs"
    ajoute("connecteur", "Connecteur MCP for Blender", "3D", conn, detail, "skills/blender/references/installation.md")

    # CONFORT
    ajoute("playwright", "Playwright (relevé des textes)", "CONFORT", module("playwright"),
           "présent" if module("playwright") else "absent", "skills/studio-coeur/references/controles.md")
    ajoute("faster_whisper", "faster-whisper (horodatage de la voix au mot)", "CONFORT", module("faster_whisper"),
           "présent" if module("faster_whisper") else "absent")
    ajoute("earshot", "earshot (écoute du mix par l'agent)", "CONFORT", bool(shutil.which("earshot")),
           "présent" if shutil.which("earshot") else "absent", "skills/son/references/earshot.md")
    return out

def main():
    args = sys.argv[1:]
    sortie_json = args[args.index("--json") + 1] if "--json" in args else None
    res = controles()
    print(f"Système : {platform.system()} {platform.release()} ({SYS})\n")
    for niveau, titre in (("INDISPENSABLE", "Indispensable (sans lui, aucune vidéo ne sort)"),
                          ("3D", "Styles 3D et 2.5D"), ("CONFORT", "Confort (contrôles plus complets)")):
        print(titre)
        for r in (x for x in res if x["niveau"] == niveau):
            print(f"  [{'OK' if r['ok'] else 'MANQUE'}] {r['nom']} : {r['detail']}")
            if not r["ok"]:
                if r["commande"]:
                    print(f"           à lancer : {r['commande']}")
                if r["aide"]:
                    print(f"           guide    : {r['aide']}")
        print()
    manque = {n: [r["nom"] for r in res if r["niveau"] == n and not r["ok"]] for n in ("INDISPENSABLE", "3D", "CONFORT")}
    if manque["INDISPENSABLE"]:
        print("RÉSULTAT : il manque de l'indispensable. Installer, puis relancer ce script.")
    elif manque["3D"]:
        print("RÉSULTAT : prêt pour les styles 2D. Les styles 3D et 2.5D demandent encore : " + ", ".join(manque["3D"]) + ".")
    else:
        print("RÉSULTAT : tout l'indispensable et la 3D sont en place." +
              (" Confort à compléter : " + ", ".join(manque["CONFORT"]) + "." if manque["CONFORT"] else ""))
    print("Three.js : rien à installer (il se charge dans la page du film).")
    if sortie_json:
        with open(sortie_json, "w", encoding="utf-8") as f:
            json.dump({"systeme": SYS, "controles": res, "manque": manque}, f, ensure_ascii=False, indent=2)
    return 1 if manque["INDISPENSABLE"] else 0

if __name__ == "__main__":
    sys.exit(main())
