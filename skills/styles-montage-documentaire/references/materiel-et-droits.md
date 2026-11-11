# Matériel réel, droits et faits (commun à la catégorie)

Les styles de cette catégorie sont faits de **matériel réel** : rushes du client, archives, photos, documents, données, imagerie. Ce fichier dit d'où le prendre, ce qu'on a le droit d'utiliser, et comment prouver ce qu'on affirme. Il s'applique à toutes les fiches ; chaque fiche ajoute ses sources propres (imagerie satellite, relevés laser, fichiers de CAO, lames de microscope…).

## 1. Demander d'abord au client

Avant toute recherche, une seule question : « As-tu ton propre matériel pour ce sujet, et le droit de l'utiliser ? » Vidéos, photos, documents (rapports, courriers, factures, plans), données (tableur), enregistrements, scans d'archives, fichiers techniques. **Son matériel passe toujours en premier** ; les sources libres ne font que combler les trous.

## 2. Sources libres : où chercher

Juger **chaque fichier sur sa propre page**, jamais sur le résultat de recherche.

| Source | Ce qu'on y trouve | Ce qu'il faut vérifier |
|---|---|---|
| Wikimedia Commons | vidéos, photos, cartes et livres scannés | la licence et l'auteur sur la page du fichier ; pour une vidéo importée d'une plateforme, une revue de licence **validée** (une revue « en attente » ne suffit pas) |
| Agences publiques des États-Unis (NASA, NOAA, USGS, Archives nationales, recensement) | images, films, données, cartes | les œuvres d'agents fédéraux sont dans le domaine public ; vérifier que la page ne crédite pas un prestataire ou un tiers ; ne jamais utiliser un insigne officiel comme graphisme |
| Internet Archive | films et imprimés anciens | uniquement si la page indique domaine public, CC0 ou CC BY ; écarter les copies de plateformes vidéo et les versions colorisées ou « restaurées » |
| Bibliothèques et archives nationales, musées en accès ouvert | photos, presse ancienne, objets | la mention de droits de chaque objet |
| Portails de données publiques (instituts de statistique, villes, IGN, Eurostat, Banque mondiale, Our World in Data) | chiffres, emprises de bâtiments, relevés | les conditions de chaque jeu de données ; créditer aussi la source d'origine |
| Documents officiels (rapports, décisions, statistiques) sur le site de l'organisme | la source de chaque fait | citer la formulation exacte |
| Natural Earth | contours pour les cartes dessinées en code | cadrer à l'échelle de la région ; pas de frontières sauf si c'est le sujet ; zones disputées hors cadre |

## 3. Licences : feu vert, feu orange, feu rouge

- **Feu vert** : domaine public, CC0, CC BY (créditer auteur, titre, licence, à l'écran quand la fiche le demande et toujours dans `CREDITS`), licences ouvertes d'État à simple attribution.
- **Feu orange, dire les conditions au client et demander son accord avant d'utiliser** : CC BY-SA et autres licences de partage à l'identique (dont les bases cartographiques collaboratives), « aucune restriction connue » (ce n'est **pas** une licence), conditions propres à un portail.
- **Feu rouge, jamais** : licences non commerciales (NC), images d'agences de presse, extraits d'émissions ou de matchs de diffuseurs, captures de services de cartographie commerciaux, origine inconnue, copies sans source, versions colorisées ou « restaurées par IA », figures de revues scientifiques.
- **Jamais d'image générée présentée comme une archive, une preuve, un objet réel ou un lieu réel.** Une image d'illustration générée porte la mention « ILLUSTRATION » tant qu'elle est à l'écran.
- **Les films de démonstration cités dans les fiches** contiennent des rushes, photos et données de tiers sous leurs propres licences : on y renvoie par un lien, on n'en extrait rien.

## 4. Avant de télécharger

Dire au client, en un message : **quoi** (titre, durée ou nombre de pages), **d'où** (adresse de la page), **sous quelle licence**, et le poids estimé. Garder le dossier des sources brutes sous environ 1,5 Go ; ne télécharger que les secondes ou les pages utiles ; une requête à la fois sur les sites qui limitent le débit.

## 5. Les trois fichiers à tenir dans le projet

- **`SOURCES.md`** : pour chaque fichier, titre, auteur, date, licence, adresse de la page, et les secondes (ou pages) réellement utilisées.
- **`FAITS.md`** : pour chaque nombre, date, nom et affirmation à l'écran ou dans la voix : l'adresse de la source, **la formulation citée**, et pour toute valeur dérivée (somme, ratio, mesure) le calcul ou la méthode. Les déductions sont listées à part et marquées à l'écran (`≈`, « déduit », « schéma »). Relire le script et les sous-titres contre ce fichier avant le dernier rendu.
- **`CREDITS`** : tout le matériel tiers utilisé, avec sa licence ; livré avec la vidéo.

Règles d'écriture : **les mots ne sont jamais plus forts que la source** ; ce que seul un article affirme est attribué (« selon… ») ; quand deux sources primaires se contredisent, en choisir une et noter le conflit ; les pages officielles changent, donc citer la page **et l'année**.

## 6. Personnes à l'écran

- Aucun gros plan ni ralenti d'une personne privée identifiable ; on montre les anonymes en groupe, au travail, en plans brefs, ou en foule.
- Personnalités publiques et personnes au cœur d'un événement d'actualité : possible, sans moquerie.
- Flouter numéros de téléphone, plaques, noms lisibles, adresses ; cadrer hors champ maisons et jardins dans les vues aériennes et les relevés.
- Jamais de portrait généré présenté comme la photo d'une personne réelle.

## 7. Qualité d'image du matériel réel

| Matériel | Agrandissement maximal | Préparation (ffmpeg) |
|---|---|---|
| Image récente | 1,5× | recadrage, `lanczos`, `unsharp=5:5:0.45` |
| Film d'archive | 2,5× | `hqdn3d` → `lanczos` → léger `unsharp` ; un seul réglage de niveaux par plan |
| Photo, scan, document | 1 pixel source par pixel écran | recadrer sur la partie utile |

- Retirer filigranes, logos de chaîne et cartons d'archive **en recadrant**, jamais en les couvrant d'un texte ; écarter les plans au texte incrusté.
- Le grain s'ajoute à l'encodage final, pas dans la page.
- Le texte imprimé dans un document reste une image : ce qui doit être lu est recomposé en typographie (ou surligné), et un texte qui n'existe qu'en transcription est étiqueté « transcription ».

## 8. Temps de lecture (rappel commun)

La règle chiffrée est celle de la porte de livraison (`studio-coeur/references/controles.md`, section 2) ; pour cette catégorie, lancer le contrôle avec `--strict`.

- Texte à l'écran : (nombre de lettres ÷ 15) + 1,5 s, jamais moins de 1,5 s, immobile et entièrement dans le cadre (règle `--strict`).
- Sous-titre en phrase entière : la durée de la phrase dite + 0,6 s, 1,8 s au moins. Sous-titres au mot : 0,7 s au moins, 17 caractères par seconde au plus (règle de la porte).
- Comparaison, verdict : chaque élément entièrement visible au moins 2,5 s avant la suite.
- Compteur : compté à sa valeur d'arrivée.

Origine de ces règles : sections « Material », « Footage », « Facts » et « Pitfalls » des fiches de lemomo-ai/lemo-opuscar (commit `9eb7739`, MIT), réunies et adaptées par Flot Web.
