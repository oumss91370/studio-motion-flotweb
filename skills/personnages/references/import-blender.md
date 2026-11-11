# Monter un personnage plat dans Blender

Le personnage est une pile de **plans** (rectangles plats) qui portent les images PNG, debout dans le décor 3D. Trois exigences :

1. les lumières du décor ne l'ombrent pas (matériau **émissif**) ;
2. une **ombre de contact** douce le pose au sol ;
3. ses expressions s'échangent image par image.

Blender propose aussi un import tout fait (**File → Import → Images as Planes**, avec le choix « Emit »). Le montage par script ci-dessous donne le même résultat et reste identique d'une version à l'autre.

Charger aussi le skill `blender` (début de session, contrôles avec `look`).

## Tailles et repère

- Tous les PNG ont la même taille (voir `pieces-svg.md`) : chaque plan a donc **la même dimension** et **la même position**, et les pièces se superposent toutes seules.
- Hauteur du plan = hauteur du gabarit convertie en mètres. Pour un personnage de 1,60 m dessiné dans un gabarit de 1000 unités où il occupe 900 unités : plan de `1,60 / 0,9 = 1,78 m` de haut, largeur en proportion (`× 600/1000`).
- Le plan est vertical, face à la caméra, son bord bas posé au sol sur la marque.
- Les pièces sont étagées en profondeur de **1 à 2 mm** vers la caméra pour éviter le scintillement : jambes, corps, bras, tête, yeux et bouche, extras, coiffe.

## Matériau émissif

```python
import bpy

def materiau_plat(nom, chemin_png):
    img = bpy.data.images.load(chemin_png, check_existing=True)
    mat = bpy.data.materials.new(nom); mat.use_nodes = True
    nt = mat.node_tree; nt.nodes.clear()
    tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img
    emi = nt.nodes.new("ShaderNodeEmission")
    tra = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(tex.outputs["Color"], emi.inputs["Color"])
    nt.links.new(tex.outputs["Alpha"], mix.inputs[0])       # facteur = transparence de l'image
    nt.links.new(tra.outputs[0], mix.inputs[1])
    nt.links.new(emi.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs["Surface"])
    if hasattr(mat, "surface_render_method"):                # Blender 4.2 et plus
        mat.surface_render_method = "DITHERED"
    else:
        mat.blend_method = "HASHED"
    return mat
```

- **Émission, force 1** : le plan affiche les couleurs de l'image, quelles que soient les lumières du décor.
- **Méthode « dithered »** pour les pièces du personnage : leurs bords sont nets, et cette méthode reste compatible avec la profondeur de champ et le tri des plans. La méthode « blended » est réservée à l'ombre de contact (bords doux).
- Le personnage **ne projette pas d'ombre** par ses plans (on verrait l'ombre d'un rectangle ou d'une découpe dure) : `obj.visible_shadow = False`. L'ombre vient du disque de contact.

## Plan d'une pièce

```python
def plan_piece(nom, mat, largeur, hauteur, parent, decal=0.0):
    l = largeur / 2
    sommets = [(-l, 0, 0), (l, 0, 0), (l, 0, hauteur), (-l, 0, hauteur)]   # debout, face à -Y
    mesh = bpy.data.meshes.new(nom); mesh.from_pydata(sommets, [], [(0, 1, 2, 3)])
    uv = mesh.uv_layers.new(name="UV")
    for i, co in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]):
        uv.data[i].uv = co
    o = bpy.data.objects.new(nom, mesh); o.data.materials.append(mat)
    bpy.data.collections["PERSONNAGES"].objects.link(o)
    o.parent = parent
    o.location.y = -decal          # vers la caméra
    o.visible_shadow = False
    return o
```

## Hiérarchie et pivots

Les rotations se font autour d'objets vides placés aux pivots notés dans la fiche du personnage (convertis en mètres).

```
PERSO_racine            (vide, au sol, sur la marque)
├─ PERSO_ombre          (disque de contact, au sol)
├─ PERSO_jambe_g / _d   (vide à la hanche → plan)
└─ PERSO_corps_pivot    (vide au bassin)
   ├─ plan corps
   ├─ PERSO_bras_g / _d (vide à l'épaule → plan)
   └─ PERSO_tete_pivot  (vide au cou)
      ├─ plan tête
      ├─ plans yeux-*   (tous empilés, un seul visible)
      ├─ plans bouche-* (tous empilés, un seul visible)
      ├─ plans extra-*
      └─ plan costume
```

Comme tous les plans ont la même origine (le bas du gabarit), créer chaque plan à l'origine de la racine, puis lui donner pour parent son pivot **en gardant sa position dans le monde** (`o.matrix_parent_inverse = pivot.matrix_world.inverted()`).

Poser un personnage = déplacer `PERSO_racine`. Le faire jouer = tourner les pivots.

## Ombre de contact

Un disque posé au sol sous les pieds, noir, transparent, aux bords doux. Il ne dépend pas des lumières : il marche dans tous les décors.

```python
def ombre_contact(nom, parent, largeur=0.9, profondeur=0.35, force=0.45):
    mesh = bpy.data.meshes.new(nom)
    mesh.from_pydata([(-.5, -.5, 0), (.5, -.5, 0), (.5, .5, 0), (-.5, .5, 0)], [], [(0, 1, 2, 3)])
    mesh.uv_layers.new(name="UV")
    o = bpy.data.objects.new(nom, mesh)
    bpy.data.collections["PERSONNAGES"].objects.link(o)
    o.parent = parent; o.location.z = 0.003; o.scale = (largeur, profondeur, 1); o.visible_shadow = False
    mat = bpy.data.materials.new(nom); mat.use_nodes = True
    nt = mat.node_tree; nt.nodes.clear()
    coord = nt.nodes.new("ShaderNodeTexCoord")
    grad = nt.nodes.new("ShaderNodeTexGradient"); grad.gradient_type = "SPHERICAL"
    carte = nt.nodes.new("ShaderNodeMapping"); carte.inputs["Scale"].default_value = (2, 2, 2)
    mult = nt.nodes.new("ShaderNodeMath"); mult.operation = "MULTIPLY"; mult.inputs[1].default_value = force
    noir = nt.nodes.new("ShaderNodeEmission"); noir.inputs["Color"].default_value = (0, 0, 0, 1)
    tra = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader"); out = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(coord.outputs["Object"], carte.inputs["Vector"])
    nt.links.new(carte.outputs[0], grad.inputs["Vector"])
    nt.links.new(grad.outputs["Fac"], mult.inputs[0])
    nt.links.new(mult.outputs[0], mix.inputs[0])
    nt.links.new(tra.outputs[0], mix.inputs[1]); nt.links.new(noir.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs["Surface"])
    if hasattr(mat, "surface_render_method"): mat.surface_render_method = "BLENDED"
    else: mat.blend_method = "BLEND"
    o.data.materials.append(mat)
    return o
```

Réglages : largeur d'environ 1,2 fois l'écartement des pieds, opacité au centre de 0,35 à 0,5, bords qui s'effacent complètement. L'ombre rétrécit et s'éclaircit quand le personnage décolle du sol (un saut), puis revient au contact.

**Toujours vérifier par un rendu** que le disque a bien un centre sombre et des bords doux ; si le dégradé est décentré ou trop petit, ajuster l'échelle du nœud Mapping.

## Échanger les expressions

Toutes les variantes d'yeux et de bouche sont empilées au même endroit ; une seule est visible. On cache les autres en les réduisant à une échelle minuscule (méthode des visages de remplacement en stop-motion, reprise du skill `blender-claymation`), avec des clés en **interpolation constante**.

```python
def montrer(variantes, nom_visible, image):
    """variantes : dict nom -> objet plan. Rend visible `nom_visible` à partir de `image`."""
    for nom, o in variantes.items():
        o.scale = (1, 1, 1) if nom == nom_visible else (1e-4, 1e-4, 1e-4)
        o.keyframe_insert("scale", frame=image)

montrer(yeux, "plisses", 380)
montrer(yeux, "neutre", 396)
```

Après avoir posé toutes les clés d'expression, passer leurs courbes en interpolation constante (voir `bpy-portable.md` du skill `blender` pour l'accès aux courbes selon la version). Sinon les plans gonflent et dégonflent entre deux clés.

## Faire face à la caméra

- Plan fixe ou avancée de caméra dans l'axe : les plans restent face à la caméra, rien à faire.
- Travelling latéral ou caméra très décalée : au-delà d'environ 25° de biais, le personnage paraît mince. Ajouter sur `PERSO_racine` une contrainte qui le fait tourner **autour de l'axe vertical seulement** vers la caméra (contrainte « Locked Track », axe verrouillé Z). Ne jamais le faire basculer vers une caméra en plongée : il doit rester debout.
- Règle du style : un personnage plat ne tourne pas en perspective pendant un plan. S'il doit changer d'orientation, changer de vue dessinée (à une coupe ; voir `limites-du-pantin.md`).

## Clés de déplacement : toujours tenir l'arrivée

Constat d'un film réel (11/11/2026), trouvé par la critique : un personnage qui se déplace dans un plan **continuait de glisser** après son arrivée, vers la position qu'il occupe au plan suivant (un personnage qui ne s'arrêtait pas, d'autres qui sortaient du cadre). Cause : la clé d'arrivée n'était pas tenue, et Blender interpolait jusqu'à la clé suivante.

- La clé d'**arrivée** d'un déplacement se pose en interpolation **constante** : elle tient la position jusqu'à la clé suivante (c'est l'interpolation de la clé de gauche qui règle le trajet vers la suivante).
- Toutes les clés de **placement** en début de plan sont constantes.
- Ne poser des clés que sur les axes qui bougent : une clé « tout l'objet » à mi-plan crée des trajets non voulus sur les autres axes.
- Contrôler : rendre l'image de l'arrivée et la dernière image du plan ; le personnage doit être au même endroit.

Le kit de la catégorie `styles-2-5d-histoire-vraie` le fait dans `Perso.deplace()` et signale une clé non tenue à la construction de la scène (`controle_glissements`).

## Couleur : garder les aplats

Le réglage de vue de Blender (AgX ou Filmic) transforme les couleurs à la sortie. C'est bon pour le décor, mais les aplats du personnage sortent **ternis ou décalés** par rapport au dessin.

Mesure faite en Blender 5.3 (Cycles, émission de force 1) : avec la vue **AgX**, une peau dessinée en `#F2C9A0` sort en `#C2AF9D` (grise) et un rouge `#C8362C` sort en `#BD3C28` ; avec la vue **Standard**, les deux sortent à l'identique du dessin.

Deux façons de faire, à choisir une fois pour toute la vidéo :

| Méthode | Comment | Quand |
|---|---|---|
| **Vue « Standard »** | `scene.view_settings.view_transform = "Standard"`. Les aplats sont exacts. En contrepartie, le décor brûle plus vite dans les blancs : baisser la puissance des lumières jusqu'à ce qu'aucune zone ne soit blanche. | Par défaut : le personnage est vraiment dans le décor (masqué par les objets, pris dans le flou) et ses couleurs sont justes. |
| **Deux passes** | Rendre le décor seul avec la vue AgX, puis le personnage seul sur fond transparent en vue « Standard » ; superposer les deux dans HyperFrames. | Si le décor a besoin de la douceur d'AgX (fortes lumières, fenêtres très claires) et que rien ne passe devant le personnage. |

Monter la force d'émission ne rattrape pas la vue AgX : elle éclaircit sans rendre la saturation.

Dans tous les cas : **vérifier sur un rendu réel** en comparant la couleur de la peau et de l'accent au dessin, pas dans la vue.

## Mise au point

Placer `PERSO_racine` sur la marque du plan, celle qui sert d'objet de mise au point à la caméra (skill `blender`). Le personnage est net, le fond est flou. Deux personnages à des profondeurs différentes : faire le point sur celui qui porte le plan.

## Contrôles

- `look(mode="camera", shading="rendered")` : le personnage est-il plat (aucun dégradé de lumière sur lui) ? A-t-il son ombre ? Est-il net ?
- `look(mode="angles", target=["PERSO_racine"], views=["front","right","top"])` : les pièces sont-elles bien étagées, sans trou entre elles vues de face ?
- `look(mode="frames", frames=[…], view="camera")` autour de chaque action.
- Gros plan rendu du visage pour chaque réaction importante.

## Erreurs fréquentes

| Erreur | Correction |
|---|---|
| Le personnage est assombri d'un côté | Le matériau n'est pas émissif (Principled) : refaire avec `materiau_plat`. |
| Un rectangle noir ou gris autour du personnage | La transparence n'est pas branchée ou la méthode de rendu n'est pas réglée. |
| Le personnage flotte | Pas d'ombre de contact, ou racine au-dessus du sol. |
| Les pièces scintillent | Pas de décalage en profondeur entre les plans. |
| Le personnage est flou | Il n'est pas sur la marque de mise au point. |
| Les yeux gonflent entre deux expressions | Interpolation des clés d'échelle non constante. |
| Le personnage glisse après s'être arrêté, ou part avant la coupe | Clé d'arrivée du déplacement non tenue : la passer en interpolation constante. |
| Couleurs délavées | Voir « Couleur : garder les aplats ». |
| Bords crénelés ou bruités | Augmenter les échantillons de rendu ; exporter les PNG en 2×. |
