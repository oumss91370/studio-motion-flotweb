# Construire un décor en 3 passes

Principe (cours « 2.5D motion studio », guide « scene » du connecteur) : on monte un décor comme une équipe de tournage, dans l'ordre **formes et caméras, puis lumière, puis habillage**, et on **regarde après chaque passe**. Une erreur de cadrage trouvée en passe 1 coûte une minute ; la même erreur trouvée après l'habillage coûte tout le décor.

Avant de commencer, il faut la liste de plans : quels plans se passent dans ce décor, quel cadrage, où se tient le personnage, où est l'objet héros.

## Organisation du fichier

- Une collection par groupe : `DECOR`, `LUMIERES`, `CAMERAS`, `MARQUES`, `HEROS`, `PERSONNAGES`.
- Tout objet créé a un nom lisible (`Mur_Nord`, `CAM_P07`, `MARQUE_P07`). Les étapes suivantes et le client s'y réfèrent par leur nom.
- Petites étapes : exécuter un bloc, afficher ce qu'on veut savoir avec `print`, regarder, continuer.
- Enregistrer après chaque passe.

## Passe 1 : formes et caméras

But : valider l'espace et **tous les cadrages** avec des formes grises.

1. Sol, murs, plafond si on le voit, grandes masses (trône, piliers, table, estrade) en cubes et cylindres gris, **à l'échelle réelle** en mètres.
2. Une **marque** par position de personnage : un objet vide (`Empty`) posé au sol, à l'endroit des pieds. Elle servira à placer le personnage et à faire la mise au point.
3. Un gabarit de personnage : un plan gris vertical de la taille du personnage (par exemple 0,7 × 1,6 m) sur chaque marque, pour juger sa taille dans le cadre.
4. **Toutes les caméras de la liste de plans**, nommées par plan, en vertical. Si un plan a un mouvement, poser la position de départ et la position d'arrivée.

```python
import bpy, math
s = bpy.context.scene

def cam(nom, pos, cible, focale=35):
    data = bpy.data.cameras.new(nom); data.lens = focale
    o = bpy.data.objects.new(nom, data)
    bpy.data.collections["CAMERAS"].objects.link(o)
    o.location = pos
    c = o.constraints.new("TRACK_TO"); c.target = bpy.data.objects[cible]
    c.track_axis, c.up_axis = "TRACK_NEGATIVE_Z", "UP_Y"   # une caméra regarde le long de -Z
    return o

cam("CAM_P07", (0.0, -4.2, 1.5), "MARQUE_P07", focale=35)
```

Focales en vertical : 24–28 mm pour un intérieur large, 35–50 mm pour un plan moyen, 85 mm et plus pour un gros plan d'objet. En vertical, le décor doit avoir de la **hauteur** (piliers, tentures, fenêtres hautes, plafond) : un décor pensé en largeur laisse le haut et le bas du cadre vides.

**Contrôle de la passe 1**
- `look(mode="camera")` pour chaque caméra (rendre active la caméra avant : `s.camera = bpy.data.objects["CAM_P07"]`).
- `look(mode="angles", views=["top","three_quarter"])` pour l'ensemble.
- Questions : le personnage est-il assez grand ? La marque est-elle hors des zones d'interface (haut ≈160 px, bas 360 px, droite ≈135 px) ? Y a-t-il un premier plan, un plan moyen et un fond ? Deux plans du même décor ont-ils des cadrages vraiment différents ?
- Montrer la planche au client avant d'aller plus loin.

## Passe 2 : lumière motivée

But : que l'image soit belle **en gris**, avant toute matière.

« Motivée » veut dire que chaque lumière a une source qu'on pourrait montrer dans le décor.

1. **Une lumière principale**, qui vient d'un endroit précis : la fenêtre, la porte ouverte, le feu. Une lumière de zone (`AREA`) placée dans l'ouverture, ou un soleil (`SUN`) qui passe par elle.
2. **Des sources visibles chaudes** : bougies, torches, lampes, braises. Chacune est un petit objet émissif **plus** une lumière ponctuelle au même endroit.
3. **Une HDRI Poly Haven faible** (force 0,2 à 0,6) pour déboucher les ombres, pas pour éclairer.
4. Deux températures : une ambiance (froide ou neutre) contre des sources chaudes. C'est ce contraste qui donne la richesse.
5. **Interdit** : l'éclairage studio à trois points (principale, débouchage, contre-jour posés autour du sujet sans raison). Il fait « rendu 3D » et tue le décor.

```python
# lumière principale dans la fenêtre
d = bpy.data.lights.new("Cle_Fenetre", "AREA"); d.energy = 900; d.color = (1.0, 0.85, 0.65)
d.shape = "RECTANGLE"; d.size, d.size_y = 1.2, 2.4
o = bpy.data.objects.new("Cle_Fenetre", d); bpy.data.collections["LUMIERES"].objects.link(o)
o.location = (-3.4, 1.0, 2.2); o.rotation_euler = (0, math.radians(-90), 0)

# source visible : une bougie
p = bpy.data.lights.new("Bougie_01", "POINT"); p.energy = 25; p.color = (1.0, 0.6, 0.3)
p.shadow_soft_size = 0.03
b = bpy.data.objects.new("Bougie_01", p); bpy.data.collections["LUMIERES"].objects.link(b)
b.location = (1.1, 0.4, 1.05)
```

Les puissances sont des points de départ : les régler en regardant l'image, pas en lisant les nombres.

**Contrôle de la passe 2**
- `look(mode="camera", shading="rendered")` depuis **3 caméras** au moins (le mode `rendered` fonctionne avec EEVEE et Workbench ; avec Cycles, faire un rendu d'une image et l'afficher avec `look(image="Render Result")`).
- Questions : y a-t-il du blanc brûlé ou du noir bouché ? Corriger la puissance des lumières avant de toucher à l'exposition. L'endroit le plus lisible de l'image est-il la marque du personnage ? Voit-on d'où vient la lumière ? Les ombres donnent-elles du relief aux formes grises ?
- Montrer ces images au client : c'est ici que se décide l'ambiance.

## Passe 3 : habillage

But : la richesse. C'est le contraste entre ce décor riche et des personnages très simples qui fait la signature de la 2.5D.

1. **Matières** : textures Poly Haven sur les grandes surfaces (`min_size_m=2` pour murs et sols). Rien de parfaitement propre : de la variation de couleur, de la rugosité qui change, de l'usure dans les creux et au bas des murs.
2. **Arêtes** : biseau sur tout ce qui est proche de la caméra.
3. **Tissus et grands motifs** : tentures, tapis, bannières. Ils remplissent la hauteur du cadre vertical.
4. **Petits accessoires**, groupés contre les grands, avec de légères différences de taille et d'angle (une rangée parfaite fait faux). Dupliquer avec `obj.copy()`.
5. **Profondeur de champ** sur chaque caméra, mise au point sur la marque.
6. **Air** : un léger volume ou de la poussière seulement si le rendu reste rapide ; sinon s'en passer.

Ne pas mélanger des objets bas en polygones et des objets photoréalistes dans la même image.

**Contrôle de la passe 3**
- Un vrai rendu par caméra, lu en grand.
- Une planche de toutes les caméras du décor.
- `get_scene_info(fields=["ground","size"])` : rien ne flotte, rien n'est sous le sol.
- Questions : le sujet se détache-t-il du fond ? Un détail brillant vole-t-il l'attention ? Le décor est-il lisible à la taille d'un téléphone (réduire l'image à 360 px de large et regarder) ?

## Mouvements de caméra

- Lents, avec une raison : une avancée (travelling avant) pour entrer dans une idée, un travelling latéral pour suivre, un plan fixe pour une réaction.
- Pas de dérive au hasard, pas de rotation permanente autour du sujet.
- Animer la **position** de la caméra (un vrai travelling : les objets proches bougent plus que le fond), pas seulement la focale.
- Deux clés par mouvement, interpolation douce en entrée et en sortie. Amplitude courte : sur 2 secondes, 20 à 40 cm d'avancée à échelle humaine suffisent.

```python
c = bpy.data.objects["CAM_P18"]
c.location = (0, -4.2, 1.5); c.keyframe_insert("location", frame=1230)
c.location = (0, -3.9, 1.5); c.keyframe_insert("location", frame=1290)
```

## Erreurs fréquentes

| Erreur | Correction |
|---|---|
| Décor construit puis caméras posées à la fin | Les caméras se posent en passe 1, avant toute matière. |
| Lumière plate, tout est visible pareil | Baisser la HDRI, garder une seule lumière principale, laisser des zones sombres. |
| Sources chaudes invisibles à l'image | Ajouter un petit objet émissif à l'endroit de la lumière ponctuelle. |
| Décor « large » dans un cadre vertical | Ajouter de la hauteur : piliers, tentures, plafond, premier plan en bas du cadre. |
| Tout est net | Activer la profondeur de champ, mise au point sur la marque. |
| Surfaces propres comme du plastique | Variation de couleur et de rugosité, usure. |
| Trente décors pour une minute | 3 à 5 décors, plusieurs caméras chacun. |
