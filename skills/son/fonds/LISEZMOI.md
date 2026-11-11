# Fonds sonores de repli (4 boucles)

Quatre fonds continus pour un film qui n'a ni voix ni musique, quand il n'y a pas de réseau ou pas de musique libre qui convienne. Avec un fond, le film peut viser −14 LUFS sans écraser ses bruitages (voir l'étape 7 du skill).

**Ce que c'est, honnêtement.** Des sons calculés : ondes pures empilées, bruit filtré, réverbération calculée. Pas d'instrument, pas d'interprète, pas de mixage fait à l'oreille : personne n'a écouté ces fichiers, ils ont seulement été mesurés. Attendez-vous à un rendu « orgue électronique » pour les nappes et « console de jeu » pour la boucle rétro, correct sous des bruitages et à bas niveau, pauvre s'il est seul au premier plan. Ce ne sont **pas** des musiques de catalogue : dès qu'un film compte (publicité, lancement, série), chercher une vraie musique (`../references/sources-libres.md`, « Musique ») et le dire à la personne.

## Les fichiers

Mesures du 11/11/2026 (méthode de `../scripts/niveau.py` : `ebur128=peak=true`), OGG Vorbis stéréo 48 kHz.

| Fichier | Caractère | Durée de la boucle | Tempo | Niveau | Crête | Part de l'énergie sous 150 Hz | Pour |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nappe-calme.ogg` | 4 accords tenus de 5 s (la mineur 7, fa majeur 7, do, sol), un peu d'air, aucune pulsation | 20,00 s | aucun | −17,9 LUFS | −8,3 dBTP | 2 % | explication posée, portrait, style peint, plan calme |
| `pulsation-legere.ogg` | note douce sur chaque temps, contretemps très léger, petit motif de trois notes, deux accords (do, la mineur) | 19,20 s (8 mesures) | 100 battements par minute, un temps = 0,6 s | −17,9 LUFS | −7,5 dBTP | 1 % | lancement de produit, infographie, tutoriel |
| `tension.ogg` | bourdon de la avec un si bémol qui frotte, souffle qui enfle toutes les 10 s, tic d'horloge chaque seconde, double battement sourd toutes les 5 s | 20,00 s | tic à 60 par minute | −18,0 LUFS | −7,9 dBTP | 13 % | suspense, compte à rebours, histoire de survie |
| `retro-puce.ogg` | arpèges d'ondes carrées, basse, bruit en guise de charleston, petite mélodie ; grille do, sol, la mineur, fa | 16,00 s (8 mesures) | 120 battements par minute, un temps = 0,5 s | −18,0 LUFS | −5,4 dBTP | 3 % | pixel art, jeu rétro, 8 bits |

**Bouclables** : oui, sans couture. Vérifié par mesure : le saut entre le dernier et le premier échantillon est plus petit que les sauts ordinaires à l'intérieur du fichier (par exemple 51 pour 418 sur la nappe, en pas de 16 bits), et la boucle étendue à 45 s par FFmpeg est la répétition exacte du fichier, à un pas de quantification près. Le fichier commence et finit donc en plein son : il faut un fondu d'entrée et de sortie dans le film.

Tonalité commune : do majeur / la mineur. Les sons à hauteur du film (tintements, pops accordés) se choisissent dans cette tonalité (règle « une seule tonalité »).

## Utiliser

1. Copier le fichier dans le projet : `assets/musique/nappe-calme.ogg`.
2. Film plus long que la boucle : l'allonger (FFmpeg répète la boucle, sans couture) :

   ```bash
   ffmpeg -y -stream_loop -1 -i assets/musique/nappe-calme.ogg -t 45 -c:a pcm_s16le assets/musique/nappe-calme-45s.wav
   ```

3. Dans `index.html`, une balise, sur une piste à elle :

   ```html
   <audio id="fond" class="clip" src="assets/musique/nappe-calme.ogg" data-start="0" data-duration="10"
          data-volume="0.5" data-fade-in="0.3" data-fade-out="1.2" data-track-index="19" data-timeline-role="music"></audio>
   ```

   Niveau : bruitages 3 à 10 dB au-dessus du fond (règle 9) ; partir de `data-volume` 0,5 et mesurer. Avec une boucle rythmée, caler les coupes et les apparitions sur les temps (0,6 s ou 0,5 s) : c'est ce qui fait croire à une musique choisie.
4. Niveau final après le rendu : `finaliser.py renders/final.mp4` (profil par défaut, −14 LUFS).

Voie rapide, sans toucher à la composition : `finaliser.py renders/final.mp4 --fond <fichier>` répète le fond sous tout le film, 10 dB sous le son le plus fort, avec fondus. Essais sur quatre films de test : −14,0 à −14,2 LUFS, crête −1,6 dBTP, limiteur 1,3 à 2,8 dB pendant moins de 1 % du temps. Le fond n'est alors calé sur rien à l'image : à réserver aux nappes sans tempo (`nappe-calme`, `tension`).

Dans la note de livraison : « fond sonore : boucle de repli du studio (synthèse), non écoutée ».

## Comment ils sont faits

`fabriquer.py` (dans ce dossier) les recalcule à l'identique (graine fixe), en une minute environ :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/fonds/fabriquer.py" --dossier assets/musique [--seulement nappe-calme] [--wav]
```

Il n'utilise que le moteur de repli `../scripts/sfx/` (whaleyxbt/claude-motion, MIT, non modifié) : `pad` pour les accords tenus, `blip` et `click` pour les notes et les tics, `bandnoise` pour le souffle, `dsp.pulse` et `dsp.crush` pour les ondes carrées, `dsp.reverb` pour l'espace. Aucun échantillon, aucun fichier téléchargé, aucune mélodie existante. La boucle est sans couture parce que tout ce qui dépasse la fin est reporté au début (écriture circulaire) et que la réverbération est calculée sur deux tours dont on garde le second. Le niveau est un simple gain constant vers −18 LUFS.

Pour un autre fond (autre tempo, autre tonalité, autre durée) : copier `fabriquer.py` dans le projet, changer les notes et les durées, garder la classe `Boucle`.

## Licence

Fonds créés par le studio (Flot Web) avec du code sous licence MIT ; ils ne reprennent aucune œuvre existante. **Libres d'usage dans les vidéos du client**, y compris monétisées ou vendues, sans crédit obligatoire, sans limite de durée ni de plateforme ; ils peuvent être modifiés, coupés, superposés. Ne pas les inscrire dans un système de revendication de droits (Content ID) : d'autres clients du studio utilisent les mêmes boucles.

## Limites connues

- Timbres pauvres (ondes pures) : fatigants au-delà de 30 à 40 s, et la boucle se reconnaît dès le deuxième tour.
- `nappe-calme` ondule lentement (battement d'environ une fois par seconde entre les deux canaux désaccordés) : voulu, mais audible au casque.
- `tension` porte 13 % de son énergie sous 150 Hz : sur un téléphone, il reste surtout le tic et le frottement aigu.
- `retro-puce` a une crête plus haute (−5,4 dBTP) et de l'énergie entre 2 et 6 kHz (6 %) : le garder bas sous une voix.
- Aucune écoute humaine ni par earshot n'a validé ces fichiers. Si earshot est installé : `earshot timeline <fichier>` avant le premier usage.
