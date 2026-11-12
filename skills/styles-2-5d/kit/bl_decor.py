"""Bibliothèque Blender du décor « dessiné » : matières peintes procédurales, trois passes, fusion, rendu avec reprise.

Rien ici n'est propre à un film : le décor lui-même est dans bl_scene.py, qui importe ce fichier.

Ce que la mesure a montré, et ce que fait ce fichier :
- tout ce qui est proche est en VRAIS VOLUMES ; le ciel, le soleil, les nuages et les collines sont peints après (compo.py) ;
- les matières sont des TEXTURES DESSINÉES, jamais des aplats : planches à joints sombres tous les 0,32 D (joint de 0,02 D),
  bois dessiné (veines qui ondulent, nœuds, cernes), taches douces sur les enduits et les sols ; aucune texture photographique ;
- la lumière n'est PAS cuite dans la couleur. Trois passes par image, assemblées par compo.py selon les lois de l'ambiance :
    passes/albedo/<plan>_<image>.png   couleur peinte, sans lumière (8 bits, sRVB)
    passes/lum/…                       16 bits : R = part de soleil reçue (ombres portées douces), V = lampes, B = occlusion
    passes/data/…                      16 bits : R, V = normale en repère caméra, B = profondeur / PROF_MAX
  Régler une ambiance ne demande donc aucun nouveau rendu.
Testé avec Blender 5.3 (EEVEE). Écrit par Flot Web.
"""
import bpy, bmesh, math, pathlib, random, sys
from mathutils import Vector
sys.dont_write_bytecode = True
ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import regles as R
import camera as C
import plaque as PQ

D = R.D_MONDE
ENERGIE_SOLEIL = 2.6
VERS_SOLEIL = [0.0, 0.0, 1.0]         # fixé par soleil() : la direction du soleil est inscrite dans les matières (un seul soleil par film)
rad = math.radians


def lin(h):
    """'#rrvvbb' -> couleur linéaire pour Blender."""
    c = [v / 255 for v in R.hexa(h)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)


# ====================================================================== scène
def init(samples=16):
    """Vide le fichier, règle le moteur, le format et le monde (noir : toute la lumière vient des passes)."""
    s = bpy.context.scene
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.lights, bpy.data.cameras,
                 bpy.data.images, bpy.data.actions, bpy.data.collections, bpy.data.worlds, bpy.data.node_groups):
        for b in list(coll):
            coll.remove(b)
    for moteur in ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT"):
        try:
            s.render.engine = moteur
            break
        except TypeError:
            continue
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = R.LARGEUR, R.HAUTEUR, 100
    s.render.fps = R.IPS
    s.render.use_motion_blur = False
    e = s.eevee
    e.taa_render_samples = samples
    for attr, val in (("use_raytracing", False), ("use_shadows", True), ("use_volumetric_shadows", False), ("shadow_resolution_scale", 1.0),
                      ("shadow_ray_count", 2), ("shadow_step_count", 8), ("use_bokeh_jittered", False)):
        if hasattr(e, attr):
            setattr(e, attr, val)
    s.view_settings.view_transform = "Standard"
    try:
        s.view_settings.look = "None"
    except TypeError:
        pass
    im = s.render.image_settings
    im.file_format, im.color_mode, im.compression = "PNG", "RGB", 15
    s.render.use_overwrite = True
    w = bpy.data.worlds.new("MONDE")
    try:
        w.use_nodes = True
    except Exception:
        pass
    bg = next(x for x in w.node_tree.nodes if x.type == "BACKGROUND")
    bg.inputs[0].default_value = (0, 0, 0, 1)
    bg.inputs[1].default_value = 0.0
    s.world = w


def collection(nom):
    c = bpy.data.collections.get(nom)
    if not c:
        c = bpy.data.collections.new(nom)
        bpy.context.scene.collection.children.link(c)
    return c


# ====================================================================== petite boîte à outils de nœuds
class NT:
    def __init__(s, m):
        try:
            m.use_nodes = True
        except Exception:
            pass
        s.m, s.n, s.l = m, m.node_tree.nodes, m.node_tree.links
        for x in list(s.n):
            if x.type != "OUTPUT_MATERIAL":
                s.n.remove(x)
        s.out = next((x for x in s.n if x.type == "OUTPUT_MATERIAL"), None) or s.n.new("ShaderNodeOutputMaterial")
        s._pos = {}

    def _set(s, sock, v):
        if isinstance(v, bpy.types.NodeSocket):
            s.l.new(v, sock)
        elif isinstance(v, (tuple, list)) and len(v) == 3 and sock.type == "RGBA":
            sock.default_value = (*v, 1)
        else:
            sock.default_value = v

    def sock(s, node, ident, out=False):
        for k in (node.outputs if out else node.inputs):
            if k.identifier == ident or k.name == ident:
                return k
        raise KeyError(ident)

    def math(s, op, a, b=None, c=None, clamp=False):
        n = s.n.new("ShaderNodeMath"); n.operation = op; n.use_clamp = clamp
        for i, v in enumerate((a, b, c)):
            if v is not None:
                s._set(n.inputs[i], v)
        return n.outputs[0]

    def mix(s, fac, a, b):
        n = s.n.new("ShaderNodeMix"); n.data_type = "RGBA"
        s._set(s.sock(n, "Factor_Float"), fac); s._set(s.sock(n, "A_Color"), a); s._set(s.sock(n, "B_Color"), b)
        return s.sock(n, "Result_Color", True)

    def lisse(s, v, a, b):
        """Rampe douce : 0 sous a, 1 au-dessus de b."""
        n = s.n.new("ShaderNodeMapRange"); n.interpolation_type = "SMOOTHSTEP"
        s._set(n.inputs["Value"], v); n.inputs["From Min"].default_value = a; n.inputs["From Max"].default_value = b
        return n.outputs[0]

    def pos(s, coords):
        """Coordonnées (x, y, z) : 'monde' (motifs continus d'un objet à l'autre) ou 'objet' (suit l'objet)."""
        if coords not in s._pos:
            if coords == "monde":
                g = s.n.new("ShaderNodeNewGeometry"); v = g.outputs["Position"]
            else:
                g = s.n.new("ShaderNodeTexCoord"); v = g.outputs["Object"]
            sx = s.n.new("ShaderNodeSeparateXYZ"); s.l.new(v, sx.inputs[0])
            s._pos[coords] = (v, sx.outputs[0], sx.outputs[1], sx.outputs[2])
        return s._pos[coords]

    def bruit(s, vec, echelle, detail=1.0, etire=None):
        """Bruit ; etire = (sx, sy, sz) : périodes en mètres selon chaque axe (traînées du fil du bois)."""
        if etire:
            mp = s.n.new("ShaderNodeMapping"); mp.vector_type = "POINT"
            mp.inputs["Scale"].default_value = tuple(1.0 / e for e in etire)
            s.l.new(vec, mp.inputs["Vector"]); vec = mp.outputs[0]; echelle = 1.0
        n = s.n.new("ShaderNodeTexNoise")
        s.l.new(vec, n.inputs["Vector"]); n.inputs["Scale"].default_value = echelle; n.inputs["Detail"].default_value = detail
        return n.outputs[0]

    def bandes(s, c, periode, largeur):
        """1 dans une bande de `largeur` tous les `periode` le long de la coordonnée c ; renvoie aussi le numéro de la planche."""
        t = s.math("DIVIDE", c, periode)
        f = s.math("FRACT", t)
        d = s.math("ABSOLUTE", s.math("SUBTRACT", f, 0.5))
        return s.math("GREATER_THAN", d, 0.5 - largeur / (2 * periode)), s.math("FLOOR", t)

    def hasard(s, v):
        n = s.n.new("ShaderNodeTexWhiteNoise"); n.noise_dimensions = "1D"
        s.l.new(v, n.inputs["W"])
        return n.outputs["Value"]

    def entre(s, c, a, b):
        return s.math("MULTIPLY", s.math("GREATER_THAN", c, a), s.math("LESS_THAN", c, b))

    def onde(s, phase, profil):
        """Profil périodique de la phase (une période par unité), par le nœud Wave en bandes : "SAW" rampe de 0 à 1,
        "TRI" 0 sur les entiers et 1 entre deux, "SIN" sinusoïde."""
        w = s.n.new("ShaderNodeTexWave"); w.wave_type = "BANDS"; w.bands_direction = "X"; w.wave_profile = profil
        w.inputs["Scale"].default_value = 1.0; w.inputs["Distortion"].default_value = 0.0
        cx = s.n.new("ShaderNodeCombineXYZ")
        s.l.new(s.math("MULTIPLY", phase, 2 * math.pi / 20.0), cx.inputs[0])     # le nœud Wave multiplie la coordonnée par 20
        s.l.new(cx.outputs[0], w.inputs["Vector"])
        return w.outputs[1]

    def bois_dessine(s, vec, fibre, fil=1.0, net=0.05, decalage=None):
        """Bois DESSINÉ, pas un bruit étiré : des veines qui ondulent le long du fil (Noise), s'écartent autour de nœuds
        clairsemés (Voronoi) où elles se referment en cernes, et sont tracées en traits fins (Wave). Réglages : regles.BOIS, en D.
        fibre : axe du fil ; fil : échelle du dessin (1 = une veine tous les 0,06 D) ; net : douceur du bord des veines ;
        decalage : valeur par planche (les veines ne se suivent pas d'une planche à l'autre).
        Renvoie (cernes, veines, cœur des nœuds), trois masques de 0 à 1."""
        Bo = R.BOIS
        i = "xyz".index(fibre)
        a1, a2 = [j for j in range(3) if j != i]
        sx = s.n.new("ShaderNodeSeparateXYZ"); s.l.new(vec, sx.inputs[0])
        travers = s.math("ADD", sx.outputs[a1], s.math("MULTIPLY", sx.outputs[a2], 0.83))     # toute face parallèle au fil porte des veines
        pv = Bo["veine"] * D * fil
        e = [Bo["onde"][1] * D * fil] * 3; e[i] = Bo["onde"][0] * D * fil
        ondule = s.math("MULTIPLY", s.math("SUBTRACT", s.bruit(vec, 1.0, 2.0, etire=e), 0.5), 2.0 * Bo["onde"][2])
        phase = s.math("ADD", s.math("DIVIDE", travers, pv), ondule)
        if decalage is not None:
            phase = s.math("ADD", phase, s.math("MULTIPLY", decalage, 37.0))
        ech = [1.0 / (Bo["noeud"][1] * D * fil)] * 3; ech[i] = 1.0 / (Bo["noeud"][0] * D * fil)
        mp = s.n.new("ShaderNodeMapping"); mp.vector_type = "POINT"; mp.inputs["Scale"].default_value = tuple(ech)
        s.l.new(vec, mp.inputs["Vector"])
        vo = s.n.new("ShaderNodeTexVoronoi"); vo.feature = "F1"; vo.inputs["Scale"].default_value = 1.0
        s.l.new(mp.outputs[0], vo.inputs["Vector"])
        sep = s.n.new("ShaderNodeSeparateColor"); s.l.new(vo.outputs["Color"], sep.inputs[0])
        present = s.math("GREATER_THAN", sep.outputs[0], Bo["noeud"][4])                    # toutes les cellules n'ont pas de nœud
        dist, rk = vo.outputs["Distance"], Bo["noeud"][2]
        bosse = s.math("MULTIPLY", s.math("SUBTRACT", 1.0, s.lisse(dist, rk * 0.5, rk * 2.4)), present)
        phase = s.math("ADD", phase, s.math("MULTIPLY", bosse, Bo["noeud"][3]))             # les veines contournent le nœud et s'y referment en cernes
        cernes = s.math("POWER", s.onde(s.math("MULTIPLY", phase, 0.5), "SAW"), 1.6)         # un cerne : clair, de plus en plus sombre, puis une limite nette
        lt = Bo["trait"] / Bo["veine"]
        e2 = [0.05 * D * fil] * 3; e2[i] = 1.6 * D * fil
        pleine = s.math("ADD", 0.45, s.math("MULTIPLY", s.lisse(s.bruit(vec, 1.0, 1.0, etire=e2), 0.36, 0.56), 0.55))   # une veine n'a pas partout la même force
        veines = s.math("MULTIPLY", s.math("SUBTRACT", 1.0, s.lisse(s.onde(phase, "TRI"), lt * (1 - net * 4), lt * (1 + net * 4))), pleine)
        fin = s.math("MULTIPLY", s.math("SUBTRACT", 1.0, s.lisse(s.onde(s.math("MULTIPLY", phase, Bo["grain"][0]), "TRI"), 0.18, 0.42)), Bo["grain"][1])
        veines = s.math("MAXIMUM", veines, fin)
        coeur = s.math("MULTIPLY", s.math("SUBTRACT", 1.0, s.lisse(dist, rk * 0.30, rk * 0.55)), present)
        return cernes, veines, coeur


def _groupe_passe():
    ng = bpy.data.node_groups.get("PASSE")
    if ng:
        return ng
    ng = bpy.data.node_groups.new("PASSE", "ShaderNodeTree")
    ng.interface.new_socket(name="passe", in_out="OUTPUT", socket_type="NodeSocketFloat")
    v = ng.nodes.new("ShaderNodeValue"); v.name = "V"
    o = ng.nodes.new("NodeGroupOutput")
    ng.links.new(v.outputs[0], o.inputs[0])
    return ng


def _finir(t, couleur, emissif=False, a_plat=False):
    """Branche les trois passes : couleur peinte / lumière (R soleil, V lampes, B occlusion) / données (normale, profondeur)."""
    n, l = t.n, t.l
    ea = n.new("ShaderNodeEmission"); t._set(ea.inputs["Color"], couleur)
    el = n.new("ShaderNodeEmission")
    if emissif:
        el.inputs["Color"].default_value = (1.0, 0.0, 1.0, 1)          # R = 1 exactement : « brille tout seul » (flammes, lampes, fenêtres)
    else:
        dif = n.new("ShaderNodeBsdfDiffuse"); dif.inputs["Color"].default_value = (1, 1, 1, 1)
        if a_plat:                                                      # cailloux, touffes : éclairés comme le sol qui les porte (normale vers le haut)
            haut = n.new("ShaderNodeCombineXYZ"); haut.inputs[2].default_value = 1.0
            l.new(haut.outputs[0], dif.inputs["Normal"])
        s2r = n.new("ShaderNodeShaderToRGB"); l.new(dif.outputs[0], s2r.inputs[0])
        sep = n.new("ShaderNodeSeparateColor"); l.new(s2r.outputs["Color"], sep.inputs[0])
        ao = n.new("ShaderNodeAmbientOcclusion"); ao.inputs["Distance"].default_value = 0.55; ao.samples = 8
        comb = n.new("ShaderNodeCombineColor")
        # part de soleil reçue (0 = ombre, 0,9 = plein soleil) : le Lambert est divisé par N·L, calculé ICI avec la vraie normale
        # (reconstruire la normale après coup perd son signe dès que la caméra lève le nez)
        geo0 = n.new("ShaderNodeNewGeometry")
        dot = n.new("ShaderNodeVectorMath"); dot.operation = "DOT_PRODUCT"
        if a_plat:
            dot.inputs[0].default_value = (0, 0, 1)
        else:
            l.new(geo0.outputs["Normal"], dot.inputs[0])
        dot.inputs[1].default_value = tuple(VERS_SOLEIL)
        ndl = dot.outputs["Value"]
        vis = t.math("DIVIDE", sep.outputs[0], t.math("MULTIPLY", t.math("MAXIMUM", ndl, 0.08), ENERGIE_SOLEIL / math.pi), clamp=True)
        part = t.math("MULTIPLY", t.math("MULTIPLY", vis, t.lisse(ndl, 0.03, 0.16)), 0.9)
        l.new(part, comb.inputs[0]); l.new(t.math("MULTIPLY", sep.outputs[1], 0.25, clamp=True), comb.inputs[1])
        if a_plat:
            comb.inputs[2].default_value = 0.0                          # B = 0 : « petit détail posé au sol » (ni occlusion ni contour en post-traitement)
        else:
            l.new(t.math("MAXIMUM", ao.outputs["AO"], 0.02), comb.inputs[2])
        l.new(comb.outputs[0], el.inputs["Color"])
    geo = n.new("ShaderNodeNewGeometry")
    vt = n.new("ShaderNodeVectorTransform"); vt.vector_type, vt.convert_from, vt.convert_to = "NORMAL", "WORLD", "CAMERA"
    l.new(geo.outputs["Normal"], vt.inputs["Vector"])
    sx = n.new("ShaderNodeSeparateXYZ"); l.new(vt.outputs[0], sx.inputs[0])
    cam = n.new("ShaderNodeCameraData")
    z = t.math("DIVIDE", cam.outputs["View Z Depth"], R.PROF_MAX, clamp=True)
    cx = n.new("ShaderNodeCombineXYZ")
    l.new(t.math("MULTIPLY_ADD", sx.outputs[0], 0.5, 0.5), cx.inputs[0]); l.new(t.math("MULTIPLY_ADD", sx.outputs[1], 0.5, 0.5), cx.inputs[1]); l.new(z, cx.inputs[2])
    ed = n.new("ShaderNodeEmission"); l.new(cx.outputs[0], ed.inputs["Color"])
    g = n.new("ShaderNodeGroup"); g.node_tree = _groupe_passe()
    m1 = n.new("ShaderNodeMixShader"); l.new(t.math("GREATER_THAN", g.outputs[0], 0.5), m1.inputs[0]); l.new(ea.outputs[0], m1.inputs[1]); l.new(el.outputs[0], m1.inputs[2])
    m2 = n.new("ShaderNodeMixShader"); l.new(t.math("GREATER_THAN", g.outputs[0], 1.5), m2.inputs[0]); l.new(m1.outputs[0], m2.inputs[1]); l.new(ed.outputs[0], m2.inputs[2])
    l.new(m2.outputs[0], t.out.inputs["Surface"])
    try:
        t.m.surface_render_method = "DITHERED"
    except Exception:
        pass


# ====================================================================== matières peintes
def matiere(nom, base, ton2=None, fibre=None, coords="objet", veine=None, planches=None, tache=None, emissif=False, special=None,
            var=0.5, fil=1.0, a_plat=False, net=0.05, lisere=None):
    """Crée la matière `nom`. Toutes les couleurs en '#rrvvbb'.
    base / ton2 : les deux tons de la matière ; fibre : axe du fil du bois ('x', 'y', 'z') -> bois DESSINÉ (NT.bois_dessine :
    veines qui ondulent, nœuds, cernes) ; veine : couleur des veines et des nœuds ; fil : échelle du dessin ; net : douceur des veines ; planches = (axe en travers, largeur en m, joint en m, couleur du joint) : utiliser
    R.DECOR['planche'] × D et R.DECOR['joint'] × D ; tache = (taille en m, couleur, force) : taches douces peintes ;
    special : fonction (t, couleur, axes, vecteur) -> couleur, pour un mur composé ; a_plat : petit détail posé au sol ;
    lisere : couleur du liseré sombre peint sur le pourtour d'un caillou ; emissif : brille tout seul (lampe, flamme, fenêtre)."""
    m = bpy.data.materials.get(nom) or bpy.data.materials.new(nom)
    t = NT(m)
    if emissif and not (ton2 or special):
        _finir(t, lin(base), True)
        return m
    vec, X, Y, Z = t.pos(coords)
    ax = dict(x=X, y=Y, z=Z)
    col = t.n.new("ShaderNodeRGB").outputs[0]; col.default_value = (*lin(base), 1)
    if ton2 and fibre:                                      # bois dessiné : cernes entre les deux tons, veines et nœuds dans la couleur `veine`
        num = None
        if planches:                                        # chaque planche a sa teinte et son propre dessin
            _, num = t.bandes(ax[planches[0]], planches[1], planches[2])
            num = t.hasard(num)
        f, v, noeud = t.bois_dessine(vec, fibre, fil, net, num)
        if planches:
            f = t.math("ADD", t.math("MULTIPLY", f, 0.7), t.math("MULTIPLY", t.math("SUBTRACT", num, 0.35), var), clamp=True)
        col = t.mix(f, col, lin(ton2))
        if veine:
            col = t.mix(t.math("MULTIPLY", v, 0.9), col, lin(veine))
            col = t.mix(t.math("MULTIPLY", noeud, 0.92), col, lin(veine))
    elif ton2:
        f = t.lisse(t.bruit(vec, 1.0 / (tache[0] if tache else 0.6), 1.5), 0.42, 0.62)
        col = t.mix(f, col, lin(ton2))
    if tache:
        f = t.lisse(t.bruit(vec, 1.0 / tache[0], 2.0), 0.48, 0.72)
        col = t.mix(t.math("MULTIPLY", f, tache[2]), col, lin(tache[1]))
    if planches:
        j, _ = t.bandes(ax[planches[0]], planches[1], planches[2])
        col = t.mix(j, col, lin(planches[3]))
    if special:
        col = special(t, col, ax, vec)
    if a_plat and lisere:                                   # cailloux : liseré sombre peint sur le pourtour
        lw = t.n.new("ShaderNodeLayerWeight"); lw.inputs["Blend"].default_value = 0.5
        loin = t.lisse(t.n.new("ShaderNodeCameraData").outputs["View Z Depth"], R.DECOR["lisere_loin"][0] * D, R.DECOR["lisere_loin"][1] * D)
        pres = t.math("SUBTRACT", 1.0, loin)                # le liseré s'efface avec la distance : sur un caillou de 3 px il ferait un point noir
        col = t.mix(t.math("MULTIPLY", t.math("MULTIPLY", t.lisse(lw.outputs["Facing"], 0.80, 0.92), 0.8), pres), col, lin(lisere))
    _finir(t, col, emissif, a_plat)
    return m


def bois(nom, base, ton2, veine, **k):
    """Matière de bois dont le fil suit le grand axe de chaque objet : crée nom@x, nom@y, nom@z ; orienter_fil() choisit."""
    for a in "xyz":
        matiere(f"{nom}@{a}", base, ton2, fibre=a, veine=veine, **k)
    return matiere(nom, base, ton2, fibre="z", veine=veine, **k)


def orienter_fil(noms):
    """Chaque objet en bois prend la variante dont le fil suit son plus grand côté."""
    for o in bpy.data.objects:
        if o.type != "MESH":
            continue
        for sl in o.material_slots:
            nm = sl.material.name if sl.material else ""
            if nm in noms:
                d = o.dimensions
                a = "xyz"[max(range(3), key=lambda i: d[i])]
                sl.material = bpy.data.materials[f"{nm}@{a}"]


# ====================================================================== formes
def _finir_objet(nom, bm, col, mat, pos, rot, ombre):
    me = bpy.data.meshes.new(nom)
    bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(nom, me)
    collection(col).objects.link(o)
    o.location, o.rotation_euler = pos, rot
    m = bpy.data.materials.get(mat)
    if m is None:
        raise KeyError(f"matière « {mat} » non définie (objet « {nom} ») : la créer avec matiere() avant la géométrie")
    me.materials.append(m)
    o.visible_shadow = ombre
    return o


def boite(nom, taille, pos, mat, rot=(0, 0, 0), col="DECOR", ombre=True, origine=(0, 0, 0.5)):
    """Boîte de dimensions réelles (m). Par défaut l'origine est au centre de la BASE : pos = point posé au sol."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector(((v.co.x + origine[0]) * taille[0], (v.co.y + origine[1]) * taille[1], (v.co.z + origine[2]) * taille[2]))
    return _finir_objet(nom, bm, col, mat, pos, rot, ombre)


def cylindre(nom, r, h, pos, mat, r2=None, seg=20, rot=(0, 0, 0), col="DECOR", ombre=True):
    """Cylindre ou cône tronqué, origine à la base."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=r, radius2=r if r2 is None else r2, depth=h)
    for v in bm.verts:
        v.co.z += h / 2
    for f in bm.faces:
        f.smooth = abs(f.normal.z) < 0.85
    return _finir_objet(nom, bm, col, mat, pos, rot, ombre)


def sphere(nom, r, pos, mat, seg=16, rot=(0, 0, 0), col="DECOR", ombre=True):
    """Sphère ou ellipsoïde (r = rayon, ou (rx, ry, rz))."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=max(6, seg // 2), radius=1.0)
    s = (r, r, r) if isinstance(r, (int, float)) else r
    for v in bm.verts:
        v.co = Vector((v.co.x * s[0], v.co.y * s[1], v.co.z * s[2]))
    for f in bm.faces:
        f.smooth = True
    return _finir_objet(nom, bm, col, mat, pos, rot, ombre)


def toit(nom, taille, pos, mat, rot=(0, 0, 0), col="DECOR"):
    """Toit à deux pans : prisme de base taille[0] × taille[1], faîte dans la longueur (y), hauteur taille[2]."""
    lx, ly, h = taille
    bm = bmesh.new()
    pts = [(-lx / 2, -ly / 2, 0), (lx / 2, -ly / 2, 0), (0, -ly / 2, h), (-lx / 2, ly / 2, 0), (lx / 2, ly / 2, 0), (0, ly / 2, h)]
    v = [bm.verts.new(p) for p in pts]
    for f in ((0, 1, 2), (5, 4, 3), (0, 3, 4, 1), (1, 4, 5, 2), (2, 5, 3, 0)):
        bm.faces.new([v[i] for i in f])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    return _finir_objet(nom, bm, col, mat, pos, rot, True)


def semer(nom, n, zone, mats, taille=(0.6, 2.2), graine=1, eviter=(), col="SOL"):
    """Cailloux : n ellipsoïdes aplatis semés dans zone = (x0, y0, x1, y1). taille en multiples du diamètre médian (0,03 D).
    eviter : liste de (x, y, rayon) à laisser libres."""
    rnd = random.Random(graine)
    d0 = R.DECOR["caillou"] * D
    k = 0
    while k < n:
        x, y = rnd.uniform(zone[0], zone[2]), rnd.uniform(zone[1], zone[3])
        if any(math.hypot(x - ex, y - ey) < er for ex, ey, er in eviter):
            continue
        d = d0 * rnd.uniform(*taille) * (2.5 if rnd.random() < 0.08 else 1.0)
        sphere(f"{nom}_{k}", (d / 2 * rnd.uniform(0.9, 1.5), d / 2, d * 0.22), (x, y, d * 0.08), rnd.choice(mats), seg=8,
               rot=(0, 0, rnd.uniform(0, 3.14)), col=col, ombre=False)
        k += 1


def touffes(nom, n, zone, mat, graine=2, eviter=(), col="SOL"):
    """Touffes d'herbe sèche : 5 à 8 brins de 0,25 à 0,5 D."""
    rnd = random.Random(graine)
    k = 0
    while k < n:
        x, y = rnd.uniform(zone[0], zone[2]), rnd.uniform(zone[1], zone[3])
        if any(math.hypot(x - ex, y - ey) < er for ex, ey, er in eviter):
            continue
        for j in range(rnd.randint(5, 8)):
            a = rnd.uniform(0, 2 * math.pi); incl = rnd.uniform(8, 38)
            cylindre(f"{nom}_{k}_{j}", 0.014, rnd.uniform(*R.DECOR["touffe"]) * D, (x + 0.03 * math.cos(a), y + 0.03 * math.sin(a), 0), mat, r2=0.002, seg=5,
                     rot=(rad(incl) * math.cos(a), rad(incl) * math.sin(a), 0), col=col, ombre=False)
        k += 1


# ====================================================================== lumières
def soleil(rayon, penombre=None):
    """Soleil du film. rayon = direction dans laquelle VA la lumière (x, y, z), z négatif. ROUGE pur : sa couleur réelle est posée par compo.py.
    À appeler AVANT de créer les matières (sa direction y est inscrite).
    penombre : diamètre apparent du soleil, en degrés (par défaut regles.DECOR["soleil_deg"]). C'est lui qui adoucit les ombres avec la
    distance : bord 10–90 % ≈ 0,75 × distance à l'objet × angle en radians (3,5° : 0,05 D à 1 D de l'objet, 0,5 D à 11 D, le bout d'une ombre longue)."""
    n = math.sqrt(sum(v * v for v in rayon))
    VERS_SOLEIL[:] = [-v / n for v in rayon]
    d = bpy.data.lights.new("SOLEIL", "SUN")
    d.color, d.energy = (1, 0, 0), ENERGIE_SOLEIL
    d.angle = rad(R.DECOR["soleil_deg"] if penombre is None else penombre)
    o = bpy.data.objects.new("SOLEIL", d)
    collection("LUMIERES").objects.link(o)
    o.rotation_euler = Vector(rayon).normalized().to_track_quat("-Z", "Y").to_euler()
    _regler_ombres(d)
    return o


def lampe(nom, pos, energie=60.0, rayon=0.3, portee=11.0):
    """Lampe ponctuelle (suspension, applique, flamme). VERT pur, sans ombre portée : en intérieur il n'y a pas d'ombre nette, et le rendu est 3 fois plus rapide."""
    d = bpy.data.lights.new(nom, "POINT")
    d.color, d.energy = (0, 1, 0), energie
    d.shadow_soft_size = rayon
    d.use_shadow = False
    d.use_custom_distance, d.cutoff_distance = True, portee
    o = bpy.data.objects.new(nom, d)
    collection("LUMIERES").objects.link(o)
    o.location = pos
    return o


def globe(nom, r, pos, mat, energie=None, rayon=0.3, col="DECOR"):
    """Source de lumière visible, RONDE : une sphère émissive (et sa lampe si energie est donné). Le halo posé à l'assemblage est la
    surface qui brille, étalée : une boîte émissive donne une tache rectangulaire, une sphère donne un disque. Jamais de boîte pour une lampe."""
    o = sphere(nom, r, pos, mat, seg=16, col=col, ombre=False)
    if energie:
        lampe(f"{nom}_L", (pos[0], pos[1], pos[2] - 1.6 * (r if isinstance(r, (int, float)) else r[2])), energie=energie, rayon=rayon)
    return o


def _regler_ombres(l):
    for attr, val in (("use_shadow_jitter", True), ("shadow_jitter_overblur", 10.0), ("shadow_filter_radius", 1.5)):
        if hasattr(l, attr):
            setattr(l, attr, val)


def fond(centre=(0, 0, 0), rayon=320.0):
    """Sphère noire qui ferme la scène : chaque pixel a une profondeur (≥ PROF_MAX = ciel, peint par compo.py)."""
    matiere("fond", "#000000", emissif=True)
    return sphere("FOND", rayon, centre, "fond", seg=24, col="FOND", ombre=False)


# ====================================================================== fusion
def fusionner(noms):
    """Réunit les objets fixes d'une collection en un maillage par matière : des milliers d'objets ralentissent chaque passe
    (mesuré : 3 656 objets réunis en 535, 30 s puis 9 s par image)."""
    bpy.context.view_layer.update()
    total = 0
    for nom in noms:
        col = bpy.data.collections.get(nom)
        if not col:
            continue
        lots = {}
        for o in list(col.objects):
            if o.type != "MESH" or o.parent or o.children or o.animation_data or len(o.material_slots) != 1 or o.modifiers:
                continue
            lots.setdefault((o.material_slots[0].material.name, o.visible_shadow), []).append(o)
        for (mat, sh), objs in lots.items():
            if len(objs) < 2:
                continue
            cible = bpy.data.objects.new(f"{nom}_{mat}_{int(sh)}", bpy.data.meshes.new(f"{nom}_{mat}_{int(sh)}"))
            col.objects.link(cible)
            cible.data.materials.append(bpy.data.materials[mat])
            cible.visible_shadow = sh
            with bpy.context.temp_override(active_object=cible, selected_editable_objects=[cible] + objs, selected_objects=[cible] + objs):
                bpy.ops.object.join()
            total += len(objs)
    for me in list(bpy.data.meshes):
        if me.users == 0:
            bpy.data.meshes.remove(me)
    print("fusion :", total, "objets réunis ; il reste", len(bpy.data.objects), "objets")


# ====================================================================== caméra et rendu
def camera_film():
    cd = bpy.data.cameras.new("CAM")
    cd.clip_start, cd.clip_end = 0.05, 800
    cd.sensor_fit, cd.sensor_height = "VERTICAL", 36
    cam = bpy.data.objects.new("CAM", cd)
    collection("CAMERAS").objects.link(cam)
    bpy.context.scene.camera = cam
    return cam


def enregistrer(chemin):
    chemin = pathlib.Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(chemin))
    print("construit :", chemin.name, "| objets :", len(bpy.data.objects), "| matières :", len(bpy.data.materials), "| lumières :", len(bpy.data.lights))


def a_rendre(film, quoi="tout"):
    """Liste (plan, image, tronçon) des rendus à faire. tronçon = None pour un rendu image par image ; sinon une plaque (plaque.py),
    rendue une seule fois pour toutes les images du tronçon. quoi = "tout" | "film" | "A:12,L:9001" (images isolées, toujours en 3D)."""
    if quoi not in ("tout", "film"):
        return [(x.split(":")[0], int(x.split(":")[1]), None) for x in quoi.split(",")]
    plans = PQ.preparer(film)
    out = []
    for k in list(film.ORDRE) + (list(getattr(film, "FIXES", [])) if quoi == "tout" else []):
        for t in plans[k]:
            if t["mode"] == "3d":
                out += [(k, f, None) for f in range(t["a"], t["b"])]
            else:
                out.append((k, t["image_ref"], t))
    return out


def rendre(film, dossier, pct=100, quoi="tout", animer=None):
    """Rend les trois passes de chaque (plan, image). Les images déjà rendues sont sautées : relancer reprend où l'on s'était arrêté.
    quoi = "tout" | "film" (sans les images fixes de contrôle) | "A:12,A:40,L:9001" ; animer(plan, image) : crochet facultatif appelé avant chaque image."""
    sc = bpy.context.scene
    cam = sc.camera
    paires = a_rendre(film, quoi)
    sc.render.resolution_percentage = pct
    suf = "" if pct == 100 else f"_{pct}"
    im = sc.render.image_settings
    val = bpy.data.node_groups["PASSE"].nodes["V"].outputs[0]
    dossier = pathlib.Path(dossier)
    for d in ("albedo", "lum", "data"):
        (dossier / f"{d}{suf}").mkdir(parents=True, exist_ok=True)
    sol = bpy.data.objects.get("SOLEIL")
    n = 0
    for k, f, t in paires:
        plan = film.PLANS[k]
        nom = t["nom"] if t else f"{k}_{f:04d}"
        chemins = [dossier / f"{d}{suf}" / f"{nom}.png" for d in ("albedo", "lum", "data")]
        if all(c.exists() for c in chemins):
            continue
        if t:                   # une plaque : la pose de l'image de référence, un champ plus large, une image plus grande
            pos, _, _, fwd, foc = t["base"]
            cam.location = pos
            cam.rotation_euler = Vector(fwd).to_track_quat("-Z", "Y").to_euler()
            sc.render.resolution_x, sc.render.resolution_y = t["taille"]
        else:
            pos, vis, foc = C.camera(plan, f)
            cam.location = pos
            cam.rotation_euler = (Vector(vis) - Vector(pos)).to_track_quat("-Z", "Y").to_euler()
            sc.render.resolution_x, sc.render.resolution_y = R.LARGEUR, R.HAUTEUR
        cam.data.lens = foc
        if sol:
            sol.data.energy = ENERGIE_SOLEIL if plan.get("soleil", plan["ambiance"] != "interieur") else 0.0
        if animer:
            animer(k, f)
        bpy.context.view_layer.update()
        for i, (ch, vue, prof, ech) in enumerate(zip(chemins, ("Standard", "Raw", "Raw"), ("8", "16", "16"), (8, 10, 1))):
            val.default_value = float(i)
            bpy.data.node_groups["PASSE"].update_tag()
            sc.view_settings.view_transform = vue
            im.color_depth = prof
            sc.eevee.taa_render_samples = ech
            sc.render.filepath = str(ch)
            bpy.ops.render.render(write_still=True)
        n += 1
        print("IMAGE", nom, flush=True)
    val.default_value = 0.0
    print("rendu terminé", n, "/", len(paires), flush=True)
