"""Rendus de contrôle sans interface, à basse résolution, relus en planche (ne modifie pas film.blend).

  python outils/rendre.py --controle planche <prefixe> <pct> [milieu|debut|fin] [ids séparés par des virgules]
  python outils/rendre.py --controle images  <prefixe> <pct> <image,image,…>
  python outils/rendre.py --controle tour    <prefixe> <pct>

planche : une image par plan (au milieu, au début ou à la fin du plan)
images  : les images demandées, chacune avec la caméra de son plan
tour    : l'objet héros seul (collection HEROS) sous 6 angles, sur sol neutre, avant de le poser dans le décor

Écrit revue/tmp/<prefixe>….jpg ; assembler ensuite avec  python outils/planche.py.
On relit des RENDUS, pas la vue 3D : eux seuls montrent les plans émissifs et la profondeur de champ.
"""
import bpy, math, pathlib, sys
from mathutils import Vector
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans

args = R.arguments()
mode, prefixe, pct = args[0], args[1], int(args[2])
if not bpy.data.filepath:
    bpy.ops.wm.open_mainfile(filepath=str(R.BLEND))
s = bpy.context.scene
TMP = R.REVUE / "tmp"
TMP.mkdir(parents=True, exist_ok=True)
s.render.resolution_percentage = pct
s.render.use_overwrite = True


def rend(nom):
    import time
    s.render.filepath = str(TMP / f"{nom}.{R.EXT}")
    t = time.time()
    bpy.ops.render.render(write_still=True)
    print(f"écrit {s.render.filepath} en {time.time() - t:.2f} s/image", flush=True)


def image(n, nom):
    p = plans.plan_de(n)
    s.camera = bpy.data.objects[f"CAM_{p['id']:02d}"]      # frame_set ne suit pas les repères : on choisit la caméra
    s.frame_set(n)
    rend(nom)


if mode == "planche":
    ou = args[3] if len(args) > 3 else "milieu"
    ids = [int(x) for x in args[4].split(",")] if len(args) > 4 else sorted(plans.PLANS)
    for pid in ids:
        p = plans.PLANS[pid]
        n = {"milieu": (p["a"] + p["b"]) // 2, "debut": p["a"] + 2, "fin": p["b"] - 2}[ou]
        image(n, f"{prefixe}{pid:02d}")
elif mode == "images":
    for n in args[3].split(","):
        image(int(n), f"{prefixe}{int(n):0{R.CHIFFRES}d}")
elif mode == "tour":
    heros = [o for o in bpy.data.collections["HEROS"].all_objects]
    for o in bpy.data.objects:                 # tout cacher sauf l'objet héros (rien n'est enregistré)
        if o not in heros and o.type in ("MESH", "LIGHT"):
            o.hide_render = True
    s.frame_set(0)
    pts = [o.matrix_world @ Vector(c) for o in heros if o.type == "MESH" for c in o.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    c, t = (lo + hi) / 2, max((hi - lo).length, 0.05)

    def lampe(nom, loc, energie, couleur):
        d = bpy.data.lights.new(nom, "AREA")
        d.energy, d.color, d.size = energie, couleur, t * 1.5
        o = bpy.data.objects.new(nom, d)
        o.location = loc
        o.rotation_euler = (c - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
        s.collection.objects.link(o)
    me = bpy.data.meshes.new("tour_sol")
    k = t * 8
    me.from_pydata([(c.x - k, c.y - k, lo.z), (c.x + k, c.y - k, lo.z), (c.x + k, c.y + k, lo.z), (c.x - k, c.y + k, lo.z)], [], [(0, 1, 2, 3)])
    mat = bpy.data.materials.new("tour_sol")
    mat.diffuse_color = (0.3, 0.3, 0.3, 1)
    me.materials.append(mat)
    s.collection.objects.link(bpy.data.objects.new("tour_sol", me))
    lampe("tour_cle", c + Vector((t * 1.6, -t * 2.0, t * 2.2)), 60 * t * t, (1.0, 0.9, 0.75))
    lampe("tour_contre", c + Vector((-t * 2.0, t * 1.5, t * 1.4)), 25 * t * t, (0.6, 0.75, 1.0))
    cam = bpy.data.objects.new("CAM_TOUR", bpy.data.cameras.new("CAM_TOUR"))
    s.collection.objects.link(cam)
    cam.data.sensor_fit, cam.data.lens, cam.data.clip_start = "VERTICAL", 60, 0.01
    for m in list(s.timeline_markers):
        s.timeline_markers.remove(m)
    s.camera = cam
    d = t * 3.2
    vues = {"1-face": (0, -d, t * 0.25), "2-trois-quarts": (d * 0.7, -d * 0.7, t * 0.8), "3-cote": (-d, 0.001, t * 0.25),
            "4-dos": (0, d, t * 0.25), "5-dessus": (0.001, -0.05, d), "6-ras-du-sol": (-d * 0.6, -d * 0.6, -(c.z - lo.z) + 0.02 * t)}
    for nom, v in vues.items():
        cam.location = c + Vector(v)
        cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()
        rend(f"{prefixe}{nom}")
else:
    raise SystemExit("mode inconnu : planche, images ou tour")
print("bl_cli terminé")
