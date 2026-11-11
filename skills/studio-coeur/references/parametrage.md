# Mode paramétrage

Le paramétrage construit la fiche « ma chaîne » : qui est le client, pour qui il publie, à quoi ressemblent ses vidéos. Il se fait une fois, puis se retouche. Le contenu de la fiche et les suggestions par défaut sont dans le skill `marque` ; ce document dit **comment conduire la conversation et où enregistrer**.

Le client le lance en disant par exemple : « Avec le connecteur Flot Studio, lance mon paramétrage », « continue mon paramétrage », « on règle ma chaîne ».

## Deux façons d'enregistrer

### A. Avec le connecteur Flot Studio (outils annoncés, à venir)

Ces quatre outils sont prévus côté serveur. **Vérifie qu'ils sont dans ta liste d'outils avant de t'en servir.** S'ils n'y sont pas, passe en B sans en parler comme d'une panne.

| Outil | Ce qu'il fait |
|---|---|
| `parametrage_etat()` | renvoie l'étape en cours, la question à poser, les suggestions par défaut, et les demandes en attente que le client a faites depuis sa page |
| `parametrage_repondre({ etape, reponse })` | enregistre la réponse du client et renvoie l'étape suivante |
| `profil_chaine()` | renvoie la fiche complète, avec sa version |
| `feuille_de_route({ workflow })` | renvoie la marche à suivre pour la première vidéo, selon la fiche et la catégorie choisie (les droits sont vérifiés) |

La boucle :

1. `parametrage_etat()`.
2. S'il y a des **demandes en attente** (le client a cliqué « Demander à mon agent » sur sa page : une critique de son histoire, des idées de niches, des variantes de personnage), traite-les d'abord et renvoie le résultat par l'outil que le serveur indique pour cela.
3. Pose **la question de l'étape**, une seule, avec les suggestions reçues comme options.
4. Le client répond. S'il hésite, aide-le (voir « Quand le client ne sait pas »). Reformule sa réponse en une ligne et fais-la confirmer si elle est floue.
5. `parametrage_repondre({ etape, reponse })`. Lis ce qui revient : c'est l'étape suivante. Ne saute pas d'étape et n'en invente pas.
6. Recommence jusqu'à ce que le serveur annonce la fin.
7. `profil_chaine()` : relis la fiche au client en dix lignes et demande s'il veut changer quelque chose.
8. Propose la suite : `feuille_de_route({ workflow })` pour sa première vidéo, puis le parcours normal de ce skill.

C'est le serveur qui tient l'ordre et l'état. Si le client s'arrête au milieu, il reprendra où il en était : au retour, `parametrage_etat()` te le dit.

Préviens-le une fois, au début : ses réponses sont enregistrées sur son compte Flot Studio pour construire sa fiche.

### B. Sans le connecteur : le fichier `ma-chaine.md`

Même conversation ; l'état est un fichier dans le dossier du client.

1. Cherche `ma-chaine.md` à la racine du dossier de travail. Absent : crée-le d'après le gabarit du skill `marque` (`gabarits/ma-chaine.md`).
2. L'étape en cours est la première rubrique encore vide (ou marquée « à compléter »), dans l'ordre du skill `marque`.
3. Pose la question, obtiens la réponse, **écris-la tout de suite dans le fichier**, puis passe à la suivante. Une interruption ne perd rien.
4. À la fin, relis la fiche au client et propose sa première vidéo.

Si le connecteur arrive plus tard, propose d'y envoyer la fiche locale en rejouant les étapes ; ne prétends pas qu'elle y est déjà.

## Conduire la conversation

- **Une question par message.** Pas de formulaire.
- **2 ou 3 options**, ta recommandation en premier avec sa raison en une ligne, tirée de ce que le client a déjà dit. Des exemples concrets de sa niche, pas des mots vagues.
- Toujours deux sorties : **« je ne sais pas, propose-moi »** et **« on en parle librement »**.
- **Conversation libre** : quand il la choisit, arrête les questions une à une. Affiche la liste de ce qui est décidé et de ce qui reste, avec ta recommandation pour chaque point ouvert. Il répond dans l'ordre qu'il veut, plusieurs points à la fois. Tu mets la liste à jour à chaque tour, et tu enregistres chaque point réglé (un appel `parametrage_repondre` par étape, ou une écriture dans le fichier).
- **« Décide pour moi »** : prends tes recommandations pour tout le reste, liste-les en un message, enregistre-les en les marquant « choix de l'agent », et dis-lui qu'il peut les changer quand il veut.
- Ne redemande pas ce qu'il a déjà dit, même trois messages plus tôt.
- Dix questions environ, pas plus. Regroupe ce qui va ensemble (palette et typo, format et rythme).
- Reste dans le sujet de sa chaîne. Ne note pas d'informations personnelles qui ne servent pas à faire ses vidéos.

## Quand le client ne sait pas

1. Donne les **suggestions par défaut** : celles renvoyées par `parametrage_etat`, sinon celles du skill `marque` (`references/suggestions.md`).
2. S'il hésite encore, pose une question plus petite et concrète (« tu préfères expliquer ou raconter ? », « tu regardes quelles chaînes ? »).
3. S'il te demande ton avis, donne-le franchement, avec ce que le choix coûte (« une niche très large : plus de sujets, mais plus dur de se faire reconnaître »).
4. Pour l'histoire ou le concept de la chaîne, applique la méthode de `references/histoire.md` : trois pistes, une recommandée, puis critique honnête de ce qu'il propose (ce qui marche, ce qui manque, une amélioration).

## Ce qu'il ne faut pas faire

- Appeler un outil qui n'est pas dans ta liste, ou dire qu'une réponse est « enregistrée sur ton compte » quand elle est seulement dans le fichier local.
- Remplir une rubrique avec une supposition sans la marquer « choix de l'agent ».
- Enchaîner sur la fabrication d'une vidéo avant que la fiche ait au moins : niche, public, ton, palette, typo, format.
- Écrire dans les fichiers de réglage de l'assistant du client (ses instructions permanentes) sans qu'il l'ait demandé. La fiche vit sur son compte ou dans `ma-chaine.md`, nulle part ailleurs.

Sources : entretien « une question par message, recommandation en premier, conversation libre, tu décides » de MY-STYLES.md, lemo-opuscar (LemoLab, MIT) ; `brainstorming` de Superpowers (Jesse Vincent, MIT). Réécrit. Les outils du connecteur sont ceux annoncés par Flot Studio ; leurs réponses exactes seront à vérifier quand ils seront livrés.
