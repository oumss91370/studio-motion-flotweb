"""Briques communes des mesures au pixel : lecture, luminance, couleur (Lab, ΔE2000), échantillonnage sous-pixel, tracés.

Aucune dépendance hors numpy, Pillow, OpenCV (pas de matplotlib : les courbes sont tracées avec Pillow).
Conventions : x vers la droite, y vers le bas (pixels) ; angles en degrés, 0° = à droite (3 h), 90° = en haut (12 h),
180° = à gauche, 270° = en bas, sens trigonométrique vu à l'écran. Luminance = Rec. 709 sur les valeurs sRVB (0–255).

Écrit par Flot Web (skill `reproduire-reel`). Fonctionne sous Windows, macOS et Linux.
"""
import sys
sys.dont_write_bytecode = True
import json, math, pathlib, subprocess
for _flux in (sys.stdout, sys.stderr):          # une console qui ne connaît pas un caractère ne doit pas arrêter une mesure
    try:
        _flux.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

def lire_json(chemin):
    """Lit un fichier JSON en UTF-8, avec ou sans marque d'ordre des octets (certains éditeurs de Windows en ajoutent une)."""
    return json.loads(pathlib.Path(chemin).read_text(encoding="utf-8-sig"))

def infos_video(video):
    """Largeur et hauteur TELLES QU'AFFICHÉES (rotation appliquée), cadence, nombre d'images, durée (ffprobe)."""
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height,r_frame_rate,avg_frame_rate,nb_frames,codec_name:stream_tags=rotate:stream_side_data=rotation:format=duration",
                            "-of", "json", str(video)], capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
    except FileNotFoundError:
        raise SystemExit("ffprobe introuvable : installer FFmpeg (version 5.1 ou plus) et vérifier qu'il est dans le PATH")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"ffprobe ne lit pas {video} : {e.stderr.strip() or 'fichier absent ou illisible'}")
    d = json.loads(r.stdout)
    if not d.get("streams"):
        raise SystemExit(f"{video} : aucune piste vidéo")
    s = d["streams"][0]
    def frac(t):
        a, b = (str(t).split("/") + ["1"])[:2]
        try:
            return float(a) / float(b) if float(b) else 0.0
        except ValueError:
            return 0.0
    fps = frac(s.get("r_frame_rate", "30/1")) or 30.0
    moy = frac(s.get("avg_frame_rate", "0/1"))
    duree = float(d.get("format", {}).get("duration") or 0)
    exact = str(s.get("nb_frames", "")).isdigit()
    n = int(s["nb_frames"]) if exact else int(round(duree * (moy or fps)))
    rot = 0.0
    for sd in s.get("side_data_list", []):
        if "rotation" in sd:
            rot = float(sd["rotation"])
    if not rot and str(s.get("tags", {}).get("rotate", "")).lstrip("-").isdigit():
        rot = float(s["tags"]["rotate"])
    W, H = int(s["width"]), int(s["height"])
    if abs(round(rot)) % 180 == 90:                 # FFmpeg applique la rotation à la lecture : les images sortent tournées
        W, H = H, W
    return dict(largeur=W, hauteur=H, ips=round(fps, 3), ips_moyenne=round(moy or fps, 3), images=n, images_exactes=exact,
                duree_s=round(duree, 3), codec=s.get("codec_name"), rotation=int(round(rot)),
                cadence_variable=bool(moy and abs(fps - moy) > 0.01 * fps))

def lire_images(video, nums, larg=None, crop=None):
    """Images numéro `nums` (base 0, ordre de décodage) d'une vidéo, lues en une seule passe. Renvoie {numéro: image PIL}.
    larg : largeur de sortie (None = pleine résolution, sans redimensionnement) ; crop : (x, y, w, h) en pixels de la source."""
    nums = sorted(set(int(n) for n in nums if int(n) >= 0))
    if not nums:
        return {}
    inf = infos_video(video)
    W, H = inf["largeur"], inf["hauteur"]
    vf = []
    if crop:
        x, y, w, h = [int(v) for v in crop]
        vf.append(f"crop={w}:{h}:{x}:{y}"); W, H = w, h
    if larg:
        h2 = max(2, int(round(H * larg / W / 2)) * 2)
        vf.append(f"scale={int(larg)}:{h2}"); W, H = int(larg), h2
    cmd = (["ffmpeg", "-nostdin", "-v", "error", "-i", str(video)] + (["-vf", ",".join(vf)] if vf else [])
           + ["-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
    # on arrête FFmpeg dès la dernière image voulue : ses messages de fin (« Error muxing a packet ») sont sans objet, on les tait
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    taille = W * H * 3
    veux, out, i, dernier = set(nums), {}, 0, nums[-1]
    try:
        while i <= dernier:
            buf = p.stdout.read(taille)
            if len(buf) < taille:
                break
            if i in veux:
                out[i] = Image.frombuffer("RGB", (W, H), buf, "raw", "RGB", 0, 1).copy()
            i += 1
    finally:
        p.stdout.close(); p.kill(); p.wait()
    if not out:
        raise ValueError(f"aucune image lue dans {video} (numéros demandés : {nums[0]} à {nums[-1]}) : vérifier le fichier, les numéros "
                         "et la version de FFmpeg (5.1 ou plus : `ffmpeg -version`)")
    return out

def lire_gris(video, larg=96):
    """Toute la vidéo en niveaux de gris, très réduite : tableau (images, hauteur, largeur) uint8. Sert à mesurer le mouvement."""
    inf = infos_video(video)
    h2 = max(2, int(round(inf["hauteur"] * larg / inf["largeur"] / 2)) * 2)
    r = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(video), "-vf", f"scale={larg}:{h2}", "-fps_mode", "passthrough",
                        "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0 or not r.stdout:
        raise SystemExit(f"FFmpeg ne lit pas {video} : {r.stderr.decode('utf-8', 'replace').strip()[-400:] or 'aucune image'} "
                         "(il faut FFmpeg 5.1 ou plus : `ffmpeg -version`)")
    a = np.frombuffer(r.stdout, dtype=np.uint8)
    n = len(a) // (larg * h2)
    return a[:n * larg * h2].reshape(n, h2, larg)

def etiquette(im, texte, t=15, haut=20, fond=(24, 24, 24)):
    """Ajoute un bandeau de texte au-dessus d'une image."""
    out = Image.new("RGB", (im.width, im.height + haut), fond)
    out.paste(im, (0, haut))
    ImageDraw.Draw(out).text((3, 1), texte, fill=(255, 255, 255), font=police(t, True))
    return out

def mosaique(ims, cols, marge=4, fond=(24, 24, 24)):
    """Range des images de même taille en grille."""
    ims = list(ims)
    if not ims:
        return None
    w, h = ims[0].size
    rangs = (len(ims) + cols - 1) // cols
    out = Image.new("RGB", (cols * (w + marge) + marge, rangs * (h + marge) + marge), fond)
    for i, im in enumerate(ims):
        out.paste(im, (marge + (i % cols) * (w + marge), marge + (i // cols) * (h + marge)))
    return out

def image_video(video, n):
    """Image numéro n (base 0) d'une vidéo, en pleine résolution, sans redimensionnement. Renvoie une image PIL."""
    ims = lire_images(video, [n])
    if int(n) not in ims:
        raise ValueError(f"la vidéo {video} n'a pas d'image numéro {n}")
    return ims[int(n)]

def ouvrir(chemin):
    """Image PIL. Accepte « fichier.png » ou « video.mp4@123 » (image numéro 123 de la vidéo)."""
    c = str(chemin)
    if "@" in c and c.rsplit("@", 1)[1].isdigit():
        v, n = c.rsplit("@", 1)
        return image_video(v, int(n))
    im = Image.open(c)
    if im.mode in ("RGBA", "LA", "PA") or (im.mode == "P" and "transparency" in im.info):
        # une image à fond transparent n'a pas de décor : le bord extérieur du trait ne se mesure pas. On la pose sur un gris moyen et on le dit
        print(f"ATTENTION : {pathlib.Path(c).name} a un fond transparent ; elle est posée sur un gris moyen. Pour un contrôle chiffré, "
              "rendre l'élément sur un fond comparable à celui de la référence.", file=sys.stderr)
        im = im.convert("RGBA")
        fond = Image.new("RGBA", im.size, (128, 128, 128, 255))
        return Image.alpha_composite(fond, im).convert("RGB")
    return im.convert("RGB")

def lire(chemin):
    """Image RVB float32 (0–255), sans aucun redimensionnement. Accepte aussi « video.mp4@123 »."""
    return np.asarray(ouvrir(chemin), dtype=np.float32)

def luma(rgb):
    return rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722

def hexa(c):
    r, g, b = [int(round(float(max(0, min(255, v))))) for v in c[:3]]
    return f"#{r:02x}{g:02x}{b:02x}"

def de_hexa(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float32)

def lab(rgb):
    """sRVB 0–255 -> CIE Lab (D65). Accepte un tableau (..., 3)."""
    c = np.asarray(rgb, dtype=np.float64) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], axis=-1)

def de2000(c1, c2):
    """Écart de couleur CIEDE2000 entre deux couleurs sRVB (0–255)."""
    L1, a1, b1 = lab(np.asarray(c1, dtype=np.float64)); L2, a2, b2 = lab(np.asarray(c2, dtype=np.float64))
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1 = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0.0
    h2 = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0.0
    dL, dC = L2 - L1, C2p - C1p
    dh = 0.0 if C1p * C2p == 0 else ((h2 - h1 + 180) % 360) - 180
    dH = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hm = h1 + h2
    elif abs(h1 - h2) <= 180:
        hm = (h1 + h2) / 2
    else:
        hm = (h1 + h2 + 360) / 2 if h1 + h2 < 360 else (h1 + h2 - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hm - 30)) + 0.24 * math.cos(math.radians(2 * hm))
         + 0.32 * math.cos(math.radians(3 * hm + 6)) - 0.20 * math.cos(math.radians(4 * hm - 63)))
    Sl = 1 + 0.015 * (Lm - 50) ** 2 / math.sqrt(20 + (Lm - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cpm, 1 + 0.015 * Cpm * T
    Rt = -2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7)) * math.sin(math.radians(60 * math.exp(-((hm - 275) / 25) ** 2)))
    return float(math.sqrt((dL / Sl) ** 2 + (dC / Sc) ** 2 + (dH / Sh) ** 2 + Rt * (dC / Sc) * (dH / Sh)))

def tsl(c):
    """sRVB -> (teinte °, saturation %, luminosité %) au sens TSL (HSL)."""
    r, g, b = [float(v) / 255 for v in c[:3]]
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0.0, 0.0, l * 100
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    h = ((g - b) / d % 6) if mx == r else ((b - r) / d + 2) if mx == g else ((r - g) / d + 4)
    return h * 60, s * 100, l * 100

def ecart_tsl(base, autre):
    h0, s0, l0 = tsl(base); h1, s1, l1 = tsl(autre)
    return dict(teinte=round(((h1 - h0 + 180) % 360) - 180, 1), saturation=round(s1 - s0, 1), luminosite=round(l1 - l0, 1))

def echantillons(img, xs, ys):
    """Interpolation bilinéaire aux positions flottantes (tableaux de même forme)."""
    xs = np.asarray(xs, dtype=np.float32); ys = np.asarray(ys, dtype=np.float32)
    if xs.ndim == 2 and xs.shape[0] > 30000:        # cv2.remap n'accepte pas plus de 32 767 lignes : on découpe
        return np.concatenate([cv2.remap(img, xs[i:i + 30000], ys[i:i + 30000], cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
                               for i in range(0, xs.shape[0], 30000)])
    return cv2.remap(img, xs, ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

def croisement(pos, val, niveau, i0, sens):
    """Position (interpolée) où val croise `niveau` en partant de l'indice i0 dans le sens +1 / -1. None si jamais."""
    i = i0
    n = len(val)
    while 0 <= i + sens < n:
        a, b = val[i], val[i + sens]
        if (a - niveau) * (b - niveau) <= 0 and a != b:
            t = (niveau - a) / (b - a)
            return float(pos[i] + (pos[i + sens] - pos[i]) * t)
        i += sens
    return None

# ------------------------------------------------------------------ tracés (Pillow)
_POLICES = {True: ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "Helvetica.ttc"],
            False: ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf", "Helvetica.ttc"]}

def police(t=16, gras=False):
    """Police d'étiquetage : Arial, sinon DejaVu ou Liberation (Linux), sinon la police intégrée à Pillow."""
    for nom in _POLICES[bool(gras)]:
        try:
            return ImageFont.truetype(nom, t)
        except OSError:
            continue
    try:
        return ImageFont.load_default(t)
    except TypeError:
        return ImageFont.load_default()

COULEURS = [(214, 39, 40), (31, 119, 180), (44, 160, 44), (255, 127, 14), (148, 103, 189), (23, 190, 207), (140, 86, 75), (127, 127, 127)]

def courbe(series, titre, xlabel, ylabel, taille=(900, 420), xlim=None, ylim=None, xticks=None, bandes=None, points=False):
    """series = [(nom, xs, ys[, couleur[, style]])] ; ys peut contenir des NaN (trous). style: 'ligne' | 'tirets' | 'points'.
    bandes = [(x0, x1, étiquette)] zones grisées. Renvoie une image PIL."""
    W, H = taille
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    f, fb = police(14), police(16, True)
    ml, mr, mt, mb = 62, 16, 34, 46
    allx = np.concatenate([np.asarray(s[1], dtype=float) for s in series]); ally = np.concatenate([np.asarray(s[2], dtype=float) for s in series])
    ally = ally[np.isfinite(ally)]
    x0, x1 = xlim or (float(np.nanmin(allx)), float(np.nanmax(allx)))
    if ylim:
        y0, y1 = ylim
    else:
        y0, y1 = (float(ally.min()), float(ally.max())) if len(ally) else (0, 1)
        e = (y1 - y0) * 0.08 or 1.0
        y0, y1 = y0 - e, y1 + e
    X = lambda x: ml + (x - x0) / (x1 - x0) * (W - ml - mr)
    Y = lambda y: H - mb - (y - y0) / (y1 - y0) * (H - mt - mb)
    for bx0, bx1, et in bandes or []:
        d.rectangle((X(bx0), mt, X(bx1), H - mb), fill=(236, 236, 240))
        d.text(((X(bx0) + X(bx1)) / 2, mt + 2), et, fill=(120, 120, 130), font=f, anchor="ma")
    # graduations
    def pas(a, b):
        r = (b - a) / 6
        p = 10 ** math.floor(math.log10(r))
        return next(m * p for m in (1, 2, 5, 10) if m * p >= r)
    py = pas(y0, y1)
    v = math.ceil(y0 / py) * py
    while v <= y1 + 1e-9:
        d.line((ml, Y(v), W - mr, Y(v)), fill=(225, 225, 225))
        d.text((ml - 6, Y(v)), f"{v:g}", fill=(60, 60, 60), font=f, anchor="rm")
        v += py
    if xticks is None:
        px = pas(x0, x1); v = math.ceil(x0 / px) * px; xticks = []
        while v <= x1 + 1e-9:
            xticks.append(v); v += px
    for v in xticks:
        d.line((X(v), mt, X(v), H - mb), fill=(235, 235, 235))
        d.text((X(v), H - mb + 4), f"{v:g}", fill=(60, 60, 60), font=f, anchor="ma")
    d.rectangle((ml, mt, W - mr, H - mb), outline=(90, 90, 90))
    lx = ml + 8
    for i, s in enumerate(series):
        nom, xs, ys = s[0], np.asarray(s[1], dtype=float), np.asarray(s[2], dtype=float)
        col = s[3] if len(s) > 3 and s[3] else COULEURS[i % len(COULEURS)]
        style = s[4] if len(s) > 4 else "ligne"
        pts = [(X(x), Y(min(max(y, y0), y1))) if np.isfinite(y) else None for x, y in zip(xs, ys)]
        if style == "points" or points:
            for p in pts:
                if p:
                    d.ellipse((p[0] - 2.5, p[1] - 2.5, p[0] + 2.5, p[1] + 2.5), fill=col)
        if style != "points":
            for k, (a, b) in enumerate(zip(pts, pts[1:])):
                if a and b and (style == "ligne" or k % 2 == 0):
                    d.line((a, b), fill=col, width=2)
        d.line((lx, 14, lx + 22, 14), fill=col, width=3)
        d.text((lx + 26, 14), nom, fill=(30, 30, 30), font=f, anchor="lm")
        lx += 34 + int(d.textlength(nom, font=f)) + 14
    d.text((W - mr, 14), titre, fill=(0, 0, 0), font=fb, anchor="rm")
    d.text(((ml + W - mr) / 2, H - 6), xlabel, fill=(40, 40, 40), font=f, anchor="mb")
    d.text((4, mt - 4), ylabel, fill=(40, 40, 40), font=f, anchor="lb")
    return im

def agrandir(rgb, k):
    """Agrandissement au plus proche voisin (on veut voir les pixels)."""
    a = np.clip(rgb, 0, 255).astype(np.uint8)
    return Image.fromarray(a).resize((a.shape[1] * k, a.shape[0] * k), Image.NEAREST)

def empiler(ims, horizontal=False, fond=(255, 255, 255), marge=8):
    ims = [i for i in ims if i is not None]
    if horizontal:
        W = sum(i.width for i in ims) + marge * (len(ims) + 1); H = max(i.height for i in ims) + 2 * marge
    else:
        W = max(i.width for i in ims) + 2 * marge; H = sum(i.height for i in ims) + marge * (len(ims) + 1)
    out = Image.new("RGB", (W, H), fond)
    p = marge
    for i in ims:
        out.paste(i, (p, marge) if horizontal else (marge, p))
        p += (i.width if horizontal else i.height) + marge
    return out

def texte_img(lignes, largeur=900, t=15, titre=None):
    f, fb = police(t), police(t + 2, True)
    h = (len(lignes) + (1 if titre else 0)) * (t + 6) + 14
    im = Image.new("RGB", (largeur, h), (255, 255, 255)); d = ImageDraw.Draw(im)
    y = 6
    if titre:
        d.text((8, y), titre, fill=(0, 0, 0), font=fb); y += t + 8
    for l in lignes:
        d.text((8, y), l, fill=(30, 30, 30), font=f); y += t + 6
    return im
