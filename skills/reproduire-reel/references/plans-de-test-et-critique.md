# Plans de test, planche à trois colonnes, critique indépendante

Le contrôle chiffré porte sur un élément isolé. Les plans de test montrent si la technique tient **dans de vrais plans**, et un regard neuf dit ce qui trahit encore la différence. On fait cela **avant** le film entier : refaire 8 secondes coûte quelques minutes, refaire un film coûte des heures.

## 1. Choisir les plans de test

- 3 à 5 plans, 8 à 10 secondes en tout.
- Ils couvrent : **chaque ambiance** de lumière du film, un gros plan et un plan en pied, un plan où un personnage joue, un plan d'objet ou de décor.
- Ce sont des plans **de notre film**, avec nos personnages, notre voix, nos sous-titres.
- Garde les mêmes plans d'un tour à l'autre : c'est ce qui rend les versions comparables.
- Lance les rendus **au premier plan** et attends leur fin. Ne rends jamais la main pendant qu'un rendu tourne : le tour se termine sans critique ni compte rendu, et il faut tout relancer. Un seul Blender à la fois.

## 2. La planche à trois colonnes

Colonnes : **référence** (l'image de la référence au cadrage et à l'ambiance les plus proches) | **version précédente** | **nouvelle version**. Au premier tour, deux colonnes suffisent.

```
python $S/cote_a_cote.py revue/planche.json
```
Le fichier (gabarit `gabarits/planche.json`) donne, pour chaque ligne, les trois images et le centre du recadrage agrandi dans chacune (la tête, le titre, l'objet). Les recadrages sont agrandis au plus proche voisin : pas de lissage qui flatterait notre rendu.

Cette planche sert trois fois : au critique, au client, et au compte rendu.

## 3. La critique indépendante

**Qui** : un agent qui n'a **pas** fait le travail, sans accès à tes notes ni à tes réglages. On se surnote soi-même.

**Ce qu'il reçoit** : les plans de test, la planche à trois colonnes, des images pleine résolution de la référence et de nos plans (pas seulement des vignettes), et `gabarits/consigne-critique.md`. Il ne reçoit ni la fiche de style ni le tableau d'écart : il juge ce qu'il voit.

**La question, unique** : « Le rendu est-il au niveau de la référence ? Qu'est-ce qui trahit encore la différence ? »

**Ce qu'il rend** : une note sur 10 pour la référence, la version précédente et la nouvelle (et par plan si elles diffèrent), puis la liste des écarts, chacun avec OÙ (plan, zone), PROBLÈME, CHANGEMENT proposé, À GARDER.

Vérifie avant de l'envoyer que les images pleine résolution existent bien dans le dossier que tu lui donnes : une extraction qui échoue en silence l'oblige à juger sur des vignettes.

## 4. Trier la critique avec la mesure

Pour **chaque** remarque, une décision écrite :

| Décision | Quand |
|---|---|
| **Retenue** | la remarque est juste et la mesure ne la contredit pas, ou la mesure ne couvre pas ce point (une ombre qui flotte, un effet autocollant, une couleur trop vive dans son contexte) |
| **Non retenue** | la mesure dit le contraire. Cite le chiffre et l'image |
| **Reportée** | juste, mais hors du temps ou du périmètre de ce tour. Elle va dans « ce qui reste différent » |

**Quand le critique et la mesure se contredisent, la mesure tranche.** Dans l'essai du studio, sur dix remarques, deux ont été démenties : le critique voyait de jour un rapport plein / délié de 1,4 à 1,8 (la seule tête de jour sans chapeau mesurait 0,019 D en haut et 0,074 D en bas, soit près de 4) ; il voyait l'ombre du torse du mauvais côté (deux images mesurées la plaçaient bien le long du bord éclairé). Les corriger aurait éloigné notre rendu de la référence.

L'inverse est vrai aussi : la mesure ne voit que ce qu'on lui désigne. Cinq remarques retenues ce jour-là portaient sur des choses que le tableau d'écart donnait « dans la tolérance » ou ne regardait pas (l'ombre décollée des pieds, la tête trop géométrique, le blanc des yeux). **Le critique dit où regarder, la mesure dit qui a raison.**

Avant d'écarter une remarque, vérifie que la mesure porte bien sur le même cas (même ambiance, même élément). Si tu n'as pas la mesure, fais-la : ne tranche pas de mémoire.

## 5. Corriger, puis dire où on en est

1. Un tour de corrections sur les remarques retenues ; re-rends les plans de test ; refais la planche.
2. Repasse le contrôle chiffré : une correction demandée par le critique peut faire sortir une ligne de la tolérance (rendre une tête moins géométrique change sa courbe). Si c'est un choix, écris-le.
3. Seconde critique si le temps le permet. Sinon écris : « la note porte sur l'état d'avant corrections ».
4. Garde l'état d'avant corrections dans un dossier à part : rien ne se supprime.

Au client, sans arrondir : **la note du critique telle quelle**, ce qu'il a trouvé, ce qui a été corrigé, ce qui a été écarté et pourquoi, **ce qui reste différent et pourquoi**. Une note de 6,5 sur 10 avec la liste de ce qui manque vaut mieux qu'un « c'est très proche ».
