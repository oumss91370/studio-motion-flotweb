# Crédits et licences — skill `principes-mouvement`

Ce skill est une adaptation en français, réécrite pour la vidéo verticale et le moteur HyperFrames (HTML + GSAP), de sources publiées sous licence MIT. Chaque source garde ici son auteur, son dépôt, son commit et sa mention de copyright. Le texte complet de la licence MIT est reproduit une fois en fin de fichier ; il s'applique à chacune des sources ci-dessous avec sa propre ligne de copyright.

| Source | Dépôt | Commit | Licence et copyright | Ce qui est repris | Où |
|---|---|---|---|---|---|
| Motion Prompt | `showheyohtaki/motion-prompt` | `7819d3879eb7d5a1475c11c001bedffb5cab64af` (catalogue 1.6950972783) | MIT — Copyright (c) 2026 Shohei Ohtaki | Les 192 fiches et codes d'éléments (`api/v1/en/e/`), les 8 kits (`api/v1/kit/`), l'index `catalog.tsv`, copiés **sans modification** ; noms, résumés, durées et usages traduits et adaptés | `references/motion-prompt/`, `references/dictionnaire-mouvements.md`, noms de gestes dans `references/camera.md` |
| motion-design-skill | `LottieFiles/motion-design-skill` | `f9a8a041b85185ee4881b3471d3415e939aac772` | MIT — Copyright (c) 2025 LottieFiles | Les 12 principes, caractères de mouvement, matières, chorégraphie, rapport distance / durée (proportions gardées, durées recalculées pour la vidéo) | `references/principes.md` |
| claude-remotion-skill | `haidrrrry/claude-remotion-skill` | `1dcbe5e3fc6cf970bd10d3cc05f0a8a5d19d0383` | MIT — Copyright (c) 2025 haidrrrry | Règles chiffrées (décalages, sorties, pauses, zone des 75 %, son avant l'impact), courbes, structure d'un court de 30 s. **Aucun code Remotion repris.** | `references/principes.md`, `SKILL.md` |
| gsap-skills | `greensock/gsap-skills` | `aed9cfd3277740755f6bfc1155c7aa645403b760` | MIT — Copyright (c) 2026 GreenSock | Bonnes pratiques et pièges des skills `gsap-core`, `gsap-timeline`, `gsap-plugins`, `gsap-utils` (défilement, React et frameworks écartés) | `references/gsap.md` |
| claude-motion | `whaleyxbt/claude-motion` | `6f80380b91858dad66524a5b34e027dad656d538` | MIT — Copyright (c) 2026 whaleyxbt | Règles de goût (tenue de lecture, moment héros, objets persistants, anti-patterns). Partie Remotion non reprise | `references/principes.md` |
| claude-motion-design | `howseen-ai/claude-motion-design` | `3d90d349ef3fdde9b7e89de4df4a2159c9e8697f` | MIT — Copyright (c) 2026 Howseen AI (Raphaël Aubry) | Règles « anti-motion IA », test muet, raccords de coupe, zoom en logarithme, pulsation sur le temps | `references/principes.md`, `references/camera.md` |
| huashu-art-motion | `alchaincyf/huashu-art-motion` | `1468196505a51728686db118d52561aa27a25124` | MIT — Copyright (c) 2026 alchaincyf (花叔 · 花生) | Référence « langage de la caméra » (table des gestes, durées, dosage, piège des images plein cadre), seuil bleu-violet | `references/camera.md`, `references/principes.md` |
| product-launch-motion | `AbubakrChan/product-launch-motion` | `edbfb105382f21507bad895d8b5f6e0faa67487c` | MIT — Copyright (c) 2026 Abubakr Chan | Référence caméra (deux nœuds, point fixe, rotation 3D légère, profondeur, bascule de point, parallaxe, budget de cadre). Films et images d'exemple **non repris** | `references/camera.md` |

## Obligations à respecter

1. **Motion Prompt** : chaque fichier de `references/motion-prompt/e/` et `kit/` commence par la ligne `// Motion Prompt #ID · MIT License (c) 2026 Shohei Ohtaki · …`. Cette ligne ne doit pas être retirée, et elle doit être recopiée dans tout fichier où le code ou les valeurs d'un élément sont repris. La licence d'origine et la notice de tiers de l'auteur sont conservées dans `references/motion-prompt/LICENSE` et `THIRD-PARTY-NOTICES.md`.
2. Les exemples trouvés sur les réseaux (`found.html`), les vidéos et images d'aperçu du dépôt Motion Prompt ne sont pas embarqués.
3. **GSAP** (la bibliothèque, distincte des skills) est distribuée sous sa propre licence gratuite (« Standard No-Charge License », https://gsap.com/community/standard-license/ ; ce n'est pas une licence libre, voir la section « À décider » de la NOTICE) ; elle n'est pas redistribuée par ce skill.
4. Les contraintes de rendu image par image citées dans `references/gsap.md` décrivent le moteur HyperFrames (HeyGen, Apache 2.0) ; aucun fichier de HyperFrames n'est copié dans ce skill.
5. Aucun contenu du dépôt `remotion-dev/skills` n'est repris (le clone, commit `1fc074b`, ne contient aucun fichier de licence).

## Mise à jour

La copie de Motion Prompt est figée au commit indiqué. Pour la mettre à jour : comparer `count` et `version` du `catalog.json` d'origine, remplacer `references/motion-prompt/`, puis reporter les lignes ajoutées ou modifiées de `catalog.tsv` dans `dictionnaire-mouvements.md` (les numéros existants ne changent pas de sens).

## Texte de la licence MIT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
