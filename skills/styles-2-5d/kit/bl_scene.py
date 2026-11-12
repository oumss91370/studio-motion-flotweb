"""LES DÉCORS — EXEMPLE NEUTRE À REMPLACER : la cuisine d'une gardienne de phare (intérieur chaud) et la cour du phare (couchant).

Lancé dans Blender par lancer.py :
    blender -b --python outils/bl_scene.py -- construire
    blender -b decors/decor.blend --python outils/bl_scene.py -- rendre [pct] [tout | film | A:12,L:9001]

Méthode à garder pour vos décors (c'est elle qui fait le style) :
1. un soleil, déclaré AVANT les matières ; 2. des matières DESSINÉES, toutes dimensionnées en D (joint tous les 0,32 D) ;
3. des volumes simples, mais BEAUCOUP : 30 à 45 objets distincts dans le champ de chaque plan, rien de nu derrière un personnage ;
4. au moins une source de lumière visible par lieu, RONDE (B.globe), et un contrepoint froid dans une ambiance chaude (une
   fenêtre bleu de nuit, des tentures violettes) ; en intérieur, des murs meublés à la hauteur du champ (boiserie, rayonnage, tentures) ;
5. cailloux et touffes semés au sol dehors (5 à 11 par D² près du sujet) ; 6. fusionner, enregistrer.
"""
import bpy, math, pathlib, random, sys
sys.dont_write_bytecode = True
ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import regles as R
import bl_decor as B
import film as F

RAC = pathlib.Path(__import__("os").environ.get("EPISODE_RACINE", ICI.parent)).resolve()
BLEND = RAC / "decors" / "decor.blend"
D = R.D_MONDE
PL, JT = R.DECOR["planche"] * D, R.DECOR["joint"] * D
rad = math.radians
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else ["construire"]


# ====================================================================== matières
def _mur_cuisine(axe):
    """Mur composé, MEUBLÉ à la hauteur du champ : plinthe, boiserie de planches verticales jusqu'à 2,25 m (joint tous les 0,33 D,
    bois dessiné), cimaise, puis un enduit sombre à fines rayures et sa frise. Jamais de mur nu derrière un personnage."""
    def f(t, col, ax, vec):
        a, z = ax[axe], ax["z"]
        enduit = t.mix(t.math("MULTIPLY", t.lisse(t.bruit(vec, 1.3, 2.0), 0.42, 0.7), 0.6), B.lin("#8a4636"), B.lin("#6e3430"))
        ray, _ = t.bandes(a, 0.42, 0.05)                                  # fines rayures peintes du papier
        enduit = t.mix(t.math("MULTIPLY", ray, 0.55), enduit, B.lin("#5a2a2c"))
        enduit = t.mix(t.entre(z, 2.86, 3.04), enduit, B.lin("#3a1626"))
        enduit = t.mix(t.entre(z, 2.92, 2.98), enduit, B.lin("#d9a441"))
        j, num = t.bandes(a, 0.33 * D, 0.020 * D)
        h = t.hasard(num)
        cernes, veines, noeud = t.bois_dessine(vec, "z", 1.0, 0.05, h)
        bois = t.mix(t.math("ADD", t.math("MULTIPLY", cernes, 0.6), t.math("MULTIPLY", t.math("SUBTRACT", h, 0.4), 0.8), clamp=True), B.lin("#8f4632"), B.lin("#64291f"))
        bois = t.mix(t.math("MULTIPLY", veines, 0.85), bois, B.lin("#3a1418"))
        bois = t.mix(t.math("MULTIPLY", noeud, 0.9), bois, B.lin("#3a1418"))
        bois = t.mix(j, bois, B.lin("#260d18"))
        tr, _ = t.bandes(t.math("SUBTRACT", z, 1.02), 5.0, 0.07)            # une traverse à mi-hauteur : la boiserie est faite de panneaux
        bois = t.mix(t.math("MULTIPLY", t.entre(z, 0.95, 1.09), 1.0), bois, B.lin("#5a2420"))
        bois = t.mix(t.entre(z, 1.075, 1.09), bois, B.lin("#260d18"))
        c = t.mix(t.math("LESS_THAN", z, 2.25), enduit, bois)
        c = t.mix(t.entre(z, 2.25, 2.40), c, B.lin("#4a1c22"))
        c = t.mix(t.entre(z, 2.375, 2.40), c, B.lin("#260d18"))
        return t.mix(t.math("LESS_THAN", z, 0.14), c, B.lin("#35141d"))
    return f

def _tenture(t, col, ax, vec):
    """Tenture : plis verticaux (une bande sombre tous les 0,3 D, un filet clair à côté), semis de motifs, galon clair en bas."""
    pli, _ = t.bandes(t.math("ADD", ax["x"], ax["y"]), 0.30 * D, 0.10 * D)
    col = t.mix(t.math("MULTIPLY", pli, 0.7), col, B.lin("#2c1a40"))
    clair, _ = t.bandes(t.math("ADD", t.math("ADD", ax["x"], ax["y"]), 0.08 * D), 0.30 * D, 0.035 * D)
    col = t.mix(t.math("MULTIPLY", clair, 0.6), col, B.lin("#7a5488"))
    mx, _ = t.bandes(t.math("ADD", ax["x"], ax["y"]), 0.6 * D, 0.14 * D)
    mz, _ = t.bandes(ax["z"], 0.6 * D, 0.14 * D)
    col = t.mix(t.math("MULTIPLY", t.math("MULTIPLY", mx, mz), 0.8), col, B.lin("#c9a05a"))        # un semis de petits carreaux dorés
    return t.mix(t.entre(ax["z"], 0.03, 0.09), col, B.lin("#c9a05a"))

def _nuit(t, col, ax, vec):
    """La nuit par la fenêtre : un dégradé (plus clair vers l'horizon) et quelques étoiles ; pas un aplat."""
    col = t.mix(t.lisse(ax["z"], 1.2, 2.5), B.lin("#3d3c92"), B.lin("#221f5c"))
    etoiles = t.math("GREATER_THAN", t.bruit(vec, 21.0, 0.0), 0.74)
    return t.mix(t.math("MULTIPLY", etoiles, 0.9), col, B.lin("#cfd0f6"))

def _pierres(t, col, ax, vec):
    """Muret et soubassement : pierres appareillées, joints sombres."""
    jv, _ = t.bandes(t.math("ADD", ax["x"], ax["y"]), 0.62, 0.035)
    jh, _ = t.bandes(ax["z"], 0.30, 0.035)
    return t.mix(t.math("MAXIMUM", jv, jh), col, B.lin("#6b4a52"))

def _phare(t, col, ax, vec):
    """Tour : larges bandes peintes, coulures plus sombres."""
    b, _ = t.bandes(ax["z"], 4.4, 2.2)
    col = t.mix(b, col, B.lin("#c8402f"))
    return t.mix(t.math("MULTIPLY", t.lisse(t.bruit(vec, 1.0, 2.0, etire=[0.25, 0.25, 2.5]), 0.55, 0.7), 0.35), col, B.lin("#8f7c8e"))

def _sable(t, col, ax, vec):
    """Sol de la cour : taches douces, un sentier plus clair au milieu, petites taches sombres semées."""
    d = t.math("ABSOLUTE", t.math("ADD", t.math("SUBTRACT", ax["x"], 0.3), t.math("MULTIPLY", t.math("SINE", t.math("MULTIPLY", ax["y"], 0.23)), 0.45)))
    col = t.mix(t.math("MULTIPLY", t.math("SUBTRACT", 1.0, t.lisse(d, 0.5, 1.3)), 0.35), col, B.lin("#efb46a"))
    pts = t.math("GREATER_THAN", t.bruit(vec, 34.0, 0.0), 0.71)
    return t.mix(t.math("MULTIPLY", pts, 0.35), col, B.lin("#b97a40"))

def _tuiles(t, col, ax, vec):
    r, _ = t.bandes(ax["x"], 0.34, 0.07)
    g, num = t.bandes(ax["y"], 0.30, 0.035)
    col = t.mix(t.math("MULTIPLY", t.hasard(num), 0.5), col, B.lin("#4e4258"))
    col = t.mix(g, col, B.lin("#2f2438"))
    return t.mix(t.math("MULTIPLY", r, 0.55), col, B.lin("#3b2f45"))

def matieres():
    m = B.matiere
    # --- intérieur
    m("plancher", "#b4602f", "#9c4e2a", fibre="y", coords="monde", veine="#7c3a22", planches=("x", PL, JT, "#33121a"), fil=3.2, net=0.09, var=0.75)      # grande surface : joints nets, lames de teintes inégales, un dessin LARGE et doux (un fil serré et contrasté vibre et vole le regard)
    m("mur@x", "#a85a3c", coords="monde", special=_mur_cuisine("x"))
    m("mur@y", "#a85a3c", coords="monde", special=_mur_cuisine("y"))
    m("plafond", "#6a3848", "#4e283c", fibre="x", coords="monde", veine="#2c1424", planches=("y", PL, 1.5 * JT, "#24101c"), fil=1.6, var=0.8)      # lattes dessinées : un plafond n'est pas un aplat
    m("tenture", "#503056", "#44284e", coords="objet", tache=(0.5, "#3a2148", 0.5), special=_tenture)      # le violet du contrepoint froid
    m("tenture_bleue", "#3a3a80", "#312e79", coords="objet", tache=(0.5, "#27245e", 0.5), special=_tenture)
    B.bois("bois", "#8a4a30", "#55291e", "#2f1418")
    B.bois("bois_clair", "#c58a4e", "#8f5a2c", "#573420")
    B.bois("bois_peint", "#2f6f78", "#22545e", "#143a44")
    m("fonte", "#3a2a3a", "#2c1f2e", tache=(0.25, "#4f3a48", 0.5))
    m("email", "#f2e6d0", "#e0d0b6", tache=(0.2, "#c9b596", 0.4))
    m("email_bleu", "#3f6fa8", "#335a8c", tache=(0.2, "#27457a", 0.4))
    m("laiton", "#e0a83a", "#c48e2a", tache=(0.1, "#a8741f", 0.5))
    m("tissu_rouge", "#c23a2c", "#a52f25", tache=(0.4, "#8a2420", 0.45))
    m("tissu_jaune", "#f2b632", "#dca02a", tache=(0.4, "#c48a22", 0.4))
    m("tapis", "#7a2f3a", "#63242f", coords="monde", tache=(0.5, "#4f1c28", 0.5), planches=("y", 0.22, 0.03, "#e0a83a"))
    m("papier", "#f4ead2", "#e6d8b8", tache=(0.3, "#cdbb94", 0.4))
    m("corde", "#d9b25e", "#c39a48", fibre="z", veine="#8a6a2c", planches=("z", 0.05, 0.008, "#8a6a34"))
    m("pain", "#d99a52", "#b87a3a", tache=(0.1, "#8a5626", 0.5))
    m("carte", "#cfe0d8", "#a9c9c0", tache=(0.25, "#7fa8a8", 0.6))
    m("encre", "#2a1a2c")
    m("fenetre", "#2c2a72", coords="monde", emissif=True, special=_nuit)                    # la nuit par la fenêtre : bleu de nuit, le contrepoint froid
    m("abat_jour", "#ffb45e", emissif=True)                   # une lampe est chaude, orangée
    m("braise", "#ff6a1f", emissif=True)
    m("flamme", "#ffc060", emissif=True)
    # --- extérieur
    m("sable", "#e39a48", "#d98d42", coords="monde", tache=(1.4, "#cf8440", 0.7), special=_sable)
    m("pierre", "#c7a394", "#b08c82", coords="monde", tache=(0.5, "#9a7a78", 0.5), special=_pierres)
    m("crepi", "#f0d2a8", "#dcb888", coords="monde", tache=(0.9, "#c79e74", 0.6))
    m("tour", "#f4e6d0", "#e2ceb2", coords="objet", special=_phare)
    m("tuile", "#5e5068", coords="objet", special=_tuiles)
    m("metal_sombre", "#3f3350", "#33283f", tache=(0.3, "#52446a", 0.5))
    m("bouee", "#e8503a", "#c53c2e", tache=(0.15, "#f4ead2", 0.6))
    m("coque", "#2f6f78", "#24565e", fibre="y", veine="#143a44", planches=("z", 0.16, 0.02, "#10303a"))
    m("volet", "#3f7f6c", "#2f6456", fibre="z", veine="#1f4a40", planches=("x", PL, JT, "#17382f"))
    m("feuillage", "#6f9a48", "#5c8540", tache=(0.9, "#4a7038", 0.6))
    m("caillou", "#f0c090", "#e0ae7c", a_plat=True, lisere="#8a5632")
    m("caillou2", "#d8a474", "#c69264", a_plat=True, lisere="#7a4a2c")
    m("herbe", "#e8b848", a_plat=True)
    m("fenetre_chaude", "#ffc874", emissif=True)
    m("lanterne", "#ffd08a", emissif=True)


# ====================================================================== meubles et accessoires composés
def table(nom, x, y, l, p, h, mat="bois", col="INTERIEUR"):
    B.boite(f"{nom}_plateau", (l, p, 0.06), (x, y, h - 0.06), mat, col=col)
    for i, (dx, dy) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1))):
        B.boite(f"{nom}_pied{i}", (0.07, 0.07, h - 0.06), (x + dx * (l / 2 - 0.08), y + dy * (p / 2 - 0.08), 0), mat, col=col)
    B.boite(f"{nom}_ceinture", (l - 0.16, p - 0.16, 0.09), (x, y, h - 0.15), mat, col=col)

def tabouret(nom, x, y, h=0.46, col="INTERIEUR"):
    B.cylindre(f"{nom}_assise", 0.19, 0.05, (x, y, h - 0.05), "bois_clair", col=col)
    for i in range(3):
        a = 2.1 * i + 0.4
        B.cylindre(f"{nom}_pied{i}", 0.024, h - 0.05, (x + 0.13 * math.cos(a), y + 0.13 * math.sin(a), 0), "bois_clair", seg=8, col=col)

def etagere(nom, x, y, z, l, col="INTERIEUR"):
    """Étagère murale chargée : planche, deux consoles, bocaux, boîtes, livres."""
    rnd = random.Random(int(x * 100 + z * 10))
    B.boite(f"{nom}_planche", (l, 0.22, 0.04), (x, y, z), "bois", col=col)
    for k in (-1, 1):
        B.boite(f"{nom}_console{k}", (0.04, 0.18, 0.16), (x + k * (l / 2 - 0.12), y, z - 0.16), "bois", col=col)
    px = x - l / 2 + 0.1
    i = 0
    while px < x + l / 2 - 0.1:
        sorte = rnd.choice(("bocal", "boite", "livres", "pot"))
        if sorte == "bocal":
            B.cylindre(f"{nom}_o{i}", 0.055, 0.17, (px, y, z + 0.04), rnd.choice(("email", "email_bleu")), seg=12, col=col)
            B.cylindre(f"{nom}_c{i}", 0.06, 0.03, (px, y, z + 0.21), "laiton", seg=12, col=col); px += 0.17
        elif sorte == "boite":
            B.boite(f"{nom}_o{i}", (0.16, 0.13, 0.12), (px + 0.03, y, z + 0.04), rnd.choice(("tissu_rouge", "bois_clair", "tissu_jaune")), col=col); px += 0.22
        elif sorte == "livres":
            for j in range(rnd.randint(3, 5)):
                B.boite(f"{nom}_l{i}_{j}", (0.035, 0.15, rnd.uniform(0.17, 0.24)), (px, y, z + 0.04), rnd.choice(("tissu_rouge", "email_bleu", "papier", "bois_peint", "tissu_jaune")),
                        rot=(0, rad(rnd.uniform(-4, 4)), 0), col=col)
                px += 0.045
            px += 0.06
        else:
            B.cylindre(f"{nom}_o{i}", 0.07, 0.11, (px, y, z + 0.04), "laiton", r2=0.09, seg=12, col=col); px += 0.2
        i += 1

def suspension(nom, x, y, z, col="INTERIEUR", energie=140.0):
    """Suspension à globe : la source est RONDE (un globe, pas une boîte ni un cône), son halo est un disque."""
    B.cylindre(f"{nom}_fil", 0.008, 3.1 - z - 0.14, (x, y, z + 0.14), "encre", seg=6, col=col, ombre=False)
    B.cylindre(f"{nom}_coiffe", 0.07, 0.05, (x, y, z + 0.12), "laiton", r2=0.03, seg=12, col=col, ombre=False)
    B.globe(f"{nom}_globe", 0.11, (x, y, z), "abat_jour", energie=energie, rayon=0.35, col=col)

def rayonnage(nom, x0, x1, y, h=2.1, niveaux=5, col="INTERIEUR", graine=7):
    """Rayonnage du sol au champ : montants, tablettes, chargées de livres, bocaux, boîtes et pots. Il meuble le mur derrière un personnage."""
    rnd = random.Random(graine)
    l = x1 - x0
    B.boite(f"{nom}_fond", (l, 0.03, h), ((x0 + x1) / 2, y + 0.14, 0), "bois", col=col)
    n = max(2, int(round(l / 0.75)) + 1)
    for i in range(n):
        B.boite(f"{nom}_montant{i}", (0.05, 0.3, h), (x0 + l * i / (n - 1), y, 0), "bois", col=col)
    B.boite(f"{nom}_corniche", (l + 0.12, 0.36, 0.07), ((x0 + x1) / 2, y, h), "bois", col=col)
    for k in range(niveaux):
        z = 0.12 + (h - 0.2) * k / niveaux
        B.boite(f"{nom}_tablette{k}", (l, 0.3, 0.035), ((x0 + x1) / 2, y, z), "bois_clair", col=col)
        px, i, haut = x0 + 0.09, 0, (h - 0.2) / niveaux - 0.07
        while px < x1 - 0.12:
            sorte = rnd.choice(("livres", "livres", "bocal", "boite", "pot", "vide"))
            if sorte == "livres":
                for j in range(rnd.randint(3, 6)):
                    if px > x1 - 0.1:
                        break
                    ep = rnd.uniform(0.03, 0.05)
                    B.boite(f"{nom}_l{k}_{i}_{j}", (ep, 0.17, haut * rnd.uniform(0.6, 0.92)), (px, y - 0.03, z + 0.035),
                            rnd.choice(("tissu_rouge", "email_bleu", "papier", "bois_peint", "tissu_jaune", "tenture", "fonte")), rot=(0, rad(rnd.uniform(-3, 3)), 0), col=col)
                    px += ep + 0.006
                px += 0.04
            elif sorte == "bocal":
                B.cylindre(f"{nom}_o{k}_{i}", 0.055, min(0.17, haut * 0.7), (px + 0.05, y - 0.03, z + 0.035), rnd.choice(("email", "email_bleu")), seg=12, col=col)
                B.cylindre(f"{nom}_c{k}_{i}", 0.06, 0.025, (px + 0.05, y - 0.03, z + 0.035 + min(0.17, haut * 0.7)), "laiton", seg=12, col=col); px += 0.17
            elif sorte == "boite":
                B.boite(f"{nom}_o{k}_{i}", (0.17, 0.15, min(0.13, haut * 0.6)), (px + 0.085, y - 0.03, z + 0.035), rnd.choice(("tissu_rouge", "bois_clair", "tissu_jaune", "papier")), col=col); px += 0.21
            elif sorte == "pot":
                B.cylindre(f"{nom}_o{k}_{i}", 0.06, 0.11, (px + 0.07, y - 0.03, z + 0.035), "laiton", r2=0.08, seg=12, col=col); px += 0.19
            else:
                px += 0.12
            i += 1

def tenture(nom, x, y, z0, z1, l, mat="tenture", col="INTERIEUR", axe="x"):
    """Tenture pendue à sa tringle, devant un mur."""
    t = (l, 0.05, z1 - z0) if axe == "x" else (0.05, l, z1 - z0)
    B.boite(nom, t, (x, y, z0), mat, col=col)
    B.boite(f"{nom}_tringle", (l + 0.16, 0.03, 0.03) if axe == "x" else (0.03, l + 0.16, 0.03), (x, y, z1 + 0.01), "laiton", col=col)

def cadre(nom, x, y, z, l, h, mat="carte", col="INTERIEUR"):
    B.boite(f"{nom}_bord", (l + 0.08, 0.03, h + 0.08), (x, y, z), "bois", col=col)
    B.boite(f"{nom}_image", (l, 0.02, h), (x, y - 0.02, z + 0.04), mat, col=col)

def caisse(nom, x, y, z, c, rot=0.0, col="COUR"):
    B.boite(nom, (c, c, c * 0.8), (x, y, z), "bois_clair", rot=(0, 0, rad(rot)), col=col)
    B.boite(f"{nom}_latte", (c * 1.04, c * 1.04, c * 0.12), (x, y, z + c * 0.34), "bois", rot=(0, 0, rad(rot)), col=col)


# ====================================================================== l'intérieur : une cuisine, le soir
# Règles de l'intérieur sombre (regles.INTERIEUR) : la pièce est SOMBRE, une lampe principale ronde (la suspension : c'est la
# « source » des plans dans film.py), une fenêtre bleu de nuit et des tentures violettes pour le contrepoint froid, des murs
# MEUBLÉS à la hauteur du champ (boiserie jusqu'à 2,25 m, rayonnage, tentures, cadres) et rien qui déborde du cadre des plans.
LAMPE = F.LAMPE_CUISINE

def cuisine():
    col = "INTERIEUR"
    B.boite("sol_cuisine", (7.0, 9.0, 0.1), (0, -1.0, -0.1), "plancher", col=col)
    B.boite("mur_fond", (7.0, 0.2, 3.2), (0, 2.7, 0), "mur@x", col=col)
    B.boite("mur_gauche", (0.2, 9.0, 3.2), (-3.4, -1.0, 0), "mur@y", col=col)
    B.boite("mur_droit", (0.2, 9.0, 3.2), (3.4, -1.0, 0), "mur@y", col=col)
    B.boite("plafond", (7.0, 9.0, 0.1), (0, -1.0, 3.2), "plafond", col=col)
    for i, y in enumerate((-2.2, -0.4, 1.4)):
        B.boite(f"poutre{i}", (7.0, 0.18, 0.2), (0, y, 3.0), "bois", col=col)
    # la fenêtre du fond : le contrepoint froid (bleu de nuit), encadrée, rideaux, rebord chargé
    fx = 1.05
    B.boite("fenetre", (1.0, 0.04, 1.3), (fx, 2.59, 1.2), "fenetre", col=col, ombre=False)
    B.boite("fen_haut", (1.2, 0.1, 0.09), (fx, 2.56, 2.5), "bois_clair", col=col)
    B.boite("fen_bas", (1.3, 0.2, 0.07), (fx, 2.52, 1.13), "bois_clair", col=col)
    for k in (-1, 1):
        B.boite(f"fen_cote{k}", (0.09, 0.1, 1.3), (fx + k * 0.55, 2.56, 1.2), "bois_clair", col=col)
        B.boite(f"rideau{k}", (0.22, 0.06, 1.5), (fx + k * 0.69, 2.5, 1.1), "tenture_bleue", col=col)
    B.boite("fen_croisee_v", (0.05, 0.06, 1.3), (fx, 2.56, 1.2), "bois_clair", col=col)
    B.boite("fen_croisee_h", (1.0, 0.06, 0.05), (fx, 2.56, 1.85), "bois_clair", col=col)
    B.boite("tringle", (1.7, 0.04, 0.04), (fx, 2.5, 2.62), "laiton", col=col)
    B.cylindre("pot_rebord", 0.08, 0.13, (fx - 0.3, 2.48, 1.2), "email_bleu", r2=0.1, seg=12, col=col)
    B.sphere("plante_rebord", (0.13, 0.1, 0.14), (fx - 0.3, 2.48, 1.42), "feuillage", seg=10, col=col)
    B.cylindre("bougeoir", 0.05, 0.03, (fx + 0.3, 2.48, 1.2), "laiton", seg=10, col=col)
    B.cylindre("bougie", 0.022, 0.16, (fx + 0.3, 2.48, 1.23), "email", seg=8, col=col)
    B.sphere("flamme_bougie", (0.02, 0.02, 0.04), (fx + 0.3, 2.48, 1.43), "flamme", seg=8, col=col, ombre=False)
    B.lampe("bougie_L", (fx + 0.3, 2.3, 1.5), energie=8.0, rayon=0.15)
    # le mur du fond est MEUBLÉ : un rayonnage du mur de gauche à la fenêtre, une tenture violette à droite de la fenêtre
    rayonnage("rayonnage", -3.25, 0.22, 2.42)
    rnd = random.Random(11)                                             # sur la corniche du rayonnage : des silhouettes variées, pas de bande de mur nue au-dessus
    for i in range(9):
        x = -3.0 + 0.36 * i + rnd.uniform(-0.05, 0.05)
        sorte = i % 4
        if sorte == 0:
            B.cylindre(f"corniche_pot{i}", 0.09, 0.2, (x, 2.42, 2.17), "email_bleu", r2=0.12, seg=12, col=col)
        elif sorte == 1:
            B.cylindre(f"corniche_bouteille{i}", 0.045, 0.24, (x, 2.42, 2.17), "bois_peint", seg=10, col=col)
            B.cylindre(f"corniche_goulot{i}", 0.018, 0.12, (x, 2.42, 2.41), "bois_peint", seg=8, col=col)
        elif sorte == 2:
            B.boite(f"corniche_boite{i}", (0.24, 0.2, 0.16), (x, 2.42, 2.17), "tissu_jaune", col=col)
        else:
            B.cylindre(f"corniche_plat{i}", 0.15, 0.03, (x, 2.5, 2.34), "email", seg=16, rot=(rad(80), 0, 0), col=col)
    B.globe("veilleuse", 0.055, (-0.55, 2.3, 1.62), "abat_jour", energie=14.0, rayon=0.2, col=col)      # une source secondaire, floue, dans le fond
    tenture("tenture_fond", 2.35, 2.56, 0.5, 2.5, 0.7)
    B.boite("applique_fond_socle", (0.1, 0.05, 0.16), (1.92, 2.57, 2.0), "laiton", col=col)
    B.globe("applique_fond", 0.06, (1.92, 2.47, 2.12), "abat_jour", energie=16.0, rayon=0.2, col=col)
    # le poêle, à gauche, devant le rayonnage : fonte, braise visible par une porte RONDE, tuyau, bûches, seau
    B.cylindre("poele", 0.36, 0.95, (-1.75, 1.7, 0.1), "fonte", seg=20, col=col)
    B.cylindre("poele_socle", 0.42, 0.1, (-1.75, 1.7, 0), "fonte", seg=20, col=col)
    B.cylindre("poele_chapeau", 0.4, 0.07, (-1.75, 1.7, 1.05), "fonte", seg=20, col=col)
    B.cylindre("poele_porte", 0.12, 0.05, (-1.75, 1.36, 0.5), "braise", seg=16, rot=(rad(90), 0, 0), col=col, ombre=False)
    B.cylindre("tuyau", 0.09, 2.1, (-1.75, 1.9, 1.1), "fonte", seg=12, col=col)
    B.lampe("poele_L", (-1.75, 1.0, 0.5), energie=40.0, rayon=0.3)
    for i in range(5):
        B.cylindre(f"buche{i}", 0.07, 0.42, (-2.55 + 0.15 * (i % 3), 1.45 + 0.02 * i, 0.07 + 0.13 * (i // 3)), "bois_clair", seg=8, rot=(rad(90), 0, rad(6 * i)), col=col)
    B.cylindre("seau", 0.15, 0.3, (-1.15, 1.95, 0), "laiton", r2=0.19, seg=14, col=col)
    # la table, à droite derrière le personnage, sous la lampe principale : plateau garni d'un côté, bois nu de l'autre
    table("table", 0.86, 1.35, 0.9, 0.7, 0.78)
    B.boite("nappe", (0.3, 0.72, 0.012), (1.13, 1.35, 0.78), "tissu_rouge", col=col)
    B.cylindre("bol", 0.1, 0.07, (1.06, 1.2, 0.792), "email", r2=0.13, seg=14, col=col)
    B.cylindre("tasse", 0.045, 0.09, (1.18, 1.42, 0.792), "email_bleu", seg=12, col=col)
    B.cylindre("pichet", 0.065, 0.2, (1.16, 1.6, 0.792), "email", r2=0.05, seg=12, col=col)
    for i in range(3):
        B.boite(f"lettre{i}", (0.18, 0.12, 0.006), (1.0 + 0.02 * i, 1.52 - 0.02 * i, 0.792 + 0.006 * i), "papier", rot=(0, 0, rad(-12 + 14 * i)), col=col)
    # dans le plan du sujet, NETS comme lui : un tabouret et sa tasse à sa droite, un panier à sa gauche, une pelote à ses pieds
    tabouret("tabouret1", 0.84, 0.12)
    B.cylindre("tasse_tabouret", 0.045, 0.09, (0.86, 0.1, 0.46), "email", seg=12, col=col)
    B.boite("lettre_tabouret", (0.16, 0.11, 0.006), (0.8, 0.16, 0.46), "papier", rot=(0, 0, rad(24)), col=col)
    tabouret("tabouret2", 2.75, 1.0)
    suspension("suspension", LAMPE[0], LAMPE[1], LAMPE[2])
    # le mur de droite : tenture, cadre, patères, ciré, et une applique à globe
    tenture("tenture_droite", 3.27, 1.7, 0.4, 2.45, 0.9, axe="y")
    B.boite("cadre_droit_bord", (0.03, 0.5, 0.62), (3.28, 0.45, 1.35), "bois", col=col)
    B.boite("cadre_droit_image", (0.02, 0.42, 0.54), (3.26, 0.45, 1.39), "carte", col=col)
    B.boite("applique_socle", (0.05, 0.1, 0.16), (3.27, -0.45, 1.85), "laiton", col=col)
    B.globe("applique_globe", 0.09, (3.17, -0.45, 1.98), "abat_jour", energie=30.0, rayon=0.25, col=col)
    for i in range(3):
        B.cylindre(f"patere{i}", 0.018, 0.1, (3.2, -1.2 - 0.2 * i, 1.72), "laiton", seg=8, rot=(0, rad(90), 0), col=col)
    B.boite("cire_jaune", (0.07, 0.3, 0.75), (3.2, -1.4, 0.95), "tissu_jaune", col=col)
    # au sol : tapis, panier, corde lovée, pelotes, balai, coffre
    B.boite("tapis", (1.4, 1.2, 0.015), (0.86, 1.35, 0), "tapis", col=col, ombre=False)      # sous la table : le sol reste clair sous les pieds du personnage, son ombre s'y lit
    B.cylindre("panier", 0.2, 0.24, (-0.35, 0.45, 0), "corde", r2=0.25, seg=14, col=col)      # jamais devant les pieds : il cacherait l'ombre, qui doit se lire
    B.sphere("linge", (0.2, 0.2, 0.1), (-0.35, 0.45, 0.26), "email", seg=10, col=col)
    for i in range(4):
        B.cylindre(f"corde{i}", 0.2 - 0.02 * i, 0.045, (-1.25, 0.35, 0.045 * i), "corde", seg=16, col=col)
    B.sphere("pelote", 0.07, (0.62, -0.28, 0.07), "tissu_rouge", seg=10, col=col)
    B.sphere("pelote2", 0.05, (-0.45, -0.95, 0.05), "tissu_jaune", seg=10, col=col)
    B.cylindre("balai_manche", 0.016, 1.4, (-2.9, 2.2, 0.1), "bois_clair", seg=6, rot=(rad(-6), 0, 0), col=col)
    B.boite("balai_brosse", (0.3, 0.06, 0.14), (-2.9, 2.25, 0), "corde", col=col)
    B.boite("coffre", (0.9, 0.5, 0.45), (-2.7, 0.2, 0), "bois_peint", col=col)
    B.boite("coffre_couvercle", (0.94, 0.54, 0.06), (-2.7, 0.2, 0.45), "bois", col=col)


# ====================================================================== l'extérieur : la cour du phare, au couchant
def cour():
    col, y0 = "COUR", F.Y
    B.boite("sol_cour", (160.0, 100.0, 0.2), (0, y0 - 10.0, -0.2), "sable", col="SOL")      # il s'arrête avant l'autre lieu : deux sols à la même hauteur se mélangent au rendu
    # la tour, loin derrière, à contre-jour
    B.cylindre("tour", 1.9, 13.0, (5.2, y0 - 19.0, 0), "tour", r2=1.35, seg=28, col=col)
    B.cylindre("tour_galerie", 1.9, 0.25, (5.2, y0 - 19.0, 13.0), "metal_sombre", seg=28, col=col)
    for i in range(10):
        a = i * math.pi / 5
        B.cylindre(f"tour_garde{i}", 0.03, 0.8, (5.2 + 1.8 * math.cos(a), y0 - 19.0 + 1.8 * math.sin(a), 13.25), "metal_sombre", seg=6, col=col)
    B.cylindre("tour_lanterne", 1.0, 1.6, (5.2, y0 - 19.0, 13.25), "lanterne", seg=16, col=col, ombre=False)
    B.cylindre("tour_dome", 1.15, 0.9, (5.2, y0 - 19.0, 14.85), "metal_sombre", r2=0.1, seg=16, col=col)
    B.boite("tour_porte", (0.8, 0.1, 1.7), (5.2, y0 - 17.1, 0), "volet", col=col)
    for i, z in enumerate((3.2, 6.6, 10.0)):
        B.boite(f"tour_fenetre{i}", (0.45, 0.1, 0.7), (5.2, y0 - 19.0 + 1.9 - 0.04 * z, z), "fenetre_chaude", col=col, ombre=False)
    # la maison de la gardienne, à gauche
    hx, hy = -4.6, y0 - 11.5
    B.boite("maison_socle", (5.4, 4.4, 0.7), (hx, hy, 0), "pierre", col=col)
    B.boite("maison", (5.2, 4.2, 2.3), (hx, hy, 0.7), "crepi", col=col)
    B.toit("maison_toit", (5.9, 4.9, 1.7), (hx, hy, 3.0), "tuile", rot=(0, 0, rad(90)), col=col)
    B.boite("cheminee", (0.5, 0.5, 1.3), (hx - 1.4, hy, 3.4), "pierre", col=col)
    B.boite("porte_maison", (0.9, 0.1, 1.9), (hx + 1.3, hy + 2.12, 0.1), "volet", col=col)
    B.boite("marche", (1.3, 0.5, 0.18), (hx + 1.3, hy + 2.4, 0), "pierre", col=col)
    for i, dx in enumerate((-1.5, -0.2)):
        B.boite(f"fen_maison{i}", (0.7, 0.08, 0.8), (hx + dx, hy + 2.12, 1.35), "fenetre_chaude", col=col, ombre=False)
        B.boite(f"fen_maison_app{i}", (0.9, 0.16, 0.08), (hx + dx, hy + 2.16, 1.28), "pierre", col=col)
        for k in (-1, 1):
            B.boite(f"volet{i}{k}", (0.34, 0.06, 0.86), (hx + dx + k * 0.54, hy + 2.14, 1.33), "volet", col=col)
    B.lampe("maison_L", (hx - 0.8, hy + 2.8, 1.6), energie=60.0, rayon=0.4)
    # le muret, de part et d'autre du sentier
    for i in range(9):
        for k, x0 in ((-1, -2.0), (1, 2.6)):
            B.boite(f"muret{k}_{i}", (1.05, 0.42, 0.62 + 0.06 * ((i * 7) % 3)), (x0 + k * 1.02 * i, y0 - 6.5 + 0.05 * ((i * 5) % 3), 0), "pierre", col=col)
    for k, x0 in ((-1, -1.45), (1, 2.05)):
        B.boite(f"pilier{k}", (0.5, 0.5, 1.15), (x0, y0 - 6.5, 0), "pierre", col=col)
        B.sphere(f"pilier_boule{k}", 0.2, (x0, y0 - 6.5, 1.3), "pierre", seg=12, col=col)
    # la barrière de pieux et de corde, à gauche du sentier
    for i in range(7):
        B.cylindre(f"pieu{i}", 0.07, 0.95, (-1.5 - 0.05 * i, y0 - 5.2 + 1.5 * i, 0), "bois", seg=8, rot=(rad(3 * ((i * 3) % 3 - 1)), 0, 0), col=col)
        if i:
            B.cylindre(f"corde_b{i}", 0.02, 1.52, (-1.5 - 0.05 * i, y0 - 5.2 + 1.5 * i, 0.72), "corde", seg=6, rot=(rad(93), 0, 0), col=col)
    # le réverbère : la source de lumière visible
    B.cylindre("reverbere", 0.06, 2.6, (2.1, y0 - 3.4, 0), "metal_sombre", seg=8, col=col)
    B.boite("reverbere_bras", (0.5, 0.05, 0.05), (1.9, y0 - 3.4, 2.55), "metal_sombre", col=col)
    B.globe("reverbere_lanterne", 0.15, (1.7, y0 - 3.4, 2.34), "lanterne", col=col)      # une lampe est RONDE : son halo est un disque
    B.boite("reverbere_toit", (0.3, 0.3, 0.06), (1.7, y0 - 3.4, 2.5), "metal_sombre", col=col)
    B.lampe("reverbere_L", (1.7, y0 - 3.2, 2.0), energie=90.0, rayon=0.4)
    # la barque retournée, les caisses, les bouées, le banc, les casiers
    B.sphere("barque", (0.75, 2.0, 0.55), (-2.9, y0 - 2.6, 0.0), "coque", seg=18, rot=(0, 0, rad(24)), col=col)
    B.boite("barque_quille", (0.07, 3.6, 0.1), (-2.9, y0 - 2.6, 0.5), "bois", rot=(0, 0, rad(24)), col=col)
    caisse("caisse1", 2.6, y0 - 1.6, 0, 0.6, 12); caisse("caisse2", 3.25, y0 - 1.9, 0, 0.55, -8); caisse("caisse3", 2.85, y0 - 1.75, 0.5, 0.5, 30)
    caisse("caisse4", 3.4, y0 - 4.6, 0, 0.7, 20)
    for i, (x, y, r) in enumerate(((1.9, y0 - 1.2, 0.2), (2.3, y0 - 0.5, 0.16), (-1.9, y0 - 0.3, 0.18), (3.9, y0 - 2.9, 0.22))):
        B.sphere(f"bouee{i}", r, (x, y, r * 0.9), "bouee", seg=12, col=col)
        B.cylindre(f"bouee_anneau{i}", r * 0.25, r * 0.3, (x, y, r * 1.8), "metal_sombre", seg=8, col=col)
    B.boite("banc_assise", (1.5, 0.4, 0.07), (-3.4, y0 - 6.0, 0.42), "bois_clair", col=col)
    for k in (-1, 1):
        B.boite(f"banc_pied{k}", (0.1, 0.36, 0.42), (-3.4 + k * 0.6, y0 - 6.0, 0), "bois", col=col)
    for i in range(3):
        B.boite(f"casier{i}", (0.7, 0.5, 0.4), (4.4 + 0.1 * i, y0 - 5.9 + 0.05 * i, 0.4 * i), "bois_clair", rot=(0, 0, rad(8 * i)), col=col)
    for i in range(3):
        B.cylindre(f"corde_sol{i}", 0.26 - 0.03 * i, 0.06, (-0.9, y0 - 1.9, 0.06 * i), "corde", seg=16, col=col)
    for i, (x, y) in enumerate(((-0.4, y0 - 6.5), (1.0, y0 - 6.5))):
        B.cylindre(f"bitte{i}", 0.11, 0.42, (x, y + 1.6, 0), "metal_sombre", r2=0.14, seg=10, col=col)
    # le plan moyen : des objets nets près du sujet, de part et d'autre du sentier (un fond tout flou fait « autocollant »)
    caisse("caisse5", -0.75, y0 + 0.2, 0, 0.42, -14)
    B.sphere("bouee4", 0.15, (-0.55, y0 + 0.95, 0.135), "bouee", seg=12, col=col)
    B.cylindre("bitte2", 0.09, 0.36, (1.35, y0 + 0.5, 0), "metal_sombre", r2=0.12, seg=10, col=col)
    for i in range(3):
        B.cylindre(f"corde_sol_b{i}", 0.2 - 0.03 * i, 0.05, (1.5, y0 - 0.7, 0.05 * i), "corde", seg=14, col=col)
    B.boite("planche_sol", (0.16, 1.1, 0.04), (-0.95, y0 - 1.0, 0), "bois_clair", rot=(0, 0, rad(28)), col=col)
    B.cylindre("seau_cour", 0.13, 0.26, (1.25, y0 - 2.0, 0), "metal_sombre", r2=0.16, seg=12, col=col)
    B.cylindre("mat", 0.05, 4.2, (-0.9, y0 - 8.6, 0), "bois_clair", seg=8, col=col)
    B.boite("fanion", (0.75, 0.03, 0.45), (-0.5, y0 - 8.6, 3.6), "tissu_rouge", col=col)
    # arbres bas derrière la maison et le muret
    for i, (x, y, r) in enumerate(((-8.2, y0 - 13.5, 1.9), (-1.2, y0 - 15.5, 1.5), (9.6, y0 - 14.0, 2.1), (1.6, y0 - 23.0, 1.7), (-6.5, y0 - 21.0, 2.3))):
        B.cylindre(f"tronc{i}", 0.2, 1.6, (x, y, 0), "bois", seg=8, col=col)
        B.sphere(f"houppier{i}", (r, r, r * 0.8), (x, y, 1.4 + r * 0.7), "feuillage", seg=12, col=col)
    # finitions au sol : cailloux (5 à 11 par D² près du sujet) et touffes ; le sentier reste dégagé sous les pieds
    libre = [(0.3, y0 + 1.5, 0.28), (0.25, y0 - 2.5, 0.2), (-0.75, y0 + 0.2, 0.4), (-0.55, y0 + 0.95, 0.2), (1.35, y0 + 0.5, 0.15), (1.5, y0 - 0.7, 0.25), (1.25, y0 - 2.0, 0.2)]
    B.semer("caillou", 520, (-3.2, y0 - 6.0, 3.8, y0 + 4.6), ("caillou", "caillou2"), graine=3, eviter=libre)
    B.semer("caillou_loin", 160, (-9.0, y0 - 16.0, 10.0, y0 - 6.8), ("caillou", "caillou2"), taille=(1.2, 4.0), graine=4)
    B.touffes("touffe", 46, (-3.4, y0 - 6.0, 4.0, y0 + 4.4), "herbe", graine=5, eviter=[(0.3, y0 - 1.0, 1.1), (0.3, y0 + 1.5, 1.0), (0.6, y0 + 3.6, 0.9)])


def construire():
    B.init()
    B.soleil(F.SOLEIL)                       # avant les matières : sa direction y est inscrite
    matieres()
    cuisine()
    cour()
    B.fond((0, F.Y / 2, 0))
    B.orienter_fil(("bois", "bois_clair", "bois_peint"))
    B.fusionner(("INTERIEUR", "COUR", "SOL"))
    B.camera_film()
    B.enregistrer(BLEND)


if args[0] == "construire":
    construire()
else:
    B.rendre(F, RAC / "passes", int(args[1]) if len(args) > 1 else 100, args[2] if len(args) > 2 else "tout")
