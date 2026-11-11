# Médias : ce qui est gratuit, ce qui est payant, ce qui reste sur la machine

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Résumé en français de `officiel/media-use/` (0.9.33). Règle de base : tout média est un **fichier local** dans `assets/` avant le rendu ; un rendu ne télécharge jamais rien.

## Ce que le studio utilise par défaut (gratuit, local, sans compte)

| Besoin | Outil | Remarque |
| --- | --- | --- |
| Transcription mot à mot | `npx -y hyperframes@0.9.33 transcribe <fichier> --model small --language fr` | modèle téléchargé une fois ; tout reste sur la machine |
| Voix de synthèse locale | `npx -y hyperframes@0.9.33 tts` (Kokoro) | qualité correcte ; vérifier la disponibilité d'une voix française avec `tts --help` avant de la promettre |
| Grille de temps d'une musique | `npx -y hyperframes@0.9.33 beats --json` ; `audio <fichier> --only sections,onsets,moments --json` | skill `son` |
| Instants d'un son ou du film | `npx -y hyperframes@0.9.33 audio <fichier> --json` | instants des attaques et des pics, silences ; pour caler, pas pour juger le niveau |
| Niveau du film (LUFS, crête) | `son/scripts/niveau.py mesurer <mp4>` ou `rendu/scripts/verifier-export.py` | même mesure (`ebur128=peak=true`) ; `loudnorm` ne sert pas de mesure |
| Régler le niveau final | `son/scripts/finaliser.py renders/film.mp4 -o renders/film-livre.mp4` (`--sans-fond` sans voix ni musique) | après le rendu ; image copiée sans réencodage |
| Égaliser deux pistes | `npx -y hyperframes@0.9.33 normalize-audio --reference <id> --target <id> --write` | écrit le volume dans le HTML |
| Étalonnage, grain, flou, vignette | `npx -y hyperframes@0.9.33 media-treatment --selector '#plan' --analyze --json` puis `--grading <fichier.json> --apply` | jamais de filtre CSS sur une vidéo réelle |
| Détourage d'une personne | `npx -y hyperframes@0.9.33 remove-background entree.mp4 -o detourage.webm` | 168 Mo au premier lancement, lent sans carte graphique |
| Logos | fichier officiel fourni par la marque ou par la personne | jamais redessiné |
| Bruitages, ambiances, musique | skill `son` : banque CC0 fournie, sources libres vérifiées | licence lue et notée pour chaque fichier |
| Images et vidéos libres | banques libres (Pexels, Pixabay, Unsplash) : licence lue sur la page du fichier | noter l'adresse et l'auteur dans les crédits du projet |

## Ce qui demande un compte HeyGen (non inclus dans le studio)

| Fonction | Commande | Coût |
| --- | --- | --- |
| Catalogue de musiques et recherche d'images | `media-use resolve --type bgm / image` | compte gratuit |
| Voix « Voice Turbo » | `media-use resolve --type voice` | 3 minutes par mois avec le compte gratuit, payant au-delà |
| Images, plans, voix clonées, avatars générés | `media-use generate` | crédits payants |
| Rendu sur les serveurs HeyGen | `cloud render` | selon l'abonnement |
| Lien de relecture | `share` | compte gratuit, 5 projets gardés |
| **Refaire une vidéo existante image par image** | `reverse` (skill officiel `reverse-any-video`) | **abonnement Pro** |
| **Épisode dans un style éprouvé** | `templates pull` (skill officiel `style-sampling`) | **abonnement Pro**, modèles tirés du serveur |

Ces deux dernières fonctions ne sont **pas redistribuées** par ce plugin et leurs modèles n'y figurent pas. Le studio couvre ces besoins autrement : les catégories de styles du plugin pour produire dans un style, et la catégorie des formats Flot Web pour recréer le mouvement d'une vidéo de référence.

Conduite à tenir :

- Ne jamais lancer `auth login`, ni une commande qui consomme des crédits, sans demande explicite de la personne. Si elle a un compte et veut s'en servir : `npx -y hyperframes@0.9.33 auth status`, puis suivre `officiel/media-use/SKILL.md` et `references/heygen.md` (plafond de crédits dans `.hyperframes/credit-limit.json`).
- Une fonction payante refusée : transmettre le message tel quel, ne pas contourner.
- Avec un compte connecté, la télémétrie, si elle est active, est liée au compte : raison de plus de la laisser coupée.

## Scripts et fichiers officiels non recopiés ici

`references/officiel/` ne contient que la documentation. Les scripts d'aide officiels (`transcript-cut.mjs`, `audio-duck.mjs`…), les 13 chartes « frame presets », les tables de couleurs (LUT) et les 19 bruitages fournis avec `media-use` ne sont pas dans ce plugin :

- les bruitages officiels sont sous licence Pixabay, qui interdit de les redistribuer isolément : le studio ne les embarque pas (le skill `son` fournit une banque CC0) ;
- le reste est présent chez le client dans le paquet npm `hyperframes@0.9.33` (dossier `dist/skills/` du paquet) et s'utilise par les commandes de la CLI (`media-use`, `media-treatment`, `transcribe`…), sans chemin à connaître.

## Mixer dans la composition

Tout se règle par attributs sur `<audio>` ou `<video>` : `data-volume` (1 = 0 dB), `data-fade-in`, `data-fade-out`, `data-automation` (enveloppe de volume, points `{t, v}` en secondes depuis le début du clip), `data-fx-chain` (filtres, limiteur). Aperçu et rendu utilisent le même graphe : ce qui s'entend à l'aperçu est ce qui est rendu. Détail : `officiel/media-use/references/mixing.md`. Méthode, budget et niveaux : skill `son`.

- Les `data-volume` règlent l'**équilibre** entre les sons, pas le niveau final : le mixeur plafonne la crête, et les monter ne dépasse pas environ −19,5 LUFS. Le niveau du film (−14 LUFS avec voix ou musique ; niveau réglé sur la crête et feu jaune sans voix ni musique) se règle après le rendu avec `son/scripts/finaliser.py`, puis le fichier `*-livre.mp4` est contrôlé par `scripts/verifier-export.py` (`exports.md`).
- Les balises `<audio>` des bruitages sont écrites par `son/scripts/caler.py --html` : `data-start` calé sur l'image de l'impact (attaque +8 ms, jamais avant), `data-duration`, une piste par son à partir de la piste 20, `src` relatif à `index.html`. Les coller dans la racine, à côté des hôtes de scènes.

## Images réelles ternes, sombres, à styliser

C'est une demande de média, pas de CSS : inspecter le vrai `<img>` ou `<video>`, choisir une intention, suivre `officiel/media-use/references/media-treatments.md` et `grading.md`, enregistrer avec `media-treatment`.
