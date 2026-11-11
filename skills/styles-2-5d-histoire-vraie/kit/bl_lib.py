"""Bibliothèque de construction 2.5D pour Blender (4.2 ou plus récent ; essayée en 5.3).

Ce fichier ne contient RIEN de propre à un film : géométrie simple, matières, lumière motivée, personnages
plats en plans émissifs avec ombre de contact, une caméra par plan liée à un repère, réglages de rendu par
profil, contrôles (cadre, glissements). Le film lui-même s'écrit dans `bl_film.py`.

PASSE = 1 : formes en argile grise + caméras ; 2 : + lumière ; 3 : + matières, habillage, profondeur de champ.
"""
import bpy, bmesh, math, json, pathlib, sys
from mathutils import Vector
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R

PASSE = 3
rad = math.radians
G_TERRE = 9.81


# ------------------------------------------------------------------ bases
def reset():
    """Vide TOUT le fichier Blender courant. À n'appeler que dans le fichier du film, jamais dans une scène du client."""
    s = bpy.context.scene
    for m in list(s.timeline_markers):
        s.timeline_markers.remove(m)
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.lights,
                 bpy.data.cameras, bpy.data.images, bpy.data.actions, bpy.data.collections, bpy.data.worlds):
        for b in list(coll):
            coll.remove(b)
    MATS.clear()
    CAMS.clear()


def COL(nom):
    c = bpy.data.collections.get(nom)
    if not c:
        c = bpy.data.collections.new(nom)
        bpy.context.scene.collection.children.link(c)
    return c


def fcurves(idb):
    """Courbes d'animation d'un bloc, quelle que soit la version (actions à emplacements depuis 4.4)."""
    ad = idb.animation_data
    if not ad or not ad.action:
        return []
    act = ad.action
    if hasattr(act, "layers") and getattr(ad, "action_slot", None) is not None:
        out = []
        for layer in act.layers:
            for strip in layer.strips:
                cb = strip.channelbag(ad.action_slot)
                if cb:
                    out += list(cb.fcurves)
        return out
    return list(getattr(act, "fcurves", []))


def K(o, chemin, f, v=None, interp="BEZIER", idx=-1):
    """Pose une clé à l'image f. `interp` règle le trajet de CETTE clé vers la suivante :
    BEZIER (accélère puis ralentit), LINEAR (vitesse constante), CONSTANT (tenue jusqu'à la clé suivante)."""
    if v is not None:
        if idx >= 0:
            o.path_resolve(chemin)[idx] = v
        elif "." in chemin:
            pre, attr = chemin.rsplit(".", 1)
            setattr(o.path_resolve(pre), attr, v)
        else:
            setattr(o, chemin, v)
    o.keyframe_insert(chemin, frame=f, index=idx)
    for fc in fcurves(o):
        if fc.data_path == chemin and (idx < 0 or fc.array_index == idx):
            for kp in fc.keyframe_points:
                if abs(kp.co.x - f) < 1e-3:
                    kp.interpolation = interp


# ------------------------------------------------------------------ géométrie
def _finir(nom, bm, col, mat, loc=(0, 0, 0), rot=(0, 0, 0), ech=(1, 1, 1), parent=None, lisse=False, ombre=True):
    me = bpy.data.meshes.new(nom)
    bm.to_mesh(me)
    bm.free()
    if lisse:
        for p in me.polygons:
            p.use_smooth = True
    if mat:
        me.materials.append(M(mat) if isinstance(mat, str) else mat)
    o = bpy.data.objects.new(nom, me)
    o.location, o.rotation_euler, o.scale = loc, rot, ech
    if parent:
        o.parent = parent
    o.visible_shadow = ombre
    COL(col).objects.link(o)
    return o


def _biseau(bm, largeur, segments=2):
    if largeur > 0:
        bmesh.ops.bevel(bm, geom=list(bm.edges), offset=largeur, segments=segments, affect="EDGES", profile=0.5)


def boite(nom, taille, loc, col, mat, biseau=0.012, rot=(0, 0, 0), parent=None, ombre=True):
    """Boîte de dimensions `taille` (x, y, z), posée sur z = loc.z (l'origine est au centre de la base)."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=taille, verts=bm.verts)
    bmesh.ops.translate(bm, vec=(0, 0, taille[2] / 2), verts=bm.verts)
    _biseau(bm, biseau)          # aucune arête parfaitement vive : elle ne prendrait pas la lumière
    return _finir(nom, bm, col, mat, loc, rot, parent=parent, ombre=ombre)


def cylindre(nom, r, h, loc, col, mat, r2=None, seg=32, rot=(0, 0, 0), parent=None, ombre=True, biseau=0.0):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r if r2 is None else r2, depth=h)
    bmesh.ops.translate(bm, vec=(0, 0, h / 2), verts=bm.verts)
    _biseau(bm, biseau)
    return _finir(nom, bm, col, mat, loc, rot, parent=parent, lisse=True, ombre=ombre)


def sphere(nom, r, loc, col, mat, parent=None, ombre=True, seg=24):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=r)
    return _finir(nom, bm, col, mat, loc, parent=parent, lisse=True, ombre=ombre)


def tour(nom, profil, loc, col, mat, seg=48, parent=None, ombre=True):
    """Objet tourné (vase, cloche, bol) : `profil` = [(rayon, hauteur), …] du bas vers le haut."""
    bm = bmesh.new()
    n = len(profil)
    anneaux = []
    for r, z in profil:
        anneaux.append([bm.verts.new((r * math.cos(2 * math.pi * i / seg), r * math.sin(2 * math.pi * i / seg), z)) for i in range(seg)])
    for a in range(n - 1):
        for i in range(seg):
            j = (i + 1) % seg
            bm.faces.new((anneaux[a][i], anneaux[a][j], anneaux[a + 1][j], anneaux[a + 1][i]))
    for bout, sens in ((anneaux[0], -1), (anneaux[-1], 1)):
        if bout[0].co.xy.length > 1e-6:
            bm.faces.new(bout[::sens])
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finir(nom, bm, col, mat, loc, parent=parent, lisse=True, ombre=ombre)


def vide(nom, col, loc=(0, 0, 0), rot=(0, 0, 0), parent=None):
    o = bpy.data.objects.new(nom, None)
    o.empty_display_size = 0.1
    o.location, o.rotation_euler = loc, rot
    if parent:
        o.parent = parent
    COL(col).objects.link(o)
    return o


# ------------------------------------------------------------------ lumière motivée
def lumiere(nom, genre, loc, energie, couleur, col, rot=(0, 0, 0), taille=0.2, ombre=True, sx=None, sy=None):
    """genre : SUN (soleil), AREA (fenêtre, porte), POINT (bougie, lampe), SPOT. Rien en passe 1.
    Chaque lumière doit avoir une raison dans le décor ; pas d'éclairage de studio à trois points."""
    if PASSE < 2:
        return None
    d = bpy.data.lights.new(nom, genre)
    d.energy, d.color, d.use_shadow = energie, couleur, ombre
    if genre == "AREA":
        d.shape = "RECTANGLE"
        d.size, d.size_y = sx or taille, sy or taille
    elif genre == "SUN":
        d.angle = taille
    else:
        d.shadow_soft_size = taille
        portee = R.PROFILS[R.PROFIL]["portee_lumieres"]
        if portee:                       # portée limitée : moins de lumières à calculer par pixel (carte intégrée)
            d.use_custom_distance = True
            d.cutoff_distance = portee
    o = bpy.data.objects.new(nom, d)
    o.location, o.rotation_euler = loc, rot
    COL(col).objects.link(o)
    return o


def vacille(lampe, a, b, base, pas=2):
    """Vacillement d'une flamme entre les images a et b : plusieurs sinus, jamais régulier (± 6 à 10 %)."""
    if lampe is None:
        return
    for f in range(a, b, pas):
        k = 1 + 0.06 * math.sin(f * 0.61) * math.sin(f * 0.23) + 0.03 * math.sin(f * 1.7)
        K(lampe.data, "energy", f, base * k, "LINEAR")


# ------------------------------------------------------------------ matières
MATS = {}


def _mat(nom):
    m = bpy.data.materials.new(nom)
    if hasattr(m, "use_nodes") and not m.node_tree:
        m.use_nodes = True
    return m, m.node_tree.nodes, m.node_tree.links


def _vider(n):
    for x in list(n):
        if x.type != "OUTPUT_MATERIAL":
            n.remove(x)
    return next(x for x in n if x.type == "OUTPUT_MATERIAL")


def _prise(noeud, ident, sortie=False):
    return next(s for s in (noeud.outputs if sortie else noeud.inputs) if s.identifier == ident)


def matiere(nom, couleur, rugosite=0.6, metal=0.0, variation=0.25, grain=5.0, relief=0.0, couleur2=None):
    """Matière procédurale avec variation : jamais une couleur parfaitement propre.
    En passe 1 et 2, toutes les matières sont remplacées par une argile grise (on juge les formes, puis la lumière)."""
    if nom in MATS:
        return MATS[nom]
    m, n, l = _mat(nom)
    b = next(x for x in n if x.type == "BSDF_PRINCIPLED")
    if PASSE < 3:
        b.inputs["Base Color"].default_value = (0.42, 0.41, 0.40, 1)
        b.inputs["Roughness"].default_value = 0.85
        MATS[nom] = m
        return m
    b.inputs["Metallic"].default_value = metal
    tc = n.new("ShaderNodeTexCoord")
    br = n.new("ShaderNodeTexNoise")
    br.inputs["Scale"].default_value = grain
    br.inputs["Detail"].default_value = 3
    l.new(tc.outputs["Object"], br.inputs["Vector"])
    mx = n.new("ShaderNodeMix")
    mx.data_type = "RGBA"
    _prise(mx, "A_Color").default_value = (*couleur, 1)
    _prise(mx, "B_Color").default_value = (*(couleur2 or tuple(c * (1 - variation) for c in couleur)), 1)
    l.new(br.outputs["Fac"], _prise(mx, "Factor_Float"))
    l.new(_prise(mx, "Result_Color", True), b.inputs["Base Color"])
    mr = n.new("ShaderNodeMapRange")
    mr.inputs["To Min"].default_value, mr.inputs["To Max"].default_value = max(0.02, rugosite - 0.12), min(1, rugosite + 0.18)
    l.new(br.outputs["Fac"], mr.inputs["Value"])
    l.new(mr.outputs["Result"], b.inputs["Roughness"])
    if relief:
        bn = n.new("ShaderNodeBump")
        bn.inputs["Strength"].default_value = relief
        l.new(br.outputs["Fac"], bn.inputs["Height"])
        l.new(bn.outputs["Normal"], b.inputs["Normal"])
    MATS[nom] = m
    return m


def emissif(nom, couleur, force=1.0):
    """Aplat lumineux : ciel derrière une fenêtre, flamme, braise. Visible dès la passe 2."""
    if nom in MATS:
        return MATS[nom]
    m, n, l = _mat(nom)
    out = _vider(n)
    e = n.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = (*couleur, 1)
    e.inputs["Strength"].default_value = force if PASSE >= 2 else 0.0
    l.new(e.outputs[0], out.inputs["Surface"])
    MATS[nom] = m
    return m


def M(nom):
    if nom not in MATS:
        raise KeyError(f"matière « {nom} » non déclarée : appeler matiere() ou emissif() avant de l'utiliser")
    return MATS[nom]


def mat_ombre():
    """Ombre de contact : disque noir à bord doux, posé au sol sous chaque personnage. Ne dépend d'aucune lumière."""
    if "ombre_contact" in MATS:
        return MATS["ombre_contact"]
    m, n, l = _mat("ombre_contact")
    out = _vider(n)
    tc = n.new("ShaderNodeTexCoord")
    vm = n.new("ShaderNodeVectorMath")
    vm.operation = "DISTANCE"
    vm.inputs[1].default_value = (0.5, 0.5, 0.0)
    l.new(tc.outputs["UV"], vm.inputs[0])
    mr = n.new("ShaderNodeMapRange")
    mr.interpolation_type = "SMOOTHSTEP"
    mr.inputs["From Min"].default_value, mr.inputs["From Max"].default_value = 0.12, 0.5
    mr.inputs["To Min"].default_value, mr.inputs["To Max"].default_value = 0.78, 0.0
    l.new(vm.outputs["Value"], mr.inputs["Value"])
    d = n.new("ShaderNodeBsdfDiffuse")
    d.inputs["Color"].default_value = (0, 0, 0, 1)
    t = n.new("ShaderNodeBsdfTransparent")
    ms = n.new("ShaderNodeMixShader")
    l.new(mr.outputs["Result"], ms.inputs[0])
    l.new(t.outputs[0], ms.inputs[1])
    l.new(d.outputs[0], ms.inputs[2])
    l.new(ms.outputs[0], out.inputs["Surface"])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    else:
        m.blend_method = "BLEND"
    MATS["ombre_contact"] = m
    return m


def mat_plat(img):
    """Aplat émissif découpé par la transparence de l'image : la lumière du décor ne l'ombre jamais."""
    nom = "plat_" + img.name
    if nom in bpy.data.materials:
        return bpy.data.materials[nom]
    m, n, l = _mat(nom)
    out = _vider(n)
    tx = n.new("ShaderNodeTexImage")
    tx.image = img
    tx.extension = "CLIP"
    e = n.new("ShaderNodeEmission")
    e.inputs["Strength"].default_value = 1.0          # force 1 : la couleur du dessin, ni plus ni moins
    t = n.new("ShaderNodeBsdfTransparent")
    seuil = n.new("ShaderNodeMath")
    seuil.operation = "GREATER_THAN"
    seuil.inputs[1].default_value = 0.5
    ms = n.new("ShaderNodeMixShader")
    l.new(tx.outputs["Color"], e.inputs["Color"])
    l.new(tx.outputs["Alpha"], seuil.inputs[0])
    l.new(seuil.outputs[0], ms.inputs[0])
    l.new(t.outputs[0], ms.inputs[1])
    l.new(e.outputs[0], ms.inputs[2])
    l.new(ms.outputs[0], out.inputs["Surface"])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "DITHERED"
    else:
        m.blend_method = "HASHED"
    m.use_backface_culling = False
    return m


# ------------------------------------------------------------------ personnages : plans émissifs + ombre de contact
_RIG = None
PROFONDEUR = {"jambes": 0.0, "corps": -0.004, "tete": -0.008, "visage": -0.012, "bras_g": -0.016, "bras_d": -0.016}


def rig():
    global _RIG
    if _RIG is None:
        f = R.PERSONNAGES / "rig.json"
        if not f.exists():
            raise SystemExit("personnages/rig.json absent : lancer d'abord  python outils/personnages.py")
        _RIG = json.loads(f.read_text(encoding="utf-8"))
    return _RIG


def _image(rel):
    p = R.PERSONNAGES / "png" / rel
    cle = p.parent.name + "_" + p.name
    im = bpy.data.images.get(cle)
    if not im:
        im = bpy.data.images.load(str(p))
        im.name = cle
    return im


def _plan(nom, rel, boite_, pivot, k, col, parent, loc):
    """Plan texturé dont l'origine est le pivot de la pièce (x vers la droite, z vers le haut, face tournée vers −Y)."""
    x0, y0, x1, y1 = boite_
    px, py = pivot
    bm = bmesh.new()
    vs = [bm.verts.new(((x - px) * k, 0, (py - y) * k)) for x, y in ((x0, y1), (x1, y1), (x1, y0), (x0, y0))]
    f = bm.faces.new(vs)
    uv = bm.loops.layers.uv.new()
    for lp, t in zip(f.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
        lp[uv].uv = t
    return _finir(nom, bm, col, mat_plat(_image(rel)), loc, parent=parent, ombre=False)


class Perso:
    """Pantin plat : racine (pieds) > tronc > corps, bras, cou > tête + visage (yeux, bouches, extras échangés image
    par image). Rangé hors champ tant qu'on ne l'a pas placé. Une vue = une entrée de rig.json : le kit ne fournit
    que la vue de face ; une autre vue se déclare comme un second personnage qu'on échange à une coupe."""
    RANGE = (0, 0, -60)
    COLLECTION = "PERSONNAGES"

    def __init__(s, nom, etiquette=None):
        g = rig()
        d = g["persos"][nom]
        sol = g["sol_y"]
        s.nom = etiquette or nom
        s.h = d["h"]
        s.k = k = d["h"] / (sol - d["haut_y"])            # mètres par unité de dessin
        c, n = s.COLLECTION, "P_" + s.nom
        s.racine = vide(n, c, s.RANGE)
        s.tronc = vide(n + "_tronc", c, parent=s.racine)
        P = d["pieces"]
        ou = lambda piv, prof: ((piv[0] - g["toile"][0] / 2) * k, prof, (sol - piv[1]) * k)
        s.jambes = _plan(n + "_jambes", f"{nom}/jambes.png", P["jambes"]["boite"], P["jambes"]["pivot"], k, c, s.racine, ou(P["jambes"]["pivot"], PROFONDEUR["jambes"]))
        s.corps = _plan(n + "_corps", f"{nom}/corps.png", P["corps"]["boite"], P["corps"]["pivot"], k, c, s.tronc, ou(P["corps"]["pivot"], PROFONDEUR["corps"]))
        s.bras = {b: _plan(n + "_" + b, f"{nom}/{b}.png", P[b]["boite"], P[b]["pivot"], k, c, s.tronc, ou(P[b]["pivot"], PROFONDEUR[b]))
                  for b in ("bras_g", "bras_d")}
        cou = P["tete"]["pivot"]
        s.cou = vide(n + "_cou", c, ou(cou, 0), parent=s.tronc)
        s.tete = _plan(n + "_tete", f"{nom}/tete.png", P["tete"]["boite"], cou, k, c, s.cou, (0, PROFONDEUR["tete"], 0))
        s.visage_obj = vide(n + "_visage", c, (0, PROFONDEUR["visage"], 0), parent=s.cou)
        s.visages = {}
        # visages : ceux du personnage s'il a les siens (autre vue : profil, dos sans visage), sinon les visages communs
        visages = d["visages"] if "visages" in d else g["visages"]
        dossier = d.get("dossier_visages", "_visages")
        for cle, fd in visages.items():
            o = _plan(f"{n}_{cle}", f"{dossier}/{cle}.png", fd["boite"], cou, k, c, s.visage_obj, (0, -0.001 if cle.startswith("extra") else 0, 0))
            o.hide_render = o.hide_viewport = True
            s.visages[cle] = o
        bm = bmesh.new()
        f = bm.faces.new([bm.verts.new(p) for p in ((-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0))])
        uv = bm.loops.layers.uv.new()
        for lp, t in zip(f.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
            lp[uv].uv = t
        s.ombre = _finir(n + "_ombre", bm, c, mat_ombre(), (0, 0.03, 0.006), ech=(0.30 * s.h, 0.15 * s.h, 1), parent=s.racine, ombre=False)
        s.courant = {"yeux": None, "bouche": None, "extra": None}
        s._cles = set()

    # --- placement
    def place(s, f, x, y, z=0.0, vers=None, lacet=None, echelle=1.0, miroir=False):
        """Pose le personnage à l'image f (clés tenues). `vers` = point (la caméra) vers lequel le plan se tourne,
        autour de l'axe vertical seulement. `miroir` retourne le dessin gauche-droite (un profil qui regarde de
        l'autre côté) : à ne changer qu'à une coupe."""
        if vers is not None:
            d = Vector((vers[0] - x, vers[1] - y))
            lacet = math.atan2(d.x, -d.y)
        for i, v in enumerate((x, y, z)):
            K(s.racine, "location", f, v, "CONSTANT", i)
        K(s.racine, "rotation_euler", f, lacet or 0.0, "CONSTANT", 2)
        for i in range(3):
            K(s.racine, "scale", f, -echelle if (miroir and i == 0) else echelle, "CONSTANT", i)

    def range_(s, f):
        """Sort le personnage du film à partir de l'image f."""
        for i, v in enumerate(s.RANGE):
            K(s.racine, "location", f, v, "CONSTANT", i)

    def deplace(s, f0, f1, x=None, y=None, interp="LINEAR"):
        """Déplacement de f0 à f1, PUIS TENUE : la clé d'arrivée est en CONSTANT. Sans cette tenue, le personnage
        continue de glisser vers sa position du plan suivant (défaut trouvé par la critique du 11/11/2026)."""
        if x is not None:
            K(s.racine, "location", f0, None, interp, 0)
            K(s.racine, "location", f1, x, "CONSTANT", 0)
        if y is not None:
            K(s.racine, "location", f0, None, interp, 1)
            K(s.racine, "location", f1, y, "CONSTANT", 1)

    # --- visage : remplacement d'images, comme en animation par substitution
    def _echange(s, f, fam, cle):
        ancien = s.courant[fam]
        if ancien == cle:
            return
        for nm, cache in ((ancien, True), (cle, False)):
            if nm is None:
                continue
            o = s.visages[f"{fam}_{nm}"]
            if o.name not in s._cles and f > 0:
                o.hide_render = o.hide_viewport = True
                o.keyframe_insert("hide_render", frame=0)
                o.keyframe_insert("hide_viewport", frame=0)
            s._cles.add(o.name)
            o.hide_render = o.hide_viewport = cache
            o.keyframe_insert("hide_render", frame=f)
            o.keyframe_insert("hide_viewport", frame=f)
        s.courant[fam] = cle

    def visage(s, f, yeux=None, bouche=None, extra=0):
        """Change les yeux, la bouche ou l'extra à l'image f. extra=None retire l'extra ; 0 n'y touche pas."""
        if yeux:
            s._echange(f, "yeux", yeux)
        if bouche:
            s._echange(f, "bouche", bouche)
        if extra != 0:
            s._echange(f, "extra", extra)

    def cligne(s, f, retour="neutre"):
        s.visage(f, "fermes")
        s.visage(f + 3, retour)

    # --- pose
    def bras_(s, f, g=None, d=None, interp="BEZIER"):
        """Élévation du bras vers l'extérieur, en degrés (0 = le long du corps, 90 = à l'horizontale, 170 = levé).
        g = bras à gauche de l'image, d = bras à droite."""
        if g is not None:
            K(s.bras["bras_g"], "rotation_euler", f, rad(g), interp, 1)
        if d is not None:
            K(s.bras["bras_d"], "rotation_euler", f, rad(-d), interp, 1)

    def tete_(s, f, incl=None, dx=None, dy=None, interp="BEZIER"):
        """incl : inclinaison de la tête en degrés (+ = vers la droite de l'image). dx, dy : décalage du visage en
        unités de dessin (le visage glisse sur la tête : c'est le seul « regard » possible avec une vue de face)."""
        if incl is not None:
            K(s.cou, "rotation_euler", f, rad(incl), interp, 1)
        if dx is not None:
            K(s.visage_obj, "location", f, dx * s.k, interp, 0)
        if dy is not None:
            K(s.visage_obj, "location", f, -dy * s.k, interp, 2)

    def tronc_(s, f, incl=None, dz=None, interp="BEZIER"):
        if incl is not None:
            K(s.tronc, "rotation_euler", f, rad(incl), interp, 1)
        if dz is not None:
            K(s.tronc, "location", f, dz, interp, 2)

    def neutre(s, f):
        """Remet la pose à zéro (clés tenues). À appeler au début de chaque plan où le personnage apparaît."""
        s.bras_(f, 0, 0, "CONSTANT")
        s.tete_(f, 0, 0, 0, "CONSTANT")
        s.tronc_(f, 0, 0, "CONSTANT")

    def geste(s, f, cible, de, a, anticipation=0.18):
        """Geste calé sur l'image f : anticipation (léger recul) de f−4 à f, action en 5 images, puis TENUE.
        cible : "g", "d" (bras), "tete", "tronc". Aucun rebond."""
        fn = {"g": lambda fr, v, i: s.bras_(fr, g=v, interp=i), "d": lambda fr, v, i: s.bras_(fr, d=v, interp=i),
              "tete": lambda fr, v, i: s.tete_(fr, incl=v, interp=i), "tronc": lambda fr, v, i: s.tronc_(fr, incl=v, interp=i)}[cible]
        fn(f - 4, de, "BEZIER")
        fn(f, de - (a - de) * anticipation, "BEZIER")
        fn(f + 5, a, "CONSTANT")

    def marche(s, f0, f1, amplitude=0.035, pas=6):
        """Petit rebond du tronc pendant un déplacement (un appui tous les `pas` images). Ce n'est PAS un cycle de
        marche : les jambes ne bougent pas. À garder pour un personnage petit dans le cadre ou coupé à la taille."""
        f, haut = f0, False
        while f <= f1:
            s.tronc_(f, dz=amplitude if haut else 0.0)
            haut = not haut
            f += pas // 2
        s.tronc_(f1 + 2, dz=0.0, interp="CONSTANT")


# ------------------------------------------------------------------ caméras : une par plan
CAMS = {}


def camera(pid, a, b, cles, focale=35, ouverture=2.8, point=None, secousse=None):
    """Caméra du plan `pid`, active de l'image a à b (b exclue), liée à un repère de la ligne de temps.
    cles = [(t entre 0 et 1, position, point visé), …] ; trajet à vitesse constante entre les clés (pas de dérive).
    point = position de mise au point (défaut : le point visé). secousse = (force, image début, image fin)."""
    d = bpy.data.cameras.new(f"CAM_{pid:02d}")
    d.lens = focale
    d.clip_start, d.clip_end = 0.05, 1000
    d.sensor_fit = "VERTICAL"
    d.sensor_height = 36
    o = bpy.data.objects.new(f"CAM_{pid:02d}", d)
    COL("CAMERAS").objects.link(o)
    prec = None
    for t, loc, vise in cles:
        f = round(a + t * (b - 1 - a))
        loc, vise = Vector(loc), Vector(vise)
        q = (vise - loc).to_track_quat("-Z", "Y")
        e = q.to_euler("XYZ", prec) if prec else q.to_euler("XYZ")
        prec = e
        o.location, o.rotation_euler = loc, e
        if len(cles) > 1:
            for i in range(3):
                K(o, "location", f, None, "LINEAR", i)
                K(o, "rotation_euler", f, None, "LINEAR", i)
        if PASSE >= 3 and ouverture:
            d.dof.use_dof = True
            d.dof.aperture_fstop = ouverture
            d.dof.focus_distance = ((Vector(point) if point is not None else vise) - loc).length
            if len(cles) > 1:
                K(d, "dof.focus_distance", f, None, "LINEAR")
    if secousse:                       # secousse motivée par l'histoire, limitée au plan
        force, f0, f1 = secousse
        for fc in fcurves(o):
            if fc.data_path == "rotation_euler":
                m = fc.modifiers.new("NOISE")
                m.scale, m.strength, m.phase, m.blend_type = 1.6, force, fc.array_index * 37.0, "ADD"
                m.use_restricted_range = True
                m.frame_start, m.frame_end = f0, f1
                m.blend_in, m.blend_out = 3, 8
    mk = bpy.context.scene.timeline_markers.new(f"P{pid:02d}", frame=a)
    mk.camera = o
    CAMS[pid] = o
    return o


# ------------------------------------------------------------------ objets : chute réelle
def chute(obj, f_depart, z0, z1, ips=None):
    """Chute libre de z0 à z1 (mètres) à partir de l'image f_depart : une clé par image, gravité réelle, pas de
    rebond. Renvoie l'image du contact (y poser le son). 30 cm = environ 7 images à 30 i/s."""
    ips = ips or R.IPS
    K(obj, "location", f_depart, z0, "LINEAR", 2)
    f = f_depart
    while True:
        f += 1
        z = z0 - 0.5 * G_TERRE * ((f - f_depart) / ips) ** 2
        if z <= z1:
            K(obj, "location", f, z1, "CONSTANT", 2)
            return f
        K(obj, "location", f, z, "LINEAR", 2)


# ------------------------------------------------------------------ réglages de rendu
def _regle(o, attr, v):
    try:
        setattr(o, attr, v)
        return True
    except Exception as ex:
        print(f"réglage ignoré ({attr}) : {ex}")
        return False


def reglages_rendu(total, profil=None):
    """Format, moteur et échantillons selon le profil de `reglages.py`. Renvoie le monde (fond)."""
    p = R.PROFILS[profil or R.PROFIL]
    s = bpy.context.scene
    if p["moteur"] == "CYCLES":
        s.render.engine = "CYCLES"
        _regle(s.cycles, "device", "CPU")
        _regle(s.cycles, "samples", p["echantillons"])
        _regle(s.cycles, "use_adaptive_sampling", False)
        _regle(s.cycles, "use_denoising", True)
    else:
        for nom in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):      # le nom d'EEVEE dépend de la version
            try:
                s.render.engine = nom
                break
            except TypeError:
                pass
        e = s.eevee
        _regle(e, "taa_render_samples", p["echantillons"])
        _regle(e, "use_raytracing", False)
        _regle(e, "use_shadows", True)
        _regle(e, "shadow_resolution_scale", p["ombres"])
        _regle(e, "volumetric_tile_size", "8")
        _regle(e, "volumetric_samples", 64)
        _regle(e, "use_volumetric_shadows", True)
        _regle(e, "use_bokeh_jittered", False)
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = R.LARGEUR, R.HAUTEUR, 100
    s.render.fps, s.render.fps_base = R.IPS, 1.0
    s.frame_start, s.frame_end = 0, total - 1
    s.render.use_motion_blur = False
    _regle(s.view_settings, "view_transform", R.VUE)     # « Standard » : les aplats sortent à la couleur du dessin
    _regle(s.view_settings, "look", "None")
    s.render.image_settings.file_format = "JPEG" if R.EXT == "jpg" else "PNG"
    if R.EXT == "jpg":
        s.render.image_settings.quality = R.QUALITE_JPEG
    s.render.image_settings.color_mode = "RGB"
    s.render.use_file_extension = True
    s.render.use_overwrite = False        # un rendu relancé saute les images déjà faites : reprise après plantage
    s.render.use_placeholder = False
    s.render.filepath = str(R.RENDUS / R.PREFIXE)
    w = bpy.data.worlds.new("MONDE")
    if hasattr(w, "use_nodes") and not w.node_tree:
        w.use_nodes = True
    bg = next(x for x in w.node_tree.nodes if x.type == "BACKGROUND")
    # passe 1 : aucune lampe, c'est le fond gris qui éclaire l'argile ; ensuite, un fond sombre que le décor règle
    bg.inputs[0].default_value = (0.02, 0.02, 0.03, 1) if PASSE >= 2 else (0.6, 0.6, 0.6, 1)
    bg.inputs[1].default_value = 1.0
    s.world = w
    return w


# ------------------------------------------------------------------ contrôles
def cadre(cam, objets, image):
    """Où tombent ces objets dans l'image du plan ? Renvoie (gauche, haut, droite, bas) en fractions de l'image
    (0 = bord gauche / haut, 1 = bord droit / bas), d'après les boîtes englobantes."""
    from bpy_extras.object_utils import world_to_camera_view
    s = bpy.context.scene
    s.frame_set(image)
    xs, ys = [], []
    for o in objets:
        if o.type != "MESH":
            continue
        for coin in o.bound_box:
            v = world_to_camera_view(s, cam, o.matrix_world @ Vector(coin))
            xs.append(v.x)
            ys.append(1 - v.y)
    return min(xs), min(ys), max(xs), max(ys)


def controle_sujet(pid, objets, image, nom="sujet"):
    """Règle du rendu réel : le sujet tient dans les 65 % du haut (au-dessus de la bande des sous-titres) et dans
    la zone utile. Renvoie True si c'est le cas, et imprime la mesure."""
    g, h, d, b = cadre(CAMS[pid], objets, image)
    ok = b <= R.SUJET_BAS_MAX and h >= 160 / R.HAUTEUR and d <= 945 / R.LARGEUR and g >= 60 / R.LARGEUR
    print(f"cadre plan {pid:02d} image {image} [{nom}] : x {g * R.LARGEUR:.0f} à {d * R.LARGEUR:.0f}, y {h * R.HAUTEUR:.0f} à {b * R.HAUTEUR:.0f}"
          f" ; bas à {b:.0%} de la hauteur (limite {R.SUJET_BAS_MAX:.0%}) : {'ok' if ok else 'À REVOIR'}")
    return ok


def controle_glissements(debuts_de_plan):
    """Cherche le défaut « le personnage glisse vers sa position du plan suivant » : une clé de position non tenue
    juste avant un changement de plan. Renvoie la liste des problèmes (vide = bon)."""
    pb = []
    debuts = set(debuts_de_plan)
    for o in COL(Perso.COLLECTION).objects:
        for fc in fcurves(o):
            if fc.data_path != "location":
                continue
            kps = sorted(fc.keyframe_points, key=lambda k: k.co.x)
            for k0, k1 in zip(kps, kps[1:]):
                if round(k1.co.x) in debuts and k0.interpolation != "CONSTANT" and abs(k0.co.y - k1.co.y) > 1e-4:
                    pb.append(f"{o.name} (axe {'xyz'[fc.array_index]}) : clé de l'image {k0.co.x:.0f} non tenue, "
                              f"glisse de {k0.co.y:.2f} à {k1.co.y:.2f} jusqu'au plan qui commence à {k1.co.x:.0f}")
    return pb
