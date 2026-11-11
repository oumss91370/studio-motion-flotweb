"""Le film : construit toute la scène (décor, objet héros, personnages, caméras, animation) et l'enregistre.

  python outils/rendre.py --construire              # le plus simple : trouve Blender tout seul
  blender -b --python outils/bl_film.py -- --passe 3   # ou directement, avec le programme Blender
  python outils/bl_film.py -- --passe 3                # ou avec le module Python bpy

  --passe 1   formes en argile + caméras        (on juge l'échelle et les cadres)
  --passe 2   + lumière motivée                 (on juge la lumière seule)
  --passe 3   + matières, habillage, flou       (défaut)

Tout le film est UNE scène : la ligne de temps de Blender est le film (image 0 = première image), une caméra par
plan liée à un repère. Une correction devient un numéro d'image, et on ne re-rend que les images touchées.
Plusieurs décors : les construire loin les uns des autres dans la même scène (par exemple à x = 0, 400, −400).

EXEMPLE NEUTRE À REMPLACER (tout ce qui est sous « LE FILM ») : un atelier, une sonnette, un personnage, 2 plans.
Le script vide le fichier Blender courant : ne jamais l'exécuter dans une scène où il y a autre chose.
"""
import bpy, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans
import bl_lib as L

args = R.arguments()
L.PASSE = int(args[args.index("--passe") + 1]) if "--passe" in args else 3
PL = plans.PLANS
rad = math.radians

L.reset()
MONDE = L.reglages_rendu(plans.TOTAL)

# =================================================================== LE FILM (exemple à remplacer)
# ------------------------------------------------------------------ matières (passe 3 ; argile grise avant)
L.matiere("plancher", (0.30, 0.19, 0.11), rugosite=0.7, grain=9.0, relief=0.15)
L.matiere("mur", (0.62, 0.56, 0.47), rugosite=0.9, grain=3.0, variation=0.18)
L.matiere("bois", (0.36, 0.22, 0.12), rugosite=0.55, grain=14.0, relief=0.1)
L.matiere("bois_sombre", (0.13, 0.08, 0.05), rugosite=0.5, grain=10.0)
L.matiere("laiton", (0.78, 0.57, 0.22), rugosite=0.28, metal=1.0, grain=22.0, couleur2=(0.42, 0.30, 0.12))
L.matiere("terre_cuite", (0.55, 0.27, 0.16), rugosite=0.8, grain=12.0)
L.emissif("ciel_fenetre", (1.0, 0.86, 0.66), 2.2)
L.emissif("flamme", (1.0, 0.55, 0.18), 12.0)

# ------------------------------------------------------------------ décor : ATELIER (caméras tournées vers +Y)
D = "DECOR"
L.boite("sol", (6, 6, 0.1), (0, 0, -0.1), D, "plancher", biseau=0)
L.boite("mur_fond", (6, 0.2, 3.2), (0, 2.1, 0), D, "mur", biseau=0)
L.boite("mur_gauche", (0.2, 6, 3.2), (-2.3, 0, 0), D, "mur", biseau=0)
L.boite("fenetre_ciel", (0.02, 1.0, 1.4), (-2.19, 0.7, 1.25), D, "ciel_fenetre", biseau=0, ombre=False)
for i, (y, z, ty, tz) in enumerate(((0.7, 1.20, 1.16, 0.08), (0.7, 2.65, 1.16, 0.08), (0.16, 1.25, 0.08, 1.4), (1.24, 1.25, 0.08, 1.4), (0.7, 1.25, 0.05, 1.4))):
    L.boite(f"fenetre_cadre{i}", (0.07, ty, tz), (-2.17, y, z), D, "bois_sombre", biseau=0.006)
L.boite("etabli_plateau", (1.5, 0.7, 0.06), (0.55, 0.6, 0.84), D, "bois")
for i, (x, y) in enumerate(((-0.12, 0.33), (1.22, 0.33), (-0.12, 0.87), (1.22, 0.87))):
    L.boite(f"etabli_pied{i}", (0.07, 0.07, 0.84), (x, y, 0), D, "bois")
if L.PASSE >= 3:                                   # habillage : petits objets, rien de parfaitement rangé
    L.boite("etagere", (1.3, 0.24, 0.045), (0.5, 1.88, 1.85), D, "bois")
    for i, (x, r, h) in enumerate(((0.05, 0.07, 0.19), (0.32, 0.10, 0.13), (0.62, 0.06, 0.24), (0.95, 0.085, 0.16))):
        L.cylindre(f"pot{i}", r, h, (x, 1.88, 1.895), D, "terre_cuite", r2=r * 0.8, biseau=0.006)
    L.boite("caisse", (0.5, 0.42, 0.36), (1.6, 1.4, 0), D, "bois_sombre", rot=(0, 0, rad(14)))
L.cylindre("lampe_pied", 0.05, 0.10, (0.74, 0.8, 0.90), D, "laiton", r2=0.03, biseau=0.004)
L.sphere("lampe_flamme", 0.022, (0.74, 0.8, 1.035), D, "flamme", ombre=False)

# lumière motivée : la fenêtre (principale, chaude de fin de journée) et la lampe (source chaude visible)
L.lumiere("lum_fenetre", "AREA", (-2.1, 0.7, 1.95), 160, (1.0, 0.85, 0.63), "LUMIERES", rot=(0, rad(-90), 0), sx=1.0, sy=1.4)
LAMPE = L.lumiere("lum_lampe", "POINT", (0.74, 0.78, 1.06), 14, (1.0, 0.60, 0.24), "LUMIERES", taille=0.03)
L.lumiere("lum_rebond", "AREA", (0.6, -1.0, 2.6), 22, (0.55, 0.65, 1.0), "LUMIERES", sx=3, sy=3, ombre=False)   # rebond froid du plafond
L.vacille(LAMPE, 0, plans.TOTAL, 14)

# ------------------------------------------------------------------ objet héros : la sonnette, en vrai 3D
H = "HEROS"
SON_POS = (0.34, 0.52, 0.90)
heros = L.vide("HEROS_racine", H, SON_POS)
L.cylindre("sonnette_socle", 0.15, 0.022, (0, 0, 0), H, "bois_sombre", parent=heros, biseau=0.005, seg=48)
cloche = L.tour("sonnette_cloche", [(0.132, 0.0), (0.134, 0.012), (0.128, 0.034), (0.108, 0.064), (0.076, 0.088), (0.04, 0.102), (0.016, 0.106)],
                (0, 0, 0.022), H, "laiton", parent=heros, seg=64)
L.cylindre("sonnette_tige", 0.014, 0.03, (0, 0, 0.126), H, "laiton", parent=heros, seg=24)
bouton = L.cylindre("sonnette_bouton", 0.026, 0.02, (0, 0, 0.156), H, "bois_sombre", parent=heros, biseau=0.004, seg=32)

# ------------------------------------------------------------------ personnages
galet = L.Perso("galet")
GALET_POS = (-0.36, 0.15)         # devant l'établi : rien du décor ne passe devant lui

# ------------------------------------------------------------------ caméras : une par plan (id, a, b de plans.py)
p1, p2 = PL[1], PL[2]
VISE1 = (0.0, 0.5, 0.40)
L.camera(1, p1["a"], p1["b"], [(0, (0.0, -4.25, 1.05), VISE1), (1, (0.0, -4.0, 1.02), VISE1)], focale=50, ouverture=2.8, point=(GALET_POS[0], GALET_POS[1], 1.0))
L.camera(2, p2["a"], p2["b"], [(0, (0.78, -0.80, 1.50), (0.34, 0.52, 0.93))], focale=60, ouverture=5.6)

# ------------------------------------------------------------------ animation, plan par plan (numéros d'image de la vidéo)
# Plan 1 : Galet regarde la sonnette, puis lève le bras. Un regard d'abord, une anticipation, une action, une tenue.
a = p1["a"]
galet.place(a, *GALET_POS, vers=(0.0, -4.1))
galet.neutre(a)
galet.visage(a, "neutre", "fermee", None)
galet.visage(a + 8, yeux="cote")                    # le regard part 10 images avant le geste
galet.tete_(a + 6, dx=0, incl=0)
galet.tete_(a + 10, dx=14, incl=4)
galet.tete_(a + 11, dx=14, incl=4, interp="CONSTANT")
galet.geste(a + 18, "d", 0, 62)                     # bras du côté de la sonnette ; tenu ensuite
galet.visage(a + 24, bouche="sourire")
galet.range_(p2["a"])                              # hors champ au plan 2 : aucun bout de personnage ne traîne dans le cadre

# Plan 2 : le bouton s'enfonce (contact à l'image 56 : c'est là que tombe le son), la cloche vibre puis se tient.
z0 = bouton.location.z
L.K(bouton, "location", p2["a"], z0, "CONSTANT", 2)
L.K(bouton, "location", 52, z0, "BEZIER", 2)
L.K(bouton, "location", 54, z0 + 0.004, "BEZIER", 2)      # anticipation
L.K(bouton, "location", 56, z0 - 0.022, "CONSTANT", 2)    # enfoncé : contact
L.K(bouton, "location", 60, z0 - 0.022, "BEZIER", 2)
L.K(bouton, "location", 64, z0, "CONSTANT", 2)
L.K(cloche, "rotation_euler", p2["a"], 0.0, "CONSTANT", 0)
for i, f in enumerate(range(56, 82, 2)):
    amorti = math.exp(-i / 4.0)
    L.K(cloche, "rotation_euler", f, rad(1.6) * amorti * (1 if i % 2 == 0 else -1), "BEZIER", 0)
L.K(cloche, "rotation_euler", 82, 0.0, "CONSTANT", 0)
# =================================================================== FIN DU FILM

# ------------------------------------------------------------------ contrôles automatiques
s = bpy.context.scene
s.frame_set(0)
s.camera = L.CAMS[1]
corps_galet = [o for o in L.COL(L.Perso.COLLECTION).objects if o.type == "MESH" and not o.hide_render and "ombre" not in o.name]
objets_heros = [o for o in L.COL(H).objects if o.type == "MESH"]
ok = L.controle_sujet(1, corps_galet + objets_heros, 20, "Galet et sonnette")
ok = L.controle_sujet(2, objets_heros, 60, "sonnette") and ok
gl = L.controle_glissements([p["a"] for p in plans.P])
for g in gl:
    print("GLISSEMENT :", g)
print(f"film construit, passe {L.PASSE} | moteur {s.render.engine} | objets {len(bpy.data.objects)} | "
      f"caméras {len(L.CAMS)} | cadres {'ok' if ok else 'À REVOIR'} | glissements {len(gl)}")

if "--sans-enregistrer" not in args:
    R.BLEND.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(R.BLEND))
    print("enregistré :", R.BLEND)
