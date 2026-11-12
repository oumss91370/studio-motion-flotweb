"""Générateur de personnages du style « tête ronde, trait plein et délié ».

Le client DÉCRIT ses personnages (couleurs, coiffe, accessoire, pilosité, taille) ; ce fichier les dessine avec le rendu
mesuré : contour à pleins et déliés réglé par la lumière, tête à croissant d'ombre et filet de lumière, torse à ombre
propre, membres en traits constants, coiffes à trois tons, jambe du second plan éclaircie, palettes par ambiance.
Aucun personnage n'est fourni : ceux de l'exemple sont dans film.py et sont à remplacer.

    import pantin
    pantin.definir({"lea": dict(couleur="#2f6fb5", coiffe=dict(type="bonnet", tons=("#e8503a", "#c23c2e", "#f4ead2")))})
    image, ancre = pantin.rendre("lea", pantin.pose(amb="soir", lum=12, **pantin.EXPR["stupeur"]), zoom=0.5)

Paramètres de rendu d'une pose : amb = "jour" | "soir" | "interieur" | "nuit" ; lum = direction d'où vient la lumière,
à l'écran, en degrés (0 = de la droite, 90 = du haut, 180 = de la gauche).
Unité : D = diamètre de la tête = 300 unités de dessin. Sol en y = 0, le haut est en y négatif.
Lancé seul (python outils/pantin.py) : écrit les planches revue/personnages-*.png des personnages de film.py.
Dépendances : Pillow, resvg-py (pip install pillow resvg-py). Écrit par Flot Web.
"""
import io, math, pathlib, random, sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import regles as R

D = R.D_DESSIN
INK, MEMBRE, JAMBE_AR = "#2b1a2e", "#2b1a2f", "#2b1a30"     # jetons, remplacés à la fin par les couleurs de l'ambiance
A0, H1 = R.CONTOUR["a0"], R.CONTOUR["h1"]
LW = R.CONTOUR["membres"] * D
FIN = R.CONTOUR["visage"] * D
SW = R.CONTOUR["detail"] * D
CWF = R.CONTOUR["coiffe"] * D
_LUM = [0.5, -0.866]            # vecteur unitaire vers la lumière, en coordonnées de dessin (y vers le bas) ; fixé par svg_perso
CW, CH = 1800, 1700             # toile (unités de dessin)
AX, AY = CW / 2, 1500           # ancre : point au sol entre les pieds
BOUCHE_IN, LANGUE, BLANC, SUEUR = "#5a1626", "#f0808c", "#fffaf0", "#8cc2d2"
BT = 'stroke-linecap="butt"'

PERSOS = {}
DEFAUT = dict(torse="gelule", couleur="#2f6fb5", couleur2=None, garniture="#f4ead2", ceinture=None, col=None, boutons=0, bande_bas=False,
              coiffe=None, cheveux=None, accessoire=None, accessoire_couleur="#8a5a34", pilosite=None, poil=None, sourcil=None,
              h=1.65, jambes=1.3, torse_h=1.0, torse_l=0.72)
COIFFES = ("cheveux", "chignon", "bonnet", "casquette", "beret", "fichu", "cloche")
ACCESSOIRES = ("sacoche", "echarpe", "tablier")
PILOSITES = ("moustache", "barbiche", "chaume", "barbe")


def definir(persos):
    """Enregistre les personnages du client. Chaque fiche complète DEFAUT ; une clé inconnue est refusée (faute de frappe)."""
    PERSOS.clear()
    for nom, fiche in persos.items():
        inconnues = set(fiche) - set(DEFAUT)
        if inconnues:
            raise ValueError(f"personnage « {nom} » : clés inconnues {sorted(inconnues)} ; clés possibles : {sorted(DEFAUT)}")
        c = dict(DEFAUT, **fiche)
        if c["torse"] not in ("gelule", "cloche"):
            raise ValueError(f"personnage « {nom} » : torse = 'gelule' ou 'cloche'")
        if c["coiffe"] and c["coiffe"].get("type") not in COIFFES:
            raise ValueError(f"personnage « {nom} » : coiffe inconnue ; types possibles : {COIFFES}")
        if c["accessoire"] and c["accessoire"] not in ACCESSOIRES:
            raise ValueError(f"personnage « {nom} » : accessoire inconnu ; possibles : {ACCESSOIRES}")
        if c["pilosite"] and c["pilosite"] not in PILOSITES:
            raise ValueError(f"personnage « {nom} » : pilosité inconnue ; possibles : {PILOSITES}")
        c["couleur2"] = c["couleur2"] or R.melange(c["couleur"], "#2a0a24", 0.26)     # ombre propre : luminosité −11 à −17, un peu moins saturée
        c["cle"] = sum(ord(ch) for ch in nom + c["couleur"])                           # fixe la forme de la tête de CE personnage
        PERSOS[nom] = c
    return PERSOS


# ---------------------------------------------------------------- géométrie
def rot(x, y, a):
    c, s = math.cos(a), math.sin(a)
    return x * c - y * s, x * s + y * c

def f2(v):
    return f"{v:.1f}"

def P(*pts):
    return " ".join(f"{f2(x)},{f2(y)}" for x, y in pts)

def membre(a, b, c, arrondi=0.14):
    """Trait à deux segments a-b-c : droit à l'appui, plié en angle VIF au coude ou au genou (un membre arqué fait « mou »)."""
    b1 = (b[0] + (a[0] - b[0]) * arrondi, b[1] + (a[1] - b[1]) * arrondi)
    b2 = (b[0] + (c[0] - b[0]) * arrondi, b[1] + (c[1] - b[1]) * arrondi)
    return f"M{P(a)} L{P(b1)} Q{P(b)} {P(b2)} L{P(c)}"

def ik(a, c, l1, l2, signe):
    """Genou ou coude entre a et c. Si la cible est trop loin, le membre s'étire."""
    dx, dy = c[0] - a[0], c[1] - a[1]
    d = math.hypot(dx, dy) or 1e-6
    if d >= l1 + l2:
        return (a[0] + dx * l1 / (l1 + l2), a[1] + dy * l1 / (l1 + l2))
    x = (l1 * l1 - l2 * l2 + d * d) / (2 * d)
    h = math.sqrt(max(0.0, l1 * l1 - x * x))
    ux, uy = dx / d, dy / d
    return (a[0] + ux * x - uy * h * signe, a[1] + uy * x + ux * h * signe)

def trait(d, coul=INK, w=LW, extra=""):
    cap = "" if "stroke-linecap" in extra else 'stroke-linecap="round" '
    return f'<path d="{d}" fill="none" stroke="{coul}" stroke-width="{f2(w)}" {cap}stroke-linejoin="round" {extra}/>'

def forme(d, fill, w=SW, coul=INK, extra=""):
    """Forme cernée à pleins et déliés : silhouette d'encre, puis l'aplat décalé vers la lumière.
    Sous 75 % de l'épaisseur nominale (petits détails) : trait constant."""
    if fill == "none" or w < SW * 0.75 or extra:
        return f'<path d="{d}" fill="{fill}" stroke="{coul}" stroke-width="{f2(w)}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'
    k = w / SW
    dx, dy = _LUM[0] * H1 * D * k, _LUM[1] * H1 * D * k
    return (f'<path d="{d}" fill="{coul}" stroke="{coul}" stroke-width="{f2(2 * A0 * D * k)}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="{fill}" transform="translate({f2(dx)},{f2(dy)})"/>')

def tons(d, clair, moyen, uid, w=CWF, decal=0.14 * D):
    """Forme à tons francs et contour RÉGULIER (coiffes, accessoires) : ton clair, et un croissant de ton moyen du côté opposé à la lumière."""
    lx, ly = _LUM
    return (f'<clipPath id="{uid}"><path d="{d}"/></clipPath>'
            f'<path d="{d}" fill="{moyen}" stroke="{INK}" stroke-width="{f2(2 * w)}" stroke-linejoin="round"/>'
            f'<g clip-path="url(#{uid})"><path d="{d}" fill="{moyen}"/>'
            f'<path d="{d}" fill="{clair}" transform="translate({f2(lx * decal)},{f2(ly * decal)})"/></g>')


# ---------------------------------------------------------------- pose par défaut
def pose(**kw):
    p = dict(
        x=0.0, saut=0.0, h=1.0, rot=0.0,           # bassin : décalage latéral (D), saut (D), hauteur (fraction de jambe), rotation du corps entier (°)
        incl=0.0, sq=1.0,                          # torse : inclinaison (°), écrasement vertical (1 = normal)
        dir=0,                                     # orientation du corps : -1 gauche, 0 face, 1 droite
        pied_g=(-0.15, 0.0), pied_d=(0.15, 0.0),   # pieds (D), y vers le haut
        genou_g=None, genou_d=None,
        bras_g=(10.0, 4.0), bras_d=(10.0, 4.0),    # (épaule, coude) en degrés : 0 = pend, 90 = horizontal vers l'extérieur, 180 = levé
        main_g="rien", main_d="rien",              # rien | doigts | pointe | poing | objet
        objet=None,                                # objet tenu : dict(forme="carte" | "baton", couleur="#rrvvbb", l=0.3, h=0.2) en D
        bras_g_z="ar", bras_d_z="ar",              # devant ou derrière le torse
        tx=0.0, ty=0.0, tincl=0.0, tsq=1.0,        # tête : décalage (D), inclinaison (°), écrasement
        vue=0.0, haut=0.0,                         # visage : -1..1 (trois quarts gauche / droite), regard haut / bas
        yeux="point", paup=0.0, pup=(0.0, 0.0), pupr=1.0, oeil_ech=1.0,    # yeux : point | cercle | ovale | ferme | joie | plisse | croix | clin
        sourcils=(0.0, 0.0, 0.0),                  # (angle gauche, angle droit, hauteur) ; angle > 0 = colère
        bouche="trait", ouv=1.0, bouche_dx=0.0,
        sueur=None, eclats=0.0, rougeur=0.0, souffle=None, tremble=0.0,
        queue=0.0,                                 # pan d'écharpe ou de fichu : angle (mouvement secondaire)
        amb="jour", graine=0,
        lum=60.0,                                  # direction de la lumière à l'écran (°) : 0 = vient de la droite, 90 = du haut
    )
    inconnues = set(kw) - set(p)
    if inconnues:
        raise ValueError(f"pose : paramètres inconnus {sorted(inconnues)}")
    p.update(kw)
    return p


# ---------------------------------------------------------------- visage
def _oeil(kind, cx, cy, p, cote, peau):
    s = []
    e = p["oeil_ech"]
    if kind == "cercle":            # anneau Ø 0,22 à 0,24 D hors tout, trait 0,0235 D, intérieur couleur peau, pupille Ø 0,06 D
        r = 0.12 * D * e
        s.append(f'<circle cx="{f2(cx)}" cy="{f2(cy)}" r="{f2(r - FIN / 2)}" fill="{R.melange(peau, "#ffffff", 0.2)}" stroke="{INK}" stroke-width="{f2(FIN)}"/>')
        px, py = p["pup"]
        pr = 0.0325 * D * p["pupr"]
        lim = r - pr - 0.02 * D
        s.append(f'<circle cx="{f2(cx + px * lim)}" cy="{f2(cy + py * lim)}" r="{f2(pr)}" fill="{INK}"/>')
        if p["paup"] > 0:
            y = cy - r + 2 * r * p["paup"]
            s.append(trait(f"M{f2(cx - r * 1.05)},{f2(y)} L{f2(cx + r * 1.05)},{f2(y)}", w=0.034 * D))
    elif kind == "ovale":           # anneau tassé : UNE image de passage entre « fermé » et « cerclé »
        s.append(f'<g transform="translate({f2(cx)},{f2(cy)}) scale(1,0.5) translate({f2(-cx)},{f2(-cy)})">{_oeil("cercle", cx, cy, p, cote, peau)}</g>')
    elif kind == "point":           # avec paup > 0 : demi-disque sous une paupière droite (l'œil blasé)
        rx, ry = 0.04 * D * e, 0.052 * D * e
        px, py = p["pup"]
        ox, oy = px * 0.03 * D, py * 0.025 * D
        if p["paup"] > 0:
            y = cy - ry + 2 * ry * p["paup"]
            cid = f"cl{cote}{int(cx)}"
            s.append(f'<clipPath id="{cid}"><rect x="{f2(cx - 60)}" y="{f2(y)}" width="120" height="120"/></clipPath>')
            s.append(f'<ellipse cx="{f2(cx + ox)}" cy="{f2(cy + oy)}" rx="{f2(rx)}" ry="{f2(ry)}" fill="{INK}" clip-path="url(#{cid})"/>')
            s.append(trait(f"M{f2(cx - 0.085 * D)},{f2(y)} L{f2(cx + 0.085 * D)},{f2(y)}", w=0.034 * D))
        else:
            s.append(f'<ellipse cx="{f2(cx + ox)}" cy="{f2(cy + oy)}" rx="{f2(rx)}" ry="{f2(ry)}" fill="{INK}"/>')
    elif kind == "ferme":
        s.append(trait(f"M{f2(cx - 0.07 * D)},{f2(cy)} Q{f2(cx)},{f2(cy + 0.035 * D)} {f2(cx + 0.07 * D)},{f2(cy)}", w=0.034 * D))
    elif kind == "joie":
        s.append(trait(f"M{f2(cx - 0.07 * D)},{f2(cy + 0.02 * D)} Q{f2(cx)},{f2(cy - 0.06 * D)} {f2(cx + 0.07 * D)},{f2(cy + 0.02 * D)}", w=0.034 * D))
    elif kind == "plisse":
        k = cote
        s.append(trait(f"M{f2(cx - k * 0.06 * D)},{f2(cy - 0.045 * D)} L{f2(cx + k * 0.05 * D)},{f2(cy)} L{f2(cx - k * 0.06 * D)},{f2(cy + 0.045 * D)}", w=0.032 * D))
    elif kind == "croix":
        a = 0.05 * D
        s.append(trait(f"M{f2(cx - a)},{f2(cy - a)} L{f2(cx + a)},{f2(cy + a)} M{f2(cx + a)},{f2(cy - a)} L{f2(cx - a)},{f2(cy + a)}", w=0.03 * D))
    return "".join(s)

def _bouche(kind, mx, my, p):
    o = p["ouv"]
    u = D
    def q(*c):
        return P(*[(mx + x * u, my + y * u) for x, y in c])
    w = FIN
    if kind == "trait":
        return trait(f"M{q((-0.06, 0))} L{q((0.06, 0))}", w=w)
    if kind == "moue":
        return trait(f"M{q((-0.07, 0.025))} Q{q((0, -0.04))} {q((0.07, 0.025))}", w=w)
    if kind == "bas":
        return trait(f"M{q((-0.11, 0.04))} Q{q((0, -0.07))} {q((0.11, 0.04))}", w=w)
    if kind == "sourire":
        return trait(f"M{q((-0.09, -0.015))} Q{q((0, 0.075))} {q((0.09, -0.015))}", w=w)
    if kind == "coin":
        return trait(f"M{q((-0.08, 0.02))} Q{q((0.02, 0.045))} {q((0.1, -0.035))} M{q((0.085, -0.065))} L{q((0.118, -0.02))}", w=w)
    if kind == "ondule":
        return trait(f"M{q((-0.1, 0))} Q{q((-0.075, -0.035))} {q((-0.05, 0))} T{q((0, 0))} T{q((0.05, 0))} T{q((0.1, 0))}", w=w)
    if kind == "pince":
        return trait(f"M{q((-0.035, 0))} L{q((0.035, 0))} M{q((-0.06, -0.02))} L{q((-0.045, 0.02))} M{q((0.06, -0.02))} L{q((0.045, 0.02))}", w=w * 0.9)
    if kind == "dents":             # rectangle arrondi clair, grille de dents
        hw, hh = 0.125, 0.062 * o
        d = f"M{q((-hw, -hh * 0.8))} Q{q((0, -hh * 1.25))} {q((hw, -hh * 0.8))} Q{q((hw * 1.12, 0))} {q((hw, hh * 0.8))} Q{q((0, hh * 1.25))} {q((-hw, hh * 0.8))} Q{q((-hw * 1.12, 0))} {q((-hw, -hh * 0.8))} Z"
        s = forme(d, BLANC, w=0.024 * D)
        for x in (-0.075, -0.025, 0.025, 0.075):
            s += trait(f"M{q((x, -hh * 0.95))} L{q((x, hh * 0.95))}", w=0.014 * D)
        s += trait(f"M{q((-hw * 1.02, 0))} L{q((hw * 1.02, 0))}", w=0.016 * D)
        return s
    if kind == "o":
        return f'<ellipse cx="{f2(mx)}" cy="{f2(my + 0.01 * u)}" rx="{f2(0.036 * u)}" ry="{f2(0.046 * u * o)}" fill="{BOUCHE_IN}" stroke="{INK}" stroke-width="{f2(0.024 * D)}"/>'
    if kind in ("grand_o", "ouverte", "rire"):      # bouche ouverte : fond sombre, bande claire en haut (dents), langue en bas
        cid = f"bm{int(mx)}{int(my)}"
        if kind == "grand_o":
            rx, ry = 0.075, 0.105 * o
            d = f"M{q((-rx, 0.03))} Q{q((-rx, -ry + 0.03))} {q((0, -ry + 0.03))} Q{q((rx, -ry + 0.03))} {q((rx, 0.03))} Q{q((rx, ry + 0.03))} {q((0, ry + 0.03))} Q{q((-rx, ry + 0.03))} {q((-rx, 0.03))} Z"
            ty, top = ry * 0.75 + 0.03, -ry + 0.03
        elif kind == "ouverte":
            hw, hh = 0.105, 0.17 * o
            d = f"M{q((-hw, -0.02))} Q{q((0, -0.045))} {q((hw, -0.02))} Q{q((hw * 1.05, hh))} {q((0, hh))} Q{q((-hw * 1.05, hh))} {q((-hw, -0.02))} Z"
            ty, top = hh * 0.82, -0.03
        else:
            hw, hh = 0.13, 0.15 * o
            d = f"M{q((-hw, -0.04))} Q{q((0, 0.0))} {q((hw, -0.04))} Q{q((hw * 0.9, hh))} {q((0, hh))} Q{q((-hw * 0.9, hh))} {q((-hw, -0.04))} Z"
            ty, top = hh * 0.85, -0.03
        s = f'<clipPath id="{cid}"><path d="{d}"/></clipPath>'
        s += f'<path d="{d}" fill="{BOUCHE_IN}"/>'
        s += f'<ellipse cx="{f2(mx)}" cy="{f2(my + (ty + 0.03) * u)}" rx="{f2(0.07 * u)}" ry="{f2(0.05 * u)}" fill="{LANGUE}" clip-path="url(#{cid})"/>'
        if kind != "grand_o":
            s += f'<rect x="{f2(mx - 0.14 * u)}" y="{f2(my + (top - 0.02) * u)}" width="{f2(0.28 * u)}" height="{f2(0.05 * u)}" fill="{BLANC}" clip-path="url(#{cid})"/>'
        s += forme(d, "none", w=0.026 * D)
        return s
    return ""

def _pilosite(c, mx, my):
    k = c["pilosite"]
    col = c["poil"] or INK
    u = D
    def q(*pts):
        return P(*[(mx + x * u, my + y * u) for x, y in pts])
    if k == "moustache":        # petite moustache en brosse, au-dessus de la bouche
        return forme(f"M{q((-0.1, -0.085))} Q{q((0, -0.115))} {q((0.1, -0.085))} L{q((0.085, -0.04))} Q{q((0, -0.06))} {q((-0.085, -0.04))} Z", col, w=0.02 * D)
    if k == "barbiche":         # touffe au menton
        return forme(f"M{q((-0.04, 0.085))} L{q((0.04, 0.085))} L{q((0, 0.2))} Z", col, w=0.02 * D)
    if k == "chaume":           # barbe de trois jours : points
        s = ""
        for x, y in ((-0.1, 0.06), (-0.05, 0.1), (0.0, 0.115), (0.05, 0.1), (0.1, 0.06), (-0.075, 0.02), (0.075, 0.02)):
            s += f'<circle cx="{f2(mx + x * u)}" cy="{f2(my + y * u)}" r="{f2(0.011 * u)}" fill="{col}"/>'
        return s
    if k == "barbe":            # collier de barbe en tirets
        return trait(f"M{q((-0.16, -0.02))} Q{q((-0.15, 0.17))} {q((0, 0.185))} Q{q((0.15, 0.17))} {q((0.16, -0.02))}", col, 0.05 * D, 'stroke-dasharray="3 13"')
    return ""

def _coiffe(c, p, r, avant):
    """Coiffe en coordonnées de tête (centre 0,0 ; rayon r). Trois tons francs : clair, moyen (côté ombre), bandeau. Contour régulier de 0,032 D.
    avant=False : partie dessinée derrière la tête (pans du fichu)."""
    co = c["coiffe"]
    if not co:
        return ""
    k = co["type"]
    t = list(co.get("tons") or ())
    clair = t[0] if len(t) > 0 else "#d9b25e"
    moyen = t[1] if len(t) > 1 else R.melange(clair, "#3a1830", 0.28)
    bande = t[2] if len(t) > 2 else R.melange(clair, "#ffffff", 0.55)
    chev = c["cheveux"] or INK
    v = p["vue"]
    dx = v * 0.1 * r
    s = ""
    cheveux = f"M{f2(-0.80 * r)},{f2(-0.60 * r)} A{f2(r)},{f2(r)} 0 0 1 {f2(0.80 * r)},{f2(-0.60 * r)} Q{f2(dx)},{f2(-0.86 * r)} {f2(-0.80 * r)},{f2(-0.60 * r)} Z"
    if k == "fichu" and not avant:      # deux pans noués, derrière la tête, qui suivent le mouvement (queue)
        cote = -1 if v > 0.2 else 1
        nx, ny = cote * 0.93 * r, -0.42 * r
        for ln, da in ((0.62, -18), (0.5, 16)):
            a = math.radians(p["queue"] + da + (90 - 70 * cote))
            ex, ey = nx + math.cos(a) * ln * r, ny + math.sin(a) * ln * r
            mx_, my_ = nx + math.cos(a) * ln * r * 0.5 + math.sin(a) * 0.1 * r, ny + math.sin(a) * ln * r * 0.5 - math.cos(a) * 0.1 * r
            d = f"M{f2(nx)},{f2(ny)} Q{f2(mx_)},{f2(my_)} {f2(ex)},{f2(ey)}"
            s += trait(d, INK, 0.2 * r) + trait(d, moyen, 0.2 * r - 2 * CWF)
        return s
    if not avant:
        return ""
    if k in ("cheveux", "chignon"):
        s += forme(cheveux, chev, w=SW * 0.6)
        if k == "chignon":
            s += f'<circle cx="{f2(dx)}" cy="{f2(-1.12 * r)}" r="{f2(0.26 * r)}" fill="{chev}" stroke="{INK}" stroke-width="{f2(CWF)}"/>'
        return s
    if k == "bonnet":           # dôme, revers, pompon
        d = (f"M{f2(-1.04 * r)},{f2(-0.26 * r)} Q{f2(-1.06 * r)},{f2(-1.2 * r)} {f2(dx)},{f2(-1.22 * r)} Q{f2(1.06 * r)},{f2(-1.2 * r)} {f2(1.04 * r)},{f2(-0.26 * r)} "
             f"Q{f2(dx)},{f2(-0.56 * r)} {f2(-1.04 * r)},{f2(-0.26 * r)} Z")
        s += f'<circle cx="{f2(dx)}" cy="{f2(-1.3 * r)}" r="{f2(0.17 * r)}" fill="{bande}" stroke="{INK}" stroke-width="{f2(CWF)}"/>'
        s += tons(d, clair, moyen, "cf1")
        rev = f"M{f2(-1.0 * r)},{f2(-0.34 * r)} Q{f2(dx)},{f2(-0.64 * r)} {f2(1.0 * r)},{f2(-0.34 * r)}"
        s += f'<g clip-path="url(#cf1)">{trait(rev, INK, 0.3 * r, BT)}{trait(rev, bande, 0.3 * r - 2 * CWF * 0.7, BT)}</g>'
        return s
    if k == "casquette":        # calotte plate, bandeau, visière courte tournée du côté du regard
        d = (f"M{f2(-0.98 * r)},{f2(-0.40 * r)} Q{f2(-1.02 * r)},{f2(-1.12 * r)} {f2(dx)},{f2(-1.14 * r)} Q{f2(1.02 * r)},{f2(-1.12 * r)} {f2(0.98 * r)},{f2(-0.40 * r)} "
             f"Q{f2(dx)},{f2(-0.66 * r)} {f2(-0.98 * r)},{f2(-0.40 * r)} Z")
        s += forme(cheveux, chev, w=SW * 0.6)
        s += tons(d, clair, moyen, "cf1")
        ban = f"M{f2(-0.96 * r)},{f2(-0.46 * r)} Q{f2(dx)},{f2(-0.72 * r)} {f2(0.96 * r)},{f2(-0.46 * r)}"
        s += f'<g clip-path="url(#cf1)">{trait(ban, bande, 0.16 * r, BT)}</g>'
        vx = dx + v * 0.35 * r
        vis = f"M{f2(vx - 0.62 * r)},{f2(-0.46 * r)} Q{f2(vx)},{f2(-0.70 * r)} {f2(vx + 0.62 * r)},{f2(-0.46 * r)} Q{f2(vx)},{f2(-0.30 * r)} {f2(vx - 0.62 * r)},{f2(-0.46 * r)} Z"
        s += f'<path d="{vis}" fill="{moyen}" stroke="{INK}" stroke-width="{f2(CWF)}" stroke-linejoin="round"/>'
        return s
    if k == "beret":            # galette décalée d'un côté, petite tige
        bx = dx + 0.16 * r
        d = (f"M{f2(bx - 1.02 * r)},{f2(-0.74 * r)} Q{f2(bx - 0.96 * r)},{f2(-1.24 * r)} {f2(bx)},{f2(-1.26 * r)} Q{f2(bx + 1.14 * r)},{f2(-1.24 * r)} {f2(bx + 1.1 * r)},{f2(-0.86 * r)} "
             f"Q{f2(bx + 0.4 * r)},{f2(-0.62 * r)} {f2(bx - 1.02 * r)},{f2(-0.74 * r)} Z")
        s += forme(cheveux, chev, w=SW * 0.6)
        s += trait(f"M{f2(bx)},{f2(-1.26 * r)} L{f2(bx + 0.05 * r)},{f2(-1.42 * r)}", INK, 0.09 * r)
        s += tons(d, clair, moyen, "cf1")
        ban = f"M{f2(bx - 0.98 * r)},{f2(-0.76 * r)} Q{f2(bx + 0.4 * r)},{f2(-0.66 * r)} {f2(bx + 1.06 * r)},{f2(-0.88 * r)}"
        s += f'<g clip-path="url(#cf1)">{trait(ban, bande, 0.12 * r, BT)}</g>'
        return s
    if k == "fichu":            # foulard noué sur la tête, nœud sur le côté
        cote = -1 if v > 0.2 else 1
        d = (f"M{f2(-1.05 * r)},{f2(-0.30 * r)} Q{f2(-1.0 * r)},{f2(-1.14 * r)} {f2(dx)},{f2(-1.14 * r)} Q{f2(1.0 * r)},{f2(-1.14 * r)} {f2(1.05 * r)},{f2(-0.30 * r)} "
             f"Q{f2(dx)},{f2(-0.74 * r)} {f2(-1.05 * r)},{f2(-0.30 * r)} Z")
        s += tons(d, clair, moyen, "cf1")
        ban = f"M{f2(-1.0 * r)},{f2(-0.40 * r)} Q{f2(dx)},{f2(-0.80 * r)} {f2(1.0 * r)},{f2(-0.40 * r)}"
        s += f'<g clip-path="url(#cf1)">{trait(ban, bande, 0.1 * r, BT)}</g>'
        s += f'<circle cx="{f2(cote * 0.93 * r)}" cy="{f2(-0.42 * r)}" r="{f2(0.13 * r)}" fill="{moyen}" stroke="{INK}" stroke-width="{f2(CWF)}"/>'
        return s
    if k == "cloche":           # chapeau à calotte ronde et petit bord tombant
        d = (f"M{f2(-0.86 * r)},{f2(-0.50 * r)} Q{f2(-0.9 * r)},{f2(-1.3 * r)} {f2(dx)},{f2(-1.32 * r)} Q{f2(0.9 * r)},{f2(-1.3 * r)} {f2(0.86 * r)},{f2(-0.50 * r)} Z")
        bord = (f"M{f2(-1.22 * r)},{f2(-0.40 * r)} Q{f2(dx)},{f2(-0.78 * r)} {f2(1.22 * r)},{f2(-0.40 * r)} Q{f2(dx)},{f2(-0.50 * r)} {f2(-1.22 * r)},{f2(-0.40 * r)} Z")
        s += tons(d, clair, moyen, "cf1")
        ban = f"M{f2(-0.88 * r)},{f2(-0.60 * r)} Q{f2(dx)},{f2(-0.84 * r)} {f2(0.88 * r)},{f2(-0.60 * r)}"
        s += f'<g clip-path="url(#cf1)">{trait(ban, bande, 0.14 * r, BT)}</g>'
        s += tons(bord, clair, moyen, "cf2", decal=0.05 * D)
        return s
    return ""

def _goutte(x, y, ech=1.0):
    """Goutte de sueur collée à la tempe : 0,12 × 0,14 D, elle apparaît d'un coup et ne coule pas."""
    h, w = 0.115 * D * ech, 0.062 * D * ech
    return (f'<path d="M{f2(x)},{f2(y - h)} Q{f2(x + w * 1.25)},{f2(y + h * 0.35)} {f2(x)},{f2(y + h * 0.55)} Q{f2(x - w * 1.25)},{f2(y + h * 0.35)} {f2(x)},{f2(y - h)} Z" '
            f'fill="{SUEUR}" stroke="{INK}" stroke-width="{f2(0.018 * D)}" stroke-linejoin="round"/>'
            f'<path d="M{f2(x - w * 0.3)},{f2(y)} Q{f2(x - w * 0.5)},{f2(y + h * 0.25)} {f2(x - w * 0.15)},{f2(y + h * 0.38)}" fill="none" stroke="#ffffff" stroke-width="{f2(0.012 * D)}" stroke-linecap="round" opacity="0.9"/>')

def _patate(cx, cy, rad, c):
    """Tête tracée « à la main » : rapport petit axe / grand axe ≈ 0,96, plus une 3e harmonique de 0,8 %.
    La forme est fixe pour un personnage, jamais recalculée d'une image à l'autre."""
    g = c["cle"]
    ph2, ph3 = (g % 180) * math.pi / 90, (g * 7 % 360) * math.pi / 180
    pts = []
    for i in range(144):
        t = 2 * math.pi * i / 144
        r = rad * (1 + R.TETE["ovale"] * math.cos(2 * t - ph2) + 0.008 * math.cos(3 * t - ph3))
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return "M" + " L".join(f"{f2(x)},{f2(y)}" for x, y in pts) + " Z"

def _tete(c, p):
    """Tête complète en coordonnées locales (centre 0,0)."""
    r = D / 2
    amb = R.AMBIANCES[p["amb"]]
    v, hh = p["vue"], p["haut"]
    s = _coiffe(c, p, r, False)
    # disque d'encre (bord extérieur = D), disque de peau plus petit de A0 et décalé de H1 vers la lumière
    lx, ly = _LUM
    ox, oy = lx * H1 * D, ly * H1 * D
    rs = r - A0 * D
    peau_d = _patate(ox, oy, rs, c)
    s += f'<clipPath id="tclip"><path d="{peau_d}"/></clipPath>'
    s += f'<path d="{_patate(0, 0, r, c)}" fill="{INK}"/>'
    s += f'<path d="{peau_d}" fill="{amb["croissant"]}"/>'
    # croissant d'ombre à bord doux du côté opposé à la lumière ; la peau claire porte un léger dégradé le long de l'axe de la lumière
    gx0, gy0, gx1, gy1 = ox - lx * rs, oy - ly * rs, ox + lx * 0.2 * rs, oy + ly * 0.2 * rs
    s += (f'<linearGradient id="gpeau" gradientUnits="userSpaceOnUse" x1="{f2(gx0)}" y1="{f2(gy0)}" x2="{f2(gx1)}" y2="{f2(gy1)}">'
          f'<stop offset="0" stop-color="{R.melange(amb["peau"], amb["croissant"], R.TETE["degrade"])}"/><stop offset="1" stop-color="{amb["peau"]}"/></linearGradient>')
    s += (f'<filter id="fdoux" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="{f2(R.TETE["croissant_flou"] * D)}"/></filter>'
          f'<g clip-path="url(#tclip)"><circle cx="{f2(ox + lx * R.TETE["croissant"] * rs)}" cy="{f2(oy + ly * R.TETE["croissant"] * rs)}" r="{f2(rs * 1.01)}" '
          f'fill="url(#gpeau)" filter="url(#fdoux)"/>')
    # filet de lumière : croissant fin côté éclairé, effilé aux deux bouts, sur un cercle plus petit que la tête
    al = math.atan2(ly, lx)
    ra, da, bout = 0.525 * rs, 0.40 * rs, math.radians(66)
    acx, acy = ox + lx * da, oy + ly * da
    ext, inte = [], []
    for i in range(41):
        t = -bout + 2 * bout * i / 40
        w = 0.5 * R.TETE["filet"] * D * max(0.0, math.cos(math.pi / 2 * t / bout)) ** 0.6
        ext.append((acx + (ra + w) * math.cos(al + t), acy + (ra + w) * math.sin(al + t)))
        inte.append((acx + (ra - w) * math.cos(al + t), acy + (ra - w) * math.sin(al + t)))
    s += f'<path d="M{P(*ext)} L{P(*reversed(inte))} Z" fill="{amb["filet"]}" opacity="{amb["filet_op"]}"/></g>'
    # traits du visage : glissent sur la boule selon la vue (trois quarts) et le regard
    fx, fy = v * 0.23 * D, -0.03 * D + hh * 0.07 * D
    ecart = 0.132 * D
    comp_g = 1 - 0.3 * max(0.0, -v)
    comp_d = 1 - 0.3 * max(0.0, v)
    exg, exd = fx - ecart * (1 - 0.25 * max(0.0, -v)), fx + ecart * (1 - 0.25 * max(0.0, v))
    yeux = p["yeux"]
    kg, kd = (yeux, yeux) if yeux != "clin" else ("point", "ferme")
    if p["rougeur"] > 0:
        for x in (exg - 0.07 * D, exd + 0.07 * D):
            s += f'<ellipse cx="{f2(x)}" cy="{f2(fy + 0.15 * D)}" rx="{f2(0.07 * D)}" ry="{f2(0.04 * D)}" fill="{amb["joue"]}" opacity="{0.75 * p["rougeur"]:.2f}"/>'
    s += f'<g transform="translate({f2(exg)},{f2(fy)}) scale({comp_g:.3f},1) translate({f2(-exg)},{f2(-fy)})">{_oeil(kg, exg, fy, p, -1, amb["peau"])}</g>'
    s += f'<g transform="translate({f2(exd)},{f2(fy)}) scale({comp_d:.3f},1) translate({f2(-exd)},{f2(-fy)})">{_oeil(kd, exd, fy, p, 1, amb["peau"])}</g>'
    # sourcils : formes pleines de 0,16 D de long et 0,05 D d'épaisseur ; angle > 0 = colère
    ag, ad, sh = p["sourcils"]
    sc = c["sourcil"] or INK
    by = fy - (0.2 + 0.05 * (1 if yeux == "cercle" else 0)) * D - sh * 0.1 * D
    lw = 0.075 * D
    for x, a, k in ((exg, ag, -1), (exd, ad, 1)):
        ang = math.radians(a) * k
        p0 = rot(-lw, 0.012 * D, ang); p1 = rot(0, -0.03 * D, ang); p2 = rot(lw, 0.012 * D, ang)
        d = f"M{f2(x + p0[0])},{f2(by + p0[1])} Q{f2(x + p1[0])},{f2(by + p1[1])} {f2(x + p2[0])},{f2(by + p2[1])}"
        if sc != INK:
            s += trait(d, INK, 0.07 * D)
        s += trait(d, sc, 0.05 * D)
    s += _coiffe(c, p, r, True)             # la coiffe passe DEVANT les sourcils et le haut des yeux
    mx, my = fx * 0.92 + p["bouche_dx"] * D, 0.235 * D + hh * 0.05 * D
    s += _bouche(p["bouche"], mx, my, p)
    s += _pilosite(c, mx, my)
    # signes : sueur, traits de surprise, souffle
    if p["sueur"] is not None:
        ts = p["sueur"] if isinstance(p["sueur"], (tuple, list)) else (p["sueur"],)
        for i, t in enumerate(ts):
            cote = 1 if i % 2 == 0 else -1
            if v * cote > 0.3:
                cote = -cote
            if t and t > 0:
                s += _goutte(cote * (0.37 + 0.01 * i) * D, (-0.06 + 0.16 * i) * D, (1.0 - 0.2 * i) * min(1.0, t))      # collée à la TEMPE, sous la coiffe
    if p["eclats"] > 0:
        e = p["eclats"]
        for a in (-62, -90, -118):
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            r0, r1 = (0.62 + 0.1 * e) * D, (0.62 + 0.1 * e + 0.13 * e) * D
            if c["coiffe"] and c["coiffe"]["type"] not in ("cheveux",):
                r0, r1 = r0 + 0.2 * D, r1 + 0.2 * D
            s += trait(f"M{f2(ca * r0 - v * 20)},{f2(sa * r0 * 1.25)} L{f2(ca * r1 - v * 20)},{f2(sa * r1 * 1.25)}", INK, 0.03 * D, f'opacity="{min(1.0, e * 1.5):.2f}"')
    if p["souffle"] is not None and 0 < p["souffle"] < 1:
        t = p["souffle"]
        sx = mx + (0.14 + 0.2 * t) * D * (1 if v >= 0 else -1)
        s += f'<ellipse cx="{f2(sx)}" cy="{f2(my + 0.03 * D)}" rx="{f2((0.05 + 0.06 * t) * D)}" ry="{f2((0.035 + 0.04 * t) * D)}" fill="#ffffff" stroke="{INK}" stroke-width="{f2(0.016 * D)}" opacity="{(1 - t) * 0.9:.2f}"/>'
    return s


# ---------------------------------------------------------------- torse et costume
def _torse_path(c):
    tw = c["torse_l"] * D
    th = c["torse_h"] * D
    if c["torse"] == "cloche":      # épaules étroites et rondes, ourlet large (manteau long, robe)
        t, b = tw * 0.46, tw * 0.62
        return (f"M{f2(-b)},{f2(-0.06 * D)} Q{f2(-b)},0 {f2(-b + 0.07 * D)},0 L{f2(b - 0.07 * D)},0 Q{f2(b)},0 {f2(b)},{f2(-0.06 * D)} "
                f"L{f2(t)},{f2(-th + 0.3 * D)} Q{f2(t)},{f2(-th)} 0,{f2(-th)} Q{f2(-t)},{f2(-th)} {f2(-t)},{f2(-th + 0.3 * D)} Z"), tw, th
    w = tw / 2                      # gélule : 0,72 × 1,0 D
    return (f"M{f2(-w)},{f2(-0.3 * D)} Q{f2(-w)},0 0,0 Q{f2(w)},0 {f2(w)},{f2(-0.3 * D)} L{f2(w * 0.94)},{f2(-th + 0.34 * D)} "
            f"Q{f2(w * 0.94)},{f2(-th)} 0,{f2(-th)} Q{f2(-w * 0.94)},{f2(-th)} {f2(-w * 0.94)},{f2(-th + 0.34 * D)} Z"), tw, th

def _torse(c, p, uid):
    d, tw, th = _torse_path(c)
    amb = R.AMBIANCES[p["amb"]]
    lx, ly = _LUM
    cote = 1 if lx >= 0 else -1                    # côté d'où vient la lumière
    bt = BT
    # contour à pleins et déliés : silhouette d'encre, puis tout l'intérieur décalé de H1 vers la lumière
    s = f'<path d="{d}" fill="{INK}" stroke="{INK}" stroke-width="{f2(2 * A0 * D)}" stroke-linejoin="round"/>'
    s += f'<g transform="translate({f2(lx * H1 * D)},{f2(ly * H1 * D)})">'
    s += f'<clipPath id="tr{uid}"><path d="{d}"/></clipPath>'
    s += f'<path d="{d}" fill="{c["couleur"]}"/>'
    g = f'<g clip-path="url(#tr{uid})">'
    # ombre propre : bande plus sombre le long du bord éclairé (16 à 21 % de la surface), bord doux
    g += (f'<filter id="ft{uid}" x="-30%" y="-10%" width="160%" height="120%"><feGaussianBlur stdDeviation="{f2(0.02 * D)}"/></filter>'
          f'<rect x="{f2(cote * 0.2 * tw if cote > 0 else -tw)}" y="{f2(-th * 1.1)}" width="{f2(0.8 * tw)}" height="{f2(th * 1.2)}" fill="{c["couleur2"]}" filter="url(#ft{uid})"/>')
    # filet de lumière : bande de 0,022 D à 0,034 D du bord, du côté éclairé seulement
    filet = amb["filet_torse"] or R.melange(c["couleur"], "#ffe9c8", 0.55)
    g += (f'<clipPath id="tf{uid}"><rect x="{f2(0.12 * tw if cote > 0 else -tw)}" y="{f2(-th * 0.93)}" width="{f2(0.88 * tw)}" height="{f2(th * 0.8)}"/></clipPath>'
          f'<g clip-path="url(#tf{uid})"><path d="{d}" fill="none" stroke="{filet}" stroke-width="{f2(2 * (R.TORSE["filet"] + R.TORSE["filet_retrait"]) * D)}"/>'
          f'<path d="{d}" fill="none" stroke="{c["couleur2"]}" stroke-width="{f2(2 * R.TORSE["filet_retrait"] * D)}"/></g>')
    # détails du costume (tous facultatifs)
    if c["accessoire"] == "tablier":
        ac = c["accessoire_couleur"]
        g += f'<rect x="{f2(-tw * 0.3)}" y="{f2(-th * 0.62)}" width="{f2(tw * 0.6)}" height="{f2(th * 0.7)}" fill="{ac}" stroke="{INK}" stroke-width="{f2(0.016 * D)}"/>'
        g += trait(f"M{f2(-tw * 0.26)},{f2(-th * 0.62)} L{f2(-tw * 0.12)},{f2(-th * 1.0)} M{f2(tw * 0.26)},{f2(-th * 0.62)} L{f2(tw * 0.12)},{f2(-th * 1.0)}", ac, 0.05 * D)
    if c["col"] == "v":
        g += trait(f"M{f2(-tw * 0.26)},{f2(-th * 1.0)} L0,{f2(-th * 0.72)} L{f2(tw * 0.26)},{f2(-th * 1.0)}", INK, 0.085 * D)
        g += trait(f"M{f2(-tw * 0.26)},{f2(-th * 1.0)} L0,{f2(-th * 0.72)} L{f2(tw * 0.26)},{f2(-th * 1.0)}", c["garniture"], 0.05 * D)
    elif c["col"] == "rond":
        g += trait(f"M{f2(-tw * 0.3)},{f2(-th * 0.97)} Q0,{f2(-th * 0.74)} {f2(tw * 0.3)},{f2(-th * 0.97)}", INK, 0.085 * D)
        g += trait(f"M{f2(-tw * 0.3)},{f2(-th * 0.97)} Q0,{f2(-th * 0.74)} {f2(tw * 0.3)},{f2(-th * 0.97)}", c["garniture"], 0.05 * D)
    for i in range(int(c["boutons"])):
        g += f'<circle cx="0" cy="{f2(-th * (0.62 - 0.15 * i))}" r="{f2(0.028 * D)}" fill="{c["garniture"]}" stroke="{INK}" stroke-width="{f2(0.012 * D)}"/>'
    if c["ceinture"]:
        sy = -th * (0.42 if c["torse"] == "cloche" else 0.3)
        g += trait(f"M{f2(-tw)},{f2(sy)} L{f2(tw)},{f2(sy)}", INK, 0.13 * D, bt)
        g += trait(f"M{f2(-tw)},{f2(sy)} L{f2(tw)},{f2(sy)}", c["ceinture"], 0.09 * D, bt)
    if c["bande_bas"]:
        g += trait(f"M{f2(-tw)},{f2(-0.11 * D)} L{f2(tw)},{f2(-0.11 * D)}", c["garniture"], 0.06 * D, bt)
    if c["accessoire"] == "sacoche":        # bandoulière
        g += trait(f"M{f2(-tw * 0.5)},{f2(-th * 0.98)} L{f2(tw * 0.55)},{f2(-th * 0.25)}", INK, 0.09 * D)
        g += trait(f"M{f2(-tw * 0.5)},{f2(-th * 0.98)} L{f2(tw * 0.55)},{f2(-th * 0.25)}", R.melange(c["accessoire_couleur"], "#20101a", 0.35), 0.05 * D)
    g += "</g>"
    s += g + "</g>"
    if c["accessoire"] == "sacoche":
        sac = f"M{f2(tw * 0.34)},{f2(-th * 0.3)} L{f2(tw * 0.78)},{f2(-th * 0.3)} L{f2(tw * 0.74)},{f2(-th * 0.02)} L{f2(tw * 0.38)},{f2(-th * 0.02)} Z"
        s += tons(sac, c["accessoire_couleur"], R.melange(c["accessoire_couleur"], "#2a0a24", 0.3), f"sa{uid}", decal=0.05 * D)
    if c["accessoire"] == "echarpe":        # tour de cou et un pan qui pend, du côté opposé au regard ; le pan suit le mouvement (queue)
        ac = c["accessoire_couleur"]
        k = -1 if p["dir"] > 0 or p["vue"] > 0.2 else 1
        a = math.radians(p["queue"])
        x0, y0 = k * tw * 0.22, -th * 0.9
        x1, y1 = x0 + math.sin(a) * 0.42 * D + k * 0.03 * D, y0 + math.cos(a) * 0.42 * D
        pan = f"M{f2(x0)},{f2(y0)} L{f2(x1)},{f2(y1)}"
        s += trait(pan, INK, 0.15 * D, bt) + trait(pan, R.melange(ac, "#2a0a24", 0.25), 0.15 * D - 2 * CWF, bt)
        tour = f"M{f2(-tw * 0.4)},{f2(-th * 0.9)} Q0,{f2(-th * 0.8)} {f2(tw * 0.4)},{f2(-th * 0.9)}"
        s += trait(tour, INK, 0.17 * D) + trait(tour, ac, 0.17 * D - 2 * CWF)
    return s, tw, th

def _main(kind, hx, hy, dx, dy, p):
    """Main au bout du trait : rien (bout rond), doigts écartés, index pointé, poing, ou objet tenu."""
    n = math.hypot(dx, dy) or 1.0
    ux, uy = dx / n, dy / n
    s = ""
    if kind == "doigts":
        for a in (-52, -18, 18, 52):
            vx, vy = rot(ux, uy, math.radians(a))
            s += trait(f"M{f2(hx)},{f2(hy)} L{f2(hx + vx * 0.105 * D)},{f2(hy + vy * 0.105 * D)}", MEMBRE, LW * 0.62)
    elif kind == "pointe":
        s += f'<circle cx="{f2(hx)}" cy="{f2(hy)}" r="{f2(0.05 * D)}" fill="{MEMBRE}"/>'
        s += trait(f"M{f2(hx)},{f2(hy)} L{f2(hx + ux * 0.16 * D)},{f2(hy + uy * 0.16 * D)}", MEMBRE, LW * 0.66)
    elif kind == "poing":
        s += f'<circle cx="{f2(hx)}" cy="{f2(hy)}" r="{f2(0.055 * D)}" fill="{MEMBRE}"/>'
    elif kind == "objet":
        o = dict(forme="carte", couleur="#fff4dc", l=0.34, h=0.24)
        o.update(p.get("objet") or {})
        px, py = -uy, ux
        if o["forme"] == "baton":
            a = (hx - ux * 0.1 * D, hy - uy * 0.1 * D); b = (hx + ux * o["l"] * D, hy + uy * o["l"] * D)
            s += trait(f"M{P(a)} L{P(b)}", INK, 0.1 * D) + trait(f"M{P(a)} L{P(b)}", o["couleur"], 0.1 * D - 2 * CWF)
        else:                       # carte, lettre, feuille : rectangle tenu par un coin
            l, h = o["l"] * D, o["h"] * D
            cx, cy = hx + ux * h * 0.45, hy + uy * h * 0.45
            coins = [(cx - px * l / 2 - ux * h / 2, cy - py * l / 2 - uy * h / 2), (cx + px * l / 2 - ux * h / 2, cy + py * l / 2 - uy * h / 2),
                     (cx + px * l / 2 + ux * h / 2, cy + py * l / 2 + uy * h / 2), (cx - px * l / 2 + ux * h / 2, cy - py * l / 2 + uy * h / 2)]
            d = f"M{P(*coins)} Z"
            s += f'<path d="{d}" fill="{o["couleur"]}" stroke="{INK}" stroke-width="{f2(CWF)}" stroke-linejoin="round"/>'
            s += trait(f"M{P(coins[0])} L{f2(cx)},{f2(cy)} L{P(coins[1])}", INK, 0.014 * D, 'opacity="0.7"')
        s += f'<circle cx="{f2(hx)}" cy="{f2(hy)}" r="{f2(0.05 * D)}" fill="{MEMBRE}"/>'
    return s

def _bras(p, cote, ep):
    a1, a2 = p["bras_g"] if cote < 0 else p["bras_d"]
    t1, t2 = math.radians(a1), math.radians(a1 + a2)
    ua, fa = 0.43 * D, 0.42 * D
    co = (ep[0] + cote * math.sin(t1) * ua, ep[1] + math.cos(t1) * ua)
    ma = (co[0] + cote * math.sin(t2) * fa, co[1] + math.cos(t2) * fa)
    s = trait(membre(ep, co, ma), MEMBRE, LW)
    kind = p["main_g"] if cote < 0 else p["main_d"]
    return s + _main(kind, ma[0], ma[1], ma[0] - co[0], ma[1] - co[1], p)


# ---------------------------------------------------------------- assemblage
def svg_perso(nom, p):
    c = PERSOS[nom]
    al = math.radians(p.get("lum", 60.0))
    _LUM[0], _LUM[1] = math.cos(al), -math.sin(al)
    leg = c["jambes"] * D
    rnd = random.Random(int(p["graine"]))
    tr = p["tremble"]
    jx = (rnd.uniform(-1, 1) * tr * 0.02 * D) if tr else 0.0
    jy = (rnd.uniform(-1, 1) * tr * 0.012 * D) if tr else 0.0
    root = (p["x"] * D + jx, -(p["h"] * leg) - p["saut"] * D)
    a = math.radians(p["incl"])
    sq = p["sq"]
    d_t, tw, th = _torse_path(c)
    ux, uy = math.sin(a), -math.cos(a)
    top = (root[0] + ux * th * sq, root[1] + uy * th * sq)
    dr = p["dir"]
    jambes_av, jambes_ar = "", ""
    for cote, cle in ((-1, "pied_g"), (1, "pied_d")):
        hx, hy = rot(cote * 0.13 * D, -0.05 * D, a)
        hanche = (root[0] + hx, root[1] + hy)
        fx, fy = p[cle]
        pied = (fx * D, -fy * D - p["saut"] * D)
        g = p["genou_g"] if cote < 0 else p["genou_d"]
        if g is None:
            g = dr if dr else cote * 0.6
        genou = ik(hanche, pied, leg / 2, leg / 2, -g)
        loin = dr != 0 and cote == -dr          # de profil ou de trois quarts : la jambe du second plan est éclaircie vers la teinte du décor
        coul = JAMBE_AR if loin else MEMBRE
        j = trait(membre(hanche, genou, pied), coul, LW)
        pdir = dr if dr else cote
        lever = max(0.0, min(1.0, fy / 0.25))                  # pied levé : la pointe tombe
        ang = math.radians(35 * lever)
        px, py = rot(pdir * 0.17 * D, 0, ang * pdir)
        if dr == 0:
            px *= 0.75
        j += trait(f"M{P(pied)} L{f2(pied[0] + px)},{f2(pied[1] + py)}", coul, LW)      # pied : trait de 0,18 D posé à plat
        if loin:
            jambes_ar += j
        else:
            jambes_av += j
    eps = {}
    for cote in (-1, 1):
        ex, ey = rot(cote * tw * 0.44, -(th * sq - 0.21 * D), a)
        eps[cote] = (root[0] + ex, root[1] + ey)
    zb = {k: (p["bras_g_z"] if k < 0 else p["bras_d_z"]) for k in (-1, 1)}
    bras_ar = "".join(_bras(p, k, eps[k]) for k in (-1, 1) if zb[k] == "ar")
    bras_av = "".join(_bras(p, k, eps[k]) for k in (-1, 1) if zb[k] == "av")
    # la lumière est donnée À L'ÉCRAN : dans un groupe tourné (torse penché, tête inclinée, corps qui bascule), on la contre-tourne,
    # sinon le plein et le croissant d'ombre tournent avec le personnage
    lum0 = tuple(_LUM)
    def _lumiere_locale(angle_deg):
        _LUM[0], _LUM[1] = rot(lum0[0], lum0[1], -math.radians(angle_deg))
    _lumiere_locale(p["incl"] + p["rot"])
    torse, _, _ = _torse(c, p, "a")
    sx = 1 / math.sqrt(sq)
    tg = f'<g transform="translate({f2(root[0])},{f2(root[1])}) rotate({p["incl"]:.2f}) scale({sx:.3f},{sq:.3f})">{torse}</g>'
    # tête : posée sur le haut du torse (elle le recouvre un peu : pas de cou), pivot au cou
    ta = p["incl"] * 0.6 + p["tincl"]
    r = D / 2
    cx, cy = p["tx"] * D + jx * 0.6, -(r - 0.05 * D) + p["ty"] * -D + jy
    tsq = p["tsq"]
    _lumiere_locale(ta + p["rot"])
    hg = (f'<g transform="translate({f2(top[0])},{f2(top[1])}) rotate({ta:.2f}) translate({f2(cx)},{f2(cy)}) '
          f'translate(0,{f2(r)}) scale({1 / math.sqrt(tsq):.3f},{tsq:.3f}) translate(0,{f2(-r)})">{_tete(c, p)}</g>')
    _LUM[0], _LUM[1] = lum0
    corps = jambes_ar + bras_ar + jambes_av + tg + bras_av + hg
    if p["rot"]:
        corps = f'<g transform="rotate({p["rot"]:.2f} 0 {f2(-leg * 0.9)})">{corps}</g>'
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">'
           f'<g transform="translate({AX},{AY})">{corps}</g></svg>')
    amb = R.AMBIANCES[p["amb"]]
    return doc.replace(INK, amb["encre"]).replace(MEMBRE, amb["membres"]).replace(JAMBE_AR, amb["jambe_ar"])

def rendre(nom, p, zoom=1.0):
    """Renvoie (image RGBA, ancre en pixels). L'ancre est le point au sol entre les pieds."""
    import resvg_py
    from PIL import Image
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg_perso(nom, p), zoom=zoom))
    return Image.open(io.BytesIO(data)).convert("RGBA"), (AX * zoom, AY * zoom)

def hauteur_dessin(nom):
    """Hauteur du sol au sommet du crâne, en unités de dessin (sert à caler l'échelle sur la taille en mètres)."""
    c = PERSOS[nom]
    return (c["jambes"] + c["torse_h"] + 0.95) * D

def echelle(nom):
    """Mètres par unité de dessin pour ce personnage."""
    return PERSOS[nom]["h"] / hauteur_dessin(nom)

def tete_dans_le_dessin(nom, p):
    """Centre de la tête (unités de dessin, repère de la toile) pour une pose debout sans rotation : sert au contrôle chiffré."""
    c = PERSOS[nom]
    leg = c["jambes"] * D
    a = math.radians(p["incl"])
    root = (p["x"] * D, -(p["h"] * leg) - p["saut"] * D)
    th = c["torse_h"] * D * p["sq"]
    top = (root[0] + math.sin(a) * th, root[1] - math.cos(a) * th)
    ta = math.radians(p["incl"] * 0.6 + p["tincl"])
    lx, ly = rot(p["tx"] * D, -(D / 2 - 0.05 * D) - p["ty"] * D, ta)
    return AX + top[0] + lx, AY + top[1] + ly


# ---------------------------------------------------------------- expressions
EXPR = {
    "neutre blasé":     dict(yeux="point", paup=0.45, sourcils=(0, 0, -0.2), bouche="moue"),
    "colère":           dict(yeux="point", paup=0.25, sourcils=(24, 24, -0.5), bouche="dents", ouv=0.8),
    "peur":             dict(yeux="cercle", pupr=0.7, sourcils=(-20, -20, 0.5), bouche="ondule", sueur=(1,), tremble=1.0),
    "stupeur":          dict(yeux="cercle", pupr=0.55, sourcils=(-8, -8, 1.0), bouche="grand_o", eclats=1.0),
    "sourire en coin":  dict(yeux="point", paup=0.35, sourcils=(-6, 14, 0.1), bouche="coin"),
    "dents serrées":    dict(yeux="cercle", pupr=0.6, sourcils=(-14, -14, 0.4), bouche="dents", sueur=(1, 1)),
    "yeux fermés":      dict(yeux="ferme", sourcils=(-4, -4, 0), bouche="sourire"),
    "clin d'œil":       dict(yeux="clin", sourcils=(-8, 10, 0.2), bouche="coin"),
    "bouche ouverte":   dict(yeux="cercle", sourcils=(-10, -10, 0.7), bouche="ouverte"),
    "sueur":            dict(yeux="point", pup=(-0.8, 0), sourcils=(-16, -16, 0.3), bouche="pince", sueur=(1,)),
    "doute":            dict(yeux="point", paup=0.5, pup=(0.9, 0), sourcils=(16, -12, 0.0), bouche="moue", bouche_dx=0.03),
    "rire":             dict(yeux="joie", sourcils=(-10, -10, 0.5), bouche="rire", rougeur=1.0),
    "abattu":           dict(yeux="point", paup=0.6, pup=(0, 1), sourcils=(-22, -22, 0.0), bouche="bas"),
    "mépris":           dict(yeux="plisse", sourcils=(18, 18, -0.4), bouche="moue"),
    "essoufflé":        dict(yeux="cercle", pupr=0.8, sourcils=(-14, -14, 0.4), bouche="ouverte", ouv=0.8, sueur=(1, 1), souffle=0.4),
    "fier":             dict(yeux="joie", sourcils=(-4, -4, 0.4), bouche="sourire", rougeur=0.6),
}


# ---------------------------------------------------------------- animation
def _ease(t, kind):
    t = max(0.0, min(1.0, t))
    if kind == "in":
        return t * t * t
    if kind == "out":
        return 1 - (1 - t) ** 3
    if kind == "inout":
        return 4 * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2
    if kind == "step":
        return 0.0 if t < 1 else 1.0
    return t

class Anim:
    """Jeu d'un personnage, en pistes de clés. La règle du style : une pose change en UNE image (snap), puis elle est TENUE.
    va() ne sert qu'au dépassement (3 images) et au retour (4 images) d'un geste large."""
    def __init__(self, nom, **base):
        self.nom = nom
        self.base = pose(**base)
        self.pistes = {}

    def cle(self, f, ease="inout", **kw):
        for k, v in kw.items():
            if k not in self.base:
                raise ValueError(f"paramètre de pose inconnu : {k}")
            self.pistes.setdefault(k, []).append((float(f), v, ease))
            self.pistes[k].sort(key=lambda x: x[0])
        return self

    def val(self, k, f):
        ks = self.pistes.get(k)
        if not ks:
            return self.base[k]
        if f <= ks[0][0]:
            return ks[0][1]
        for (f0, v0, _), (f1, v1, e1) in zip(ks, ks[1:]):
            if f0 <= f < f1:
                if isinstance(v1, (int, float)) and isinstance(v0, (int, float)) and not isinstance(v1, bool):
                    return v0 + (v1 - v0) * _ease((f - f0) / (f1 - f0), e1)
                if isinstance(v1, (tuple, list)) and isinstance(v0, (tuple, list)) and all(isinstance(x, (int, float)) for x in list(v0) + list(v1)) and len(v0) == len(v1):
                    t = _ease((f - f0) / (f1 - f0), e1)
                    return tuple(a + (b - a) * t for a, b in zip(v0, v1))
                return v0
        return ks[-1][1]

    def va(self, f0, f1, ease="out", **kw):
        """Glisse de la valeur courante (à f0) à la cible (à f1)."""
        for k, v in kw.items():
            cur = self.val(k, f0)
            self.cle(f0, "lin", **{k: cur})
            self.cle(f1, ease, **{k: v})
        return self

    def snap(self, f, **kw):
        """Changement de pose en UNE image, sans intermédiaire, tenu ensuite."""
        for k, v in kw.items():
            cur = self.val(k, f - 1)
            self.cle(f - 1, "lin", **{k: cur})
            self.cle(f, "step", **{k: v})
        return self

    def cligne(self, f, yeux=None):
        """Clignement de 3 images (mi-clos, fermé, mi-clos) ; peut cacher un changement d'yeux."""
        avant, pa = self.val("yeux", f - 1), self.val("paup", f - 1)
        apres = yeux or avant
        mi = max(pa + 0.3, 0.75)                 # mi-clos nettement plus fermé que l'œil au repos, sinon le clignement se réduit à une image
        self.snap(f, paup=mi)
        self.snap(f + 1, yeux="ferme")
        self.snap(f + 2, yeux=apres, paup=mi)
        self.snap(f + 3, paup=pa if apres == avant else 0.0)
        return self

    def geste(self, f, depasse, final, **pose_forte):
        """Geste large complet : anticipation à poser AVANT par snap(f − 2, …) ; ici la pose forte en 1 image à f avec l'accent sur la tête
        (3 images), le dépassement de 3 images vers `depasse`, le retour de 4 images vers `final` (dict de paramètres numériques)."""
        self.snap(f, tsq=0.95, **pose_forte)
        self.va(f, f + 3, "lin", **depasse)
        self.va(f + 3, f + 7, "out", **final)
        self.snap(f + 3, tsq=1.0)
        return self

    def pose(self, f):
        p = dict(self.base)
        for k in self.pistes:
            p[k] = self.val(k, f)
        p["graine"] = int(f) // 2          # tremblement tenu 2 images
        return p


# ---------------------------------------------------------------- planches de contrôle
def planche(cases, cols, zoom, fichier, fond=(226, 214, 190), recadre=None, titre_h=44):
    from PIL import Image, ImageDraw, ImageFont
    police = None
    for nom in R.SOUS_TITRES["polices"]:
        try:
            police = ImageFont.truetype(nom, 24); break
        except OSError:
            continue
    police = police or ImageFont.load_default()
    ims = []
    for titre, nom, p in cases:
        im, _ = rendre(nom, p, zoom)
        if recadre:
            im = im.crop(tuple(int(v * zoom) for v in recadre))
        ims.append((titre, im))
    w, h = ims[0][1].size
    rows = (len(ims) + cols - 1) // cols
    pl = Image.new("RGB", (cols * w, rows * (h + titre_h)), fond)
    d = ImageDraw.Draw(pl)
    for i, (titre, im) in enumerate(ims):
        x, y = (i % cols) * w, (i // cols) * (h + titre_h)
        pl.paste(im, (x, y + titre_h), im)
        d.text((x + w / 2, y + 8), titre, fill=(40, 26, 44), font=police, anchor="ma")
    pathlib.Path(fichier).parent.mkdir(parents=True, exist_ok=True)
    pl.save(fichier)
    print(fichier, pl.size)

def planches(dossier):
    """Trois planches : distribution (face et trois quarts, quatre ambiances), expressions, poses."""
    dossier = pathlib.Path(dossier)
    noms = list(PERSOS)
    corps = (AX - 520, AY - 1420, AX + 520, AY + 60)
    tete = (AX - 330, AY - 1420, AX + 330, AY - 560)
    cases = []
    for amb, lum in (("jour", 60), ("soir", 10), ("interieur", 120), ("nuit", 160)):
        cases += [(f"{n} — {amb}", n, pose(amb=amb, lum=lum)) for n in noms]
        cases += [(f"{n} — trois quarts", n, pose(amb=amb, lum=lum, vue=0.8, dir=1, bras_d_z="av", pied_g=(-0.1, 0), pied_d=(0.16, 0))) for n in noms]
    planche(cases, 2 * len(noms), 0.36, dossier / "personnages-distribution.png", recadre=corps)
    cases = [(k, noms[i % len(noms)], pose(amb="soir", lum=20, **v)) for i, (k, v) in enumerate(EXPR.items())]
    planche(cases, 8, 0.6, dossier / "personnages-expressions.png", recadre=tete)
    n0, n1 = noms[0], noms[-1]
    poses = [
        ("pointe", n0, pose(bras_d=(96, 4), main_d="pointe", bras_d_z="av", vue=0.7, incl=4, **EXPR["fier"])),
        ("hausse les épaules", n1, pose(bras_g=(58, 78), bras_d=(58, 78), main_g="doigts", main_d="doigts", ty=-0.04, **EXPR["doute"])),
        ("marche — contact", n1, pose(dir=1, vue=0.8, pied_g=(-0.42, 0), pied_d=(0.42, 0), h=0.93, incl=6, bras_g=(-34, -10), bras_d=(-38, 46), bras_d_z="av")),
        ("marche — passage", n1, pose(dir=1, vue=0.8, pied_g=(0.05, 0.3), pied_d=(0.0, 0), h=1.0, incl=5, bras_g=(4, 10), bras_d=(4, 20), bras_d_z="av")),
        ("course", n1, pose(dir=1, vue=0.8, pied_g=(-0.62, 0.42), pied_d=(0.5, 0.06), h=0.9, saut=0.08, incl=17, bras_g=(-70, -80), bras_d=(-62, 84), bras_d_z="av", queue=-38, **EXPR["essoufflé"])),
        ("arrêt net", n1, pose(dir=1, vue=0.6, pied_g=(-0.2, 0), pied_d=(0.5, 0), h=0.86, incl=-13, sq=0.92, bras_g=(64, 40), bras_d=(70, 30), main_g="doigts", main_d="doigts", queue=40, **EXPR["stupeur"])),
        ("brandit un objet", n1, pose(bras_d=(165, 4), main_d="objet", bras_d_z="av", **EXPR["rire"])),
        ("tombe — à plat", n0, pose(rot=-90, x=0.4, h=0.2, saut=-0.35, tsq=0.8, pied_g=(-0.6, 0.6), pied_d=(-0.3, 0.62), bras_g=(100, 10), bras_d=(170, 0), yeux="croix", bouche="ondule")),
    ]
    planche(poses, 4, 0.42, dossier / "personnages-poses.png", recadre=(AX - 620, AY - 1420, AX + 620, AY + 90))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    import film, pantin as _p                         # les personnages du client : film.py appelle pantin.definir (le module importé, pas ce script)
    _p.planches(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "revue")
