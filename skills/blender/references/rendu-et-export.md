# Rendu et export vers HyperFrames

## Format

```python
import bpy
s = bpy.context.scene
s.render.resolution_x, s.render.resolution_y = 1080, 1920
s.render.resolution_percentage = 100
s.render.fps, s.render.fps_base = 30, 1.0
s.render.image_settings.file_format = "PNG"
s.render.image_settings.color_mode = "RGB"      # "RGBA" si le fond doit être transparent
```

Rendre **à la taille exacte**. Jamais plus grand puis recadré, jamais agrandi après : le cadrage vertical est une autre mise en page, pas un recadrage d'une image large.

Vérifier : `get_scene_info(fields=["settings"])` renvoie le moteur, la plage d'images, la résolution et la caméra.

## Choisir le moteur

| Moteur | Quand | Remarques |
|---|---|---|
| **EEVEE** | Par défaut. Rapide (souvent moins d'une seconde à quelques secondes par image), suffisant pour un décor stylisé éclairé. | `look(shading="rendered")` fonctionne directement. |
| **Cycles** | Gros plan de l'objet héros, verre, métal poli, lumière très douce. | Plus lent. Carte graphique utilisée automatiquement ; sur processeur seul, réduire les échantillons. `look(shading="rendered")` ne fonctionne pas : rendre une image puis `look(image="Render Result")`. |

Le nom du moteur change selon la version (EEVEE s'appelle `BLENDER_EEVEE_NEXT` de 4.2 à 4.x, `BLENDER_EEVEE` avant et à partir de 5.0). Ne jamais l'écrire en dur :

```python
def choisir_moteur(scene, souhaites=("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE")):
    for nom in souhaites:
        try:
            scene.render.engine = nom
            return nom
        except TypeError:
            pass
    return scene.render.engine

print(choisir_moteur(bpy.context.scene))
```

Échantillons de départ : EEVEE 32 à 64 pour le contrôle, 64 à 128 pour le rendu final ; Cycles 32 pour le contrôle, 96 à 192 avec débruitage pour le final. Ces valeurs supposent une carte graphique dédiée et un film court. **Sur une carte intégrée, ou pour un film de plusieurs centaines d'images, profiler d'abord** : le film réel du 11/11/2026 a été rendu à 8 échantillons (3,6 s par image au lieu de 7,5). Voir `rendu-long-et-fiable.md`.

Garder **le même moteur et le même réglage de couleur pour tous les plans d'une vidéo**, sinon les plans ne raccordent pas.

## Numéros d'image

Convention du studio : **le numéro d'image dans Blender est le numéro d'image de la vidéo** (image = secondes × 30, la vidéo commence à l'image 0). Un plan qui va de 40,5 s à 43,0 s occupe les images 1215 à 1289.

Ainsi une correction s'écrit « déplacer le contact à l'image 1262 » et vaut pour le script, Blender, le son et HyperFrames.

## Une caméra par plan : les repères

Lier chaque caméra à un repère de la ligne de temps : Blender change de caméra tout seul à cette image, y compris en ligne de commande.

```python
s = bpy.context.scene
for nom, image in (("CAM_P18", 1215), ("CAM_P19", 1266)):
    m = s.timeline_markers.new(nom, frame=image)
    m.camera = bpy.data.objects[nom]
```

## Rendre depuis le connecteur (contrôle)

```python
s = bpy.context.scene
s.frame_set(1262)
s.render.filepath = "//rendus/controle_1262"
bpy.ops.render.render(write_still=True)
```

Puis `look(image="Render Result")`. Pour une bande d'animation sans rendu complet : `look(mode="frames", frames=[1254,1258,1262,1266], view="camera", shading="rendered")`.

Ne pas lancer un rendu long par le connecteur (délai dépassé, Blender figé, connexion perdue : constaté sur un rendu pleine résolution le 11/11/2026) : au-delà de quelques images, passer en ligne de commande. Le connecteur construit et enregistre, la ligne de commande rend.

## Rendre en ligne de commande

```bash
# une image
blender -b decor2.blend -o //rendus/controle_#### -F PNG -x 1 -f 1262

# une plage : les secondes autour d'une correction
blender -b decor2.blend -o //rendus/plan18_#### -F PNG -x 1 -s 1215 -e 1290 -a
```

| Option | Rôle |
|---|---|
| `-b` | Sans interface. |
| `-o chemin` | Dossier et nom des images. `//` = à côté du fichier ; `####` = numéro d'image. |
| `-F PNG` | Format. |
| `-x 1` | Ajoute l'extension. |
| `-s`, `-e` | Première et dernière image. **Avant `-a`.** |
| `-f N` | Rend l'image N. |
| `-a` | Rend la plage. |
| `-S nom` | Scène à rendre, si le fichier en a plusieurs. |

Les options sont lues dans l'ordre : tout ce qui règle la sortie se place avant `-f` ou `-a`.

À savoir :
- La commande lit le fichier **sur le disque** : enregistrer avant.
- Sous Windows, si `blender` n'est pas reconnu : `"C:\Program Files\Blender Foundation\Blender 5.3\blender.exe" -b …`.
- Un seul rendu à la fois par carte graphique : deux en parallèle vont moins vite que deux à la suite, et **sur une carte intégrée le pilote plante à coup sûr**.
- Lancer les rendus longs en arrière-plan, **par une boucle de reprise** (les images déjà faites sont sautées, le rendu repart après un plantage), et compter les fichiers produits pour suivre l'avancement. Pour arrêter : la boucle d'abord, Blender ensuite. Méthode complète : `rendu-long-et-fiable.md`.
- Après une correction, **ne rendre que la plage touchée**, jamais toute la vidéo.

## Planche de contrôle des images rendues

```bash
# une image sur 15 du plan, en mosaïque
ffmpeg -y -framerate 30 -start_number 1215 -i rendus/plan18_%04d.png \
  -vf "select='not(mod(n\,15))',scale=270:-1,tile=6x1" -frames:v 1 revue/plan18.png
```

Lire la planche : rien ne saute, rien ne flotte, le sujet reste dans le cadre.

## Export vers HyperFrames

Blender fournit l'image des plans. HyperFrames les monte et ajoute tout le reste.

**1. Encoder chaque plan** (sans son, taille inchangée) :

```bash
ffmpeg -y -framerate 30 -start_number 1215 -i rendus/plan18_%04d.png \
  -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p -movflags +faststart plans/plan18.mp4
```

**2. Vérifier** chaque fichier :

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,nb_frames -of json plans/plan18.mp4
```

On doit lire 1080, 1920, `30/1` et le nombre d'images attendu.

**3. Poser dans HyperFrames** : chaque plan est une vidéo muette placée à `image de début ÷ 30` secondes, pour une durée de `nombre d'images ÷ 30`. Suivre le skill `rendu` pour la syntaxe exacte de la composition. Ne jamais mettre la vidéo à l'échelle dans la page.

**4. Ajouter dans HyperFrames** : sous-titres, voix, musique, bruitages, carton éventuel. Pas dans Blender.

**Variante avec fond transparent** (un élément 3D à poser sur une composition HyperFrames) : `film_transparent = True`, PNG en `RGBA`, puis encodage en WebM avec couche alpha :

```bash
ffmpeg -y -framerate 30 -start_number 1 -i passe_%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 20 passe.webm
```

## Couleur

- Le réglage « View Transform » de Blender (AgX ou Filmic par défaut selon la version) modifie les couleurs à la sortie : c'est bon pour un décor éclairé, mais cela ternit les aplats des personnages plats (mesuré en 5.3 : `#F2C9A0` sort en `#C2AF9D` avec AgX, à l'identique avec « Standard »). Voir le skill `personnages`, `references/import-blender.md`.
- Si l'image paraît délavée ou pastel, c'est en général trop de lumière : baisser la puissance des lampes avant de toucher à l'exposition.
- Ne pas ajouter de grain dans Blender ; s'il en faut, l'ajouter à l'assemblage.

## Contrôle final (après l'assemblage HyperFrames)

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,duration -of json sortie/episode.mp4
```

1080 par 1920, `30/1`, la durée prévue.
