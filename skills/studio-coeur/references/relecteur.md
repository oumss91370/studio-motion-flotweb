# Le relecteur indépendant

Celui qui a fabriqué la vidéo la juge mal : il sait ce qu'il a voulu faire et le voit à l'écran même quand ça n'y est pas. La relecture est donc faite par **un sous-agent qui n'a pas fait le film** et qui ne voit que le résultat.

## Comment l'envoyer

- Lance un sous-agent neuf, en lecture seule.
- Donne-lui **seulement** : le fichier vidéo, `revue/planche.jpg`, `revue/telephone.jpg`, les bandes de mouvement, et la consigne ci-dessous.
- Ne lui donne **pas** : le brief, le script, le storyboard, la conversation, ton avis, ni la liste de ce que tu as corrigé. Seule exception : la liste des faits et de leurs sources (pour le critère « exactitude ») et, s'il y en a une, la palette et la typo de la fiche « ma chaîne ».
- Il écrit sa réponse dans `relecture/tour-N.md`.
- Sans outil de sous-agent : relis toi-même, en dernier, après avoir fermé le code, en suivant la consigne à la lettre ; écris « relecture faite par le réalisateur, sans sous-agent » dans « Non vérifié » de la note de livraison. C'est un pis-aller, dis-le.

## Règles de la note

- **8 sur 10 ou plus à chaque critère**, sinon la vidéo n'est pas livrée.
- Quand ta note et celle du relecteur diffèrent, **la plus basse compte**. Celui qui juge son propre travail se surnote, d'environ 10 points sur 100 en moyenne.
- Le relecteur ne corrige rien. Il décrit, avec le moment exact.
- Tu ne discutes pas sa note. Tu corriges, ou tu expliques au client pourquoi tu ne corriges pas.

## Consigne à lui donner (à copier telle quelle)

```
Tu es un directeur de l'animation exigeant. Tu n'as pas fait cette vidéo et tu ne connais pas son brief.
On te donne une vidéo verticale pour les réseaux, sa planche contact (une image par seconde), la même
planche à 360 px de large (taille réelle sur un téléphone) et des bandes d'images autour des mouvements rapides.

Ton point de départ est le rejet : la vidéo doit te convaincre. Ne sois pas poli, sois précis.

1. Regarde d'abord les images sans rien lire d'autre, puis écris en UNE phrase ce que la vidéo veut dire.
   Si tu n'y arrives pas, écris-le : c'est un échec de la vidéo, pas le tien.

2. Note chaque critère de 1 à 10 (8 = publiable sans gêne, 10 = rien à reprendre) :
   - accroche : comprend-on l'enjeu dans les 2 à 3 premières secondes, sans le son ? La première image est-elle
     une vraie image ?
   - lisibilité : sur la planche à 360 px, chaque texte se lit-il, reste-t-il assez longtemps, est-il hors des
     zones couvertes par l'interface (haut, bas, bord droit) ? Le sujet est-il assez grand ?
   - mouvement : les gestes ont-ils un élan et un arrêt, ou tout glisse-t-il à vitesse constante ? Une image
     figée hors tenue finale ? Tout apparaît-il en même temps ? Un texte bouge-t-il pendant qu'on le lit ?
   - variété : y a-t-il du nouveau toutes les 2 à 4 secondes ? Les cadrages changent-ils (large, moyen,
     très gros plan) ? Ou est-ce le même plan répété ?
   - composition : un seul point d'attention par image ? Rien de collé au bord, rien qui se chevauche pendant
     une transition, pas de fond mort ? Un seul style et une seule palette du début à la fin ?
   - exactitude : les chiffres et les faits affichés correspondent-ils à la liste fournie ? Les couleurs et la
     police correspondent-elles à la fiche de la chaîne, si on te l'a donnée ? Un logo, un personnage ou une
     marque qui n'appartient visiblement pas à l'auteur ?
   - son : les sons tombent-ils sur les actions ? Y a-t-il un silence avant le moment fort ? La musique
     couvre-t-elle la voix ? Si tu ne peux pas écouter la vidéo, écris « non écouté » et ne mets PAS de note :
     une note inventée est pire qu'une note absente.

3. Cherche en particulier le « look IA » et le diaporama : dégradé bleu-violet, néons et lueurs, particules
   sans raison, titre centré sur un dégradé, textes qui arrivent en fondu l'un après l'autre, la même poussée
   de caméra à chaque plan, étiquettes dans les coins, texte flou parce qu'agrandi, personnage qui glisse
   sans jouer, phrase centrée pour finir.

4. Écris les 3 pires défauts, du pire au moins grave, chacun avec le moment (en secondes) et ce qu'on voit.
   Pas de solution technique : décris le défaut.

5. Nomme le plan le plus faible de la vidéo, et le plan le plus fort.

Réponds exactement sous cette forme :

Ce que dit la vidéo : <une phrase>

- accroche : N/10 — <pourquoi, en une ligne>
- lisibilité : N/10 — …
- mouvement : N/10 — …
- variété : N/10 — …
- composition : N/10 — …
- exactitude : N/10 — …
- son : N/10 — …

Les 3 pires défauts :
1. <t> s : …
2. <t> s : …
3. <t> s : …

Plan le plus faible : <moment> : <pourquoi>
Plan le plus fort : <moment> : <pourquoi>
Verdict : livrable / à corriger
```

## Ce que tu fais de sa réponse

1. Compare sa phrase « ce que dit la vidéo » avec l'idée validée par le client. Si elles ne disent pas la même chose, le problème est dans l'histoire ou le storyboard, pas dans les finitions : reviens-y avant de retoucher des détails.
2. Ses 3 pires défauts deviennent tes 3 corrections du tour (voir `controles.md`).
3. Le « son » sans note : fais écouter le mix avec le skill `son` (il sait écouter une piste), reporte la note obtenue dans le fichier de relecture en indiquant d'où elle vient, ou obtiens l'accord du client.
4. Au tour suivant, le relecteur est **un nouveau sous-agent**, qui ne sait pas ce qui a été corrigé.
5. Son « plan le plus faible » est celui que tu passes à `note_livraison.py`, sauf si tu en vois un pire.

## Faire entrer un nouveau style dans le catalogue

Autre usage du relecteur, pour qui ajoute un style : la démo d'un style est notée sur 100 par un relecteur indépendant, et il faut 80.

| Critère | Points |
|---|---|
| Signatures du style présentes (3 à 5 éléments qui le font reconnaître) | 35 |
| Matière crédible (on croit au papier, à l'encre, à la peinture) | 20 |
| Composition dans la logique du style | 15 |
| Personnages et objets | 15 |
| Dynamique (ce qui bouge, comment) | 10 |
| Technique (netteté, stabilité, rendu identique à chaque passe) | 5 |

Refus direct si les signatures font moins de 25, ou si les personnages paraissent bâclés.

Sources : critique notée « juge ≠ constructeur » et ses sept critères, claude-motion-design (Howseen AI, MIT) ; relecteur indépendant, règle de la note la plus basse et barème sur 100, huashu-art-motion (alchaincyf, MIT, protocole 16) ; liste des défauts « vidéo IA générique », animate (cth9191, MIT). Réécrit.
