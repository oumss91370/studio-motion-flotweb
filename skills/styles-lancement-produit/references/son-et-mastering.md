# Son et mastering d'une vidéo de lancement

Complète le skill `son` (qui reste la règle : vrais enregistrements d'abord, environ 5 bruitages par 10 s, −14 LUFS, écoute du mix). Ce fichier ajoute ce qui est propre aux vidéos de produit. Le son est l'endroit où l'on prend les mauvaises décisions avec le plus d'assurance, parce que personne ne mesure : ici, **on prouve**.

## 1. Deux façons de caler un film de lancement

| | Sur la voix | Sur la musique |
|---|---|---|
| Fiches | `lancement-narre-mot-a-mot`, `film-produit-saas` avec voix | `forme-continue-sur-la-musique`, `teaser-haute-energie`, `parcours-plan-sequence` |
| L'horloge | la transcription mot à mot de la voix | la grille de temps mesurée du morceau |
| Musique | un lit très discret | le moteur : on la choisit **avant** de chorégraphier |
| Chaque révélation tombe | sur son mot | sur un temps, le grand moment sur le « drop » |

## 2. Les trois couches (film narré)

| Couche | Rôle | Niveau |
|---|---|---|
| Voix | porte l'argument ; tout le reste la sert | l'élément le plus fort du mix |
| Lit musical | continuité entre les plans, plancher sous le silence | très bas (environ 0,1 de la pleine échelle) : si on le remarque, il est trop fort |
| Bruitages | ponctuation : confirment qu'une chose à l'écran a eu lieu | placés un par un, mesurés un par un |

Un film de lancement narré n'a pas besoin d'une partition : il lui faut un lit assez discret pour qu'on n'y pense jamais, et des repères assez nets pour être sentis plutôt qu'entendus.

## 3. La table des repères sonores

**Chaque repère nomme le mot qu'il ponctue, pas la seconde.** Quand on recoupe le script, toutes les secondes bougent, pas les mots.

```js
// [fichier, début (s, relatif au plan), durée (s), volume (0 à 1)]
const SONS = { "04-demande": [
  ["clic-souris", 0.04, 0.36, 0.45],      // « Demande » : clic dans le champ
  ["frappe-clavier", 0.27, 0.76, 0.55],   // « en français » : la requête se tape
  ["clic-souris", 1.30, 0.36, 0.50],      // « et c'est parti » : envoi
] };
```

- **Un repère par évènement, pas par élément** : six cartes qui se posent = un décalage de trois petits sons discrets, pas six.
- **Accorder le son à la physique** : un clic pour un appui, un son doux pour une arrivée, un souffle pour ce qui entre dans le cadre, un tic pour un changement d'état. **Un carillon sur un clic est le signe le plus courant du modèle tout fait.**
- **Rien ne se répète** : un repère qui sonne plus de deux fois en 45 s devient un tic.
- **Le silence est un repère** (section 6).
- Temps relatifs au plan, résolus tard contre les vrais débuts de plans : sinon chaque retouche en amont invalide toute la table.

## 4. La loi arithmétique du volume

**Le volume d'un repère ne peut pas sauver un fichier source trop faible.** C'est de l'arithmétique.

Le film d'origine avait un bruit de frappe que personne n'entendait. On a monté le volume deux fois, de 0,35 à 0,85. Effet mesuré sur le fichier livré : **0,1 dB**. La source était un enregistrement lointain à **−37 dB** en moyenne, la voix à **−17 dB** dans la même fenêtre : additionner un signal à −38 dB à un signal à −17 dB change le total d'un centième de décibel.

Avant de discuter du niveau d'un repère, mesurer les deux côtés :

```bash
ffmpeg -hide_banner -i sons/frappe-clavier.mp3 -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume"
ffmpeg -hide_banner -ss 10.72 -t 0.76 -i rendus/film.mp4 -vn -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume"
```

Si la moyenne du son est à plus de ~15 dB sous celle de la voix, aucun volume ne le sauvera : **niveler le fichier**.

## 5. Niveler un son

```bash
ffmpeg -ss 0.41 -t 1.1 -i frappe-clavier.mp3 \
  -af "volume=22dB,alimiter=level_out=0.9:limit=0.9,afade=t=out:st=0.95:d=0.15" \
  -c:a libmp3lame -b:a 192k frappe-clavier-fort.mp3
```

- **Couper depuis la première attaque, pas depuis zéro.** Les enregistrements commencent par du bruit de pièce ; coupé depuis zéro, le son est fort, toutes les mesures passent, et le repère arrive quand même en retard.
- **Les attaques sont ce qu'on protège** : pour un son percussif, c'est la crête qui dit s'il sera entendu.
- Garder l'original ; la version nivelée porte un autre nom.
- **Comparer au niveau de la voix seule, avant mastering** (dans le film d'origine, l'écart entre voix seule et fenêtre masterisée était de 4,6 dB, dans le sens qui flatte le repère).
- **Attention à la troncature** : si la durée du clip audio est plus courte que le fichier, la coupe tombe où la ligne de temps le dit, et le fondu de fin ne joue jamais. Écouter à la coupe.

## 6. Grave profond et silence

Deux gestes portent presque tout le poids émotionnel, et ils ne coûtent rien.

- **Un grave profond sous la révélation principale** : un coup grave sous l'affirmation et un sous l'appel à l'action, **long (1,7 à 1,8 s) et discret (0,2 à 0,22)**, senti plus qu'entendu. Jamais sur un temps produit : si tout a son grave, rien ne porte.
- **Du silence devant** : le coup ne marche que parce que le plan d'avant finit sur une tenue et un quasi-silence. Finir le mouvement du plan précédent tôt, laisser ~0,3 s de rien, puis frapper.

## 7. Caler sur la musique (films sans voix)

Détail de la mesure du tempo et du « drop » : `references/beat-et-drop.md` du skill `son`. Règles propres au lancement :

- Choisir le morceau **avant** de chorégraphier : énergique, adapté à la marque, avec une montée, un « drop » net et une fin satisfaisante. Le tempo seul n'est pas de l'énergie. Viser ~120 BPM.
- **Ne jamais faire confiance à une grille automatique sans contrôle** : vérifier quelques temps à l'oreille ou sur la forme d'onde.
- Choisir la fenêtre du morceau pour que **le drop tombe sur le grand moment du produit** ; démarrer juste avant l'attaque d'une mesure.
- **Chaque son est placé par son propre pic**, pas par le début de son fichier.
- Quelque chose se passe à chaque temps ; la frappe au clavier suit des subdivisions rapides pendant la montée ; les logos de clients accélèrent : temps → croches → doubles croches.
- Films qui bouclent : pas de limiteur qui pompe à la jointure ; un gain fixe.
- Les sources d'origine **synthétisent** tous leurs sons. Dans ce plugin : **vrais enregistrements d'abord**, synthèse en repli seulement (skill `son`), et une musique sous licence claire, téléchargée chez le client (ne jamais embarquer de fichier de banque de sons dans un livrable revendu).

## 8. Mastering en deux passes

```bash
# passe 1 : mesurer
ffmpeg -i rendus/film-brut.mp4 -af loudnorm=I=-14:print_format=json -f null -
# passe 2 : corriger, limiter, réencoder
ffmpeg -i rendus/film-brut.mp4 -c:v libx264 -preset slow -crf 19 -tune film -pix_fmt yuv420p \
  -af "loudnorm=I=-14:TP=-1.0:LRA=7:linear=true:measured_I=…:measured_TP=…:measured_LRA=…:measured_thresh=…,alimiter=limit=0.891:level=disabled:attack=5:release=50" \
  -c:a aac -b:a 192k -movflags +faststart rendus/film.mp4
```

Cibles : **−14 LUFS intégrés, crête vraie ≤ −1,0 dBTP.**

**Deux pièges** :
1. `loudnorm` en mode linéaire calcule **un seul gain** pour tout le fichier d'après la passe 1. Ajouter un son plus fort après la mesure, et une crête dépasse (le film d'origine est monté à +1,1 dBFS : saturé). Le limiteur après `loudnorm` n'est pas une précaution en trop, c'est ce qui rattrape ça.
2. `alimiter` **ajoute un gain de rattrapage** si on ne le désactive pas : seul, il a donné −13,0 LUFS / 0,0 dBFS. Passer `level=disabled`.

Garder tout l'argument `-af` dans une seule chaîne entre guillemets.

## 9. Vérifier dans le fichier livré

Ne jamais déclarer un mix fini sur le rapport du filtre. Mesurer le fichier qu'on livre :

```bash
ffmpeg -i rendus/film.mp4 -af ebur128=peak=true:framelog=quiet -f null - 2>&1 | grep -E "^\s+(I|Peak|LRA):"
```

Attendu : `I: -14.0 LUFS`, crête ≤ −0,8 dBFS (l'encodage AAC ajoute un cheveu). Mesurer sur le fichier **stéréo**.

Prouver que chaque repère ajouté est présent : comparer la même fenêtre dans l'ancien et le nouveau master (dans le film d'origine : crête de −4,6 dB, repère inaudible, à −1,4 dB, frappes audibles). « Ça sonne mieux pour moi » n'est pas une preuve. Puis **écouter** (skill `son`, écoute par earshot) : distinguer « mesuré » et « entendu » dans le compte rendu au client.

## 10. Licences

Figer en local sa banque de sons et de musiques et noter la licence de chaque fichier. Préférer les sources à licence commerciale globale, garder les noms de fichiers d'origine, écrire la licence dans les crédits du projet.

Origine : AbubakrChan/product-launch-motion, commit `edbfb10`, `legacy/references/07-sound-and-master.md`, `references/technique.md`, `SKILL.md` (MIT) ; règle de la grille automatique : howseen-ai/claude-motion-design, commit `3d90d34` (MIT). Réécrit en français et aligné sur le skill `son` par Flot Web.
