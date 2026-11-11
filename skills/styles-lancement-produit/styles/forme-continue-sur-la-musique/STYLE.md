# Forme continue sur la musique (lancement sans coupe)

## 1. Identité
- **Nom** : Forme continue sur la musique. Identifiant : `forme-continue-sur-la-musique`.
- **Inspiration** : les films de lancement des éditeurs de logiciels les plus soignés et le motion d'interface de niveau « portfolio de designer » : moderne, net, quelque chose à chaque temps. Inspiration seulement, jamais une copie ni un modèle tout fait.
- **Principe** : **une seule forme, jamais coupée.** Chaque état est le même élément qui change de taille, de rayon et de couleur pendant que son contenu se remplace par un court flou. Les transitions sont des transformations, des mouvements de caméra, ou un zoom dans un élément qui devient la scène suivante (une tuile s'ouvre en boîte de réception, une carte de réponse devient la commande). **Un curseur pilote chaque changement** par de vrais clics et de vrais glissés. Tout est calé sur la musique, choisie avant la chorégraphie.
- **Posture** : l'agent est le réalisateur. Il prend les décisions créatives, les note (« DÉCISION : … ») et les liste à la fin pour que le client puisse en renverser une en une réponse.
- **Pour quels sujets** : lancement d'une application ou d'un logiciel, annonce d'une fonction, boucle d'interface pour les réseaux (8 à 15 s qui bouclent), film de marque de 30 s.
- **Ne marche pas pour** : un produit physique, un service sans interface, un message qui demande une voix (voir `lancement-narre-mot-a-mot`).

## 2. Palette, typographie, matières
- **Palette** : le système de couleurs de la marque du client (fiche « ma chaîne »), pas « du noir et un violet ». Structure type : fond clair chaud presque blanc, dégradé de marque pour les éléments héros, nappes de lumière douces, encre presque noire. Dérivation complète : `references/etalonnage.md` §10.
- **Variante sobre** : fond gris chaud clair, composants noirs et blancs, un seul accent.
- **Police** : une seule police d'interface nette (celle de la marque, sinon Geist, Inter ou DM Sans, toutes libres). Chiffres à largeur de case fixe pour les compteurs.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Geist et de DM Sans ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/geist`, `@fontsource/dm-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** : interfaces inventées pour le film (ne pas recopier en bloc le site du client), coins généreux, ombres courtes. Un seul jeu d'icônes, une seule épaisseur de trait.
- **Interdits de matière** : lueurs, dégradés sur les éléments d'interface, explosions de particules, tout « look de modèle ».

## 3. Composition 9:16
- **La caméra zoome pour que chaque état remplisse le cadre** : l'état occupe 70 à 85 % de la largeur (760 à 920 px), centré vers y 820. **Une image vide est un défaut.**
- Empiler verticalement : la pastille devient une carte haute, la liste descend, le graphique se dresse. Les reculs révèlent l'échelle en hauteur (un message → une colonne de dizaines).
- Texte : mot ou nombre héros ≥ 120 px ; libellés ≥ 34 px ; 5 mots au plus par état.
- Le curseur reste dans le cadre à tout zoom ; taille 60×74 px.
- Mot-symbole de fin : centré, entre y 700 et y 1000, tenu ≥ 1,5 s.
- Zones d'interface : rien d'important au-dessus de y 160, sous y 1560, à droite de x 945.
- **16:9 ou carré** : mêmes règles, états plus larges ; le carré (1440×1440) convient aux boucles.

## 4. Ce qui bouge
- **Action principale** : la transformation de la forme, sur ressort, déclenchée par le curseur. **Ressorts partout, un minuscule dépassement au plus** (amortissement 0,72 à 0,9 ; 1,0 pour la caméra et le texte).
- **Boucles de fond** : (1) le curseur vivant (inclinaison selon sa vitesse, courte traînée, étiquette de nom qui suit avec retard) ; (2) un mouvement secondaire qui garde le temps vivant pendant qu'une idée est tenue (barre qui avance, point qui pulse en rythme).
- **Échange de contenu** : sortie courte et précoce (0,12 s, flou 10 px), entrée sur ressort. Sans cela, ancien et nouveau texte se chevauchent.
- **Bords avant et arrière sur deux ressorts** : l'indicateur d'onglet et le bouton d'interrupteur s'étirent (le bord avant est raide, le bord arrière souple).
- **Manipulation directe** : pendant qu'un glissé est tenu, la valeur vient de la position du curseur ; au relâchement, elle repart en ressort de là où elle était.
- **Compteur à rouleaux pour les vrais nombres** : une bande 0-9 par chiffre, chaque case à la largeur de son chiffre final, rognage vertical seulement.
- **Logos de clients un par un, « boum, boum, boum »**, sur le temps, la même forme redimensionnée et recolorée à chaque coup ; jamais une rangée « ils nous font confiance ».
- **Deux curseurs** possibles : celui de l'utilisateur (« Toi ») tape et clique dans l'introduction, puis passe la main au curseur du produit, à ses couleurs.
- **Autorisés** : #012 morphing, #161 élément partagé, #083 curseur, #085 onde de clic, #028 zoom, #020 traversée de zoom, #057 onglets, #059 interrupteur, #062 réglage, #056 notification, #007 compteur, #043 filé (rare), #127 boucle.
- **Interdits** : coupes franches entre états, #123 rebonds, #015 particules, #022 reflets et lueurs gratuits, temps mort, #006 machine à écrire sur un titre (la frappe n'existe que dans un champ de saisie).

## 5. Rythme et montage
- **La musique d'abord** : ~120 BPM, une montée, un « drop » net, une fin. Grille de temps mesurée ; départ sur un temps fort ; fenêtre du morceau choisie pour que **le drop tombe sur le grand moment du produit**.
- **Quelque chose à chaque temps** (0,5 s à 120 BPM). La frappe suit des subdivisions rapides pendant la montée ; les coups de logos accélèrent : temps → croches → doubles croches.
- **Facile à suivre** : une idée claire par scène, des demandes et des réponses courtes, et assez de temps posé pour lire le résultat. Si ça va trop vite : simplifier le contenu ou ajouter des temps, pas presser le spectateur.
- Structure type en 7 mesures pour une boucle : bouton → chargement → coche → îlot d'état → aperçu → réglage → interrupteur → onglets → graphique → recherche → notification → retour au bouton.
- **Boucle** : la dernière image est la première, **position et vitesse du curseur comprises**, sinon la boucle accroche.
- Une cible qui doit **arriver** à l'instant T est lancée ~0,3 s avant (le ressort part à son évènement).
- **Version courte (8 à 12 s)** : prendre la fenêtre du morceau autour du « drop » : 4 s de montée, le drop, 4 s de suite ; trois transformations de forme ; couper l'introduction.

## 6. Recette technique
- **Moteur** : HyperFrames. Deux écritures possibles : (a) timeline GSAP avec amortis à très faible dépassement ; (b) pour la fidélité au style, **ressorts en forme fermée** calculés depuis `hf-seek` : chaque style est une fonction pure du temps.
```js
function reponse(tau, {w, z}) {                 // réponse à un échelon d'un ressort amorti, 0 → 1
  if (tau <= 0) return 0;
  if (z >= 1) { const x = w * tau; return 1 - Math.exp(-x) * (1 + x); }
  const wd = w * Math.sqrt(1 - z * z);
  return 1 - Math.exp(-z * w * tau) * (Math.cos(wd * tau) + (z * w / wd) * Math.sin(wd * tau));
}
class Piste {                                   // plusieurs cibles = somme d'un ressort par changement
  constructor(v0) { this.v0 = v0; this.cur = v0; this.ev = []; }
  vers(t, v, r) { if (v !== this.cur) { this.ev.push([t, v - this.cur, r]); this.cur = v; } return this; }
  a(t) { let v = this.v0; for (const [ti, d, r] of this.ev) v += d * reponse(t - ti, r); return v; }
}
const largeur = new Piste(420).vers(1.0, 780, {w: 22, z: 0.82});      // la forme s'élargit au temps 1,0
window.addEventListener("hf-seek", e => { forme.style.width = largeur.a(e.detail.time) + "px"; });
```
- **Étirement par les bords** : bord arrière `{w: 19, z: 0.9}`, bord avant `{w: 34, z: 0.9}` ; largeur = droite − gauche.
- **Calques** : fond (nappes de marque), monde (transformé par la caméra : position et **zoom en logarithme** sur ressorts), surimpressions en espace écran (curseurs, mot-symbole).
- **Caméra et curseur** : `references/camera-et-curseur.md`. **Étalonnage** : `references/etalonnage.md`. **Son** : `references/son-et-mastering.md` §7.
- **Contrôle** : une image par temps en planche ; les transitions à ±0,1 s ; un brouillon basse définition regardé à vitesse réelle (des images fixes ne prouvent pas que le rythme marche) ; après le rendu, une planche à 1 image par seconde et une recherche de sauts d'image.
- **Flou de mouvement** : celui du moteur, activé par **`data-motion-blur="on"`** sur la racine (l'attribut nu, sans valeur, n'active rien : vérifié sur HyperFrames 0.9.33 le 11/11/2026). Réservé aux mouvements rapides. **Ne sont pas floutés** : un élément placé dans un contexte 3D (`preserve-3d`, parent incliné avec `perspective`) et un `<svg>` animé directement (le mettre dans un `<div>` et animer le `<div>`). Vérifier sur une image extraite en plein mouvement. Détails : skill `rendu`, section « Flou de mouvement ».
- **Pièges** : jamais `will-change` sur ce que la caméra agrandit ; une fonction qui cache un élément (opacité 0) doit être défaite par la fonction de dessin ; chiffres proportionnels qui sautent dans un compteur ; pour une boucle, additionner aussi les ressorts de la période précédente.

## 7. Son
- Musique sous licence claire ou composition originale avec un vrai arc ; pas une boucle répétitive.
- Chaque son d'interface est placé **par son pic mesuré** sur la grille des temps. Sons courts et variés : clic (appui et relâche), tic, touche, note, petit carillon rare, coup sourd, souffle. Les sons de glissé suivent la vitesse de l'élément.
- La source synthétise tout ; ici : vrais enregistrements d'abord (skill `son`), synthèse en repli, et budget d'environ 5 bruitages par 10 s **hors musique** : choisir les contacts qui comptent.
- −14 LUFS ; pour une boucle, pas de limiteur qui pompe à la jointure.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Aucune coupe franche : chaque passage est une transformation, un mouvement de caméra ou un zoom dans un élément.
- [ ] Chaque changement est causé par le curseur, visible et dans le cadre.
- [ ] Une image par temps : aucune image vide, serrée, illisible ou hors grille.
- [ ] Le grand moment du produit tombe sur le drop (écart ≤ 2 images).
- [ ] Les grands nombres sont réels et sourcés ; la micro-histoire inventée (noms, messages) est annoncée comme telle dans le compte rendu.
- [ ] Logos : uniquement de vrais clients, depuis leurs fichiers, un par un.
- [ ] Boucle : image de fin = image de début, curseur compris.
- [ ] Texte net pendant les zooms ; zones d'interface respectées ; −14 LUFS mesuré.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu
- Les films d'exemple du dépôt d'origine appartiennent à un client de l'auteur et montrent des marques tierces : **aucune réutilisation, pas même en lien de vitrine**. Aperçu Flot Web à produire.

## 10. Origine
- Dépôt : AbubakrChan/product-launch-motion, commit `edbfb10` (version 2). Fichiers : `SKILL.md`, `references/prompts.md`, `references/technique.md`.
- Licence : MIT. La notice du dépôt exclut explicitement les films d'exemple et leurs images.
- Adaptations Flot Web : français, HyperFrames (la source rend avec son propre outil), 9:16, vrais enregistrements d'abord, consignes propres à la machine de l'auteur retirées.
