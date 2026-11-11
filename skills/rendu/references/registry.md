# Le registry officiel : blocs et composants prêts à l'emploi

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Résumé en français de `officiel/hyperframes-registry/` et inventaire fait sur le dépôt officiel (commit `ffb13c3`, 11/11/2026) : **457 éléments**, soit 210 blocs, 238 composants et 9 exemples de projet. Le nombre change à chaque version : la recherche en direct fait foi.

- **Bloc** : une scène complète avec sa propre timeline (transition, carte, graphique, titre 3D…). S'installe dans `compositions/<nom>.html`.
- **Composant** : un extrait à fusionner dans une scène (effet de texte, style de sous-titres, mouvement de caméra, texture). S'installe dans `compositions/components/<nom>.html`.
- **Exemple** : un projet de départ (`init --example <nom>`).

Un élément installé est du code ordinaire du projet : on le modifie, on le réduit, on le met aux couleurs de la chaîne.

## Chercher et installer

Il n'existe pas de commande `hyperframes registry` : on cherche avec `catalog`, on installe avec `add`.

```bash
npx -y hyperframes@0.9.33 catalog --query "<ce que le plan doit faire, en anglais>" --json
npx -y hyperframes@0.9.33 catalog --type block --tag vertical --json
npx -y hyperframes@0.9.33 catalog --tag caption-style --json
npx -y hyperframes@0.9.33 add <nom> --json                       # écrit les fichiers, imprime l'extrait de montage
npx -y hyperframes@0.9.33 add <nom> --vars '{"title":"…"}' --json
```

- **Requête en anglais**, même pour une vidéo en français : le catalogue est indexé en anglais (une requête sans mot reconnu répond `No searchable words in query`, ce n'est pas une absence).
- La recherche est locale et n'envoie rien. Le niveau par défaut (`words`) ne trouve que les éléments qui reprennent les mots de la requête ; `--on-device` classe par sens après un téléchargement unique d'environ 33 Mo : le proposer, ne jamais l'activer sans accord.
- `add` a besoin du réseau, même pour un élément déjà installé ; la recherche marche hors connexion.
- Sous PowerShell, passer le JSON de `--vars` par un fichier (les guillemets se perdent).
- Rien ne convient : le dire, puis construire à la main. Ne pas envoyer le signalement proposé par la CLI (`feedback --search-miss`) : la télémétrie est coupée.

## Les 15 éléments nativement verticaux

Tous en 1080×1920 sauf mention. Les autres éléments sont pensés pour le 1920×1080 : les recomposer (voir plus bas), ne pas les écraser.

| Nom | Type | Durée | Ce que c'est | Attention |
| --- | --- | --- | --- | --- |
| `notes-reveal` | bloc | 24,9 s | une note tapée lettre par lettre dans une appli de notes | |
| `message-thread-reveal` | bloc | 25,8 s | une conversation par messages sur un téléphone (bulles, indicateur de saisie, carte de lien) | |
| `notification-cascade` | bloc | 14 s | des notifications qui tombent et s'empilent | |
| `share-sheet-carousel` | bloc | 7,2 s | une feuille de partage qui monte et fait défiler des aperçus | |
| `ai-chat-reveal` | bloc | 19,3 s | une question tapée, envoyée, puis une réponse d'IA mot à mot | |
| `flowchart-vertical` | bloc | 12 s | arbre de décision animé, notes adhésives, curseur | 1440×2560 |
| `week-in-merges` | bloc | 16 s | course d'avatars par ligne (classement) | 1080×1350 (4:5) |
| `vignelli` | exemple | 10 s | typographie forte avec accents rouges | projet de départ |
| `instagram-follow` | bloc | 4,5 s | carte de profil et bouton « suivre » | interface d'une marque tierce |
| `tiktok-follow` | bloc | 4,5 s | carte de profil et bouton « suivre » | interface d'une marque tierce |
| `spotify-card` | bloc | 5 s | carte « en cours de lecture » | interface d'une marque tierce |
| `chatgpt-exchange` | bloc | 14,9 s | échange à la manière d'un assistant, avec tableau | interface d'une marque tierce |
| `claude-exchange` | bloc | 21,4 s | échange à la manière d'un assistant, avec étapes de recherche | interface d'une marque tierce |
| `slack-notification-ad` | bloc | 12 s | écran verrouillé qui se remplit de demandes | publicité HeyGen : contenu à remplacer |
| `heygen-avatar-promo-card` | bloc | 10 s | carte promotionnelle avec mosaïque d'avatars | publicité HeyGen : à éviter |

Éléments étiquetés `vertical` en plus de ceux-ci : `chat-thread`, `notes-typing`, `social-proof-card`, `yt-vertical-fill`.

**Marques tierces.** Les blocs qui imitent l'interface d'une application connue servent d'inspiration de mise en scène. Dans une vidéo vendue ou monétisée : remplacer noms, logos et couleurs par ceux de la chaîne ou par une interface neutre, sauf si la vidéo parle réellement de ce produit et le montre honnêtement. Jamais de logo redessiné ; jamais présenté comme officiel.

## Les 16 styles de sous-titres (`caption-style`)

| Composant | Effet | Convient à |
| --- | --- | --- |
| `caption-highlight` | fond coloré qui balaie derrière le mot actif | réseaux sociaux, énergie haute |
| `caption-pill-karaoke` | pastille avec couleur qui avance mot à mot | musique, voix rythmée |
| `caption-kinetic-slam` | un mot plein écran, entrées alternées | annonce, accroche |
| `caption-editorial-emphasis` | deux polices, fort contraste de taille sur les mots clés | documentaire, récit |
| `caption-clip-wipe` | révélation de gauche à droite par mot | propre, moderne |
| `caption-weight-shift` | la graisse change d'une ligne à l'autre | élégant, typographique |
| `caption-gradient-fill` | texte en dégradé, entrée élastique | vif |
| `caption-emoji-pop` | texte cerné avec émojis | décontracté |
| `caption-neon-glow` | néon cyan et magenta | nuit, jeu |
| `caption-neon-accent` | accents néon multicolores | ludique |
| `caption-glitch-rgb` | aberration chromatique et lignes d'écran | technologie, jeu |
| `caption-matrix-decode` | caractères brouillés avant le mot | science-fiction |
| `caption-particle-burst` | particules sur les mots clés | célébration |
| `caption-parallax-layers` | texte en couches derrière le sujet | profondeur, face caméra détourée |
| `caption-texture` | matière qui coule dans de grandes capitales (6 textures) | dramatique |
| `caption-camera-follow` | une phrase écrite dans un espace plus grand que l'image, la caméra suit | texte seul, sans autre image |

À part : `caption-blend-difference` (étiqueté `text`, pas `caption-style`) inverse le texte par rapport au fond, utile sur un fond imprévisible.

Les composants de sous-titres ont un fond transparent. Sur une image claire ou chargée, ajouter une couche de contraste **dans la composition hôte**, sous l'hôte des sous-titres, pas dans le composant. Méthode complète : `sous-titres.md`.

## Familles utiles pour un studio vertical

| Besoin | Exemples d'éléments (vérifier par `catalog`) |
| --- | --- |
| Transitions | `beat-freeze-cut`, `chromatic-radial-split`, `cinematic-zoom` |
| Surimpressions, bandeaux | `lt-clean-bar`, `editorial-flash-overlay`, `camcorder-hud` |
| Titres et typographie animée | `canopy-part-title`, `code-slice-hero`, exemple `kinetic-type` |
| Données | `bar-chart-race`, `data-chart`, exemple `nyt-graph` |
| Texte et primitives de mouvement | `blur-in`, `bottom-up-letters`, `agent-cursor` |
| Caméra | `camera-shake`, `camera-scan-gate` |
| Démonstration de produit | `before-after-wipe`, `browser-device-stage`, `app-showcase` |
| Textures | `grain-overlay`, `ascii-render-pass`, `aurora`, `blob` |

Étiquettes les plus fournies : `motion-primitive`, `showcase`, `transition`, `typography`, `overlay`, `webgpu`, `background`, `3d`, `product-demo`, `captions`, `data`, `cursor`, `title-card`, `mock-ui`, `social`, `handwritten`, `lower-third`.

## Câbler un bloc

```html
<div id="notification-cascade"
     data-composition-id="notification-cascade"
     data-composition-src="compositions/notification-cascade.html"
     data-start="2" data-duration="8"
     data-track-index="1" data-track-kind="graphics"
     data-width="1080" data-height="1920"
     data-variable-values='{"title":"…"}'></div>
```

- `data-composition-id` doit être l'identifiant interne du bloc ; partir de l'extrait imprimé par `add`.
- `data-duration` : au plus la durée propre du bloc. La timeline du bloc est pilotée par le moteur : ne pas l'ajouter à celle de l'hôte.
- Garder les identifiants préfixés tels qu'installés : deux éléments ne peuvent alors pas se heurter.
- Relier les variables de couleur et de police du bloc à celles de la chaîne (skill `marque`).
- Blocs calés sur la musique : instants donnés par `npx -y hyperframes@0.9.33 beats --json`, moins le `data-start` du montage.

## Câbler un composant

Copier ses balises, son `<style>` et son script dans la scène, et suivre le commentaire en tête du fichier s'il se branche sur la timeline. Prendre la plus grande unité qui convient, puis la modifier.

## Utiliser en vertical un bloc pensé pour le paysage

1. L'installer, le monter dans une scène 1080×1920 avec ses dimensions d'origine (`data-width="1920" data-height="1080"`), puis le cadrer par un conteneur transformé (échelle 0,56 pour tenir en largeur) : acceptable pour un graphique ou une carte.
2. Mieux : ouvrir son fichier et refaire la mise en page en colonne (une chose par ligne, textes ×1,35). Ne jamais étirer.
3. Vérifier les zones d'interface (`zones-interface.md`) et relancer `check`.

## Aperçus et droits

- Chaque élément a une vidéo d'aperçu hébergée par HeyGen (domaine `static.heygen.ai`) ; son adresse exacte est dans le résultat `--json` de `catalog` (champ `preview`) ; galerie : `https://hyperframes.heygen.com/catalog`. **On donne le lien, on ne recopie pas ces vidéos** dans un produit, une page de vente ou une formation.
- Le code des éléments est sous licence Apache 2.0. Quelques blocs 3D (`canopy-part-title`, `code-slice-hero`, `cuboid-carousel`, `frost-sequence-camera-orbit`, `glass-shard-title`, `orbit-card`, `wireframe-portal-title`) embarquent GSAP sous sa propre licence : les installer par `add` chez le client, ne pas les recopier dans le plugin.
- Ce plugin ne contient aucun élément du registry : ils sont téléchargés chez le client à la demande.

Références officielles : `officiel/hyperframes-registry/SKILL.md`, `references/search.md`, `wiring-blocks.md`, `wiring-components.md`, `install-locations.md`, `examples/`.
