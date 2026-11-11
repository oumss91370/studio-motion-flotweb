# Dérushage : couper les silences et les ratés

Format de montage (pas un look) : la première étape de tout montage des propres rushes du client. Il prépare la matière pour `reel-face-cam` et `animations-sur-la-voix`.

## 1. Identité
- **Nom** : Dérushage, silences et ratés. Identifiant : `derushage-silences-rates`.
- **Inspiration** : le montage « face caméra » serré des créateurs de vidéos courtes, où l'on ne voit pas les coupes mais où il n'y a plus d'air mort.
- **Principe** : à partir de l'enregistrement brut du client et de sa transcription mot à mot, deux passes distinctes. **Passe 1, les silences** : mécanique et déterministe, elle retire l'air mort avant le premier mot, après le dernier, et les pauses trop longues, **en gardant une respiration naturelle**. **Passe 2, les ratés** : bégaiements, mots répétés, faux départs et reprises ; c'est une affaire de **jugement**, donc soumise à une relecture avant toute coupe.
- **Pour quels sujets** : toute vidéo où le client se filme en train de parler (reel, short, publicité, tutoriel, vidéo longue).
- **Ne marche pas pour** : un enregistrement sans parole (pas de transcription), un entretien à plusieurs voix qui se chevauchent, une performance où les silences font partie du jeu (humour, émotion : monter à la main).
- **Droits** : uniquement les rushes du client ou ceux dont il a les droits. Ne jamais remplacer la prise fournie par une plus ancienne.

## 2. Palette, typographie, matières
Sans objet pour l'image : ce format ne pose ni couleur ni texte. Sa « matière » est la parole.
- **Matière d'entrée** : le fichier brut (garder l'original intact) + une transcription mot à mot `{ mots: [{ texte, debut, fin }] }`.
- **Matières de sortie** : la liste de décisions de montage (plages gardées et retirées, avec la raison de chaque coupe), la transcription recalée sur la nouvelle ligne de temps, un résumé lisible des décisions, la vidéo coupée.
- **Transcription** : avec l'outil du skill `rendu` (transcription locale, préciser la langue : sans `--language fr`, le modèle **traduit en anglais**). Supprimer les mots inventés sur les silences (repérés par `silencedetect=noise=-35dB:d=0.6`).
- **Police de repli** : sans objet (ce style ne pose pas de texte) ; si un sous-titre est ajouté, Montserrat.
- **Où la prendre** : sans objet.

## 3. Composition 9:16
- Le dérushage ne recadre pas : il livre la vidéo coupée dans son format d'origine. Le cadrage vertical se fait à l'étape suivante, **depuis la source en résolution native**, jamais depuis une copie réduite.
- Si le client s'est filmé en horizontal pour un reel vertical : repérer dès maintenant la position du visage (elle guidera les recadrages et l'emplacement des sous-titres), et vérifier qu'un recadrage 9:16 garde les gestes des mains.
- Garder 0,22 s d'image avant le premier mot : l'image 0 doit déjà montrer le client en train de s'animer, jamais un visage figé qui attend.

## 4. Ce qui bouge
- **Action principale** : la coupe elle-même, franche, placée dans un vrai silence entre deux groupes de souffle.
- **Boucles de fond** : aucune ; ce format n'ajoute pas de mouvement.
- **Autorisés** : #041 coupe sautée (c'est le langage normal du face caméra) ; un léger changement d'échelle entre deux prises (100 % → 108 à 112 %) à l'étape suivante, pour motiver une coupe visible.
- **Interdits** : accélérer la voix ; #186 fondu de morphing pour masquer une coupe dans une phrase ; #044 fondu enchaîné entre deux phrases ; couper à l'intérieur d'un groupe de souffle.

## 5. Rythme et montage
**Règles de la passe 1 (silences)**
- Une pause de moins de **0,55 s** n'est pas touchée : c'est le rythme naturel de la parole.
- Pour une pause coupée, on **garde une respiration**, selon le contexte : **0,24 s** pour une longue pause (≥ 2 s), **0,20 s** après une fin de phrase (`.` `!` `?`), **0,14 s** sinon. La respiration gardée penche légèrement vers la fin de la phrase précédente.
- Air mort du début réduit à **0,22 s**, celui de la fin à **0,34 s**.
- Réglage par défaut : environ 15 à 20 % d'une prise brute part en pur silence. Baisser le seuil pour un montage plus nerveux, le monter pour garder plus d'air.
- Repères mesurés sur des reels performants : parole qui démarre dans les 0,1 s ; pauses entre phrases sous ~0,2 s ; respirations naturelles après une virgule ou un « D'abord, » de 0,2 à 0,4 s, **qu'on garde** ; 4,0 à 4,7 mots par seconde.

**Règles de la passe 2 (ratés)**
- Trois types de candidats, repérés mécaniquement : **bégaiement** (répétition immédiate d'un mot), **reprise** (deux segments identiques ou presque : on garde la dernière prise propre), **faux départ** (un début de phrase abandonné qui recommence).
- **Relecture obligatoire** : lire chaque candidat dans son contexte. Faux positifs fréquents : la répétition d'insistance (« jamais, jamais »), le « c'est, c'est ça… » rhétorique, une énumération. Un rapport « zéro candidat » peut manquer une reprise évidente : **relire toute la transcription à la main**.
- Présenter les candidats au client avec une recommandation par élément, recueillir son accord, écrire les coupes approuvées avec leur raison.
- Une diction très propre peut donner peu ou pas de coupes : c'est un résultat valable. On ne coupe pas de la parole naturelle pour atteindre un quota.

**Règle commune, la plus importante** : **on coupe entre deux groupes de souffle, jamais dedans.** Un mot de remplissage ne part que s'il a du silence des deux côtés ; s'il s'enchaîne avec le mot suivant, il reste, car le couper rogne les mots voisins. Deux prises ne se raccordent que là où les deux côtés sont silencieux. Ne couper qu'après l'extinction complète d'un mot : les transcriptions font finir les mots 40 à 80 ms avant que la consonne ne meure.

## 6. Recette technique
- **Moteur** : ffmpeg pour la coupe (une seule passe), outils de transcription du skill `rendu`. HyperFrames n'intervient qu'ensuite.
- **Une seule passe, images exactes.** Encoder chaque segment à part puis les concaténer décale la synchro des lèvres d'environ une image à la moitié des raccords. Construire un seul graphe de filtres :
```
[0:v]trim=start=0.00:end=4.12,setpts=PTS-STARTPTS[v0];[0:a]atrim=start=0.00:end=4.12,asetpts=PTS-STARTPTS[a0];
[0:v]trim=start=5.31:end=9.80,setpts=PTS-STARTPTS[v1];[0:a]atrim=start=5.31:end=9.80,asetpts=PTS-STARTPTS[a1];
[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]
```
  écrit dans un fichier et passé à ffmpeg en script de filtre ; image et son restent synchrones. Aligner les bornes sur des limites d'images (multiples de 1/30 s).
- **Recalage de la transcription** : pour chaque mot gardé, nouveau temps = ancien temps − somme des durées retirées avant lui. Tout ce qui vient après (sous-titres, animations, bruitages) lit **cette** transcription. Toute modification ultérieure du montage reconstruit ce qui en dépend à partir de la même table.
- **Ordre** : passe 1 → passe 2 sur la transcription déjà recalée → rendu de la coupe propre **une fois** → verrouillage du montage après la maquette animée, avant les graphismes soignés.
- **Raccord audio** : coupe franche ; pour un son plus serré, un fondu de 20 à 30 ms peut être ajouté. Jamais de fondu sur le dernier mot.
- **Pièges** : normaliser toutes les entrées vidéo sur la même base de temps avant de superposer ; télécharger le fichier entier et couper en local ; mettre un silence artificiel à l'endroit d'un mot rogné le fait sonner « coupé ». La version qui marche a moins de coupes, toutes entre les phrases, quitte à durer quelques secondes de plus.

## 7. Son
- Ni musique ni bruitage à cette étape. On ne normalise la voix qu'à l'étape de mixage (skill `son`, −14 LUFS).
- Écouter chaque raccord : un mot amputé s'entend même quand la transcription le « devine » correctement.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] L'original est intact ; la coupe est faite en une seule passe.
- [ ] Aucune coupe à l'intérieur d'un groupe de souffle ; chaque mot voisin d'une coupe est entier (**retranscrire le rendu final** et comparer les mots de chaque raccord avec le brut, puis écouter).
- [ ] Synchro des lèvres : comparer l'image de chaque raccord avec le brut (un nombre d'images identique ne prouve pas que ce sont les bonnes).
- [ ] Bandes de 10 images de part et d'autre de chaque coupe : aucune image vide, aucun saut de cadre.
- [ ] Chaque coupe de la passe 2 a été approuvée et sa raison est écrite.
- [ ] Les respirations après virgule et après un mot d'annonce (« D'abord, ») sont toujours là.
- [ ] La transcription recalée correspond à la vidéo coupée (contrôle sur 5 mots répartis).
- [ ] La voix n'a été ni accélérée ni ralentie.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Pas d'aperçu libre de droits : les vidéos d'exemple du dépôt d'origine sont à droits réservés et portent la marque de leur auteur. Aperçu Flot Web à produire (avant / après sur un même rush).

## 10. Origine
- Dépôt : nateherkai/hyperframes-student-kit (« Herk Edit Kit »), commit `10511e5`. Fichiers : `.claude/skills/cut-silences/SKILL.md`, `.claude/skills/cut-mistakes/SKILL.md`, `docs/EDITING-PLAYBOOK.md` (parties « The edit, step by step », « House reel style », « Lessons that cost us time »).
- Licence : MIT (© 2026 Nate Herk) pour le kit d'origine ; ajouts « pipeline » sous la permission d'usage du kit, **à conserver** : « Herk Edit Kit Use Permission. Copyright 2026 the contributors to this teaching kit. » (texte complet dans `licenses/styles-montage-documentaire.md`).
- Adaptations Flot Web : réécriture en français, transcription par les outils du skill `rendu`, scripts d'origine non repris (règles et seuils seulement), marque et copies HyperFrames de l'auteur ignorées.
