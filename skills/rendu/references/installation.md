# Installation chez le client (HyperFrames 0.9.33)

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

À faire une fois par machine. La personne est débutante : donne une commande à la fois, dis ce qu'elle fait, vérifie le résultat avant la suivante. Les installations de logiciels (Node.js, FFmpeg) sont lancées par la personne ou avec son accord explicite.

## Ce qu'il faut

| Élément | Version | Rôle |
| --- | --- | --- |
| Node.js | 22 ou plus | fait tourner la commande `hyperframes` |
| FFmpeg et FFprobe | version récente (6 ou plus) | encodage vidéo, son, contrôle du fichier |
| Chrome sans interface | celui que HyperFrames télécharge | dessine chaque image |
| Python 3 | 3.9 ou plus | scripts de contrôle du studio (facultatif pour le rendu lui-même) |
| Place et mémoire | environ 2 Go de disque, 8 Go de mémoire conseillés | chaque processus de rendu ouvre un Chrome (≈ 256 Mo) |

Aucun compte n'est nécessaire pour créer, contrôler, prévisualiser et rendre en local.

## Windows 10 / 11 (PowerShell)

```powershell
winget install OpenJS.NodeJS.LTS
winget install Gyan.FFmpeg
winget install Python.Python.3.12
```

Fermer puis rouvrir le terminal (sinon `node` et `ffmpeg` restent introuvables), puis :

```powershell
node --version
ffmpeg -version
ffprobe -version
setx HYPERFRAMES_NO_TELEMETRY 1
setx DO_NOT_TRACK 1
setx HYPERFRAMES_SKIP_SKILLS 1
```

Rouvrir encore le terminal (`setx` ne vaut que pour les terminaux ouverts après), puis passer à « Vérification ».

Pièges Windows :
- `python` peut ouvrir le Microsoft Store au lieu de Python : utiliser `py -3` ou le chemin complet.
- Dans PowerShell, un JSON écrit dans la commande perd ses guillemets : écrire le JSON dans un fichier et passer son chemin (`--variables-file valeurs.json`, `--grading etalonnage.json`).
- Garder les projets dans un chemin court, sans accent ni espace (par exemple `C:\videos\ma-video`). Les chemins de plus de 260 caractères sont corrigés depuis la 0.9.27, mais d'autres outils (FFmpeg, Python) y restent sensibles.
- Un antivirus peut ralentir le premier lancement de Chrome : relancer une fois avant de conclure à une panne.

## macOS

```bash
brew install node ffmpeg python
echo 'export HYPERFRAMES_NO_TELEMETRY=1' >> ~/.zshrc
echo 'export DO_NOT_TRACK=1' >> ~/.zshrc
echo 'export HYPERFRAMES_SKIP_SKILLS=1' >> ~/.zshrc
source ~/.zshrc
```

Sans Homebrew : installateur Node.js depuis nodejs.org, et binaires FFmpeg posés dans un dossier hors des projets (voir « FFmpeg sans gestionnaire de paquets »).

Piège macOS : dans un bac à sable d'agent très fermé, Chrome meurt au démarrage. Ce n'est pas une panne d'installation : livrer la composition contrôlée, le dire, et rendre hors du bac à sable. Ne jamais fabriquer un moteur de remplacement (images une à une avec un autre outil).

## Linux (Debian / Ubuntu) et serveur distant

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs ffmpeg python3
echo 'export HYPERFRAMES_NO_TELEMETRY=1' >> ~/.bashrc
echo 'export DO_NOT_TRACK=1' >> ~/.bashrc
echo 'export HYPERFRAMES_SKIP_SKILLS=1' >> ~/.bashrc
source ~/.bashrc
```

- Si Chrome ne démarre pas (bibliothèques système manquantes), `npx -y hyperframes@0.9.33 doctor` nomme ce qui manque ; sur Debian / Ubuntu, il s'agit le plus souvent de `libnss3 libatk-bridge2.0-0 libgbm1 libasound2 libxkbcommon0 libgtk-3-0` et de polices (`fonts-liberation fonts-noto-color-emoji`).
- Sans carte graphique, le résumé du rendu affiche `screenshot capture · software gpu` : c'est le chemin lent, normal sur un petit serveur. Réduire `--workers` si la mémoire manque.
- Dans un conteneur : vérifier `/dev/shm` (ligne dédiée de `doctor`).
- **Aperçu à distance** (tunnel, serveur, Codespaces) : depuis les versions 0.9.30 et 0.9.31, l'aperçu refuse les noms d'hôte qu'il ne sert pas (erreur 403). Nommer l'hôte, séparé par des virgules s'il y en a plusieurs :

```bash
HYPERFRAMES_PREVIEW_ALLOWED_HOSTS=studio.exemple.fr npx -y hyperframes@0.9.33 preview --background
```

## Vérification (toutes plateformes)

```bash
npx -y hyperframes@0.9.33 --version             # 0.9.33 (le premier appel télécharge la CLI)
npx -y hyperframes@0.9.33 telemetry status      # doit indiquer que la télémétrie est désactivée
npx -y hyperframes@0.9.33 browser ensure        # trouve ou télécharge le Chrome épinglé
npx -y hyperframes@0.9.33 doctor --json         # sort toujours avec le code 0 : lire les champs
```

Comment ces deux commandes se comportent vraiment (observé en 0.9.33) :

- `doctor --json` sort **toujours** avec le code 0, même quand quelque chose manque, et son `ok` global est `false` sur une machine normale : il compte `whisper-cpp`, les voix locales (Kokoro), la musique locale (MusicGen) et Docker, tous facultatifs. Ne regarder que les lignes **Node.js**, **FFmpeg**, **FFprobe** et **Chrome** : chacune doit avoir `"ok": true`.
- La ligne **Chrome** dit où il a été trouvé : `cache: …/.cache/hyperframes/chrome/…` (celui que HyperFrames a téléchargé), `env: …` (celui désigné par `HYPERFRAMES_BROWSER_PATH`). Si elle dit « Chrome not found … Run: npx hyperframes browser ensure », lancer `browser ensure`.
- `browser ensure` cherche d'abord sur la machine. S'il répond `Source: cache` et « Ready to render », le Chrome était déjà là (téléchargé lors d'une autre session ou par un autre projet) : **rien n'a été téléchargé**. Un « Chrome not found » de `doctor` suivi d'un `Source: cache` de `browser ensure` a été vu pendant les essais : ce n'est pas une panne, c'est `browser ensure` qui fait foi. Sinon il télécharge le Chrome sans interface (environ 260 Mo sous Linux, une seule fois) dans `~/.cache/hyperframes/chrome`. Relancer ensuite `doctor --json` : la ligne Chrome doit être `ok`.
- Téléchargement interrompu ou Chrome qui ne se lance plus : `browser ensure --force` efface et recommence.
- La ligne **Version** peut signaler une version plus récente : c'est attendu, le studio reste sur 0.9.33.

### Machine sans réseau

Le premier lancement a besoin d'Internet pour trois choses : la commande elle-même (npm), le Chrome sans interface, et les polices ou plugins non embarqués. Une fois ces trois choses en cache, contrôle et rendu tournent sans réseau.

| Élément | Préparation, pendant que le réseau est là | Sans réseau |
| --- | --- | --- |
| La commande | un premier `npx -y hyperframes@0.9.33 --version` la met en cache | `npx --offline -y hyperframes@0.9.33 <commande>` (vérifié : répond `0.9.33` depuis le cache) |
| Chrome | `browser ensure` | rien à faire s'il est en cache. Sinon copier le dossier `~/.cache/hyperframes/chrome` d'une machine du même système, ou désigner un Chrome ou Chromium déjà installé : `HYPERFRAMES_BROWSER_PATH=/chemin/vers/chrome` (`doctor` affiche alors `env: …` ; un chemin faux est ignoré sans message) |
| GSAP | rien : `gsap.min.js`, `CustomEase.min.js` et `MotionPathPlugin.min.js` 3.15.0 sont embarqués | `SplitText` et les autres plugins : copie locale dans `assets/vendor/` (`../SKILL.md`, « GSAP ») |
| Polices | les 18 familles fournies sont embarquées dans leurs graisses de base | autres polices et autres graisses : fichiers `woff2` dans `assets/fonts/` (`../SKILL.md`, « Polices ») |
| Modèles (`transcribe`, `remove-background`, `tts`) | les lancer une fois | restent en cache |

Ce qui ne marche jamais sans réseau : `catalog` et `add` (registry en ligne), `capture`, `share`, tout ce qui touche HeyGen. Si ni la commande ni le Chrome ne sont en cache et qu'il n'y a pas de réseau, on ne peut pas rendre : le dire à la personne, livrer la composition écrite et contrôlée à la main, ne pas fabriquer un moteur de remplacement.

Test de bout en bout (deux minutes) :

```bash
npx -y hyperframes@0.9.33 init essai --skip-skills --resolution portrait --non-interactive
cd essai
npx -y hyperframes@0.9.33 check --json
npx -y hyperframes@0.9.33 render --quality draft -o renders/essai.mp4
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate -of default=nw=1 renders/essai.mp4
```

Attendu : `h264`, `1080`, `1920`, `30/1`. Sur ce projet vide, `check` renvoie `ok: true` avec l'avertissement `sweep_static` (« Nothing on screen moved ») : normal, le gabarit n'a aucune animation. Supprimer ensuite le dossier `essai` (il contient un `CLAUDE.md` et un `AGENTS.md` à ne pas suivre : `../SKILL.md`, « Créer le projet »).

## Couper la télémétrie : trois moyens, en poser au moins deux

1. Variable d'environnement `HYPERFRAMES_NO_TELEMETRY=1` (ou `DO_NOT_TRACK=1`), comme ci-dessus : vaut pour toute la machine.
2. Réglage enregistré : `npx -y hyperframes@0.9.33 telemetry disable`, contrôlé par `telemetry status`.
3. Fichier `.env` à la racine du projet contenant `HYPERFRAMES_NO_TELEMETRY=1` : suit le projet s'il change de machine.

Ce que la télémétrie envoie quand elle est active : des compteurs d'usage (commandes, nom du skill, type de machine, agent utilisé), anonymes tant que la personne n'est pas connectée à un compte HeyGen, liés à ce compte ensuite. Le studio la coupe par défaut ; la personne peut la réactiver (`telemetry enable`) si elle le souhaite.

Conséquences pour l'agent : ne pas lancer `hyperframes events --skill=…` (le « usage beacon » des textes officiels), ni `hyperframes feedback`, ni `feedback --file-issue` (qui publie le projet).

## Autres variables utiles

| Variable | Effet |
| --- | --- |
| `HYPERFRAMES_SKIP_SKILLS=1` | `init` et `skills` n'installent aucun skill officiel (ceux du plugin suffisent) |
| `HYPERFRAMES_NO_UPDATE_CHECK=1` | plus de rappel de mise à jour (le studio est épinglé) |
| `HYPERFRAMES_FFMPEG_PATH`, `HYPERFRAMES_FFPROBE_PATH` | chemins absolus vers les binaires FFmpeg à utiliser |
| `HYPERFRAMES_BROWSER_PATH` | chemin absolu d'un Chrome ou Chromium à utiliser à la place de celui du cache |
| `PYTHONDONTWRITEBYTECODE=1` | les scripts Python du studio n'écrivent pas de dossier `__pycache__` dans le plugin |
| `HYPERFRAMES_PREVIEW_ALLOWED_HOSTS` | noms d'hôte autorisés pour l'aperçu à distance |
| `HYPERFRAMES_RENDER_DETACHED=1` | rendu détaché, seulement s'il dépasse le délai de l'outil qui le lance |

## FFmpeg sans gestionnaire de paquets

Télécharger `ffmpeg` et `ffprobe` pour le système (page de téléchargement de ffmpeg.org), les poser dans un dossier **hors de tout projet** (par exemple `C:\outils\ffmpeg\bin` ou `~/outils/ffmpeg`), puis :

```bash
export HYPERFRAMES_FFMPEG_PATH="/chemin/absolu/ffmpeg"
export HYPERFRAMES_FFPROBE_PATH="/chemin/absolu/ffprobe"
```

(Windows : `setx HYPERFRAMES_FFMPEG_PATH "C:\outils\ffmpeg\bin\ffmpeg.exe"`, idem pour `ffprobe.exe`.)

Depuis la 0.9.32, la CLI n'exécute plus un FFmpeg trouvé **dans le dossier du projet** ou dans le dossier courant (un projet peut venir de n'importe qui). L'ancien emplacement `.hyperframes/bin` ne doit donc plus servir : binaires hors du projet, variables ci-dessus ou `PATH`.

## Mettre à jour plus tard

Le studio est validé sur 0.9.33. HyperFrames publie souvent (neuf versions entre le 8 et le 11 novembre 2026) : on ne suit pas chaque version. Une mise à jour se fait quand le plugin du studio annonce une nouvelle version validée ; elle change le numéro dans toutes les commandes de ce skill. Un projet existant garde sa version tant qu'il n'est pas terminé.

Sources : `officiel/hyperframes-cli/references/doctor-browser.md`, `init-and-scaffold.md`, `upgrade-info-misc.md`, `officiel/hyperframes/references/skill-lifecycle.md`, journal des versions du dépôt (`docs/changelog.mdx`).
