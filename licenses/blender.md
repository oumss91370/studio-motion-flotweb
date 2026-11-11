# Crédits du skill `blender`

| Source | Auteur | Dépôt | Commit | Licence | Ce qui est repris |
|---|---|---|---|---|---|
| MCP for Blender (paquet `mcp-for-blender` 2.2.7, anciennement `blender-mcp`) | Siddharth Ahuja | https://github.com/ahujasid/mcp-for-blender | `2e4b0bc` | MIT | Description des 9 outils et de leurs paramètres (`src/blender_mcp/server.py`), étapes d'installation, variables d'environnement, dépannage, sécurité et collecte de données (`README.md`), logique de recherche du dossier des add-ons (`src/blender_mcp/addon_manager.py`, `setup_cli.py`), consignes du serveur et guides « scene » et « bpy » (`src/blender_mcp/guides/`). Reformulé en français ; aucun fichier du dépôt n'est copié dans le plugin. Projet tiers, sans lien avec la fondation Blender. |
| blender-claymation-skill | angrypenguinpng | https://github.com/angrypenguinpng/blender-claymation-skill | `0be7cc0` | MIT | Structure d'un skill Blender (contrôle des outils, plan, images d'essai peu coûteuses avant le rendu complet, rendu d'une plage après correction, planche de contrôle), notes d'API Blender 4.2 à 5.x (`SKILL.md`, `references/look-guide.md`, `scripts/contact_sheet.sh`). |
| Cours « How to build a 2.5D motion studio with Opus 5.5 (Full Course) » | article public, auteur non indiqué dans la copie analysée | — | — | — | Méthode en 3 passes (formes, lumière, habillage), règle de l'objet héros en 3D avec planche 6 angles, rendu à la taille exacte, rendu d'une image ou d'une plage en ligne de commande. Idées reformulées, sans reprise de texte. |
| Poly Haven | Poly Haven | https://polyhaven.com | — | CC0 | Bibliothèque d'assets recommandée (aucun asset n'est fourni avec le plugin). |
| Blender | Blender Foundation | https://www.blender.org | — | GPL (logiciel) | Options de ligne de commande et API Python, citées d'après la documentation. |

Vérification du studio : les extraits de code du skill (réglages de rendu, choix du moteur, caméra et contrainte, lumières, profondeur de champ, repères liés aux caméras) ont été exécutés dans Blender 5.3.0 (module `bpy`) lors de l'écriture.

Texte de la licence MIT : à joindre une fois dans la NOTICE du plugin, avec les mentions de droits d'auteur « Copyright (c) 2025 Siddharth Ahuja » et « Copyright (c) 2026 angrypenguinpng ».
