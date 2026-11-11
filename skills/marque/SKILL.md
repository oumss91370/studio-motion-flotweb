---
name: marque
description: "Construire, lire et tenir à jour la fiche « ma chaîne » du client (niche, public, persona, nom, ton, palette, typographie, personnages récurrents, ambiance, format et rythme de publication). À utiliser au paramétrage d'une chaîne, quand le client dit « règle ma chaîne », « change mes couleurs », « c'est quoi ma niche ? », et avant chaque vidéo pour lire la fiche."
---

# Marque : la fiche « ma chaîne »

Sans fiche, chaque vidéo choisit ses propres couleurs, sa propre police et son propre ton, et la chaîne ne ressemble à rien. La fiche « ma chaîne » est la mémoire de la marque du client : on la construit une fois, on la lit avant chaque vidéo, on la corrige quand le client change d'avis.

Le skill `studio-coeur` pilote la conversation (mode paramétrage) ; ce skill dit **quoi demander, quoi proposer, et comment écrire la fiche**.

## Où vit la fiche

1. **Sur le compte Flot Studio du client**, si le connecteur est branché et que ses outils sont dans ta liste : `profil_chaine` la lit ; `parametrage_etat` et `parametrage_repondre` la construisent étape par étape (outils annoncés, à venir : voir `studio-coeur`, `references/parametrage.md`).
2. **Sinon dans le fichier `ma-chaine.md`**, à la racine du dossier de travail du client, d'après `gabarits/ma-chaine.md`.

Ne tiens pas deux fiches différentes. Si les deux existent, celle du compte fait foi ; signale les écarts au client. N'écris la fiche nulle part ailleurs, et jamais dans les fichiers d'instructions de l'assistant du client sans qu'il le demande.

## Les règles

1. **Jamais de trou comblé par une supposition silencieuse.** Si le client ne sait pas, tu proposes ; s'il te laisse choisir, tu choisis et tu écris « (choix de l'agent) » à la fin de la valeur, pour qu'il puisse la retrouver et la changer.
2. **Ce que le client a tapé gagne** sur ce que tu as relevé d'une image ou d'un site (une couleur lue sur une image est toujours un peu fausse).
3. **La fiche fixe le look, pas l'ambition.** Elle ne rend pas les vidéos timides : dans le cadre qu'elle pose, on y va franchement.
4. **Une seule chose par rubrique.** Cinq références aux looks différents donnent une chaîne incohérente : fais choisir un look maître, ou dis quel look sert à quoi.
5. **Rien qui n'appartienne pas au client** : logos et polices viennent de ses fichiers ; pas de personnage, de marque ou de musique d'autrui.
6. **Pas de bleu-violet par défaut.** C'est la couleur des vidéos générées sans direction. Si c'est vraiment la couleur de sa marque, note « Bleu-violet autorisé : oui, <raison> » : les contrôles de `studio-coeur` en tiendront compte.
7. **Seulement ce qui sert aux vidéos.** La fiche ne recueille pas d'informations personnelles.

## Construire la fiche

Une question par message, 2 ou 3 options avec ta recommandation en premier, toujours « je ne sais pas, propose-moi » : tu donnes alors les suggestions de `references/suggestions.md`. Écris chaque réponse tout de suite (dans le fichier, ou par `parametrage_repondre`).

| # | Rubrique | La question | Si le client ne sait pas |
|---|---|---|---|
| 1 | Niche | « Ta chaîne parle de quoi, et qu'est-ce qu'on y gagne en la regardant ? » | les 8 familles de niches ; test des 10 sujets |
| 2 | Public | « Qui regarde ? Que sait-il déjà ? » | « des gens qui découvrent le sujet, sur téléphone, souvent sans le son » |
| 3 | Persona | « Qui parle dans tes vidéos ? » | le prof sympa en voix off, ou une mascotte |
| 4 | Nom | « Comment s'appelle la chaîne ? » | 5 noms de formes différentes |
| 5 | Ton | « Trois mots pour dire comment tu parles. » | la liste de 12 mots et ce que chacun change |
| 6 | Palette | « Tes couleurs ? (codes hex, ou un site où les relever) » | 2 ou 3 des 8 palettes prêtes, selon la niche |
| 7 | Typographie | « Tes polices ? » | une paire de polices libres selon le ton |
| 8 | Personnages récurrents | « Y a-t-il un personnage qui revient ? » | aucun (recommandé pour débuter), ou une mascotte simple |
| 9 | Ambiance | « Que doit-on ressentir dans la première seconde ? » | 8 sensations, les styles et le son qui vont avec |
| 10 | Format et rythme | « Où publies-tu, quelle durée, à quel rythme ? » | vertical 9:16, 20 à 30 s, 2 par semaine |
| 11 | Jamais | « Une chose que tes vidéos ne doivent jamais faire ? » | la liste à cocher |
| 12 | À promouvoir | « Y a-t-il une offre ou un lien à mettre en avant ? » (facultatif) | rien : passer |

Regroupe ce qui va ensemble quand le client est à l'aise (palette et typographie, format et rythme). Dix messages environ, pas plus.

### Paramétrage express (le client veut sa vidéo tout de suite)

Cinq questions : niche, public, ton, palette, format. Le reste est rempli avec tes recommandations, marquées « (choix de l'agent) ». Dis-lui que la fiche se complétera au fil des vidéos.

### Les références (facultatif, très utile)

Demande 3 à 5 images ou vidéos qu'il aime (les siennes ou d'autres), rangées dans un dossier `references/` chez lui. Lis-les toutes, puis note dans la rubrique Ambiance ce que tu y vois **vraiment** : couleurs et rôle de chacune, type de police, façon de bouger (vif, doux, saccadé), matière (grain, papier, aplat), ce qui revient. Là où tu ne peux pas trancher, écris « à demander » plutôt que de deviner. Si les références montrent plusieurs looks, nomme-les et fais choisir.

On retient une grammaire, jamais un personnage, un logo, une mélodie ou un plan précis. Les fichiers de référence restent chez le client.

### Contrôler la palette et la fiche

```
python3 scripts/verifier_fiche.py ma-chaine.md
```

Bloquant : une rubrique indispensable vide (niche, public, ton, fond / texte / accent, polices, format et durée), une couleur qui n'est pas un code hex, un bleu-violet non autorisé, un contraste texte / fond sous 4,5. À voir : rubriques encore vides, accent peu visible sur le fond, choix de l'agent à faire confirmer.

Quand la fiche vit sur le compte, recopie-la dans un fichier temporaire au même format pour lancer le contrôle.

### Montrer avant d'enregistrer

À la fin, relis la fiche au client en dix lignes, avec la palette en pastilles de couleur si tu peux en faire une image, et la liste de **tes** choix. Il confirme ou corrige. Ensuite seulement la fiche compte comme terminée.

## Lire la fiche avant une vidéo

Ce que `studio-coeur` y prend :

| Rubrique | Sert à |
|---|---|
| Niche, public | choisir le sujet, le niveau d'explication, les exemples |
| Persona, ton | écrire le script, choisir la voix, tutoyer ou vouvoyer, l'ouverture et la fin habituelles |
| Palette, typographie | le verrou du storyboard ; l'accent garde le sens écrit dans « Ce que montre l'accent » |
| Personnages | qui apparaît, avec quels signes (skill `personnages`) |
| Ambiance | le style proposé en premier, la couleur du son |
| Format, rythme | durée, mise en page, voix ou non |
| Jamais | une liste d'interdits à relire avant de livrer |

**La fiche et le style.** Chaque style a sa propre palette et sa propre typo (fiche `STYLE.md`). Quand elles ne s'accordent pas avec celles de la chaîne :
- garde la structure clair / sombre du style, et fais entrer la couleur de la chaîne **comme accent** ;
- garde la police de la chaîne pour les titres si le style le supporte, sinon celle du style, et dis-le au client ;
- si l'écart est trop grand (une chaîne pastel dans un style noir et néon), propose un autre style plutôt que de dénaturer les deux.

## Tenir la fiche à jour

- Le client corrige quelque chose pendant une vidéo (« pas ce mot », « plus gros », « jamais de rouge ») : demande s'il veut que ce soit la règle pour toutes ses vidéos. Si oui, mets la fiche à jour.
- Chaque changement : la nouvelle valeur dans sa rubrique, une ligne dans le **Journal** (date, rubrique, avant → après, pourquoi), la version augmentée de 1, la date de mise à jour. Sur le compte, le serveur tient la version.
- Un « (choix de l'agent) » confirmé par le client perd sa mention.
- Ne change pas la palette ou le nom d'une chaîne qui a déjà publié sans le dire clairement : les spectateurs reconnaissent une chaîne à ces deux choses.
- Tous les dix épisodes environ, ou quand les vidéos commencent à diverger de la fiche : propose une relecture rapide.

## Fichiers

| Fichier | Contenu |
|---|---|
| `gabarits/ma-chaine.md` | le gabarit de la fiche, 12 rubriques et un journal |
| `references/suggestions.md` | niches, personas, noms, tons, 8 palettes à 6 rôles, paires de polices libres, personnages, ambiances, formats et rythmes |
| `scripts/verifier_fiche.py` | contrôle de la fiche et de la palette (Python 3, sans dépendance) |

Crédits et licences des sources : `licenses/marque.md` à la racine du plugin.
