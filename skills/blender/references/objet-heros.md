# L'objet héros en vrai 3D

Règle : **l'objet dont parle l'histoire n'est jamais un dessin plat.** Il a ses gros plans, sa lumière, son moment. C'est lui que le spectateur doit pouvoir décrire après la vidéo.

Il se construit **à part**, se contrôle **seul**, et n'entre dans un décor qu'une fois validé.

## 1. Préparer

- Une image de référence ou une description précise fournie par le client. Pour un objet historique, noter dans les sources d'où vient la description (dimensions, matière, nombre d'éléments).
- Une collection `HEROS`, un sol neutre gris clair, une lumière simple (une grande lumière de zone de côté et une HDRI neutre faible). Ce banc d'essai ne sert qu'au contrôle.

## 2. Construire

- **Échelle réelle**, en mètres. Un objet de 30 cm fait 0,30 m. La profondeur de champ et la lumière ne se comportent bien qu'à la bonne échelle.
- Formes simples d'abord (silhouette), détails ensuite.
- **Biseauter toutes les arêtes** : modificateur Bevel, 2 à 3 segments, largeur de 1 à 3 % de la plus petite dimension. C'est le biseau qui accroche la lumière.
- Les parties qui bougent (un couvercle, une bille, une aiguille) sont des objets séparés, avec leur point de pivot au bon endroit, rattachés à un objet vide racine `Heros`.
- Origine de la racine au point de contact avec le sol : l'objet se pose en donnant simplement sa position.

```python
o = bpy.data.objects["Heros_Corps"]
m = o.modifiers.new("Biseau", "BEVEL"); m.segments = 3; m.width = 0.004
```

## 3. Matière avec usure

- Une matière principale (métal, bois, pierre, céramique) et, si besoin, une matière d'accent.
- De l'usure dans les creux : assombrir et rendre plus mat là où la surface est concave, éclaircir légèrement les arêtes. Avec les nœuds de matière : l'entrée « Pointiness » du nœud Geometry (Cycles), ou une occlusion ambiante, mélangée à la couleur et à la rugosité.
- De la variation : une texture de bruit très large qui fait varier la couleur de quelques pour cent et la rugosité.
- Chercher les nœuds par leur type, pas par leur nom (voir `bpy-portable.md`).

## 4. Planche 6 angles

```
look(mode="angles", target=["Heros"],
     views=["front","right","back","left","top","three_quarter"],
     shading="rendered", max_size=1400)
```

Lire la planche et vérifier :

- **Silhouette** : reconnaît-on l'objet en ombre chinoise, sous chaque angle ?
- **Proportions** : conformes à la référence ?
- **Arêtes** : un liseré clair sur les bords (le biseau travaille) ?
- **Matière** : ni plastique ni miroir ; l'usure se voit dans les creux ?
- **Dessous et dos** : pas de face manquante, pas de trou.
- **Lisibilité à petite taille** : réduire mentalement à 200 px ; le détail qui compte dans l'histoire se voit-il encore ?

Contrôle complémentaire en fil de fer pour les intersections : `look(mode="angles", target=["Heros"], shading="wireframe")`.

Corriger et refaire la planche jusqu'à ce que les six vues soient bonnes. Montrer la planche au client.

## 5. Poser dans le décor

1. Lier ou ajouter la collection `HEROS` dans le fichier du décor.
2. Poser la racine sur sa marque.
3. Vérifier le contact : `get_scene_info(query="Heros", fields=["ground","size","location"])`. Le champ `ground` dit si l'objet est posé, flotte ou traverse.
4. Regarder par la caméra du gros plan : `look(mode="camera", shading="rendered")`.
5. Donner à l'objet sa propre lumière motivée s'il le faut (un rayon de la fenêtre, une bougie proche), jamais un projecteur sans source.

## 6. Animer l'objet

- Les temps clés viennent de la liste de plans, en **numéros d'image**.
- La physique tient l'animateur honnête : une chute de 30 cm dure environ un quart de seconde, soit 7 à 8 images à 30 i/s. Plus lent, l'objet a l'air de flotter. Une chute accélère (entrée douce, arrivée rapide), sans rebond si la matière est lourde.
- Contrôler le mouvement en bande : `look(mode="frames", frames=[1254,1256,1258,1260,1262,1264], view="camera")`.
- Le bruitage de l'impact se cale sur l'image du contact (skill `son`).

## Liste de contrôle

- [ ] Échelle réelle, origine au point de contact.
- [ ] Toutes les arêtes biseautées.
- [ ] Usure et variation dans la matière.
- [ ] Planche 6 angles lue et validée.
- [ ] Contact au sol vérifié dans le décor.
- [ ] Au moins un gros plan prévu dans la liste de plans.
