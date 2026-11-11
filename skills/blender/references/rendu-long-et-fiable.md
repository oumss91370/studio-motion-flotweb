# Rendu long et fiable

Rendre un plan de 60 images se fait sans y penser. Rendre un film de 1 800 images sur l'ordinateur d'un client, sans le surveiller, demande une méthode. Celle-ci vient d'un rendu réel.

**D'où viennent ces règles.** Un film de 61,5 s (1 845 images en 1080×1920, 36 plans, trois décors, brume volumétrique, personnages plats) rendu par le studio le 11/11/2026 sur un PC Windows à **carte graphique intégrée**, Blender 5.3, EEVEE, piloté par le connecteur MCP. Résultat : 1 h 50 de machine, une dizaine de plantages du pilote graphique, tous repris sans intervention. Ce qui est mesuré ce jour-là est dit « mesuré » ; le reste est une valeur de départ à vérifier sur la machine du client.

Les outils cités (`rendre.py`, `refaire.py`, `suivi.py`) sont ceux du kit de la catégorie `styles-2-5d-histoire-vraie` (`kit/`, lire son `LISEZMOI.md`). Ils valent pour tout film dont la ligne de temps est dans Blender.

## 1. Profiler avant le rendu complet

Ne jamais lancer un rendu complet sans avoir mesuré le temps d'une image. Une minute de mesure évite une heure d'attente.

1. Rendre **à pleine taille** 4 à 6 images prises dans des plans différents : un plan large, un gros plan, le plan le plus chargé en lumières, un plan avec brume. Avec le kit : `python outils/rendre.py --profiler` (il annonce la moyenne et la durée du film).
2. Multiplier : `secondes par image × nombre d'images`. À 7,5 s par image, 1 845 images font 3 h 50 ; à 3,6 s, 1 h 50.
3. **Annoncer ce chiffre à la personne avant de lancer**, avec le nombre de tours de correction qu'il permet dans la journée.
4. Si c'est trop long, alléger **un réglage à la fois**, re-mesurer, et **regarder l'image** : un réglage qui ne se voit pas est gratuit, un réglage qui se voit est un choix.

Ce qui a fait passer le film réel de **7,5 à 3,6 s par image** (mesuré, carte intégrée, EEVEE). Le compte rendu cite ces quatre leviers ensemble, sans donner le gain de chacun ; les mesurer un par un sur sa propre scène :

| Levier | Avant → après | Ce que ça coûte à l'image |
|---|---|---|
| Échantillons de rendu | 16 → 8 (`scene.eevee.taa_render_samples`) | bords un peu moins lisses ; **tramage visible en pleine taille sur les aplats sombres** ; la brume volumétrique tramée en damier sur les gros plans (voir § 7) |
| Résolution des ombres | pleine → moitié (`scene.eevee.shadow_resolution_scale = 0.5`) | ombres portées moins fines : à juger sur un gros plan |
| Textures procédurales | allégées. Dans le code du film : un même bruit pour la couleur et la rugosité, `Detail` à 3, un second bruit à `Detail` 2 pour le relief (l'état d'avant n'est pas consigné) | matières moins fines de près |
| Portée des lumières | limitée à 11 m sur les lampes ponctuelles (`light.use_custom_distance = True`, `light.cutoff_distance = 11`) | rien, tant que la portée couvre la pièce |

La scène du film avait aussi le lancer de rayons, le flou de mouvement et le bokeh à jitter coupés (`use_raytracing`, `use_motion_blur`, `use_bokeh_jittered` à `False`) ; leur effet sur le temps n'a pas été mesuré à part.

À ne **pas** faire pour gagner du temps : baisser la résolution puis agrandir (le cadrage et les sous-titres se jugent au format final), ni rendre une image sur deux.

## 2. Réglages par type de carte

Lire la carte dans les préférences de Blender ou demander à la personne. Carte intégrée : le processeur graphique fait partie du processeur (ordinateurs portables de bureau, mini-PC). Carte dédiée : une carte séparée, avec sa propre mémoire.

| | Carte graphique intégrée | Carte graphique dédiée | Pas de carte utilisable |
|---|---|---|---|
| Moteur | EEVEE | EEVEE (Cycles pour un gros plan de verre ou de métal poli) | Cycles sur processeur |
| Échantillons | **8** (mesuré) | 32 à 64 (valeur de départ du skill, non mesurée sur le film réel) | 16 avec débruitage |
| Ombres | demi-résolution | pleine | sans objet |
| Portée des lampes ponctuelles | limitée (11 m) | libre | libre |
| Brume volumétrique | plans larges seulement | partout, à contrôler en gros plan | à éviter |
| Temps par image, 1080×1920 | **3,6 s** (mesuré ; 7,5 s avant allègement) | non mesuré ; estimation du compte rendu : cinq à dix fois plus rapide | **65 s** (mesuré sur 2 cœurs, scène d'exemple du kit) : pour des contrôles à taille réduite seulement |
| Rendus en parallèle | **jamais** | un seul reste la règle | un seul |
| Plantages du pilote | fréquents (une dizaine sur 1 845 images) : boucle de reprise obligatoire | rares ; garder la boucle | aucun constaté |

Dans le kit, ces trois colonnes sont les profils `integree`, `dediee` et `processeur` de `outils/reglages.py`.

Garder **le même moteur, les mêmes échantillons et le même réglage de couleur pour tous les plans** d'un film : un plan re-rendu avec d'autres réglages ne raccorde plus.

## 3. Le connecteur construit, la ligne de commande rend

| Par le connecteur MCP (`execute_blender_code`, `look`) | En ligne de commande, sans interface |
|---|---|
| construire la scène, poser caméras et lumières | le rendu du film |
| regarder (`look`), rendre **une** image de contrôle, quelques images à taille réduite | tout rendu de plus de quelques images à pleine taille |
| **enregistrer le fichier** | les planches de contrôle de tous les plans |

Pourquoi (constaté le 11/11/2026) : un rendu pleine résolution lancé par le connecteur a fait **perdre la connexion** à Blender ; un rendu long y finit de toute façon en **délai dépassé**, et Blender reste figé pour la personne pendant ce temps.

La ligne de commande lit le fichier **sur le disque** : enregistrer avant chaque rendu, sinon on rend l'ancienne version. Avec le kit, la scène est reconstruite et enregistrée par `python outils/rendre.py --construire`, et rien n'oblige à garder Blender ouvert.

Pour juger une image, préférer un **rendu à basse résolution relu en planche** à la vue 3D : la vue ne montre ni les plans émissifs des personnages plats tels qu'ils sortiront, ni la profondeur de champ. (Sur le film réel, l'outil `look` n'a presque pas servi pour cette raison.)

## 4. Jamais deux Blender en parallèle sur une carte intégrée

Deux rendus en même temps sur une carte intégrée : le pilote graphique plante **à coup sûr** (constaté), et quand il ne plante pas, les deux vont moins vite qu'à la suite. Cela vaut aussi pour « un rendu de contrôle pendant que le film tourne » et pour un Blender ouvert dont la vue est en mode rendu.

- Un seul processus de rendu à la fois. Le kit pose un verrou (`rendus/.verrou`) et refuse une deuxième boucle.
- Pendant un rendu long, ne rien demander d'autre à la carte : pas de `look(shading="rendered")`, pas de second rendu « juste pour voir ».
- Pour gagner du temps, on allège (§ 1) ou on change de machine ; on ne parallélise pas.

## 5. La boucle de reprise

Principe : **le rendu saute les images qui existent déjà ; une boucle le relance tant qu'il en manque.** Un plantage coûte alors l'image en cours, pas le film.

- Dans la scène : `scene.render.use_overwrite = False` (une image déjà sur le disque n'est pas refaite) et `scene.render.use_placeholder = False`.
- Autour : tant qu'il manque des images dans la plage, relancer `blender -b film.blend -o <dossier>/f_#### -s <début> -e <fin> -a` ; s'arrêter quand il n'en manque plus, ou après trois essais de suite sans aucune image nouvelle (l'erreur est alors dans la scène, pas dans le pilote).
- Un fichier incomplet peut rester après un plantage : si une image est illisible ou de taille nulle, la déplacer et relancer.
- Nommer les fichiers par **le numéro d'image de la vidéo**. Re-rendre une plage, c'est déplacer ces fichiers-là et relancer la boucle : le film se recolle tout seul.
- Ne jamais supprimer : déplacer les images remplacées dans un dossier à part, que la personne videra.

Avec le kit (tout en Python, mêmes commandes sous Windows, macOS et Linux) :

```
python outils/rendre.py               tout le film, avec reprise
python outils/rendre.py 914 983       une plage
python outils/suivi.py --boucle       avancement, cadence, fin estimée (dans un autre terminal)
python outils/refaire.py tour1 914-983 1242-1287    re-rendu par plages : anciennes images déplacées, trous comblés
python outils/rendre.py --arreter     arrêt propre
```

Essai du kit (11/11/2026, exemple de 90 images, Cycles sur processeur à taille réduite) : avec un arrêt brutal simulé toutes les 20 images, la boucle a repris 4 fois et rendu les 90 images sans en perdre ni en refaire. Sur le film réel, la même mécanique (alors un script shell) a repris 9 plantages du pilote.

## 6. Le piège de la boucle fantôme

Ce qui est arrivé : pour arrêter le rendu, l'agent a tué **Blender**. La **boucle** qui le relançait, elle, vivait toujours : elle a relancé un Blender. Un nouveau rendu a ensuite été lancé par-dessus. Pendant un quart d'heure, **deux rendus ont tourné en même temps** : lenteur, plantages, et des images d'une ancienne version de la scène mêlées aux nouvelles. Il a fallu tout arrêter, écarter les images douteuses et relancer.

Puis, en nettoyant, un filtre trop large (« arrêter tout ce qui ressemble à Blender ») a aussi tué **le pont du connecteur** (le processus `mcp-for-blender`). Il s'est relancé seul, sans perte, mais la session aurait pu s'arrêter là.

Règles :

1. **Arrêter la boucle avant Blender.** Toujours dans cet ordre. Avec le kit : `python outils/rendre.py --arreter` demande à la boucle de s'arrêter, et c'est elle qui arrête son propre Blender.
2. **Ne jamais arrêter des processus par un filtre sur le nom** (`taskkill /IM blender.exe`, `pkill -f blender`, `Get-Process *blender* | Stop-Process`). Ces filtres attrapent le Blender que la personne a ouvert, et le pont du connecteur dont le nom contient « blender ». Arrêter **un processus précis, par son numéro**, celui qu'on a lancé soi-même.
3. **Avant de relancer, vérifier qu'il ne reste rien** : aucune boucle, aucun Blender sans interface (`python outils/suivi.py` dit « boucle de rendu : ARRÊTÉE »).
4. **Après un doute, vérifier les images** : trier le dossier par date. Des images plus anciennes que le dernier enregistrement de la scène dans une plage censée être refaite sont à déplacer et à re-rendre.
5. Une tâche de fond qu'on « arrête » dans l'outil de l'agent n'arrête pas forcément les processus qu'elle a lancés : contrôler.

## 7. Brume volumétrique : le damier

À faible échantillonnage (8 échantillons), la brume volumétrique d'EEVEE dessine un **motif en damier** sur les gros plans : la brume est calculée par tuiles et il n'y a pas assez d'échantillons pour les fondre. Sur un plan large, le motif se perd dans le décor et la brume fait son travail (rais de lumière).

- Garder la brume sur les plans larges ; **la couper sur les gros plans** (11 plans sur 36 dans le film réel), en posant une clé à interpolation constante sur sa densité au début de chaque plan.
- La régler plus légère sur les lointains, pour que les couches du paysage restent des silhouettes distinctes.
- Contrôler en **pleine taille**, pas sur une planche : le damier disparaît à la réduction.
- Sur une carte dédiée, monter les échantillons avant de couper la brume (non essayé).

## 8. Vue « Standard » plutôt qu'AgX pour les aplats

Avec la vue AgX (le réglage par défaut), la peau des personnages plats sortait **grise**. En vue « Standard », un aplat sort à sa couleur : peau mesurée à (242, 207, 165) pour (246, 210, 169) dessiné.

```python
s = bpy.context.scene
s.view_settings.view_transform = "Standard"
s.view_settings.look = "None"
```

Contrepartie mesurée : en « Standard », **les flammes et les fenêtres saturent plus vite**. Baisser la puissance des lumières jusqu'à ce qu'aucune zone ne soit blanche, plutôt que de revenir à AgX. Choisir une fois pour tout le film. Détail et variante en deux passes : skill `personnages`, `references/import-blender.md`.

## 9. Activer Poly Haven dans le connecteur, avant de commencer

Sur le poste du rendu réel, les bibliothèques du connecteur (Poly Haven, Sketchfab, générateurs) étaient **désactivées**. Conséquence : aucune texture réelle, aucun HDRI, **tout le film en matières procédurales**. C'est la première cause de la pauvreté des décors relevée par la critique.

- Au début de la session, `get_addon_status` dit quelles bibliothèques sont activées. Si Poly Haven ne l'est pas, **le dire à la personne et le lui faire activer avant de construire** : dans Blender, touche `N` dans la vue 3D, onglet « MCP for Blender », cocher « Poly Haven » (voir `installation.md`).
- Poly Haven est en CC0 : c'est la bibliothèque par défaut. Sketchfab et les générateurs ne s'activent que si la personne le demande (licences variables, crédits possibles).
- Si la personne refuse ou ne peut pas : continuer en procédural, **et l'écrire dans la note de livraison** (« décors sans textures réelles »). Ne pas le découvrir à la critique.
- Les textures se téléchargent pendant la construction, par le connecteur ; le rendu en ligne de commande les relit ensuite depuis le fichier enregistré.

## 10. Où faire tourner le rendu

- EEVEE a besoin d'une carte graphique, et le connecteur pilote le Blender **du poste de la personne**. Un serveur sans carte ne sert à rien pour EEVEE : c'est le poste qui rend.
- Constat fait en écrivant le kit : EEVEE accepte de rendre sans carte, en rendu logiciel, sur une machine Linux (une image, 35 s au quart de la taille). C'est bon à savoir pour un contrôle, pas pour un film.
- Un film se rend bien la nuit ou pendant une autre étape (le son, les documents) : la boucle de reprise est faite pour ça.

## Liste de contrôle avant un rendu long

- [ ] Temps par image mesuré à pleine taille sur 4 à 6 images ; durée totale annoncée à la personne.
- [ ] Profil choisi d'après la carte ; mêmes réglages pour tous les plans.
- [ ] Vue « Standard », aucun blanc brûlé ; brume coupée sur les gros plans, contrôlée en pleine taille.
- [ ] Fichier **enregistré** ; `use_overwrite` à `False`.
- [ ] Aucun autre Blender en train de rendre, aucune boucle restante.
- [ ] Rendu lancé en ligne de commande par la boucle de reprise, pas par le connecteur.
- [ ] Suivi lancé ; on sait arrêter proprement (la boucle d'abord).
- [ ] À la fin : nombre d'images attendu, aucune image vide, dates cohérentes avec le dernier enregistrement.

## Ce qui n'a pas été essayé

Les réglages de la colonne « carte dédiée », le rendu sur plusieurs machines, Cycles sur carte graphique, et les commandes du kit lancées avec le programme `blender` sous Windows ou macOS (l'essai du kit a tourné avec le module Python `bpy` sous Linux). Les mesurer au premier usage et corriger ce document.
