# Installer Blender et le connecteur chez le client

Source : README de `mcp-for-blender` (Siddharth Ahuja, MIT, version 2.2.7). Le connecteur a deux moitiés : un **add-on** dans Blender, qui ouvre un petit serveur local, et un **serveur MCP** lancé par l'application Claude, qui lui parle.

Le client est débutant : faire les étapes avec lui une par une, et vérifier chacune avant la suivante.

## 1. Blender

- Télécharger sur blender.org, ou :
  - Windows : `winget install BlenderFoundation.Blender`
  - macOS : `brew install --cask blender`
  - Linux : `sudo snap install blender --classic`
- Version 4.2 ou plus récente. **Ouvrir Blender une fois puis le refermer** : c'est ce qui crée son dossier utilisateur.

## 2. uv

uv est le petit outil qui lance le serveur du connecteur.

- Windows : `winget install --id=astral-sh.uv -e`, puis **ouvrir un nouveau terminal**.
- macOS : `brew install uv`
- Linux : `curl -LsSf https://astral.sh/uv/install.sh | sh`, puis nouveau terminal.

Toujours l'installeur officiel, **jamais `pip install uv`** (la commande `uvx` risque de ne pas exister ou d'être cachée dans un environnement que l'application ne voit pas).

Vérifier : `uvx --version` répond un numéro.

## 3. Installation automatique

```bash
uvx mcp-for-blender setup
```

Cette commande :
- repère les applications compatibles (Claude Desktop, Claude Code, etc.) et laisse choisir lesquelles configurer ;
- ajoute seulement une entrée `blender` dans leur configuration, en gardant une copie `.bak` de chaque fichier modifié ;
- installe l'add-on dans Blender et l'active.

Ensuite : **quitter complètement** l'application Claude et la rouvrir (Windows : clic droit sur l'icône dans la zone de notification, Quitter ; macOS : Cmd+Q), puis ouvrir Blender.

## 4. Piège Windows : le dossier des add-ons n'existe pas

Symptôme : `setup` ou `install-addon` répond qu'il ne trouve pas de dossier d'add-ons Blender (« Could not find a Blender user addons directory »).

Cause : l'installeur cherche `%APPDATA%\Blender Foundation\Blender\<version>\scripts\addons`. Ce dossier n'existe pas tant que Blender n'a jamais été ouvert, ou quand aucun add-on n'a jamais été installé par l'utilisateur.

Correction (PowerShell) :

```powershell
$v = "5.3"   # la version installée : 4.2, 4.5, 5.3…
$dossier = "$env:APPDATA\Blender Foundation\Blender\$v\scripts\addons"
New-Item -ItemType Directory -Force -Path $dossier | Out-Null
$env:BLENDERMCP_ADDONS_DIR = $dossier
uvx mcp-for-blender install-addon
```

La commande affiche l'endroit où elle a écrit le fichier (`blender_mcp.py`). Pour voir les dossiers que l'installeur détecte : `uvx mcp-for-blender addon-paths`.

Si rien n'y fait, installation à la main : télécharger `addon.py` depuis le dépôt du connecteur, puis dans Blender **Edit → Preferences → Add-ons → Install…** et choisir ce fichier.

## 5. Activer et démarrer dans Blender

1. **Edit → Preferences → Add-ons**, chercher « MCP for Blender », cocher la case (catégorie Interface).
2. Dans la vue 3D, touche `N` pour ouvrir le panneau latéral, onglet **MCP for Blender**.
3. Cocher **Poly Haven** (aucun compte, aucune clé).
4. Le serveur démarre à l'ouverture de Blender. S'il n'est pas lancé, cliquer **Start MCP Server**.

## 6. Installation manuelle du connecteur (si `setup` n'a pas trouvé l'application)

Claude Code :

```bash
claude mcp add blender uvx mcp-for-blender
```

Claude Desktop (**Settings → Developer → Edit Config**) :

```json
{
  "mcpServers": {
    "blender": { "command": "uvx", "args": ["mcp-for-blender"] }
  }
}
```

Puis `uvx mcp-for-blender install-addon` pour l'add-on.

## 7. Vérifier

Appeler `get_addon_status`. La réponse donne la version de Blender, celle de l'add-on et les bibliothèques actives. Ensuite, un test complet :

1. `execute_blender_code` : créer un cube.
2. `look(mode="viewport")` : on doit voir le cube.
3. `search_assets(source="polyhaven", query="studio", asset_type="hdris", limit=3)` : on doit recevoir une liste.

## Dépannage

| Problème | Correction |
|---|---|
| `spawn uvx ENOENT` dans l'application | L'application lancée depuis le menu ne voit pas le PATH du terminal. Mettre le chemin complet de uvx comme commande (`where uvx` sous Windows, `which uvx` ailleurs), ou sous Windows : `"command": "cmd", "args": ["/c", "uvx", "mcp-for-blender"]`. Puis quitter et rouvrir l'application. |
| Les outils `blender` n'apparaissent pas | L'application n'a pas été complètement quittée. La quitter depuis la zone de notification, la rouvrir. |
| Connexion refusée | Blender n'est pas ouvert, ou le serveur de l'add-on n'est pas démarré (panneau `N`, **Start MCP Server**). La première commande échoue parfois : réessayer une fois. |
| Deux applications configurées | Ne faire tourner **qu'un seul** serveur MCP à la fois (une seule application ouverte avec le connecteur). |
| Erreur d'installation liée à Python (conda, pyenv) | Fixer Python 3.11 : `"args": ["--python", "3.11", "mcp-for-blender"]` et `"env": {"UV_PYTHON_PREFERENCE": "only-managed"}`. |
| Une ancienne erreur revient après correction | `uv cache clean mcp-for-blender blender-mcp` puis `uvx --refresh mcp-for-blender`. |
| Blender se fige pendant un import Poly Haven | Normal : le téléchargement bloque l'interface. Demander du 1k ou du 2k. |
| Délai dépassé | Découper le script en étapes plus petites. |
| Add-on trop ancien (message dans une réponse d'outil) | `uvx mcp-for-blender@latest update`, puis redémarrer l'application et Blender. |

## Sécurité et données (à dire au client)

- Le serveur de l'add-on n'a **ni mot de passe ni chiffrement** : quiconque atteint son port (9876 par défaut) peut exécuter du Python dans Blender. Le laisser sur `localhost`, ne pas l'ouvrir au réseau.
- L'agent peut exécuter n'importe quel Python dans Blender. Pour un filet de sécurité, activer le mode sûr : variable d'environnement `BLENDER_MCP_SAFE_MODE=1` dans la configuration du connecteur. Les scripts qui lisent ou écrivent des fichiers directement, lancent des programmes ou accèdent au réseau sont alors bloqués ; modeler, éclairer, rendre et enregistrer fonctionnent toujours.
- Collecte de données : par défaut, le connecteur n'envoie qu'un relevé anonyme d'usage (nom de l'outil, réussite, durée, versions, système). Les demandes, le code, les captures et la scène ne sont envoyés que si le client coche le consentement dans les préférences de l'add-on. Pour tout couper : variable d'environnement `DISABLE_TELEMETRY=true` dans la configuration, ou l'outil `disable_telemetry`.
- Le connecteur est un projet tiers, sans lien avec la fondation Blender.
- `generate_3d` (modèles générés par IA) peut consommer des crédits payants : ne jamais l'utiliser sans l'accord du client.
