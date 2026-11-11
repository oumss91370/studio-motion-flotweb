# Zones d'interface et première image (vertical 1080×1920)

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

L'application dessine par-dessus la vidéo : barre du haut, légende, nom du compte et boutons en bas, colonne de boutons à droite. Ce qui est dessous ne se lit pas.

## Les zones du studio (table de référence unique)

**Cette table est la seule référence du plugin.** Les autres skills et les fiches de style y renvoient ; la porte de livraison (`studio-coeur`, `scripts/controle_textes.py`) contrôle exactement ces valeurs.

```
x = 0   60                            945   1080
y = 0    ┌──────────────────────────────────────┐
         │  HAUT : rien d'important (160 px)    │
y = 160  ├────┬────────────────────────┬────────┤
         │    │                        │        │
         │    │  ZONE UTILE            │ DROITE │
         │    │  x 60 → 945            │ 135 px │
         │    │  y 160 → 1560          │ rien   │
         │    │                        │ d'im-  │
y = 1330 │    │ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  │ portant│
         │    │  texte secondaire      │        │
y = 1560 ├────┴────────────────────────┴────────┤
         │  BAS : rien d'important (360 px)     │
y = 1920 └──────────────────────────────────────┘
```

| Zone | Pixels (1080×1920) | Ce qu'on y met |
| --- | --- | --- |
| Haut | y de 0 à 160 | fond, décor |
| Bas | y de 1560 à 1920 (360 px) | fond, décor ; jamais de texte, de sous-titre ni de logo |
| Droite | x de 945 à 1080 (135 px) | fond, décor ; la colonne de boutons occupe surtout la moitié basse |
| Marge gauche | x de 0 à 60 | fond, décor |
| **Zone utile** | **x de 60 à 945, y de 160 à 1560** | tout ce qui se lit, le visage, le produit. C'est la limite que la porte de livraison contrôle |
| Sous-titres | bas du bloc entre y = 1220 et y = 1320 | voir `sous-titres.md` |

Conseil de placement, à l'intérieur de la zone utile (ce n'est pas une seconde limite) : le texte **indispensable** se place de préférence au-dessus de y = 1330. Entre y = 1330 et y = 1560, la légende dépliée et les publicités peuvent recouvrir l'image : y mettre la suite du sujet, le décor ou un texte secondaire. HyperFrames donne ce même repère (`officiel/hyperframes/references/types/vertical.md` : mots et produit jusqu'à 1330). Pour une publicité, remonter tout le texte au-dessus de y = 1250.

Autres formats (carré, paysage) : marge de 5 % sur chaque bord ; voir « Paysage » en bas de page.

Le centre optique du vertical est un peu au-dessus du milieu : placer le sujet principal autour de y = 700 à 850.

## Tailles de texte

- Titres : environ ×1,35 par rapport au paysage (un titre de 72 px en paysage devient 96 px). Chiffres clés : ×1,4.
- Rien de ce qui doit être lu sous 28 px ; sous-titres jamais sous 42 px.
- Environ 5 mots par ligne pour une affirmation. Trop long : on coupe des mots, on ne réduit pas la taille.
- Test du téléphone : la capture réduite à 360 px de large doit rester lisible.

## Première seconde

- **Image 0 = vignette + accroche** : un visage, le résultat, ou une ligne forte déjà à l'écran. Jamais noire, jamais un logo seul, jamais un fondu depuis le noir.
- La personne décide en une seconde environ : le changement ou la question arrive dans le premier temps.
- L'accroche se comprend sans le son.

## Rythme du vertical

Plans de 1 à 2 s, un nouveau temps fort toutes les 2 à 4 s, la chute avant que la personne ne passe à la suite. Une boucle (dernière image qui raccorde sur la première) est un choix, pas un défaut. Les règles de mouvement détaillées sont dans le skill `principes-mouvement`.

## Contrôler

Dessiner les zones sur une capture ou sur une image du rendu, puis ouvrir le PNG :

```bash
npx -y hyperframes@0.9.33 snapshot --at 0,3,8
PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/rendu/scripts/zones.py" .hyperframes/artifacts/snapshots/<dossier>/<capture>.png
PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/rendu/scripts/zones.py" renders/ma-video.mp4 --a 3 -o controle-zones.png
```

Voile rouge translucide (30 %, l'image reste lisible dessous, sur une capture comme sur une image du MP4) : zones interdites. Cadre vert : zone utile. Trait jaune : y = 1330 (texte indispensable de préférence au-dessus). Aucun mot, visage ou élément clé ne doit toucher le rouge ; tout texte à lire doit tenir dans le cadre vert. Faire ce contrôle sur l'image 0, sur chaque plan qui contient du texte et sur un sous-titre.

Les guides ne se dessinent **jamais** dans la composition elle-même : l'éditeur affiche les siens, et le script ci-dessus ne modifie qu'une copie.

## Liste de contrôle

- [ ] Image 0 lisible, non noire, accroche présente.
- [ ] Aucun texte ni élément clé hors de la zone utile : au-dessus de y = 160, sous y = 1560, à droite de x = 945, à gauche de x = 60.
- [ ] Texte indispensable de préférence au-dessus de y = 1330.
- [ ] Sous-titres entre y = 1220 et y = 1320, jamais sur un visage.
- [ ] Aucun texte sous 28 px ; lisible à 360 px de large.
- [ ] Un sujet par plan, centré, empilé verticalement.

## Paysage (YouTube)

Contenu dans les 90 % centraux de l'image, textes clés et sous-titres dans les 80 % centraux ; sous-titres à 80–120 px du bas. Le lecteur YouTube recouvre le bas (barre de lecture) et le coin inférieur droit (filigrane) pendant les premières secondes et à la pause.
