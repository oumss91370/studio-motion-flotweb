---
name: blender
description: "Piloter Blender (4.2 ou plus récent) par le connecteur MCP `blender` pour fabriquer des décors 3D éclairés, des objets en vrai 3D et des plans rendus en vertical 1080×1920, puis les envoyer vers HyperFrames. À utiliser dès qu'une vidéo demande de la 3D ou de la 2.5D (décor éclairé, objet héros, profondeur de champ, personnages plats dans un décor 3D)."
---

# Blender par le connecteur MCP

Blender sert à ce que le HTML ne sait pas faire : de la vraie lumière, de vraies ombres, de la profondeur de champ, un objet qu'on peut filmer de près. L'assemblage final (montage, sous-titres, voix, son) reste dans HyperFrames (skill `rendu`).

Le parcours général est piloté par `studio-coeur`. Les règles de mouvement viennent de `principes-mouvement`, le son de `son`, les personnages plats de `personnages`.

## Quand passer par Blender

| Besoin | Outil |
|---|---|
| Décor éclairé, ombres portées, flou de profondeur, objet filmé en gros plan | **Blender** |
| Personnages plats debout dans un décor 3D (2.5D) | **Blender** (personnages en plans) |
| Objet simple qui tourne, sans lumière travaillée | Three.js dans HyperFrames suffit |
| Texte, sous-titres, graphiques, transitions | HyperFrames |

Version : Blender 4.2 ou plus récent (méthode testée en 5.3). Le connecteur accepte Blender 3.0+, mais ce skill n'est écrit que pour 4.2+.

## Les 9 outils du connecteur

Le connecteur s'appelle `blender` (outils `mcp__blender__…`). L'agent écrit lui-même le Python de Blender ; le connecteur ajoute ce que Python ne fait pas seul : **voir**.

| Outil | À quoi il sert |
|---|---|
| `get_addon_status` | Version de Blender et de l'add-on, bibliothèques activées. **Premier appel de chaque session.** |
| `get_scene_info` | La scène en texte : une ligne par objet, avec les champs demandés (`location`, `size`, `ground`, `materials`, `settings`…). Pour les nombres, pas pour l'image. |
| `execute_blender_code` | Exécute du Python (`bpy`) dans le Blender ouvert du client. |
| `look` | **Voir** : `mode` = `viewport`, `camera`, `angles` (planche multi-vues) ou `frames` (bande d'animation) ; `shading` = `solid`, `material`, `rendered`, `wireframe`, `xray` ; ou `image=` pour afficher un rendu. |
| `search_assets` / `import_asset` | Chercher puis importer des HDRI, textures et modèles (Poly Haven, Sketchfab, Poly Pizza). |
| `generate_3d` | Génère un modèle 3D par IA. **Peut coûter un crédit au client : ne jamais l'appeler sans son accord.** |
| `disable_telemetry`, `record_trajectory_feedback` | Réglages de collecte de données (voir installation). |

Règle de base : **après chaque étape, `look`, puis lire l'image.** On juge l'image, pas l'intention. Garder `max_size` à 768 (défaut) pour les contrôles courants, monter à 1200–1600 seulement pour lire un détail : les images restent dans la conversation.

## Installation chez le client

Détail complet et dépannage : `references/installation.md`. En résumé :

1. Installer **Blender** (blender.org, ou `winget install BlenderFoundation.Blender` sous Windows) et **l'ouvrir une fois**.
2. Installer **uv** avec son installeur officiel (jamais `pip install uv`) : `winget install --id=astral-sh.uv -e` sous Windows, puis ouvrir un nouveau terminal.
3. Lancer `uvx mcp-for-blender setup` : il déclare le connecteur `blender` dans les applications trouvées, installe l'add-on et l'active.
4. **Quitter complètement** l'application Claude (sous Windows : depuis la zone de notification) et la rouvrir. Ouvrir Blender.
5. Dans Blender : touche `N` dans la vue 3D, onglet **MCP for Blender**, cocher **Poly Haven**, vérifier que le serveur tourne (sinon **Start MCP Server**). **Ne pas sauter la case Poly Haven** : sans elle, aucun HDRI ni texture réelle, tout le film sort en matières procédurales (constaté sur un film réel, voir `references/rendu-long-et-fiable.md`, § 9).
6. Vérifier avec `get_addon_status`.

**Piège Windows.** Si `setup` ou `install-addon` répond qu'il ne trouve pas le dossier des add-ons, c'est que le dossier `scripts\addons` de l'utilisateur n'existe pas encore. Le créer et l'indiquer :

```powershell
$v = "5.3"   # version de Blender installée, sous la forme majeure.mineure
$dossier = "$env:APPDATA\Blender Foundation\Blender\$v\scripts\addons"
New-Item -ItemType Directory -Force -Path $dossier | Out-Null
$env:BLENDERMCP_ADDONS_DIR = $dossier
uvx mcp-for-blender install-addon
```

Puis dans Blender : **Edit → Preferences → Add-ons**, chercher « MCP for Blender », cocher.

## Début de session

1. `get_addon_status` : noter la version de Blender (elle change des noms dans l'API, voir `references/bpy-portable.md`) **et les bibliothèques activées**. Si Poly Haven est désactivé, le dire à la personne et le lui faire activer avant de construire.
2. `get_scene_info` avec `fields=["location","size","settings"]` : savoir ce qui existe déjà. **Ne jamais vider une scène du client sans lui demander.**
3. Régler le format tout de suite (voir plus bas) : toutes les caméras se cadrent en vertical dès la première forme.
4. Enregistrer le fichier dans le dossier du projet (`bpy.ops.wm.save_as_mainfile(filepath=…)`) et enregistrer après chaque passe.

## Réglages de rendu (vertical)

```python
import bpy
s = bpy.context.scene
s.render.resolution_x, s.render.resolution_y = 1080, 1920
s.render.resolution_percentage = 100
s.render.fps, s.render.fps_base = 30, 1.0
s.render.image_settings.file_format = "PNG"
```

- **Rendre exactement en 1080×1920. Ne jamais rendre plus grand puis recadrer, ni agrandir après coup** : le cadrage, la profondeur de champ et la taille des détails doivent être jugés au format final.
- Le moteur se lit avant de s'écrire (son nom dépend de la version) : voir `references/rendu-et-export.md`.
- Unités en mètres, tailles réelles : une porte fait environ 2,1 m, une table 0,75 m, une personne 1,7 m.

## Construire un décor en 3 passes

Méthode complète, exemples de code et erreurs fréquentes : `references/decor-3-passes.md`.

**On s'arrête après chaque passe, on regarde, on corrige, et seulement ensuite on passe à la suivante.** Dans le parcours client, la passe 1 et la passe 2 sont montrées au client.

| Passe | Ce qu'on fait | Contrôle visuel obligatoire |
|---|---|---|
| **1. Formes et caméras** | Formes grises à la bonne échelle (murs, sol, grands meubles, marques au sol des personnages). **Toutes les caméras** de la liste de plans, déjà en vertical. | `look(mode="camera")` sur chaque caméra, plus une `look(mode="angles")` du décor entier. Rien d'important dans les zones d'interface. |
| **2. Lumière motivée** | Une lumière principale qui a une raison d'être dans le décor (fenêtre, porte ouverte, feu), des sources visibles chaudes (bougies, torches, lampes), une HDRI Poly Haven faible pour déboucher. **Pas d'éclairage studio trois points.** | Images en `shading="rendered"` depuis 3 caméras. Ni blanc brûlé, ni noir bouché ; le regard va là où le personnage se tiendra. |
| **3. Habillage** | Matières avec usure et variation, tissus, tapis, petits accessoires, profondeur de champ sur chaque caméra, mise au point là où le personnage se tient. | Un rendu réel par caméra, lu en grand, puis une planche de toutes les caméras. |

Réutiliser les décors : une vidéo de 60 s en demande 3 à 5, pas 30. Un décor = un fichier `.blend` (ou une scène), plusieurs caméras.

## Objet héros : toujours en vrai 3D

L'objet dont parle l'histoire n'est jamais un dessin plat. Il est construit à part, contrôlé seul, puis posé dans le décor. Détail : `references/objet-heros.md`.

1. Construire à l'échelle réelle, dans sa propre collection, sur un sol neutre.
2. **Biseauter toutes les arêtes** (une arête parfaitement vive n'existe pas et ne prend pas la lumière).
3. Matière avec de l'usure dans les creux.
4. **Planche 6 angles** avant toute mise en place :
   `look(mode="angles", target=["Heros"], views=["front","right","back","left","top","three_quarter"], shading="rendered", max_size=1400)`
5. Corriger, puis poser l'objet sur sa marque dans le décor et vérifier le contact avec `get_scene_info(query="Heros", fields=["ground","size"])`.

## Assets Poly Haven (CC0)

- Poly Haven : environ 2 400 HDRI, textures et modèles, **tous en CC0** (utilisables dans une vidéo monétisée, sans crédit obligatoire). Aucune clé, aucun compte.
- Chercher : `search_assets(source="polyhaven", query="intérieur chaud fin d'après-midi", asset_type="hdris", previews=3)`. La recherche comprend l'intention et fonctionne en français. `previews` montre des vignettes avant de télécharger.
- Importer : `import_asset(source="polyhaven", id="…", asset_type="textures", apply_to=["Mur"], resolution="2k")`. Sans `apply_to`, la matière est créée mais inutilisée.
- Résolution : **1k–2k** pour le fond, 4k seulement pour un gros plan. Blender se fige pendant le téléchargement (c'est normal), et chaque cran de résolution pèse environ quatre fois plus.
- Pour les murs et les sols, demander `min_size_m=2` pour que la texture ne se répète pas à l'image.
- Après chaque import de modèle : mettre à l'échelle d'après la boîte englobante renvoyée, poser au sol, vérifier l'orientation avec `look(mode="angles", target=[nom])`.
- **Par défaut, rester sur Poly Haven.** Sketchfab et Poly Pizza ont des licences variables (souvent CC BY : crédit obligatoire) ; ne les utiliser que si le client le demande, et noter le crédit dans le fichier de crédits de la vidéo.

## Profondeur de champ

```python
cam = bpy.data.objects["CAM_P07"]
cam.data.dof.use_dof = True
cam.data.dof.focus_object = bpy.data.objects["MARQUE_P07"]   # un objet vide posé là où se tient le sujet
cam.data.dof.aperture_fstop = 2.8
```

- Mise au point sur un objet vide (la « marque »), jamais sur une distance tapée à la main : si la caméra bouge, le point suit.
- Ouverture de départ : f/2,8 à f/4 pour un plan moyen à échelle humaine, f/1,8 à f/2,8 pour un gros plan d'objet. Plus l'objet est petit et proche, plus le flou est fort.
- Le flou sert à détacher le sujet. Si le sujet lui-même devient flou sur une partie du plan, fermer l'ouverture.
- Les petites sources lumineuses du fond (bougies, fenêtres) deviennent des disques doux : c'est voulu.

## Rendre une image ou une plage en ligne de commande

Quand on corrige, on ne rend jamais toute la vidéo : une image, ou les secondes concernées.

```bash
# une seule image
blender -b episode.blend -o //rendus/controle_#### -F PNG -x 1 -f 1262

# une plage (début et fin AVANT -a)
blender -b episode.blend -o //rendus/plan18_#### -F PNG -x 1 -s 1215 -e 1290 -a
```

- Les options sont lues dans l'ordre : `-o`, `-F`, `-s`, `-e` se placent **avant** `-f` ou `-a`.
- `//` veut dire « à côté du fichier .blend » ; `####` est le numéro d'image sur 4 chiffres.
- `-S "NomDeScene"` choisit la scène si le fichier en contient plusieurs.
- Sous Windows, si `blender` n'est pas reconnu, donner le chemin complet entre guillemets : `"C:\Program Files\Blender Foundation\Blender 5.3\blender.exe"`.
- Le rendu en ligne de commande ne passe pas par le connecteur : Blender peut rester ouvert, mais **enregistrer le fichier avant** (la commande lit le fichier sur le disque).
- Pour voir un rendu : `look(image="chemin/vers/controle_1262.png")`.

Choix du moteur, caméras liées à des repères, numéros d'image, encodage : `references/rendu-et-export.md`.

## Rendu long : au-delà de quelques dizaines d'images

Dès qu'un film a sa ligne de temps dans Blender (plusieurs centaines d'images), lire `references/rendu-long-et-fiable.md` **avant** de lancer. Ses règles viennent d'un film réel de 1 845 images rendu le 11/11/2026 sur une carte graphique intégrée (1 h 50, une dizaine de plantages repris seuls) :

1. **Profiler d'abord** : mesurer 4 à 6 images à pleine taille, annoncer la durée, alléger un réglage à la fois (7,5 → 3,6 s par image : échantillons, ombres à demi-résolution, textures procédurales allégées, portée des lumières).
2. **Régler selon la carte** : intégrée, dédiée, ou processeur seul.
3. **Le connecteur construit et enregistre ; la ligne de commande rend.** Un rendu lourd par le connecteur perd la connexion ou dépasse le délai.
4. **Jamais deux Blender en parallèle** sur une carte intégrée.
5. **Boucle de reprise** : le rendu saute les images déjà faites, une boucle le relance après un plantage ; re-rendu par plages d'images.
6. **Arrêter la boucle avant Blender** (sinon elle le relance : « boucle fantôme »), et ne jamais arrêter des processus par un filtre sur le nom : on tue aussi le pont du connecteur.
7. **Brume volumétrique** : motif en damier sur les gros plans à faible échantillonnage ; la couper plan par plan.
8. **Vue « Standard »** plutôt qu'AgX quand il y a des aplats (personnages plats).

Les outils correspondants (boucle, re-rendu par plages, suivi, profilage) sont dans le kit de la catégorie `styles-2-5d` (`kit/`), en Python pour Windows, macOS et Linux.

**Décor peint en trois passes.** Quand le style demande un décor peint dont la lumière se règle par ambiance (style `tete-ronde-trait-plein-delie`), on ne cuit pas la lumière dans le rendu : on rend la couleur, la lumière et les données en trois passes, et on compose ensuite. Méthode, chiffres et pièges : `references/trois-passes-et-matieres-peintes.md`.

## Export vers HyperFrames

1. Un plan = une suite d'images PNG en 1080×1920, numérotée avec les **numéros d'image de la vidéo** (le plan 18 qui commence à l'image 1215 s'appelle `plan18_1215.png`, etc.).
2. Encoder chaque plan en MP4 (sans son) avec ffmpeg, à 30 i/s, sans changer la taille.
3. Dans HyperFrames, poser chaque plan comme une vidéo muette à son instant (`image ÷ 30` secondes). Les sous-titres, la voix, la musique et les bruitages s'ajoutent dans HyperFrames (skills `rendu` et `son`).
4. Vérifier le fichier final : 1080 par 1920, 30 i/s, durée prévue.

Commandes exactes : `references/rendu-et-export.md`.

## Contrôles avant de dire « c'est prêt »

- [ ] Chaque passe a été regardée avec `look` avant la suivante.
- [ ] Format 1080×1920, 100 %, 30 i/s (lu dans `get_scene_info(fields=["settings"])`).
- [ ] Rien ne flotte, rien ne traverse : champ `ground` de `get_scene_info` sur les objets posés.
- [ ] Une lumière principale motivée, au moins une source chaude visible, pas de trois points studio.
- [ ] L'objet héros a sa planche 6 angles, arêtes biseautées.
- [ ] Mise au point sur la marque du sujet pour chaque caméra.
- [ ] Rien d'important dans les zones d'interface (haut ≈160 px, bas 360 px, droite ≈135 px).
- [ ] Fichier enregistré, plans rendus à la taille exacte, sans recadrage.
- [ ] Rendu long : temps par image mesuré et annoncé, un seul Blender, boucle de reprise, aucune boucle restante à la fin (`references/rendu-long-et-fiable.md`).

## Références

- `references/installation.md` : installation pas à pas, piège Windows, dépannage, sécurité et collecte de données.
- `references/decor-3-passes.md` : la méthode en 3 passes avec le code.
- `references/objet-heros.md` : construction et contrôle de l'objet héros.
- `references/rendu-et-export.md` : moteur, caméras, ligne de commande, export vers HyperFrames.
- `references/trois-passes-et-matieres-peintes.md` : décor peint rendu en trois passes (couleur, lumière, données), textures procédurales en diamètres de tête, fusion par matière, petits détails au sol (essai réel du 12/11/2026).
- `references/rendu-long-et-fiable.md` : profilage, réglages par carte, boucle de reprise, boucle fantôme, brume, vue « Standard », Poly Haven (rendu réel du 11/11/2026) ; § 11 : une plaque de décor par tronçon de caméra (essai du 12/11/2026).
- `references/bpy-portable.md` : écrire du Python Blender qui marche sur la machine d'un autre.

Crédits : voir `licenses/blender.md` à la racine du plugin.
