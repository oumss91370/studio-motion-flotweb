# Exports et contrôle du fichier final

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

## Formats du studio

| Destination | Taille | Images/s | Durée conseillée | Projet à créer | Rendu |
| --- | --- | --- | --- | --- | --- |
| Instagram Reels | 1080×1920 | 30 | 15 à 90 s | `--resolution portrait` | `render --quality delivery` |
| TikTok | 1080×1920 | 30 | 15 à 90 s | `--resolution portrait` | `render --quality delivery` |
| YouTube Shorts | 1080×1920 | 30 | jusqu'à 3 min | `--resolution portrait` | `render --quality delivery` |
| YouTube (long) | 1920×1080 | 30 | libre | `--resolution landscape` | `render --quality delivery` |
| YouTube 1440p | 2560×1440 | 30 | libre | `--resolution landscape-1440p` | `render --quality delivery` |
| YouTube 4K | 3840×2160 | 30 | libre | `--resolution landscape` | `render --quality delivery --resolution landscape-4k` |

Fichier attendu partout : conteneur MP4 avec index en tête (lecture immédiate), image H.264 en `yuv420p`, couleur BT.709, débit d'environ 8 Mbit/s au plus en 1080p, son AAC stéréo 48 kHz. Niveau du son (règles du skill `son`) :

| Film | Niveau | Crête | Verdict du contrôle |
| --- | --- | --- | --- |
| Avec voix ou musique | **−14 LUFS** intégrés, ±1 | −1 dBTP au plus | vert dans la plage, rouge en dehors |
| Sans voix ni musique (bruitages seuls) | pas de cible LUFS ; jamais au-dessus de −14 | bruitage le plus fort entre −3 et −1 dBTP | **jaune** : livrable, à écrire dans la note de livraison |

Les durées maximales et les débits acceptés par les plateformes changent : en cas de doute, vérifier la page d'aide de la plateforme le jour de la publication. Les valeurs ci-dessus sont celles du studio, pas des limites officielles.

Pourquoi le 1440p pour YouTube : un fichier envoyé en 1440p ou plus est en général mieux compressé par la plateforme qu'un fichier 1080p, donc plus net une fois en ligne. Un projet 1080p ne monte pas à 1440p (facteur non entier) : créer le projet en 1440p dès le départ, ou rendre en 4K.

Un même sujet pour le vertical et pour le paysage : ce sont deux compositions. On ne recadre pas un film paysage en vertical, on le recompose (un sujet centré, empilé, textes ×1,35).

## Rendre

```bash
npx -y hyperframes@0.9.33 render --quality draft -o renders/essai.mp4        # pour vérifier le rythme
npx -y hyperframes@0.9.33 render --quality delivery -o renders/ma-video.mp4  # livraison
```

Film à grain, bruit ou trame fine animés : ajouter `--max-bitrate 8M --buffer-size 16M`, sinon le fichier peut dépasser 30 Mbit/s (42 Mo pour 10 s sur un film de test), long à envoyer et de toute façon recompressé par la plateforme.

## Régler le niveau du son, après le rendu

Le mixeur de HyperFrames plafonne la crête : monter les `data-volume` ne dépasse pas environ −19,5 LUFS. Le niveau final se règle donc **sur le fichier rendu**, par le script du skill `son`, qui extrait le son, le règle et le remonte sur l'image copiée sans réencodage :

```bash
S="${CLAUDE_PLUGIN_ROOT}/skills/son/scripts"
PYTHONDONTWRITEBYTECODE=1 python3 "$S/finaliser.py" renders/ma-video.mp4 -o renders/ma-video-livre.mp4               # avec voix ou musique
PYTHONDONTWRITEBYTECODE=1 python3 "$S/finaliser.py" renders/ma-video.mp4 -o renders/ma-video-livre.mp4 --sans-fond   # bruitages seuls
```

C'est `ma-video-livre.mp4` qu'on contrôle, qu'on regarde et qu'on publie. Options (fond ajouté au dernier moment, limiteur) : skill `son`, étape 7.

Le son placé dans la composition (`<audio>` avec `id`) est mixé dans le fichier. Si la bande son a été fabriquée à part (skill `son`), soit elle entre comme un seul `<audio id="bande-son">` avant le rendu, soit elle est posée après coup sans réencoder l'image :

```bash
ffmpeg -i renders/ma-video.mp4 -i audio/bande-son.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -shortest -movflags +faststart renders/ma-video-son.mp4
```

## Contrôle avec `ffprobe`

Contrôle automatique du fichier livré (taille, codec, couleur, cadence, durée, poids, débit, piste son, niveau sonore, crête, première image, index en tête) :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/rendu/scripts/verifier-export.py" renders/ma-video-livre.mp4 --format reel --duree 18
PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/rendu/scripts/verifier-export.py" renders/ma-video-livre.mp4 --format reel --duree 18 --sans-fond
```

- `--format` : `reel`, `tiktok`, `short`, `youtube`, `youtube-1440p`, `youtube-4k`. `--duree` : le `data-duration` de la racine.
- `--sans-fond` : film sans voix ni musique (même option que `niveau.py` et `finaliser.py`). `--muet` : vidéo volontairement sans piste son. `--json` : résultat lisible par un script (`feu`, `son`, `controles`).
- Chaque ligne est `OK`, `ATTENTION` ou `ECHEC`. **Feu vert** : tout est OK. **Feu jaune** : au moins une `ATTENTION` (film sans voix ni musique, débit au-dessus de 8 Mbit/s en 1080p, 16 en 1440p, 35 en 4K, son non AAC…) : livrable, chaque réserve s'écrit dans la note de livraison. **Feu rouge** : au moins un `ECHEC`, code de sortie 1.
- Le son est mesuré **exactement comme dans `son/scripts/niveau.py`** : `ebur128=peak=true`, lecture du bloc « Summary ». Les deux scripts donnent les mêmes chiffres au dixième (vérifié sur 6 fichiers de test : −24,7 / −25,9 / −16,0 / −14,0 / −14,1 / −19,1 LUFS) et le même verdict avec `--sans-fond`.

Contrôle à la main, si Python manque :

```bash
ffprobe -v error -show_entries stream=codec_type,codec_name,profile,width,height,avg_frame_rate,pix_fmt,sample_rate,channels:format=duration,size -of json renders/ma-video.mp4
```

| Champ | Valeur attendue (vertical) |
| --- | --- |
| `codec_name` (image) | `h264` |
| `width` × `height` | `1080` × `1920` |
| `avg_frame_rate` | `30/1` |
| `pix_fmt` | `yuv420p` |
| `codec_name` (son) | `aac` |
| `sample_rate`, `channels` | `48000`, `2` |
| `duration` | le `data-duration` de la racine, à une image près |

Niveau sonore du fichier (mesuré, pas entendu), la seule méthode du studio :

```bash
ffmpeg -hide_banner -nostats -i renders/ma-video-livre.mp4 -map 0:a:0 -af ebur128=peak=true -f null -
```

Lire, dans le bloc « Summary » de la fin, `I:` (niveau intégré, cible −14 ±1), `LRA:` (plage dynamique) et `Peak:` (crête vraie, −1 ou moins). Ne pas mesurer avec `loudnorm=print_format=json` : sur un film court, son `input_i` s'écarte jusqu'à 0,8 LU (film de test : −15,3 au lieu de −16,0).

## Regarder le fichier, pas seulement le mesurer

Extraire trois images du MP4 (la première, le milieu, la dernière) et les ouvrir :

```bash
ffmpeg -y -i renders/ma-video.mp4 -frames:v 1 controle-debut.png
ffmpeg -y -ss 9 -i renders/ma-video.mp4 -frames:v 1 controle-milieu.png
ffmpeg -y -sseof -0.1 -i renders/ma-video.mp4 -frames:v 1 controle-fin.png
```

- Première image : l'accroche est lisible, pas de noir, pas de logo seul.
- Milieu : textes nets, rien dans les zones d'interface (`zones-interface.md`).
- Dernière image : pas de noir involontaire, pas de sous-titre resté affiché.

Planche d'une image par seconde, pour repérer un plan mort ou un flash :

```bash
ffmpeg -y -i renders/ma-video.mp4 -vf "fps=1,scale=216:-1,tile=10x3" controle-planche.png
```

## Réencodage de secours

Seulement si le contrôle échoue sur le conteneur ou la couleur (par exemple un fichier maître rendu en 4:4:4), ou pour ramener un fichier trop lourd vers 8 Mbit/s (ajouter alors `-maxrate 8M -bufsize 16M`) :

```bash
ffmpeg -i entree.mp4 -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 30 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 256k -ar 48000 -ac 2 -movflags +faststart sortie.mp4
```

4K rendu puis réduit en 1440p : ajouter `-vf scale=2560:1440:flags=lanczos`. Une taille, une cadence ou une durée fausse ne se corrige pas par réencodage : corriger la composition et rendre à nouveau.

## Vignette et première image

- Reels, TikTok, Shorts montrent souvent l'image 0 avant la lecture : elle doit être la meilleure image fixe du film (visage, résultat, ou une ligne forte).
- Vignette séparée (YouTube long : 1280×720 ; couverture de Reel : 1080×1920 avec le sujet au centre, car la grille du profil recadre la couverture : vérifier le recadrage dans l'application) : une composition fixe avec `data-no-timeline`, capturée par `snapshot`, ou une image extraite du film.

## Sous-titres en fichier séparé (YouTube)

`npx -y hyperframes@0.9.33 transcribe assets/voix.mp3 --model small --language fr --to srt` écrit un `.srt` à téléverser avec la vidéo, en plus des sous-titres incrustés.

## Note de livraison (à donner à la personne)

Chemin du fichier livré, format, durée, poids ; résultat du contrôle (feu, niveau sonore et crête mesurés : dire « mesuré, non écouté » ; pour un film sans voix ni musique : « niveau réglé sur la crête, x dBTP, y LUFS ») ; chaque ligne `ATTENTION` du contrôle ; ce qui n'a pas pu être vérifié ; crédits à coller dans la description (sons et musiques sous licence, skill `son`).
