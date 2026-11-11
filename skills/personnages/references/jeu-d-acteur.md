# Jeu d'acteur

Sources : cours « 2.5D motion studio » (partie « Acting, not bouncing »), `ANIMATION_GUIDE.md` de ClaudeAnimationBase (John Heibel, MIT), skill `painted-animation` d'opus-video-skills (tuzhechen2005, MIT).

## Le problème

Du mouvement écrit en code sort mécanique : toutes les parties bougent en même temps, sur la même courbe, de la même quantité. Et le personnage ne pense pas : il rebondit, salue, sourit, sans que rien ne se passe sur son visage avant.

Le remède tient en une phrase : **le personnage remarque, pense, puis agit, et les yeux bougent en premier.** Le spectateur comprend un choix quand il le voit se faire.

## La ligne de jeu

Une par plan où un personnage est à l'écran. Elle s'écrit **avant** d'animer, dans la liste de plans, avec des numéros d'image.

```
PLAN 07 (2,1 s, images 372-434)  « toute la cour a ri »
  pensée        l'inventeur sait qu'il a raison
  anticipation  les yeux se plissent d'abord, 4 images avant tout autre mouvement (380)
  action        la tête se tourne vers la caméra sur le mot « ri » (396)
  tenue         rester sur le regard 10 images (396-406)
  émotion       déterminé  (entrée à 380, réaction 0,7)
  bouche        fermée ; petite-ouverte sur « ri » seulement
```

### Pensée

Ce que le personnage comprend, veut, craint ou décide **dans ce plan**. Si on ne trouve pas de pensée, le personnage n'a rien à faire dans le plan : montrer autre chose (l'objet, le décor, un autre personnage).

Une bonne pensée change quelque chose entre la première et la dernière image du plan.

### Anticipation

Le petit mouvement qui prépare le grand et dit au spectateur où regarder.

- **Toujours un regard d'abord** : les yeux se tournent, se plissent ou s'ouvrent 3 à 6 images avant que le reste bouge.
- Pour un grand mouvement, un petit mouvement en sens inverse : un léger recul avant d'avancer, un tassement avant de se redresser.
- Ordre des parties : yeux, puis tête, puis corps, puis bras ; ce qui pend (chapeau, cape, accessoire) arrive en dernier et dépasse un peu.

### Action

**Un seul** mouvement principal par plan, calé sur **un mot** de la voix (son image de début, donnée par les temps mot à mot).

- Rapide si elle a été annoncée : 4 à 8 images pour un tour de tête, 6 à 10 pour un geste du bras.
- Sur un arc, jamais en ligne droite.
- Poussée plus loin que ce qui semble naturel : dans une vidéo courte, le subtil ne se lit pas.

### Tenue

Le temps où l'on reste sur la pose. Une action peut être très rapide, mais **ce qu'elle veut dire a besoin de temps tenu**.

- 8 à 12 images au minimum ; 20 à 30 pour la réaction qui porte le plan.
- Pendant la tenue, le personnage ne se fige pas : il respire, il peut cligner une fois.
- La coupe arrive après la tenue, pas pendant l'action (sauf coupe volontaire dans le mouvement).

## Le temps du spectateur

Celui qui a écrit le plan sait ce qui s'y passe. Le spectateur le voit une seule fois, à vitesse réelle.

- Lister pour chaque plan **ce que le spectateur doit comprendre**, dans l'ordre. Chaque élément a besoin de temps pour être trouvé, compris et enregistré.
- **Une chose à la fois.** Quand deux choses arrivent en même temps, le spectateur n'en voit qu'une. Une cause, puis sa réaction, jamais superposées.
- **Mener l'œil** : le regard va vers ce qui bouge, ce qui est clair, ce qui est grand, ou ce qu'un personnage regarde. Avant un moment important, amener l'œil au bon endroit.
- Aller vite sur ce qui ne compte pas, s'arrêter sur ce qui compte. Une vitesse constante, rapide ou lente, aplatit tout.

## Repos : respirer, pas rebondir

**Interdit** : le balancement en boucle, le sautillement permanent, le hochement de tête régulier, les bras qui battent sans raison. C'est la signature de l'animation générée.

Seule exception, le registre « jeu cartoon » (catégorie `styles-cartoon`, mascottes, vidéos musicales ; voir `31-emotions.md`) : le corps peut rebondir en continu **à condition d'être calé sur le tempo de la musique**. En jeu sobre (défaut, et toujours pour la 2.5D « histoire vraie »), l'interdit est entier.

**Autorisé au repos** :

| Mouvement | Valeurs de départ |
|---|---|
| Respiration | échelle verticale du corps de 1,00 à 1,015, cycle de 3 à 4 s, courbe douce |
| Clignement | yeux `fermes` pendant 2 à 3 images, toutes les 3 à 6 s, jamais à intervalle fixe, jamais pendant une action |
| Regard | un déplacement des yeux quand quelque chose bouge ailleurs dans le plan |

Deux personnages dans le même plan : ils ne respirent pas en phase, ne clignent pas ensemble, ne bougent pas au même instant. Celui qui écoute regarde celui qui agit.

## Les bouches

La bouche n'est pas un synchronisme labial. Dans une vidéo racontée par un narrateur, le personnage ne parle presque jamais.

- Bouche `fermee` par défaut.
- **Échanger la bouche seulement sur les mots accentués** : 2 à 4 par phrase, ceux que la voix appuie (le chiffre, le nom, le verbe fort, le mot de la chute).
- Une bouche ouverte dure le temps du mot (6 à 12 images), puis revient à `fermee`.
- Si le personnage « dit » la phrase (citation, réplique) : `petite-ouverte` sur les mots accentués, `grande-ouverte` sur le mot le plus fort, rien entre.
- Jamais de bouche qui s'ouvre et se ferme à chaque syllabe.

Pour trouver les mots accentués : écouter la voix (skill `son`), ou repérer dans les temps mot à mot les mots les plus longs et ceux suivis d'un silence.

## Changer d'expression

Voir `31-emotions.md`, section « Changer d'émotion ». En résumé : plissement des yeux, échange caché sous le plissement, réaction du corps à la taille de l'émotion, stabilisation. Un visage qui passe d'une expression à l'autre entre deux images, sans rien autour, est une erreur.

## Principes à garder en tête

- **Poids** : ce qui est lourd met du temps à partir et à s'arrêter, et retombe sans rebond.
- **Écrasement et étirement** à volume constant : très peu sur un personnage sobre (2 à 5 %), davantage en cartoon.
- **Ralentir en entrée et en sortie** de chaque pose.
- **Pas de jumeaux** : un bras fait l'action, l'autre fait moins et un peu plus tard.
- **Action secondaire** : un chapeau qui suit, une cape qui retombe. Elle soutient l'action principale et ne lui vole jamais l'attention.
- **Direction à l'écran** : un personnage qui va vers la droite continue vers la droite au plan suivant.
- **Taille** : en plan moyen, le personnage occupe au moins un quart de la hauteur du cadre ; en gros plan, le visage remplit la moitié de la largeur. Un personnage minuscule ne joue pas.

## Animer dans l'ordre

1. Poser les **poses clés** (début, anticipation, action, tenue) en interpolation constante.
2. Les regarder en images fixes. Si elles ne se lisent pas, le mouvement ne les sauvera pas.
3. Ajouter le mouvement entre les poses, avec les décalages entre parties.
4. Regarder une bande d'images de l'action.
5. Ajouter respiration et clignements en dernier.

## Erreurs fréquentes

| Erreur | Correction |
|---|---|
| Le personnage rebondit pendant tout le plan | Supprimer la boucle ; garder la respiration. |
| Le geste part sans prévenir | Ajouter le regard 3 à 6 images avant. |
| Tout bouge à la même image | Décaler : yeux, tête, corps, bras. |
| La pose n'est tenue que 3 images | Tenir 8 à 12 images, raccourcir autre chose. |
| La bouche s'agite sur toute la phrase | Garder 2 à 4 mots accentués. |
| Le visage change d'un coup | Passer par le plissement et la réaction. |
| Deux personnages bougent ensemble | L'un agit, l'autre regarde ; puis l'inverse. |
| Le personnage sourit sans raison | Écrire la pensée ; sinon visage neutre. |
| Le personnage tient une pancarte qui dit ce qu'il ressent | Le montrer par le jeu : regard, pose, marque dessinée. |
