"""LE FILM — EXEMPLE NEUTRE À REMPLACER ENTIÈREMENT par les personnages, les lieux et l'histoire du client.

Exemple fourni (7 s, 3 plans, 2 personnages, 2 plans d'intérieur sombre, 1 extérieur au couchant) : une gardienne de phare attend
une lettre depuis trois semaines ; ce soir, on frappe : c'est le facteur. Sujet inventé pour le kit, sans rapport avec
une œuvre existante. Lu par bl_scene.py (dans Blender), compo.py, controle.py : aucune dépendance à bpy ici.

Ce qu'on change pour un nouveau film : PERSOS, PLANS (bornes, ambiance, caméra par stations), le jeu (fonctions
ci-dessous), CARTONS (sous-titres), SOLEIL ; et les décors dans bl_scene.py.
"""
import math, pathlib, sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pantin
from pantin import Anim, EXPR

# ---------------------------------------------------------------- personnages : le client les DÉCRIT, pantin.py les dessine
PERSOS = pantin.definir({
    "gardienne": dict(couleur="#2a6f97", garniture="#f4ead2", col="rond", boutons=2, ceinture="#6b3f2a",
                      coiffe=dict(type="bonnet", tons=("#e8503a", "#bf3a2e", "#f4ead2")), accessoire="echarpe", accessoire_couleur="#f2b632",
                      h=1.60, jambes=1.2),
    "facteur": dict(couleur="#e0a526", garniture="#3a2a4a", col="v", ceinture="#3a2a4a",
                    coiffe=dict(type="casquette", tons=("#3f5fa8", "#2f4884", "#f2c85b")), cheveux="#5a3020",
                    accessoire="sacoche", accessoire_couleur="#9a5a34", pilosite="moustache", poil="#5a3020",
                    h=1.72, jambes=1.36, torse_l=0.66, torse_h=0.94),
})

# ---------------------------------------------------------------- plans
# Un plan = des bornes [a, b[ en numéros d'image, une ambiance (jour | soir | interieur | nuit) et une caméra par stations :
# (image, position, point visé, focale en mm, "arrivee" = on y arrive en freinant | "derive" = glissement lent jusque-là).
# Deux plans qui se recouvrent sont reliés par un fondu enchaîné sur la durée du recouvrement (6 à 11 images).
# Grammaire mesurée : un déplacement de 9 à 10 images toutes les 33 images environ (départ sec, long freinage) ; entre deux,
# la caméra DÉRIVE de 20 à 30 px par seconde (ici 3 à 5 cm de côté ou d'avancée par tenue) : elle n'est jamais immobile.
# Cadrage dominant : plan en pied serré, personnage à 60 à 73 % de la hauteur, caméra à 1,9 D du sol.
Y = -60.0                      # l'extérieur est construit loin de l'intérieur : y = −60
SOLEIL = (-0.08, 0.95, -0.30)  # direction dans laquelle VA la lumière : soleil bas, face à la caméra de l'extérieur -> les ombres viennent vers elle
LAMPE_CUISINE = (0.95, 0.35, 1.95)  # la lampe principale de l'intérieur (la suspension, construite là par bl_scene.py) : de côté, un peu
                                    # derrière le personnage -> son ombre part de l'autre côté et RESTE DANS LE CADRE (une lampe derrière lui l'enverrait sous le bord bas)
# En intérieur, chaque plan donne sa lampe principale : source=(x, y, z). L'assemblage en déduit l'ombre du personnage (à l'opposé),
# le liseré de lumière (côté lampe) et le côté du délié du trait. Cadrage serré devant un fond sombre et flou ; rien ne déborde du cadre.
PLANS = {
    "A": dict(a=0, b=57, ambiance="interieur", source=LAMPE_CUISINE, flou=0.75,      # flou un peu réduit : la table, à 1,3 m derrière, reste lisible
              mots="Elle attend depuis trois semaines.",
              cam=[(0, (0.80, -3.20, 1.12), (0.36, 0.0, 1.00), 35, "derive"),
                   (10, (0.40, -2.62, 1.00), (0.36, 0.0, 1.00), 35, "arrivee"),      # station 1 : plan en pied serré, de face
                   (56, (0.46, -2.60, 1.00), (0.39, 0.0, 1.00), 35, "derive")]),     # dérive pendant la tenue
    "C": dict(a=50, b=109, ambiance="interieur", source=LAMPE_CUISINE, flou=0.75,
              mots="Ce soir, on frappe.",
              cam=[(50, (-0.70, -2.95, 0.90), (0.32, 0.1, 1.00), 35, "derive"),      # station 2 : de trois quarts, légère contre-plongée
                   (66, (-0.66, -2.92, 0.90), (0.32, 0.1, 1.00), 35, "derive"),
                   (76, (-0.46, -2.60, 0.94), (0.30, 0.05, 1.04), 35, "arrivee"),    # station 3 : poussée sur la stupeur ; les bras écartés restent dans le cadre
                   (108, (-0.43, -2.54, 0.94), (0.30, 0.05, 1.05), 35, "derive")]),  # avancée régulière pendant la tenue
    "B": dict(a=101, b=210, ambiance="soir",
              mots="C'est le facteur. Enfin !",
              cam=[(101, (1.45, Y + 6.3, 1.10), (0.20, Y - 5.0, 1.80), 35, "derive"),
                   (111, (0.90, Y + 5.4, 0.85), (0.30, Y - 4.0, 1.55), 35, "arrivee"),     # station 4 : le plan entre déjà en mouvement
                   (131, (0.86, Y + 5.32, 0.85), (0.31, Y - 4.0, 1.50), 35, "derive"),
                   (141, (0.75, Y + 4.10, 0.75), (0.40, Y + 1.5, 1.05), 35, "arrivee"),    # station 5 : la caméra se pose quand il s'arrête
                   (150, (0.74, Y + 4.07, 0.75), (0.40, Y + 1.5, 1.06), 35, "derive"),
                   (159, (0.62, Y + 3.95, 0.70), (0.40, Y + 1.5, 1.12), 35, "arrivee"),    # station 6 : poussée sur la pose forte
                   (186, (0.57, Y + 3.92, 0.70), (0.40, Y + 1.5, 1.12), 35, "derive"),
                   (196, (0.46, Y + 4.25, 0.72), (0.40, Y + 1.5, 1.10), 35, "arrivee"),    # station 7 : léger recul final
                   (209, (0.44, Y + 4.28, 0.72), (0.40, Y + 1.5, 1.10), 35, "derive")]),
    # images fixes pour le contrôle chiffré (hors film) : plans larges à la focale mesurée de 25 mm
    "L": dict(a=9001, b=9002, ambiance="interieur", source=LAMPE_CUISINE, flou=0.45, mots="",
              cam=[(9001, (-1.9, -4.6, 1.30), (1.1, 1.6, 1.25), 25, "derive")]),
    "E": dict(a=9002, b=9003, ambiance="soir", mots="",
              cam=[(9002, (1.7, Y + 7.5, 1.05), (-0.4, Y - 14.0, 2.6), 25, "derive")]),
    "P": dict(a=9003, b=9004, ambiance="interieur", source=LAMPE_CUISINE, mots="",    # le plancher vu dans l'axe des lames, dans la flaque de la lampe : mesure des joints
              cam=[(9003, (1.25, -2.3, 1.0), (1.25, 0.5, 0.1), 35, "derive")]),
    "T": dict(a=9004, b=9005, ambiance="interieur", source=LAMPE_CUISINE, mots="",    # le plateau de la table, net et éclairé : mesure du bois dessiné
              cam=[(9004, (0.66, -0.35, 1.55), (0.70, 1.32, 0.78), 35, "derive")]),
}
ORDRE = ["A", "C", "B"]
FIXES = ["L", "E", "P", "T"]
TOTAL = 210

# ---------------------------------------------------------------- sous-titres : (image de début, image de fin, texte). 1 à 2 mots, 3 au plus ; 3 à 22 images par carton.
CARTONS = [(0, 14, "Elle attend"), (14, 24, "depuis"), (24, 46, "trois semaines."), (50, 64, "Ce soir,"), (64, 86, "on frappe."),
           (110, 120, "C'est"), (120, 142, "le facteur."), (150, 172, "Enfin !")]

# ---------------------------------------------------------------- jeu
# Règles du style : une pose change en UNE image (snap) puis elle est tenue ; anticipation 2 images ; dépassement 3 + retour 4
# sur les gestes larges seulement ; clignement de 3 images ; l'action tombe 2 à 4 images APRÈS le mot ; un seul personnage joue.
def _gardienne():
    a = Anim("gardienne", vue=-0.45, pup=(-0.9, 0.0), bras_g=(8, 4), bras_d=(8, 4), queue=4, **EXPR["neutre blasé"])
    a.cligne(18)
    a.snap(30, vue=0.1, pup=(0.0, 0.0), tincl=4, bouche="bas")          # elle revient vers nous, lasse : regard caméra
    a.cligne(47)
    # la stupeur (le carton « on frappe. » apparaît à l'image 64) : 2 images yeux fermés, 1 image d'ovale écrasé, puis les anneaux
    # d'un coup ; recul du buste de 0,1 D en 3 images, retour partiel en 5 ; tenue de 39 images, figée
    a.snap(66, yeux="ferme", paup=0.0, ty=0.03, incl=3, bras_g=(2, 0), bras_d=(2, 0), sourcils=(-6, -6, 0.3))
    a.snap(68, yeux="ovale", pupr=0.55, pup=(0.0, 0.0), sourcils=(-8, -8, 0.8))
    a.geste(69, depasse=dict(bras_g=(40, 62), bras_d=(40, 62)), final=dict(bras_g=(46, 58), bras_d=(46, 58)),
            ty=-0.05, tincl=0, vue=0.0, bras_g=(50, 56), bras_d=(50, 56), main_g="doigts", main_d="doigts",
            yeux="cercle", sourcils=(-8, -8, 1.0), bouche="grand_o", eclats=1.0, queue=-22)
    a.va(69, 72, "lin", x=-0.10, incl=-9)                               # le recul : le buste part en arrière
    a.va(72, 77, "out", x=-0.05, incl=-5)                               # retour partiel
    a.snap(72, eclats=0.0)                                              # les traits de surprise durent 3 images
    a.snap(74, sueur=(1,))                                              # la goutte apparaît d'un coup et reste collée à la tempe
    a.va(72, 80, "out", queue=6)                                        # le pan de l'écharpe retombe : seul mouvement pendant la tenue
    return a

GARDIENNE = _gardienne()

def _facteur(f):
    """Course de face vers la caméra (un pas toutes les 5 images, genoux pliés en angle vif), arrêt net, souffle, puis il brandit la lettre."""
    f0, f1 = 104, 141
    y0, y1 = Y - 6.5, Y + 1.5
    base = dict(amb="soir", yeux="cercle", pupr=0.7, sourcils=(-16, -16, 0.5), bouche="ouverte", ouv=0.9, sueur=(1, 1))
    if f < f1:
        t = max(0.0, (f - f0) / (f1 - f0))
        y = y0 + (y1 - y0) * (1 - (1 - t) ** 1.6)
        ph = (f - f0) / 10.0 * 2 * math.pi
        s = math.sin(ph)
        return (0.1 + 0.3 * t, y), pantin.pose(h=0.9, saut=0.05 + 0.07 * abs(math.cos(ph)), incl=5 * s, tincl=-3 * s,
                                                pied_g=(-0.17, max(0.0, s) * 0.55), pied_d=(0.17, max(0.0, -s) * 0.55),
                                                bras_g=(-10 + 55 * s, 96), bras_d=(-10 - 55 * s, 96), **base)
    pos = (0.4, y1)
    if f < 144:         # arrêt net, 3 images : jambes raides et écartées, bras écartés (les mains restent dans le cadre)
        k = f - f1
        return pos, pantin.pose(h=(0.90, 0.93, 0.95)[k], sq=(0.9, 0.94, 0.97)[k], pied_g=(-0.42, 0), pied_d=(0.42, 0),
                                bras_g=(52, 40), bras_d=(52, 40), main_g="doigts", main_d="doigts", ty=-0.02, **base)
    if f < 150:         # souffle : penché en avant, jambes droites, tenu
        return pos, pantin.pose(h=0.97, incl=14, tincl=6, pied_g=(-0.3, 0), pied_d=(0.3, 0), bras_g=(8, 6), bras_d=(8, 6), ty=-0.02,
                                souffle=(f - 144) / 6.0 if f < 148 else None, **{**base, "yeux": "ferme"})
    if f < 153:         # le carton « Enfin ! » apparaît à l'image 150 : anticipation, le bras descend avant de monter
        return pos, pantin.pose(h=0.96, pied_g=(-0.3, 0), pied_d=(0.3, 0), bras_g=(14, 20), bras_d=(-16, 30), incl=5, **{**base, "sueur": (1,)})
    k = f - 153         # il brandit la lettre 3 images après le mot : pose en 1 image, dépassement de 3 images, retour, puis tenue figée
    haut = (172, 168, 164, 160, 162, 164, 165, 165)[min(k, 7)]
    fin = dict(amb="soir", yeux="joie", bouche="rire", rougeur=1.0, sourcils=(-8, -8, 0.6))        # plus de sueur : il est content
    return pos, pantin.pose(h=1.0, sq=(1.05, 1.02, 1.0)[min(k, 2)], pied_g=(-0.26, 0), pied_d=(0.26, 0), bras_g=(22, 16), bras_d=(haut, 4),
                            main_d="objet", objet=dict(forme="carte", couleur="#fff4dc", l=0.36, h=0.25), bras_d_z="av",
                            tsq=0.95 if k < 3 else 1.0, eclats=1.0 if k < 3 else 0.0, **fin)

def acteurs(k, f):
    """Liste (nom, position au sol (x, y), pose) pour l'image f du plan k."""
    if k in ("A", "C"):
        return [("gardienne", (0.30, 0.0), GARDIENNE.pose(f))]
    if k == "B":
        pos, p = _facteur(max(f, 104))
        return [("facteur", pos, p)]
    if k == "L":
        return [("gardienne", (0.30, 0.0), pantin.pose(vue=0.3, **EXPR["neutre blasé"]))]
    if k == "E":
        return [("facteur", (0.4, Y + 1.5), pantin.pose(bras_d=(165, 4), main_d="objet", bras_d_z="av", **EXPR["rire"]))]
    return []

def mise_au_point(k, f):
    """Point du monde sur lequel la caméra fait le point quand aucun personnage n'est dans le plan."""
    if k == "P":
        return (1.25, -0.4, 0.0)
    if k == "T":
        return (0.70, 1.32, 0.78)
    return (0.3, 0.0, 1.0) if k in ("A", "C", "L") else (0.4, Y + 1.5, 1.0)

# ---------------------------------------------------------------- contrôle chiffré (controle.py)
# Personnages : images où un personnage est debout, bien visible. Décor : cibles en coordonnées du MONDE (mètres), projetées par controle.py.
#   texture : zone (x0, y0, x1, y1) d'un sol dessiné ; joints=True si on y attend un joint tous les 0,32 D
#   bois    : zone (x0, y0, x1, y1) à la hauteur z d'une pièce de bois nette et éclairée (contraste du fil : 18 à 21 niveaux)
#   trait   : segment a -> b en travers de la silhouette d'un objet net (a dehors, b dedans, ou l'inverse)
#   fond    : segment a -> b en travers d'une arête lointaine (flou de profondeur)
#   sol_net : zone du sol autour des pieds du sujet
CONTROLE_PERSONNAGES = [("A", 25), ("C", 95), ("B", 147)]       # des poses où rien ne touche la tête (un bras levé contre elle gonfle le plein mesuré)
CONTROLE_OMBRES = [("E", 9002)]            # un plan large où l'ombre du torse est dans le cadre
CONTROLE_FILM = ("B", 180)
CONTROLE_CHAMP = [("A", 25), ("C", 60), ("C", 95), ("B", 147)]     # ce qui entre dans le champ : rien de nu derrière le personnage, aucun membre au bord du cadre
CONTROLES = [
    dict(image=("P", 9003), type="texture", nom="plancher", zone=(0.95, -0.75, 1.55, 0.05), axe="x", joints=True),   # une zone ÉCLAIRÉE : dans la pénombre la texture s'efface
    dict(image=("T", 9004), type="bois", nom="plateau de la table", zone=(0.46, 1.08, 0.88, 1.62), z=0.781, axe="y"),  # une pièce de bois nette et éclairée, veines en travers de l'axe
    dict(image=("L", 9001), type="trait", nom="panier", a=(0.003, 0.38, 0.12), b=(-0.252, 0.431, 0.12)),
    dict(image=("A", 25), type="sol_net", nom="intérieur", zone=(-0.4, -0.7, 1.0, 0.7)),
    dict(image=("B", 147), type="sol_net", nom="extérieur", zone=(-0.3, Y + 0.9, 1.1, Y + 2.3)),
    dict(image=("B", 125), type="fond", nom="bord de la tour sur le ciel", a=(3.94, Y - 19.22, 11.0), b=(3.30, Y - 19.34, 11.0)),
    dict(image=("L", 9001), type="sol_net", nom="plan large intérieur", zone=(-0.4, -0.7, 1.0, 0.7)),
    dict(image=("E", 9002), type="sol_net", nom="plan large extérieur", zone=(-0.3, Y + 0.9, 1.1, Y + 2.3)),
]
