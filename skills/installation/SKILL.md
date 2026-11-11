---
name: installation
description: "À utiliser à la toute première utilisation du plugin, avant la première vidéo, ou dès qu'un outil manque (« commande introuvable », Blender absent, HyperFrames ne se lance pas, pas de navigateur, connecteur Blender non connecté). Vérifie ce qui est installé sur la machine du client, installe ce qui manque avec son accord (Node, FFmpeg, HyperFrames et son navigateur, Python et numpy, puis Blender, uv et le connecteur MCP for Blender pour la 3D), et note le résultat pour ne pas recommencer à chaque vidéo."
---

# Installation et vérification du studio

Ce skill prépare la machine une fois pour toutes. Il passe **avant** tout le reste : le skill `studio-coeur` y renvoie à son étape 0 tant que le fichier `studio-motion.installe.json` n'existe pas dans le dossier de travail du client.

## Ce qu'il faut, et pour quoi

| Niveau | Outil | Sert à |
|---|---|---|
| Indispensable | Python 3.10 ou plus, numpy | scripts de contrôle du plugin (porte de livraison, textes, son) |
| Indispensable | Node.js 20 ou plus (avec `npx`) | lancer HyperFrames |
| Indispensable | FFmpeg et ffprobe | encodage, mesures, son |
| Indispensable | HyperFrames 0.9.33 et son navigateur | rendre la vidéo |
| 3D et 2.5D | Blender 4.2 ou plus | décors, objets et rendus 3D |
| 3D et 2.5D | uv, connecteur MCP for Blender | piloter Blender depuis la conversation |
| Confort | Playwright | relevé automatique des textes à l'écran |
| Confort | faster-whisper | horodatage d'une voix au mot (sous-titres) |
| Confort | earshot | écoute du mix par l'agent |

**Three.js n'a rien à installer** : il se charge dans la page du film (par npm ou par une copie dans `assets/vendor/`), comme GSAP. Les styles 3D légers marchent donc sans Blender ; chaque fiche de style dit quel moteur elle demande.

## Marche à suivre

1. **Vérifier.** Depuis le dossier de travail du client :

   ```
   PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/installation/scripts/verifier_installation.py" --json studio-motion.installe.json
   ```

   Sous Windows, si `python3` n'existe pas, essayer `python` puis `py -3`. Si Python lui-même manque, l'installer d'abord (Windows : `winget install Python.Python.3.12` ; macOS : `brew install python` ; Linux : `sudo apt-get install -y python3 python3-pip`), puis relancer.
   Le script n'installe rien : il affiche, pour chaque outil, « OK » ou « MANQUE » avec la commande à lancer sur ce système.

2. **Dire au client ce qui manque, en une fois, et demander son accord avant d'installer.** Une question à options : « tout installer », « seulement l'indispensable (vidéos 2D) », « je le fais moi-même ». Annoncer la place et le temps : Blender pèse plusieurs centaines de Mo, le navigateur de HyperFrames environ 150 Mo, earshot environ 2 Go de modèles.

3. **Installer dans cet ordre**, une commande à la fois, en lisant le résultat de chacune :
   1. Node, puis FFmpeg ;
   2. HyperFrames : `npx -y hyperframes@0.9.33 --version`, puis `npx -y hyperframes@0.9.33 browser ensure`, puis `npx -y hyperframes@0.9.33 doctor` (détails, télémétrie à couper et cas sans réseau : `skills/rendu/references/installation.md`) ;
   3. numpy ;
   4. si le client veut la 3D : Blender, uv, puis le connecteur (`skills/blender/references/installation.md`, **y compris le piège Windows du dossier des add-ons**), et l'activation de l'add-on dans Blender ;
   5. le confort, seulement si le client le demande.

   Une installation qui demande un mot de passe administrateur, un redémarrage ou une fenêtre à valider est faite par le client : lui donner la commande exacte et attendre.

4. **Revérifier** avec la même commande. Le fichier `studio-motion.installe.json` garde l'état (système, outils, ce qui manque). Tant qu'il manque de l'indispensable, ne pas commencer de vidéo.

5. **Essai réel de 30 secondes**, pour être sûr que la chaîne tourne : créer un projet HyperFrames d'essai avec l'exemple complet de `skills/rendu/references/contrat-et-boucle.md`, lancer `lint`, `check` et `render`, puis `skills/rendu/scripts/verifier-export.py` sur le MP4. Si la 3D est installée : ouvrir Blender, démarrer le serveur du connecteur, et demander une capture de la scène par le connecteur. Dire au client ce qui a marché et ce qui n'a pas marché, sans rien enjoliver.

## Règles

- Ne jamais installer sans l'accord du client, ni hors des gestionnaires de paquets officiels du système (winget, Homebrew, apt, snap) et des sites des éditeurs.
- Ne jamais demander, lire ni écrire un mot de passe.
- Ne pas mettre à jour un outil déjà présent et suffisant : une version plus récente de Blender ou de Node convient.
- HyperFrames reste épinglé en `0.9.33` : toutes les commandes du plugin l'écrivent ainsi.
- Si une installation échoue, donner le message d'erreur exact au client et la page du guide concernée ; ne pas contourner en désactivant une sécurité du système.
- Refaire la vérification quand le client change de machine, ou quand un outil est signalé manquant en cours de vidéo.

## Fichiers

- `scripts/verifier_installation.py` : vérification, commandes par système, état en JSON.
- Guides détaillés : `skills/rendu/references/installation.md` (Node, FFmpeg, HyperFrames, hors ligne), `skills/blender/references/installation.md` (Blender, uv, connecteur, dépannage), `skills/son/references/earshot.md`.
