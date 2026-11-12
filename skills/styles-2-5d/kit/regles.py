"""Les règles chiffrées du style « tête ronde, trait plein et délié », en données.

C'est le prompt maître (references/prompt-maitre.md) sous forme de constantes : pantin.py, bl_decor.py, compo.py et
controle.py ne contiennent aucun chiffre de style, ils lisent celui-ci. Bibliothèque standard seulement (lu aussi dans Blender).

Unité : D = diamètre de la tête d'un personnage. Toutes les longueurs de style sont en fraction de D : c'est ce qui les
rend justes à toute taille de plan. Les valeurs viennent de mesures au pixel du studio ; « essaye » dit si l'ambiance a
été refaite et contrôlée chez nous (True) ou seulement mesurée (False : à vérifier par un contrôle chiffré avant de livrer).
"""
LARGEUR, HAUTEUR, IPS = 1080, 1920, 30
D_MONDE = 0.52              # diamètre de la tête, en mètres dans la scène 3D (personnage de 1,65 m environ = 3,2 D)
D_DESSIN = 300.0            # le même diamètre, en unités du dessin vectoriel des personnages
PROF_MAX = 150.0            # profondeur codée dans la passe de données ; au-delà = ciel

# ------------------------------------------------------------------ personnages : trait
CONTOUR = dict(
    a0=0.0452,              # épaisseur moyenne du contour (tête, torse). Loi mesurée : 0,044 D − 0,028 D × cos(angle depuis la lumière)
    h1=0.0288,              # amplitude : délié ≈ 0,017 D côté lumière, plein ≈ 0,072 D côté ombre (réglé pour retomber sur la loi une fois l'image lissée)
    membres=0.056,          # bras et jambes : trait constant, 0,054 à 0,061 D mesuré
    visage=0.0235,          # traits fins du visage (anneau de l'œil, bouche, paupière) : 0,021 à 0,025 D
    coiffe=0.032,           # contour des coiffes et accessoires : régulier, 0,029 à 0,035 D
    detail=0.030,           # petits détails à trait constant
)
TETE = dict(
    ovale=0.018,            # tête légèrement irrégulière : petit axe / grand axe 0,91 à 0,98 (ici ≈ 0,96)
    croissant=0.24,         # croissant d'ombre : la peau claire est le disque décalé de 0,24 rayon vers la lumière (≈ 20 % du disque à l'ombre)
    croissant_flou=0.02,    # écart type du bord doux, en D (transition 10–90 % mesurée : 0,05 à 0,13 D)
    filet=0.021,            # filet de lumière : 0,013 à 0,022 D de large, à 0,033 D du trait, effilé aux deux bouts
    degrade=0.30,           # la peau claire s'assombrit de 30 % du chemin vers le croissant du côté ombre (7 niveaux mesurés)
)
TORSE = dict(ombre_part=0.20,   # ombre propre : une bande de 16 à 21 % de la surface, le long du bord éclairé
             filet=0.022, filet_retrait=0.034)
ACCENTUATION = 70           # masque flou de rayon 1 px sur l'image finale, en % : donne ±16 niveaux sur 1 px de part et d'autre du trait

# ------------------------------------------------------------------ ambiances
# encre / membres : couleur du trait ; peau, croissant, filet : tête ; filet_torse ; joue ; jambe_ar : jambe du second plan (éclaircie vers le décor)
# ombre_sol : ombre du personnage. ("projetee", teinte, force du mélange, flou du bord en D, longueur) ou ("tache", teinte, force, flou en D)
# decor : lois de lumière du décor (voir compo.py).
AMBIANCES = {
    "jour": dict(
        essaye=False,
        encre="#2d2336", membres="#3a3357", peau="#fcf7f2", croissant="#ede4ef", filet="#ffffff", filet_op=0.9, filet_torse=None, joue="#f7b9a0", jambe_ar="#937f89",
        ombre_sol=("projetee", "#4664b8", 0.72, 0.064, 0.5),
        decor=dict(encre="#2f2030", ombre=("#4664b8", 0.72, 0.60), lumiere=(1.0, 0.98, 0.94), sol=(1.0, 1.0, 1.0),
                   brume=("#b9c4dc", 0.30, 14.0, 70.0), lampe=(1.0, 0.85, 0.6), force_lampe=0.0, bords=(0.30, None), contraste_local=0.28,
                   ciel=[(0.0, "#a8daff"), (6.0, "#84caff"), (16.0, "#5db3ff"), (32.0, "#3f9dff"), (55.0, "#1f8af8")],
                   soleil=None, nuages=("#f1f5fc", "#f1f5fc"), collines=(("#e6b7a6", 0.85), ("#d09a8c", 0.9)))),
    "soir": dict(
        essaye=True,
        encre="#301c2c", membres="#2c1a29", peau="#ffe4bb", croissant="#f4c49b", filet="#febd67", filet_op=0.85, filet_torse="#ff9d4c", joue="#f59b78", jambe_ar="#7d6a80",
        ombre_sol=("projetee", "#202d6c", 0.87, 0.036, 1.0),
        decor=dict(encre="#301c2c", ombre=("#202d6c", 0.87, 0.70), lumiere=(1.0, 0.92, 0.78), sol=(1.13, 1.17, 1.24),
                   brume=("#f4aa66", 0.24, 14.0, 70.0), lampe=(1.0, 0.74, 0.42), force_lampe=0.55, bords=(0.36, None), contraste_local=0.28,
                   ciel=[(0.0, "#ffb771"), (4.0, "#f3ae72"), (8.0, "#c29c9c"), (13.0, "#8a92b9"), (30.0, "#6a80b9"), (55.0, "#4968b2")],
                   soleil=("#fff0c4", "#ffd08a"), nuages=("#f6b98a", "#9c97bb"), collines=(("#d99a78", 0.85), ("#b9788a", 0.9)))),
    "interieur": dict(
        essaye=True,
        encre="#2b1623", membres="#2b1623", peau="#fddab3", croissant="#f2beac", filet="#fee9c9", filet_op=0.8, filet_torse="#ff9d4c", joue="#f59b78", jambe_ar="#6b4a55",
        ombre_sol=("tache", "#1c0d24", 0.55, 0.085),      # sans lampe déclarée (clé source du plan) ; avec : INTERIEUR["ombre"]
        # penombre : (teinte, part du mélange, facteur) hors des flaques ; k_lampe, gamma_lampe : étendue et netteté du bord des flaques ;
        # creux : les ombres d'occlusion virent au bleu de nuit ; lointain : le fond vire au violet ; halo_froid : lueur des fenêtres froides
        decor=dict(encre="#2b1623", penombre=("#251023", 0.70, 0.58), lumiere=(1.06, 0.90, 0.74), soleil_entrant=(1.04, 0.86, 0.62),
                   k_lampe=0.085, gamma_lampe=2.0, creux=("#312e79", 0.45), lointain=("#503056", 0.34, 3.2, 5.0),
                   halo_chaud=(0.85, 1.25), halo_froid=(0.16, 0.42), bords=(0.66, "#251023"), contraste_local=0.24)),
    "nuit": dict(
        essaye=False,
        encre="#241731", membres="#1a1436", peau="#ffe2bc", croissant="#f2cfbc", filet="#fec47c", filet_op=1.0, filet_torse="#ff9d4c", joue="#e9a79a", jambe_ar="#4a4577",
        ombre_sol=("tache", "#160f38", 0.60, 0.20),
        decor=dict(encre="#1a1436", lisere="#2048d2", ombre=("#070e2e", 0.60, 0.50), lumiere=(0.55, 0.62, 1.0), sol=(0.6, 0.6, 0.95),
                   brume=("#272d5f", 0.35, 8.0, 40.0), lampe=(1.0, 0.8, 0.6), force_lampe=0.9, bords=(0.40, "#070e2e"), contraste_local=0.20,
                   ciel=[(0.0, "#031c9f"), (10.0, "#031992"), (22.0, "#01157e"), (38.0, "#021368"), (55.0, "#030e53")],
                   soleil=None, nuages=None, collines=(("#0e248e", 0.8), ("#0c154d", 0.9)))),
}

# ------------------------------------------------------------------ décor
DECOR = dict(
    silhouette=0.030,       # contour des objets sur leur silhouette : 0,02 à 0,034 D
    arete=0.012,            # arêtes intérieures : 0,009 D mesuré ; 0,012 pour rester visible une fois l'image encodée
    planche=0.32,           # largeur d'une lame de plancher ou d'une planche de mur : 0,32 à 0,33 D
    joint=0.021,            # épaisseur d'un joint : 0,016 à 0,024 D ; 11 à 17 niveaux plus sombre que le bois
    clin=0.16,              # clin de façade, lambris bas
    caillou=0.03,           # diamètre médian des cailloux ; 5 à 11 par D² autour du sujet
    touffe=(0.25, 0.5),     # touffes d'herbe : une tous les 2 à 3 D
    occlusion=(0.15, 0.25), # bande sombre au pied des murs et sous les meubles
    face_ombre=0.72,        # face d'un volume tournée à l'opposé de la lumière = 0,72 × la face éclairée
    penombre=(0.07, 0.14, 0.5),   # bord flou d'une ombre portée : au contact, à mi-longueur, au bout d'une ombre longue (en D)
    soleil_deg=3.5,         # diamètre apparent du soleil (bl_decor.soleil) : bord 10–90 % ≈ 0,75 × distance à l'objet × angle, soit 0,5 D à 11 D
    lisere_loin=(8.0, 17.0),      # le liseré peint des cailloux s'efface entre 8 et 17 D de la caméra (au-delà il ferait un point noir)
)
# ------------------------------------------------------------------ bois dessiné (bl_decor.NT.bois_dessine) : veines, cernes, nœuds
BOIS = dict(
    veine=0.060,            # écart moyen entre deux veines, en D ; trait d'une veine : 0,013 D (4 px pour D = 315 px)
    trait=0.013,
    onde=(2.4, 0.30, 1.3),  # ondulation des veines : longueur d'onde le long du fil (D), cohérence en travers (D), amplitude (en veines)
    noeud=(2.6, 0.9, 0.12, 2.6, 0.45),   # nœuds : un par cellule de 2,6 D (fil) × 0,9 D (travers), rayon 0,12 cellule, déviation des veines (en veines), part des cellules sans nœud
    grain=(3.0, 0.35),      # fil fin : 3 fois plus serré que les veines, force 0,35
    contraste=(18.0, 21.0), # cible mesurée : écart type d'une pièce de bois nette et éclairée, en niveaux
    grain_fin=(8.5, 12.7),  # cible mesurée : écart type du détail fin (1 à 2 px)
    plancher=(18.0, 0.32),  # plancher : contraste, un joint tous les 0,32 D
)
# ------------------------------------------------------------------ intérieur sombre à touches froides (mesures d'une ambiance « intérieur chaud »)
INTERIEUR = dict(
    luminance=(61.0, 15.0),         # luminance moyenne de l'image : cible, tolérance
    saturation=(0.58, 0.08),        # saturation moyenne (TSV) : cible, tolérance
    prune=("#251023", "#3a1828"), part_prune=(0.48, 0.12),       # prune très sombre : près de la moitié de l'image
    brun_sombre="#592227",          # passage entre le prune et la dominante chaude (12 % mesuré)
    chaud=("#7b3120", "#9f4723"), part_chaud=(0.20, 0.08),       # UNE dominante chaude, des bruns-rouges moyens : un cinquième de l'image, pas une salle toute brune
    froid=("#503056", "#312e79"), part_froid=(0.06, 0.09),       # contrepoint froid OBLIGATOIRE (bornes) : violet et bleu de nuit, par les fenêtres et dans les ombres
    clairs=("#fdd8bc", "#d7adb3", "#dd8f47"),                    # peaux, lampes, reflets : 10 % environ
    # personnage posé en intérieur, quand le plan donne la lampe principale (clé source=(x, y, z) du plan)
    ombre=dict(teinte="#26112f", force=0.84, flou=(0.03, 0.10), longueur=(0.7, 1.0), fin=0.70, contact=1.0),   # ombre projetée à l'opposé de la lampe, prune : flou au contact / au bout (D), longueur mini / maxi (D), opacité au bout, ombre de contact sous chaque pied
    lisere=dict(teinte="#ffae5c", retrait=0.012, largeur=0.055, force=0.72),     # liseré de lumière chaud sur le bord du personnage, côté lampe (D) : un mélange vers l'orangé, lisible aussi sur la peau
    particules=dict(n=10, rayon=(0.006, 0.013), teinte="#ffd9a0", force=0.5, derive=0.035),   # quelques points clairs flottants : rayon en D, dérive en D par seconde
    accord=dict(teinte=(0.95, 0.89, 0.86), bas=0.22, clairs=(165.0, 235.0, 0.85)),   # accord à la pièce ; au-dessus de 165 à 235 de luminance, la teinte est retirée à 85 % : les blancs restent blancs
)
# ------------------------------------------------------------------ ce qui entre dans le champ (controle.py)
CHAMP = dict(
    fenetre=0.35,           # un pixel du décor est « plat » si la luminance varie de moins de `seuil` niveaux dans une fenêtre de 0,35 D autour de lui
    seuil=6.0,
    marge=0.5,              # zone examinée : la tête et le torse du personnage, élargis de 0,5 D
    plat_max=0.35,          # part de pixels plats admise derrière la tête et le torse : au-delà, le mur est nu
    bord_px=3,              # aucun pixel du personnage à moins de 3 px du bord gauche, droit ou haut du cadre
    coupes_max=2,           # silhouettes d'objets du décor coupées par le bord gauche ou droit, dans la zone nette
)
OPTIQUE = dict(
    focale=25.0,            # mm, pour un capteur de 36 mm dans la HAUTEUR (champ vertical de 71°) ; 33 à 62 mm pour les plans serrés
    hauteur_camera=1.9,     # en D au-dessus du sol : l'horizon coupe le personnage debout entre la hanche et la poitrine
    horizon=(0.50, 0.58),   # ligne d'horizon, en fraction de la hauteur de l'image, sur un plan large
    flou=0.055,             # écart type du flou = 0,055 D × |distance du point / distance de l'objet − 1| ; le fond lointain sort à 0,14 D (bord 10–90 %)
    net_devant=0.45, net_derriere=0.10, flou_max=0.085,     # zone nette autour du sujet : le sol reste NET sous les pieds jusqu'au bas de l'image
)

# ------------------------------------------------------------------ sous-titres
SOUS_TITRES = dict(
    y_centre=1350,          # 70 % de la hauteur : dans la zone utile du plugin (160 à 1560), sur les jambes en plan en pied serré
    corps=78,               # px : capitales de 55 px environ (2,8 % de la hauteur)
    polices=("Montserrat-Black.ttf", "Montserrat-ExtraBold.ttf", "seguibl.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"),
    couleur=(255, 255, 255), contour=(20, 14, 20), contour_px=6, ombre=(4, 5),
    mots_max=3,             # 1 à 2 mots, 3 au plus ; apparition et disparition sèches
)

# ------------------------------------------------------------------ jeu : durées en images (30 i/s)
JEU = dict(
    changement_de_pose=1, anticipation=2, depassement=3, retour=4, accent_tete=3,
    clignement=3, entre_deux_clignements=(13, 25), tenue_avant_geste=(13, 46), stupeur_tenue=39,
    chute=14, tenue_apres_chute=75, pas_de_marche=11, pas_presse=(5, 6),
    action_apres_le_mot=(2, 4), reaction_en_cascade=6,
)
CAMERA = dict(depart=2, freinage=(9, 10), deplacement=(9, 64), fondu=(6, 11), station=33, derive_px_s=(20, 30))

# ------------------------------------------------------------------ contrôles avant livraison : tolérances
TOLERANCES = dict(
    epaisseur_px=1.0,       # contours, traits
    delta_e=6.0,            # couleurs (encre, ombre)
    angle_deg=15.0,         # côté du plein par rapport à l'opposé de la lumière
    delie_D=(0.012, 0.026), plein_D=(0.058, 0.082),      # bornes de la loi du contour, mesurée sur l'image finale
    membres_D=(0.050, 0.064),
    joints_D=(0.26, 0.39),  # espacement des joints de planches : 0,32 D ± 20 %
    contraste_matiere=(8.0, 26.0),   # écart type d'une matière dessinée, en niveaux (bois, plancher) ; un aplat fait moins de 3
    sol_net_px=3.3,         # largeur des transitions du sol sous les pieds : 2,0 à 2,3 px mesuré, ± 1 px
    fond_flou_D=(0.105, 0.175),      # bord 10–90 % d'une arête du fond lointain : 0,14 D ± 25 %
    silhouette_D=(0.016, 0.040),
    petits_segments=(84, 250),       # densité : 112 à 202 petits segments par image, ± 25 %
    bois_contraste=(12.0, 27.0),     # écart type d'une pièce de bois nette et éclairée : 18 à 21 mesuré, ± 6
    ombre_interieur=(0.35, 0.80),    # ombre d'un personnage en intérieur : luminance de l'ombre / luminance du sol éclairé voisin (au-dessus de 0,8 elle ne se lit pas)
)


def hexa(h):
    """'#rrvvbb' -> (r, v, b) de 0 à 255."""
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def melange(c1, c2, t):
    """Mélange de deux couleurs hexadécimales : t = 0 -> c1, t = 1 -> c2."""
    a, b = hexa(c1), hexa(c2)
    return "#" + "".join(f"{int(round(x + (y - x) * t)):02x}" for x, y in zip(a, b))

# ------------------------------------------------------------------ rendu rapide : une plaque de décor par plan (plaque.py)
# parallaxe = de combien un objet proche glisse par rapport au lointain entre la pose de la plaque et la pose la plus éloignée, en px
PLAQUE = dict(
    seuil_plaque_px=12.0,   # jusque-là : une plaque recadrée par homographie (mesuré : écart de 0,5 à 0,7 niveau sur 255 à 14–18 px, 1,4 à 2,9 à 40–50 px)
    seuil_couches_px=120.0, # jusque-là : la plaque déplacée pixel par pixel selon sa profondeur (mesuré : 0,13 à 0,52 niveau jusqu'à 112 px, soit le
                            # bruit d'un second rendu ; à 307 px : 0,9 en moyenne mais des étirements locaux visibles) ; au-delà : 3D image par image
    marge=0.04,             # marge de champ autour du mouvement
    echelle_max=2.0,        # la plaque fait au plus 2 fois la taille du cadre (4 fois les pixels)
)
