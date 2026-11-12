"""Rend une plage d'images du film, en sautant celles qui existent déjà. Lancé par `rendre.py`, pas à la main.

  blender -b decors/film.blend --python outils/bl_plage.py -- <début> <fin> [--pct 25] [--dossier chemin] [--plantage N]

--pct      taille du rendu en pourcentage (essais seulement ; le film se rend à 100)
--plantage N   ESSAI de la reprise : le processus s'arrête brutalement après N images, comme un pilote qui plante
"""
import bpy, os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R

args = R.arguments()
A, Z = int(args[0]), int(args[1])
opt = lambda nom, defaut=None: args[args.index(nom) + 1] if nom in args else defaut
if not bpy.data.filepath:                      # lancé avec le module bpy : ouvrir le fichier soi-même
    bpy.ops.wm.open_mainfile(filepath=str(R.BLEND))
s = bpy.context.scene
dossier = pathlib.Path(opt("--dossier", R.RENDUS))
dossier.mkdir(parents=True, exist_ok=True)
s.render.resolution_percentage = int(opt("--pct", 100))
s.render.filepath = str(dossier / R.PREFIXE)
s.render.use_overwrite = False
s.render.use_placeholder = False
if opt("--profil"):                            # essai sur une autre machine que celle qui a construit la scène
    p = R.PROFILS[opt("--profil")]
    if p["moteur"] == "CYCLES":
        s.render.engine = "CYCLES"
        s.cycles.device, s.cycles.samples = "CPU", p["echantillons"]

limite, faites = int(opt("--plantage", 0)), [0]
def apres(*_):
    faites[0] += 1
    if limite and faites[0] >= limite:
        print(f"ESSAI : plantage simulé après {faites[0]} images", flush=True)
        os._exit(3)
bpy.app.handlers.render_write.append(apres)

manquantes = [i for i in range(A, Z + 1) if not R.image(i, dossier).exists()]
plages, debut = [], None                       # regrouper les images manquantes en plages continues
for i in manquantes:
    if debut is None:
        debut = prec = i
    elif i == prec + 1:
        prec = i
    else:
        plages.append((debut, prec))
        debut = prec = i
if debut is not None:
    plages.append((debut, prec))
print(f"bl_plage : {len(manquantes)} images à rendre en {len(plages)} plage(s), moteur {s.render.engine}, {s.render.resolution_percentage} %", flush=True)
for a, z in plages:
    s.frame_start, s.frame_end = a, z
    bpy.ops.render.render(animation=True)      # les repères de la ligne de temps changent la caméra tout seuls
print("bl_plage terminé", flush=True)
