# Lancement en 7 temps (une phrase, des preuves, du verre)

## 1. Identité
- **Nom** : Lancement en 7 temps. Identifiant : `lancement-7-temps`.
- **Inspiration** : la vidéo de lancement d'un créateur ou d'une petite marque : propre, « premium », qui vend une seule chose en 30 à 45 secondes. Surfaces en verre dépoli avec une profondeur douce, à la manière des interfaces récentes.
- **Principe** : **une seule phrase, découpée en 3 à 5 fragments**, répartis sur les temps du film ; chaque fragment se pose d'un mouvement court et assuré, par-dessus de **vraies preuves** (captures, résultats, messages de clients). Le produit est montré en train de travailler : une demande tapée en direct dans un champ réaliste, le résultat qui apparaît.
- **Pour quels sujets** : lancement d'une formation, d'un e-book, d'une offre, d'une communauté, d'un outil ; ouverture des ventes ; annonce d'une date.
- **Ne marche pas pour** : un lancement sans aucune preuve réelle à montrer (attendre d'en avoir), un produit qui demande une longue explication (voir `demo-produit-epuree`).
- **C'est le style conseillé au débutant** dans cette catégorie : structure fixe, peu de pièges.

## 2. Palette, typographie, matières
- **Les vraies couleurs de la marque**, lues dans la fiche « ma chaîne » ; à défaut, échantillonnées sur la page de vente ou le meilleur visuel du client. **Jamais une palette par défaut** : trois premiers jets de l'auteur de la source ont été refusés pour « pas mes couleurs ».
- Structure : un fond, une couleur de texte, **un accent**.
- **Police** : celle de la marque, ou une sans du système. Beaucoup d'espace.
- **Police de repli** : Inter. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : la police de la marque : fichier fourni par le client, copié dans `assets/fonts/` ; à vérifier (licence et accents). Ne pas compter sur une police « du système » : elle change d'une machine à l'autre.
- **Verre** : les surfaces du produit sont des panneaux de verre dépoli à profondeur douce. Dans HyperFrames, le faire par bande givrée + filet (voir `references/etalonnage.md` §3), pas par `backdrop-filter`.
- **Écrans du produit** : ils flottent sur des ombres douces avec une poussée lente.
- **Preuves** : du travail **réel et récent**, pas de vieux exemples.
- **Interdits de matière** : lueurs, dégradés sur le texte, personnes de banque d'images, faux témoignages.

## 3. Composition 9:16
- **Temps 1 (l'accroche)** : les premiers mots de la phrase, très grands (130 à 170 px), sur fond net, entre y 620 et y 1050.
- **Fragments suivants** : en haut de la zone utile (y 220 à y 520), la preuve ou l'écran dessous (y 560 à y 1400).
- **Écran du produit** : largeur 900 à 940 px ; le champ de saisie fait au moins 110 px de haut pour que la frappe se lise.
- **Cartes de preuve** : une ou deux par écran en vertical (pas une grille de six) ; les logos remplissent leur carte.
- **Le nombre qui compte** : 220 à 300 px, sa source en 28 px juste dessous (jamais moins : 28 px est le plancher de lecture du studio).
- **Carte de fin** : nom, appel à l'action mot pour mot, condition éventuelle ; entre y 600 et y 1200 ; **tenue au moins 3 s**.
- **Variété** : aucun temps ne partage la même mise en page qu'un autre.
- Tout est lisible sur un téléphone, **sans le son**. Zones d'interface : haut 160, bas 360, droite 135.
- **Autres formats** : 16:9 (1920×1080) et 4:5 (1080×1350) recomposés, pas recadrés.

## 4. Ce qui bouge
- **Action principale** : le fragment de phrase qui se pose (montée de 24 à 40 px avec révélation par masque, 0,35 à 0,5 s, amorti franc sans rebond).
- **Boucles de fond** : (1) poussée lente dans chaque écran du produit ; (2) un petit élément vivant pendant la tenue (curseur de texte qui clignote, barre qui progresse).
- **La demande tapée en direct** dans le champ du produit : c'est **le seul endroit où la frappe a sa place**. Puis le résultat apparaît.
- **Le temps « qualité »** : quelque chose se vérifie, passe, se coche.
- **Le nombre** : il compte jusqu'à sa valeur, avec sa source.
- **Autorisés** : #005 révélation par masque, #028 poussée lente, #006 frappe (dans le champ seulement), #007 compteur, #002 décalage en cascade des preuves, #083 curseur, #161 élément partagé entre deux temps, #046 coupe sèche.
- **Interdits** : #006 machine à écrire sur les titres, #123 rebonds, lueurs, dégradés sur le texte, tout nombre que le client n'a pas donné.

## 5. Rythme et montage
Sept temps par défaut, 45 secondes :

| # | Temps | Contenu |
|---|---|---|
| 1 | 0 à 4 s | Premiers mots de la phrase, en grand, sur fond net. L'accroche. |
| 2 | 4 à 9 s | Mots suivants par-dessus de vraies preuves (messages, résultats, écrans). |
| 3 | 9 à 17 s | Le produit au travail : un écran, un curseur qui tape une vraie demande, le résultat qui apparaît. |
| 4 | 17 à 22 s | Le temps « qualité » : quelque chose se vérifie, passe ou se coche. |
| 5 | 22 à 32 s | Comment ça marche : étapes, semaines ou fonctions en un seul visuel simple. |
| 6 | 32 à 38 s | Le nombre qui compte, compté, avec sa source. |
| 7 | 38 à 45 s | Nom, appel à l'action, condition. Tenu assez longtemps pour être lu. |

- **Version réseaux 20 à 25 s** : temps 1, 3, 6, 7 (accroche, produit, nombre, appel).
- **Construire d'abord les 10 premières secondes en deux ou trois styles**, en choisir un, puis seulement construire le reste.
- Montrer la feuille des temps au client et attendre son accord avant de construire.
- Un inconnu doit savoir ce qui est lancé **à la seconde 4**.
- **Version courte (8 à 12 s)** : trois temps sur sept : l'accroche (premiers mots en grand, 3 s), le produit au travail (5 s), l'appel à l'action (2 à 3 s) ; couper les preuves, le nombre et le contraste.

## 6. Recette technique
- **Moteur** : HyperFrames + GSAP. Un clip par temps (sept sections), une timeline en pause, polices embarquées.
```js
// un fragment de phrase : révélé par masque, sans rebond
const fragment = (el, t) => tl.fromTo(el, {yPercent: 105}, {yPercent: 0, duration: 0.45, ease: "power3.out"}, t);
// la demande tapée dans le champ (le seul endroit où l'on tape)
const demande = "Écris mon prochain post dans ma voix";
tl.to({n: 0}, {n: demande.length, duration: demande.length / 25, ease: "none",
  onUpdate() { champ.textContent = demande.slice(0, Math.round(this.targets()[0].n)); }}, 9.6);
```
- **Contrôle obligatoire après la construction** : capturer une image au milieu de chaque temps et vérifier : texte coupé, éléments qui se chevauchent, illisible à la taille d'un téléphone, et **tout mot ou nombre absent du brief**. Corriger ce qui est réel ; garder la première version.
- **Script et vérité** : `references/script-de-lancement.md`. **Étalonnage léger** (grain 0,1, vignette, un balayage sur l'accroche et un sur l'appel) : `references/etalonnage.md`. **Caméra et curseur** : `references/camera-et-curseur.md`.
- **Pièges** : charger les polices avant la première image (sinon image 0 en police de secours) ; une preuve illisible ne prouve rien (recadrer sur la phrase qui compte) ; un écran refait à la main doit ressembler au vrai produit du client.

## 7. Son
- Musique discrète, confiante, qui laisse la place aux temps forts ; un accent sur l'accroche, une levée sur le nombre, une résolution sur l'appel à l'action.
- Bruitages (budget du skill `son`, vrais enregistrements d'abord) : frappe douce pendant la demande, petit son de coche au temps 4, coup sourd doux quand le nombre se pose.
- Le film doit se comprendre sans le son. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
Le vérifier comme un acheteur :
- [ ] Un inconnu sait ce qui est lancé à la seconde 4.
- [ ] Chaque nombre a une source qu'on peut retrouver ; aucun prix, date, « places restantes », témoignage ou résultat inventé.
- [ ] L'appel à l'action est mot pour mot celui de la page de vente et tient au moins 3 s.
- [ ] Lisible sur un téléphone, sans le son.
- [ ] Les couleurs sont celles de la marque (comparées à la fiche « ma chaîne »).
- [ ] Aucun titre en machine à écrire ; la frappe n'existe que dans le champ du produit.
- [ ] Sept mises en page différentes ; une image du milieu de chaque temps a été contrôlée.
- [ ] Zones d'interface respectées ; −14 LUFS mesuré.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 3
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Le GIF de démonstration du dépôt d'origine porte la marque personnelle de son auteur : on ne le reprend pas. Aperçu Flot Web à produire.

## 10. Origine
- Dépôt : charlie947/motion-graphics-skills, commit `229022e`. Fichier : `skills/launch-video/SKILL.md`.
- Licence : MIT (© 2026 Charlie Hills). Images et GIF du dépôt : marque de l'auteur, non repris.
- Adaptations Flot Web : français, composition 9:16 et version courte, verre sans `backdrop-filter`, lecture de la fiche « ma chaîne » à la place de l'entretien de marque de la source.
