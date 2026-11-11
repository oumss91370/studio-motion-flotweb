# Écrire du Python Blender qui marche chez le client

Les scripts s'exécutent dans le Blender **du client** : on ne connaît ni sa version exacte, ni sa langue d'interface, ni ses add-ons. `get_addon_status` donne la version ; la lire avant d'utiliser quoi que ce soit qui en dépend.

Source : instructions du serveur et guide « bpy » de `mcp-for-blender` (MIT), notes d'API du skill `blender-claymation` (MIT).

## Chercher au lieu de deviner

```python
# valeurs permises d'une propriété à choix
[i.identifier for i in bpy.types.RenderSettings.bl_rna.properties["file_format"].enum_items]
# propriétés d'un type
[p.identifier for p in bpy.types.ShaderNodeTexImage.bl_rna.properties]
# arguments d'un opérateur
[(p.identifier, p.type) for p in bpy.ops.mesh.primitive_cube_add.get_rna_type().properties]
```

## Règles

- **Nœuds de matière : par type, jamais par nom.** Les noms sont traduits selon la langue de Blender.
  `bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")`
- **Entrées du Principled BSDF** : plusieurs ont changé de nom en 4.0 (`Emission Color`, `Subsurface Weight`, `Specular IOR Level`, `Coat Weight`, `Sheen Weight`, `Transmission Weight`). Demander avec repli :
  `e = bsdf.inputs.get("Emission Color") or bsdf.inputs.get("Emission")`
- **Jamais de valeur de liste écrite en dur** (moteur, format…) : la lire, ou l'affecter dans un `try / except TypeError` (le message d'erreur donne les valeurs acceptées). EEVEE s'appelle `BLENDER_EEVEE_NEXT` de 4.2 à 4.x et `BLENDER_EEVEE` avant et à partir de 5.0.
- **La couleur d'une matière se règle sur les entrées des nœuds.** `material.diffuse_color` ne change que l'affichage « solid » de la vue.
- À partir de 5.0, `material.use_nodes` est toujours actif : ne pas compter sur sa bascule. L'écrire (`mat.use_nodes = True`) fonctionne encore en 5.3 avec un avertissement, et la propriété doit disparaître en 6.0 : pour un script durable, `if hasattr(mat, "use_nodes"): mat.use_nodes = True`.
- **Transparence** : à partir de 4.2, `mat.surface_render_method` (`"DITHERED"` ou `"BLENDED"`) ; avant, `mat.blend_method`. Tester avec `hasattr`.
- **Animation** : poser les clés avec `obj.keyframe_insert("location", frame=f)`, qui marche partout. L'accès aux courbes a changé en 4.4 (actions à emplacements) et `Action.fcurves` a disparu en 5.0 : passer par `bpy_extras.anim_utils.action_get_channelbag_for_slot(action, obj.animation_data.action_slot)` à partir de 4.4, avec repli sur `action.fcurves` avant.

## Données plutôt qu'opérateurs

Préférer `bpy.data` et les propriétés des objets à `bpy.ops` : pas besoin de contexte, plus rapide, plus fiable.

```python
mesh = bpy.data.meshes.new("Sol"); mesh.from_pydata(sommets, [], faces)
obj = bpy.data.objects.new("Sol", mesh)
bpy.data.collections["DECOR"].objects.link(obj)
obj.modifiers.new("Biseau", "BEVEL")
```

Quand un opérateur est inévitable : le code tourne depuis une minuterie, pas depuis une zone de l'interface. Les opérateurs qui ont besoin de la vue 3D demandent un contexte :

```python
zone = next(a for a in bpy.context.screen.areas if a.type == "VIEW_3D")
region = next(r for r in zone.regions if r.type == "WINDOW")
with bpy.context.temp_override(area=zone, region=region, active_object=obj, selected_objects=[obj]):
    bpy.ops.object.shade_smooth()
```

Toujours revenir en mode objet à la fin d'une étape, même en cas d'erreur (`try / finally`).

## Façon de travailler

- Petites étapes ; `print` de ce qu'on veut savoir.
- Tout nommer.
- Une collection par groupe logique.
- Appliquer l'échelle avant un modificateur qui en dépend.
- `obj.copy()` pour répéter un accessoire (partage la géométrie) ; `obj.data.copy()` seulement si la copie doit différer.
- Unités en mètres.
- Les modèles importés arrivent avec une échelle, une rotation et une origine quelconques : les régler d'après la boîte englobante renvoyée par l'import, poser au sol (`obj.location.z -= z_min`), puis regarder.
- Ne jamais supprimer ou vider ce que le client avait dans sa scène sans son accord ; travailler dans ses propres collections.
