#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""relever_textes.py : relève les textes d'un film HyperFrames et écrit `textes.json`, pour `controle_textes.py`
et la porte de livraison.

Usage :
    python3 relever_textes.py <dossier-du-projet> [-o textes.json] [--fiche chemin/STYLE.md]
                              [--duree 12] [--pas 0.0667] [--vivant] [--vitesse 60] [--tolerance-vivant 24]
                              [--opacite 0.95] [--auto] [--mode apercu|direct] [--url <adresse>] [--chrome <chemin>]
                              [--journal releve-brut.json]

Ce qu'il fait : il ouvre le projet dans un navigateur sans fenêtre (Playwright), place le film à chaque instant
(15 fois par seconde par défaut) avec le moteur de HyperFrames, et note pour chaque texte s'il est ENTIER et
LISIBLE, et où sont ses lettres. Il n'y a rien à charger dans la page ni de fonction `aller(t)` à écrire.

Préparation dans le film : marquer chaque texte à contrôler avec l'attribut `data-texte` :
    <h1 data-texte="accroche">3 € par jour</h1>
    <p data-texte="st-01" data-sous-titre>et personne ne le voit</p>       (sous-titre calé sur la voix)
    <span data-texte="enseigne" data-passage>BOULANGERIE</span>            (décor, pas à lire)
    <div data-texte="paf" data-texte-vivant>PAF !</div>                    (texte qui tremble ou flotte par style)
Sans aucun `data-texte` dans la page (ou avec --auto), l'outil relève tout bloc de texte qu'il trouve et le
nomme `auto-1`, `auto-2`… : pratique pour un premier passage, mais à relire (un décor sera pris pour un texte).

Ce qui est mesuré, à chaque instant, pour chaque texte :
  - ses LETTRES, pas la boîte de l'élément : la boîte relevée est celle des glyphes (marges et fond exclus) ;
  - chaque morceau à part : un texte découpé par `SplitText` (lignes, mots, lettres) n'est « entier » que
    lorsque tous ses morceaux sont arrivés (opacité, position) ;
  - les masques : un morceau coupé par un parent `overflow: hidden / clip` ou par un `clip-path: inset(...)`
    n'est pas visible ; les autres formes de `clip-path` et les `mask-image` ne sont pas calculés (le texte est
    alors signalé `"masque_non_calcule": true` : vérifier ses temps à l'œil) ;
  - l'opacité : produit des opacités de l'élément et de ses parents, ≥ 0,95 (texte vivant : ≥ 0,6).
Exception : un sous-titre (`data-sous-titre`) compte dès que son premier mot est visible et jusqu'à ce que le
dernier disparaisse (ses mots arrivent avec la voix : c'est voulu) ; sa boîte est celle de ses mots visibles.
Un texte est « posé » quand il est entier et que sa boîte ne va pas plus vite que --vitesse (60 px/s par
défaut : une caméra qui dérive lentement ne l'empêche pas d'être lu ; une entrée animée, si).
TEXTE VIVANT (attribut `data-texte-vivant`, option --vivant, ou fiche « Texte vivant : oui ») : le texte peut
trembler ou flotter : il reste « posé » tant qu'il ne s'écarte pas de plus de --tolerance-vivant (24 px) de
la place où il s'est posé, et son opacité peut descendre à 0,6 (scintillement).

Toutes les présences d'un texte sont gardées (il part et revient, la caméra le déplace) : chacune fait une
entrée de `textes.json` avec le même `id`. Les trous de 0,15 s ou moins sont recousus. `controle_textes.py`
juge la zone sûre sur chaque présence et le temps de lecture sur la plus longue. La boîte d'une présence
contient toutes les positions du texte pendant cette présence (dérive, tremblement).

Film dessiné dans un CANVAS : le navigateur ne sait pas lire un texte peint. Deux voies :
  1. le film le déclare : `window.__textes = (t) => [{id, texte, x0, y0, x1, y1, taille_px, opacite}]` (boîtes
     en pixels de l'image, à l'instant t ; champs facultatifs : sous_titre, passage, vivant). L'outil appelle
     cette fonction à chaque pas et suit ces textes comme les autres ;
  2. à la main : copier `gabarits/textes-canvas.json`, le remplir (mode d'emploi dans references/controles.md).
Si la page a un canvas et ne déclare rien, `textes.json` porte `"canvas_sans_texte_declare": true` et la porte
le signale en jaune.

Comment le temps avance :
  - mode `apercu` (défaut) : l'outil lance l'aperçu de HyperFrames (`npx -y hyperframes@0.9.33 preview
    --background --no-open`), ouvre la page `/api/projects/<dossier>/preview`, passe le lecteur en mode rendu
    (`__player.enableRenderMode()`), puis pour chaque instant appelle `__player.renderSeek(t)` et attend
    `__hfWaitForSeekCompletion()` et deux images. C'est le moteur du rendu : sous-compositions, `.clip`,
    canvas pilotés par `hf-seek` sont à leur vraie place. Pour que le relevé soit le même d'une fois sur
    l'autre : toutes les polices déclarées sont chargées d'abord (une police qui arrive en cours de route
    change les boîtes), un premier passage visite tout le film sans mesurer, puis chaque instant est remesuré
    jusqu'à donner deux mesures de suite identiques. L'aperçu est arrêté à la fin. --url : utiliser un aperçu déjà lancé.
  - mode `direct` (repli, sans serveur) : ouvre `index.html` en fichier, avance chaque timeline de
    `window.__timelines` par `seek(t, false)`, cache les `.clip` hors de leur plage et envoie l'évènement
    `hf-seek`. Ne charge pas les sous-compositions (`data-composition-src`) : à réserver aux films d'un seul
    fichier.

Besoin : Python 3, `pip install playwright`, et un Chrome : celui de Playwright (`playwright install chromium`)
ou, à défaut, celui que HyperFrames a déjà téléchargé (trouvé tout seul dans ~/.cache/hyperframes/chrome).

Codes de sortie : 0 relevé écrit, 1 aucun texte trouvé (le fichier est écrit quand même), 2 projet illisible,
navigateur ou aperçu impossible à lancer.

Inspiration : contrat `window.TEXTS(t)` de readcheck.mjs, lemo-opuscar (LemoLab, MIT, commit 9eb7739), pour
l'idée du relevé et la déclaration des textes d'un canvas. Écrit pour ce plugin à partir de quatre essais
faits pendant les rendus de test (aperçu + renderSeek, seek des timelines + `.clip`, évènement `hf-seek`).
"""
import argparse
import glob
import json
import os
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fiche_reglages  # noqa: E402

HYPERFRAMES = "hyperframes@0.9.33"

# --- Ce qui tourne dans la page : mesure des textes à l'instant courant ----------------------------------
JS_MESURE = r"""
(() => {
  const W = () => document.documentElement.clientWidth, H = () => document.documentElement.clientHeight;
  const insetDe = (cp, r) => {                      // clip-path: inset(haut droite bas gauche) → rectangle
    const m = /^inset\(([^)]*)\)/.exec(cp);
    if (!m) return null;
    const v = m[1].split(/\s+round\s+/)[0].trim().split(/\s+/).map((x, i, a) => x);
    const px = (x, ref) => x.endsWith('%') ? parseFloat(x) / 100 * ref : parseFloat(x) || 0;
    const t = v[0], d = v[1] ?? t, b = v[2] ?? t, g = v[3] ?? d;
    return { x0: r.left + px(g, r.width), y0: r.top + px(t, r.height), x1: r.right - px(d, r.width), y1: r.bottom - px(b, r.height) };
  };
  const unites = (auto) => {
    const marques = [...document.querySelectorAll('[data-texte]')];
    if (marques.length && !auto) return marques.map(el => ({ el, id: el.dataset.texte, auto: false }));
    const vus = new Map();
    const marche = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n = marche.nextNode(); n; n = marche.nextNode()) {
      if (!n.nodeValue.trim()) continue;
      let el = n.parentElement;
      if (!el || el.closest('script,style,noscript,template,title,[data-releve-ignore]')) continue;
      const marque = el.closest('[data-texte]');
      if (marque) { vus.set(marque, marque.dataset.texte); continue; }
      // remonter des morceaux (SplitText, span) jusqu'au bloc de texte
      for (;;) {
        const p = el.parentElement;
        if (!p || p === document.body) break;
        const s = getComputedStyle(el);
        const morceau = s.display.startsWith('inline') || el.getAttribute('aria-hidden') === 'true' || p.hasAttribute('aria-label')
          || (el instanceof SVGElement && el.tagName.toLowerCase() === 'tspan');
        if (!morceau) break;
        el = p;
      }
      if (!vus.has(el)) vus.set(el, null);
    }
    let k = 0;
    return [...vus.entries()].map(([el, id]) => ({ el, id: id ?? ('auto-' + (++k)), auto: id == null }));
  };
  const mesurerUnite = ({ el, id, auto }, seuilOpacite) => {
    const noeuds = [];
    const marche = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n = marche.nextNode(); n; n = marche.nextNode()) if (n.nodeValue.trim() && !n.parentElement.closest('[data-releve-ignore]')) noeuds.push(n);
    // texte : les morceaux dans l'ordre ; une espace entre deux blocs (lignes), rien entre deux lettres découpées
    let texte = el.getAttribute('aria-label') || '';
    if (!texte) {
      let avant = null;
      for (const n of noeuds) {
        const p = n.parentElement;
        if (avant && avant !== p && !/\s$/.test(texte) && !/^\s/.test(n.nodeValue)) {
          const bloc = (e) => { for (; e && e !== el; e = e.parentElement) if (!getComputedStyle(e).display.startsWith('inline')) return e; return el; };
          const entre = document.createRange(); entre.setStartAfter(avant.lastChild || avant); entre.setEndBefore(n);
          if (bloc(avant) !== bloc(p) || /\s/.test(entre.toString())) texte += ' ';
        }
        texte += n.nodeValue;
        avant = p;
      }
    }
    texte = texte.trim().replace(/\s+/g, ' ');
    if (!noeuds.length || !texte) return null;
    let vb = [1e9, 1e9, -1e9, -1e9], poids = 0, vu = 0, opMin = 1, opMax = 0, x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9, masque = false, taille = 0, plusLong = 0;
    const cache = new Map();                        // élément → { opacité cumulée, zone de coupe, caché }
    const etat = (e) => {
      if (!e || e.nodeType !== 1) return { op: 1, clip: { x0: 0, y0: 0, x1: W(), y1: H() }, cache: false };
      if (cache.has(e)) return cache.get(e);
      const parent = etat(e.parentElement), s = getComputedStyle(e);
      let clip = parent.clip, cacheE = parent.cache || s.display === 'none' || s.visibility === 'hidden' || s.visibility === 'collapse';
      const coupe = (r) => { clip = { x0: Math.max(clip.x0, r.x0), y0: Math.max(clip.y0, r.y0), x1: Math.min(clip.x1, r.x1), y1: Math.min(clip.y1, r.y1) }; };
      if (!(e instanceof SVGElement) || e.tagName.toLowerCase() === 'svg') {
        const ox = s.overflowX, oy = s.overflowY;
        if ((ox && ox !== 'visible') || (oy && oy !== 'visible')) {
          const r = e.getBoundingClientRect();
          coupe({ x0: ox !== 'visible' ? r.left : -1e9, y0: oy !== 'visible' ? r.top : -1e9, x1: ox !== 'visible' ? r.right : 1e9, y1: oy !== 'visible' ? r.bottom : 1e9 });
        }
      }
      if (s.clipPath && s.clipPath !== 'none') {
        const r = insetDe(s.clipPath, e.getBoundingClientRect());
        if (r) coupe(r); else masque = true;
      }
      const mi = s.maskImage || s.webkitMaskImage;
      if (mi && mi !== 'none') masque = true;
      const res = { op: parent.op * parseFloat(s.opacity || '1'), clip, cache: cacheE };
      cache.set(e, res);
      return res;
    };
    for (const n of noeuds) {
      const p = n.parentElement, e = etat(p), w = n.nodeValue.trim().length;
      poids += w;
      const plage = document.createRange();
      plage.selectNodeContents(n);
      let rects = [...plage.getClientRects()].filter(r => r.width > 0.5 && r.height > 0.5);
      if (!rects.length) { const r = p.getBoundingClientRect(); if (r.width > 0.5 && r.height > 0.5) rects = [r]; }
      if (!rects.length || e.cache) { opMin = Math.min(opMin, 0); continue; }
      let aire = 0, aireVue = 0;
      for (const r of rects) {
        x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom);
        aire += r.width * r.height;
        aireVue += Math.max(0, Math.min(r.right, e.clip.x1) - Math.max(r.left, e.clip.x0)) * Math.max(0, Math.min(r.bottom, e.clip.y1) - Math.max(r.top, e.clip.y0));
      }
      opMin = Math.min(opMin, e.op); opMax = Math.max(opMax, e.op);
      if (e.op >= seuilOpacite) {
        vu += w * (aire ? aireVue / aire : 0);
        if (aireVue > 0.5 * aire) for (const r of rects) vb = [Math.min(vb[0], r.left), Math.min(vb[1], r.top), Math.max(vb[2], r.right), Math.max(vb[3], r.bottom)];
      }
      if (w > plusLong) {                           // taille réelle = taille de police × échelle de l'élément
        plusLong = w;
        const s = getComputedStyle(p), f = parseFloat(s.fontSize) || 0;
        let ech = 1;
        if (p instanceof SVGElement && p.getScreenCTM) { const m = p.getScreenCTM(); if (m) ech = Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)); }
        else if (p.offsetWidth > 0 && p.offsetHeight > 0) { const r = p.getBoundingClientRect(); ech = Math.sqrt((r.width * r.height) / (p.offsetWidth * p.offsetHeight)); }
        taille = f * ech;
      }
    }
    if (x1 < x0) return { id, texte, part: 0, opacite: 0, auto };
    const d = el.dataset || {};
    return { id, texte, part: poids ? vu / poids : 0, opacite: opMin, opaciteMax: opMax, x0, y0, x1, y1, taille, masque, auto,
             visible: vb[2] > vb[0] ? vb : null,
             sous_titre: 'sousTitre' in d, passage: 'passage' in d, vivant: 'texteVivant' in d };
  };
  window.__releveTextes = (auto, seuilOpacite, seuilVivant, t) => {
    const sorties = [];
    for (const u of unites(auto)) {
      const vivant = u.el.dataset && 'texteVivant' in u.el.dataset;
      const m = mesurerUnite(u, vivant ? seuilVivant : seuilOpacite);
      if (m) sorties.push(m);
    }
    if (typeof window.__textes === 'function') {    // textes déclarés par un film en canvas
      try {
        for (const c of window.__textes(t) || []) {
          sorties.push({ id: String(c.id), texte: String(c.texte ?? ''), part: 1, opacite: c.opacite ?? 1, x0: c.x0, y0: c.y0, x1: c.x1, y1: c.y1,
                         taille: c.taille_px ?? 0, masque: false, auto: false, declare: true,
                         sous_titre: !!c.sous_titre, passage: !!c.passage, vivant: !!c.vivant });
        }
      } catch (e) { window.__releveErreur = String(e); }
    }
    return sorties;
  };
  window.__releveInfos = () => ({
    largeur: W(), hauteur: H(),
    marques: document.querySelectorAll('[data-texte]').length,
    canvas: [...document.querySelectorAll('canvas')].filter(c => { const r = c.getBoundingClientRect(); return r.width * r.height >= 0.05 * W() * H(); }).length,
    declare: typeof window.__textes === 'function',
  });
})();
"""

JS_ALLER_APERCU = """async (t) => {
  window.__player.renderSeek(t);
  if (window.__hfWaitForSeekCompletion) await window.__hfWaitForSeekCompletion();
  await new Promise(ok => requestAnimationFrame(() => requestAnimationFrame(ok)));
}"""

JS_ALLER_DIRECT = """async (t) => {
  for (const tl of Object.values(window.__timelines || {})) { try { tl.pause(); tl.seek(t, false); } catch (e) {} }
  for (const el of document.querySelectorAll('[data-start]')) {       // contrat HyperFrames : un clip n'existe que sur sa plage
    if (el.hasAttribute('data-composition-id')) continue;
    const s = parseFloat(el.dataset.start), d = parseFloat(el.dataset.duration || '1e9');
    el.style.visibility = (t >= s && t < s + d) ? 'visible' : 'hidden';
  }
  window.dispatchEvent(new CustomEvent('hf-seek', { detail: { time: t, waitUntil() {} } }));
  await new Promise(ok => requestAnimationFrame(() => requestAnimationFrame(ok)));
}"""


# Toutes les polices déclarées sont chargées AVANT de mesurer : une police qui arrive en cours de relevé change
# la largeur des textes, donc leurs boîtes et leurs temps (c'était la cause de relevés différents d'une fois
# sur l'autre).
JS_POLICES = """async () => {
  try { await Promise.all([...document.fonts].map(f => f.load().catch(() => null))); } catch (e) {}
  await document.fonts.ready;
  await new Promise(ok => requestAnimationFrame(() => requestAnimationFrame(ok)));
  return document.fonts.size;
}"""

JS_MESURE_STABLE = """async ([auto, s, v, t]) => {
  await window.__releveAller(t);
  const image = () => new Promise(ok => requestAnimationFrame(ok));
  let m = window.__releveTextes(auto, s, v, t), avant = JSON.stringify(m), essais = 1;
  for (; essais < 8; essais++) {
    await image();
    const m2 = window.__releveTextes(auto, s, v, t), apres = JSON.stringify(m2);
    if (apres === avant) break;
    m = m2; avant = apres;
  }
  return [m, essais];
}"""


# --- Suivi dans le temps : présences ---------------------------------------------------------------------

def suivre(releves, pas, o):
    """`releves` : liste (t, [mesures]) dans l'ordre du temps. Rend la liste des présences (entrées de textes.json)."""
    tol_pas = max(1.0, o.vitesse * pas)
    etats = {}                                       # id → état courant
    presences = []

    def fermer(e):
        if e.get("courante"):
            presences.append(e.pop("courante"))

    for t, mesures in releves:
        vus = set()
        for m in mesures:
            cle = m["id"]
            vus.add(cle)
            e = etats.setdefault(cle, {})
            vivant = bool(m.get("vivant")) or o.vivant
            seuil_op = o.opacite_vivant if vivant else o.opacite
            st = bool(m.get("sous_titre"))
            if st:                                   # sous-titre : les mots arrivent avec la voix ; il compte dès le premier
                entier = m["part"] > 0 and m.get("visible") is not None
                boite = tuple(m["visible"]) if entier else None
            else:
                entier = m["part"] >= 0.98 and m["opacite"] >= seuil_op
                boite = (m["x0"], m["y0"], m["x1"], m["y1"]) if "x0" in m else None
            avant = e.get("boite")
            saut = max(abs(a - b) for a, b in zip(avant, boite)) if avant and boite else None
            c = e.get("courante")
            pose = False
            if st:
                pose = entier and e.get("texte") == m["texte"]
            elif entier and boite and t == 0 and not e:
                pose = True                          # présent et entier dès la première image du film
            elif entier and boite and saut is not None and e.get("texte") == m["texte"]:
                if saut <= tol_pas:
                    pose = True
                elif vivant:
                    ancre = c["_ancre"] if c else avant
                    pose = max(abs(a - b) for a, b in zip(ancre, boite)) <= o.tolerance_vivant
            if pose:
                if not c:
                    c = e["courante"] = {"id": cle, "texte": m["texte"], "debut": round(t, 3), "fin": round(t, 3),
                                         "x0": boite[0], "y0": boite[1], "x1": boite[2], "y1": boite[3],
                                         "taille_px": m["taille"], "_ancre": boite, "_depart": boite, "_derive": 0.0,
                                         "_vivant": vivant, "_m": m}
                else:
                    c["fin"] = round(t, 3)
                    c["x0"], c["y0"] = min(c["x0"], boite[0]), min(c["y0"], boite[1])
                    c["x1"], c["y1"] = max(c["x1"], boite[2]), max(c["y1"], boite[3])
                    c["taille_px"] = min(c["taille_px"], m["taille"]) if m["taille"] else c["taille_px"]
                    c["_derive"] = max(c["_derive"], max(abs(a - b) for a, b in zip(c["_depart"], boite)))
                    if saut is not None and saut <= tol_pas and not vivant:
                        c["_ancre"] = boite
            else:
                fermer(e)
            e["boite"], e["texte"] = boite if m["part"] > 0 or boite else None, m["texte"]
        for cle, e in etats.items():
            if cle not in vus:
                fermer(e)
                e["boite"] = None
    for e in etats.values():
        fermer(e)

    # recoudre les trous courts (même id, même texte), puis écarter les miettes
    presences.sort(key=lambda p: (p["id"], p["debut"]))
    cousues = []
    for p in presences:
        d = cousues[-1] if cousues else None
        if d and d["id"] == p["id"] and d["texte"] == p["texte"] and p["debut"] - d["fin"] <= o.pont + pas + 1e-6:
            d["fin"] = p["fin"]
            d["x0"], d["y0"] = min(d["x0"], p["x0"]), min(d["y0"], p["y0"])
            d["x1"], d["y1"] = max(d["x1"], p["x1"]), max(d["y1"], p["y1"])
            d["_derive"] = max(d["_derive"], p["_derive"], max(abs(a - b) for a, b in zip(d["_depart"], p["_depart"])))
        else:
            cousues.append(p)
    plus_longue = {}
    for p in cousues:
        plus_longue[p["id"]] = max(plus_longue.get(p["id"], 0), p["fin"] - p["debut"])
    sorties = []
    for p in cousues:
        if p["fin"] - p["debut"] < 0.2 and plus_longue[p["id"]] >= 0.2:
            continue                                 # miette à côté d'une vraie présence (compteur qui défile, reflet)
        m = p.pop("_m")
        s = {"id": p["id"], "texte": p["texte"], "debut": p["debut"], "fin": round(p["fin"] + pas, 3),
             "x0": round(p["x0"]), "y0": round(p["y0"]), "x1": round(p["x1"]), "y1": round(p["y1"]),
             "taille_px": round(p["taille_px"])}
        if p["_derive"] >= 2:
            s["derive_px"] = round(p["_derive"])
        if m.get("sous_titre"): s["sous_titre"] = True
        if m.get("passage"): s["passage"] = True
        if p["_vivant"]: s["vivant"] = True
        if m.get("masque"): s["masque_non_calcule"] = True
        if m.get("auto"): s["auto"] = True
        if m.get("declare"): s["declare_par_le_film"] = True
        sorties.append(s)
    sorties.sort(key=lambda s: (s["debut"], s["id"]))
    return sorties


def jamais_poses(releves, textes):
    """Textes vus à l'écran mais jamais « posés » : rendus avec une tenue nulle pour que le contrôle les montre."""
    poses = {t["id"] for t in textes}
    vus = {}
    for t, mesures in releves:
        for m in mesures:
            if m["id"] not in poses and m.get("opacite", 0) > 0.3 and "x0" in m:
                v = vus.setdefault(m["id"], {"id": m["id"], "texte": m["texte"], "debut": round(t, 3), "fin": round(t, 3),
                                             "x0": round(m["x0"]), "y0": round(m["y0"]), "x1": round(m["x1"]),
                                             "y1": round(m["y1"]), "taille_px": round(m["taille"]), "jamais_pose": True})
                if m.get("passage"): v["passage"] = True
                if m.get("sous_titre"): v["sous_titre"] = True
    return list(vus.values())


# --- Navigateur et aperçu ---------------------------------------------------------------------------------

def port_libre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def chrome_de_hyperframes():
    motifs = [os.path.expanduser("~/.cache/hyperframes/chrome/**/chrome-headless-shell*"),
              os.path.expanduser("~/Library/Caches/hyperframes/chrome/**/chrome-headless-shell*"),
              os.path.join(os.environ.get("LOCALAPPDATA", ""), "hyperframes", "chrome", "**", "chrome-headless-shell*")]
    for motif in motifs:
        for c in sorted(glob.glob(motif, recursive=True), reverse=True):
            if os.path.isfile(c) and os.access(c, os.X_OK):
                return c
    return None


def lancer_navigateur(p, chemin_chrome):
    essais = [chemin_chrome] if chemin_chrome else [None, chrome_de_hyperframes()]
    erreur = None
    for exe in essais:
        try:
            return p.chromium.launch(executable_path=exe, args=["--no-sandbox"]) if exe else p.chromium.launch(args=["--no-sandbox"])
        except Exception as e:                       # noqa: BLE001 (Playwright lève ses propres erreurs)
            erreur = e
    raise RuntimeError(f"aucun Chrome utilisable ({str(erreur).splitlines()[0] if erreur else 'introuvable'}) : "
                       "`playwright install chromium`, ou --chrome <chemin>")


def lancer_apercu(projet):
    port = port_libre()
    r = subprocess.run(["npx", "-y", HYPERFRAMES, "preview", "--background", "--no-open", "--force-new", "--port", str(port), str(projet)],
                       capture_output=True, text=True, timeout=180)
    m = re.search(r"https?://(?:localhost|127\.0\.0\.1):(\d+)", r.stdout + r.stderr)
    if r.returncode != 0 or not m:
        raise RuntimeError("l'aperçu HyperFrames n'a pas démarré : " + (r.stdout + r.stderr).strip()[-400:])
    return f"http://localhost:{m.group(1)}/api/projects/{projet.name}/preview"


def arreter_apercu(projet):
    try:
        subprocess.run(["npx", "-y", HYPERFRAMES, "preview", str(projet), "--stop"], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        pass


def format_du_projet(projet):
    try:
        html = (projet / "index.html").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 1080, 1920
    l, h = re.search(r'data-width="(\d+)"', html), re.search(r'data-height="(\d+)"', html)
    return (int(l.group(1)), int(h.group(1))) if l and h else (1080, 1920)


def main():
    ap = argparse.ArgumentParser(description="Relève les textes d'un film HyperFrames et écrit textes.json.",
                                 epilog="Détail : en-tête de ce fichier et references/controles.md.")
    ap.add_argument("projet", help="dossier du projet HyperFrames (celui qui contient index.html)")
    ap.add_argument("-o", "--sortie", default=None, help="fichier écrit (défaut : <projet>/textes.json)")
    ap.add_argument("--fiche", help="fiche STYLE.md du style : lit « Texte vivant »")
    ap.add_argument("--duree", type=float, help="durée à relever, en secondes (défaut : celle du film)")
    ap.add_argument("--pas", type=float, default=1 / 15, help="pas de temps en secondes (défaut 1/15)")
    ap.add_argument("--vivant", action="store_true", help="tous les textes peuvent trembler ou flotter")
    ap.add_argument("--vitesse", type=float, default=60.0, help="vitesse (px/s) sous laquelle un texte reste lisible (défaut 60)")
    ap.add_argument("--tolerance-vivant", type=float, default=24.0, help="écart de position toléré pour un texte vivant, en px (défaut 24)")
    ap.add_argument("--opacite", type=float, default=0.95, help="opacité à partir de laquelle un texte est lisible (défaut 0,95)")
    ap.add_argument("--opacite-vivant", type=float, default=0.6, help="même seuil pour un texte vivant (défaut 0,6)")
    ap.add_argument("--pont", type=float, default=0.15, help="trou recousu entre deux présences, en secondes (défaut 0,15)")
    ap.add_argument("--auto", action="store_true", help="relever tous les blocs de texte, même sans data-texte")
    ap.add_argument("--mode", choices=("apercu", "direct"), default="apercu")
    ap.add_argument("--url", help="adresse d'un aperçu déjà lancé (…/api/projects/<dossier>/preview)")
    ap.add_argument("--chrome", help="chemin d'un Chrome ou chrome-headless-shell")
    ap.add_argument("--journal", help="écrire aussi toutes les mesures brutes (pour comprendre un résultat)")
    o = ap.parse_args()

    projet = Path(o.projet).resolve()
    if not (projet / "index.html").is_file():
        print(f"Pas de index.html dans {projet} : donner le dossier du projet HyperFrames.")
        return 2
    reglages, avertissements = fiche_reglages.lire_reglages(o.fiche)
    for a in avertissements:
        print("[À VOIR] " + a)
    o.vivant = o.vivant or reglages["texte_vivant"]
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright manquant : pip install playwright (puis, sans Chrome de HyperFrames : playwright install chromium)")
        return 2

    largeur, hauteur = format_du_projet(projet)
    apercu_lance = False
    try:
        if o.mode == "apercu":
            url = o.url
            if not url:
                url = lancer_apercu(projet)
                apercu_lance = True
        else:
            url = (projet / "index.html").as_uri()
        with sync_playwright() as p:
            nav = lancer_navigateur(p, o.chrome)
            page = nav.new_page(viewport={"width": largeur, "height": hauteur})
            erreurs = []
            page.on("pageerror", lambda e: erreurs.append(str(e).splitlines()[0]))
            if o.mode == "direct":
                page.add_init_script("window.__timelines = window.__timelines || {};")
                gsap = glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/hyperframes/dist/vendor/npm/gsap@*/dist/*.js"))
                locaux = {Path(g).name: g for g in gsap}

                def route(r):                        # sans réseau : servir GSAP depuis la copie de HyperFrames
                    nom = r.request.url.split("?")[0].rsplit("/", 1)[-1]
                    if nom in locaux:
                        r.fulfill(path=locaux[nom], content_type="application/javascript")
                    else:
                        r.continue_()
                page.route(re.compile(r"^https?://.*\.js(\?.*)?$"), route)
            page.goto(url, wait_until="load", timeout=60000)
            if o.mode == "apercu":
                page.wait_for_function("window.__playerReady === true && !!window.__player", timeout=60000)
                page.evaluate("() => { try { window.__player.pause(); } catch (e) {} "
                              "try { window.__player.enableRenderMode && window.__player.enableRenderMode(); } catch (e) {} }")
                duree = o.duree or page.evaluate("() => window.__player.getDuration()")
                aller = JS_ALLER_APERCU
            else:
                page.wait_for_function("Object.keys(window.__timelines || {}).length > 0 || !!window.__textes", timeout=20000)
                duree = o.duree or page.evaluate("() => Math.max(0, ...Object.values(window.__timelines).map(t => t.duration()))")
                aller = JS_ALLER_DIRECT
            page.evaluate(JS_POLICES)
            page.evaluate(JS_MESURE)
            if not duree or duree <= 0:
                print("Durée du film introuvable : la donner avec --duree.")
                return 2
            n = int(round(duree / o.pas))
            page.evaluate(f"() => {{ window.__releveAller = {aller}; }}")
            # 1er passage, sans mesure : chaque scène est visitée une fois (à sa première visite, une scène peut
            # finir de s'installer après le retour du seek : mesurée à ce moment-là, elle donnerait un état faux)
            page.evaluate("async ([n, pas]) => { for (let i = 0; i < n; i += 2) await window.__releveAller(i * pas); "
                          "await window.__releveAller(0); }", [n, o.pas])
            page.evaluate(JS_POLICES)
            # 2e passage : à chaque instant, on remesure jusqu'à obtenir deux mesures de suite identiques
            releves, instables = [], 0
            for i in range(n):
                t = i * o.pas
                mesures, essais = page.evaluate(JS_MESURE_STABLE, [o.auto, o.opacite_vivant if o.vivant else o.opacite,
                                                                    o.opacite_vivant, t])
                instables += essais >= 8
                releves.append((t, mesures))
            infos = page.evaluate("() => window.__releveInfos()")
            erreur_declare = page.evaluate("() => window.__releveErreur || null")
            nav.close()
    except Exception as e:                           # noqa: BLE001
        print(f"Relevé impossible : {str(e).splitlines()[0]}")
        return 2
    finally:
        if apercu_lance:
            arreter_apercu(projet)

    textes = suivre(releves, o.pas, o)
    textes += jamais_poses(releves, textes)
    sortie = {"largeur": infos["largeur"], "hauteur": infos["hauteur"], "duree": round(duree, 3),
              "releve": {"outil": "relever_textes.py", "mode": o.mode, "pas_s": round(o.pas, 4),
                         "vitesse_lisible_px_s": o.vitesse, "texte_vivant": o.vivant,
                         "tolerance_vivant_px": o.tolerance_vivant, "data_texte": infos["marques"],
                         "releve_auto": bool(o.auto or not infos["marques"])},
              "textes": textes}
    if infos["canvas"] and not infos["declare"]:
        sortie["canvas_sans_texte_declare"] = True
    chemin = Path(o.sortie) if o.sortie else projet / "textes.json"
    chemin.write_text(json.dumps(sortie, ensure_ascii=False, indent=2), encoding="utf-8")
    if o.journal:
        Path(o.journal).write_text(json.dumps([{"t": round(t, 3), "mesures": m} for t, m in releves], ensure_ascii=False),
                                   encoding="utf-8")

    print(f"{len(textes)} présence(s) de texte relevée(s) sur {duree:.2f} s ({n} instants, mode {o.mode}) → {chemin}")
    for t in textes:
        notes = [k for k in ("vivant", "sous_titre", "passage", "auto", "masque_non_calcule", "jamais_pose") if t.get(k)]
        if t.get("derive_px"):
            notes.append(f"dérive {t['derive_px']} px")
        print(f"  {t['id']:<16} {t['debut']:>6.2f} → {t['fin']:>6.2f} s  ({t['x0']},{t['y0']})–({t['x1']},{t['y1']})  "
              f"{t['taille_px']} px  {t['texte'][:36]!r}" + ("  [" + ", ".join(notes) + "]" if notes else ""))
    if not infos["marques"] and not o.auto:
        print("[À VOIR] aucun `data-texte` dans la page : relevé automatique de tous les blocs de texte (ids auto-N). "
              "Marquer les textes utiles avec data-texte, les décors avec data-passage.")
    if sortie.get("canvas_sans_texte_declare"):
        print(f"[À VOIR] {infos['canvas']} canvas dans la page et aucun `window.__textes` : un texte dessiné dans le canvas "
              "n'est pas relevé. Le déclarer (voir l'en-tête) ou compléter à la main avec gabarits/textes-canvas.json.")
    if instables:
        print(f"[À VOIR] {instables} instant(s) où la page n'a pas donné deux mesures de suite identiques (animation "
              "qui ne dépend pas du temps du film ? `Math.random`, `Date.now`, CSS animation) : relancer et comparer.")
    if erreur_declare:
        print(f"[À VOIR] window.__textes a levé une erreur : {erreur_declare}")
    for e in sorted(set(erreurs))[:5]:
        print(f"[À VOIR] erreur dans la page : {e}")
    if any(t.get("jamais_pose") for t in textes):
        print("[À VOIR] texte(s) vus mais jamais posés (tenue 0) : entrée trop longue, texte toujours en mouvement, ou "
              "texte vivant non déclaré (data-texte-vivant, --vivant, fiche « Texte vivant : oui »).")
    return 0 if textes else 1


if __name__ == "__main__":
    sys.exit(main())
