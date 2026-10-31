# <!-- project-title -->Python Project Factory v1.0

Ein wiederverwendbares GitHub-Template für professionelle Python-Projekte und
die Entwicklung mit Codex Cloud. Die technische Basis liefert Toolchain,
Qualitätsprüfungen, Standards und eine sichere Projektinitialisierung.
Vier Codex Skills unterstützen Discovery, Refinement, Issue-Umsetzung und Review;
siehe die Verweise in [AGENTS.md](AGENTS.md). Es gibt keine Frameworks oder Dienste.

## Voraussetzungen

- Git und Python 3.12 als definierte Startversion
- [uv](https://docs.astral.sh/uv/getting-started/installation/), in CI Version 0.12.23
- Für GitHub-Template und Pull Requests: passende Repository-Berechtigungen

## Installation

```bash
uv python install 3.12
uv sync --locked
```

uv erstellt `.venv` und installiert das Projekt einschließlich der Dev-Gruppe.
`uv.lock` ist versioniert. Dependency-Änderungen erfolgen mit `uv add` bzw.
`uv add --dev`, danach werden Manifest und Lockfile gemeinsam geprüft und committed.
Es sind keine Secrets oder laufenden Dienste erforderlich. Codex Cloud verwendet
das vorhandene Checkout; zusätzliche Worktrees sind nicht nötig.

## Qualitätsprüfungen

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy src
uv run mypy scripts
uv run pytest
uv build
```

Zum Formatieren: `uv run ruff format .`. pytest misst auch Branch-Coverage mit
einer Mindestabdeckung von 85 %. Die GitHub-Actions-Pipeline führt Installation,
Prüfungen und Paketbau bei Pull Requests und Pushes auf `main` aus.

## Ein neues Projekt erstellen

1. Aktiviere in den GitHub-Repository-Einstellungen **Template repository**.
2. Erzeuge über **Use this template** ein neues Repository und klone es.
3. Initialisiere das unveränderte Template vor eigenen Strukturänderungen:

   ```bash
   python3 scripts/bootstrap_project.py --project-name weather-tools --package-name weather_tools
   uv sync --locked
   ```

4. Führe die Qualitätsprüfungen aus und committe die Initialisierung auf einem
   eigenen Branch mit anschließendem Pull Request.

Der Projektname ist ein kleingeschriebener Distribution-Name aus Buchstaben,
Ziffern und einzelnen Bindestrichen (beginnend mit einem Buchstaben).
Der Paketname ist ein kleingeschriebener ASCII-Python-Bezeichner; Keywords,
Soft-Keywords, Standardbibliotheksnamen und Template-Platzhalter sind ausgeschlossen.

Das Skript aktualisiert Projektname, Build-Pfad und Paket-Metadatum in
`pyproject.toml`, den lokalen Projekteintrag in `uv.lock`, README-Titel und
Strukturpfad sowie den Smoke-Test-Import. Es verschiebt das Platzhalterpaket.
Andere Dateien bleiben erhalten. Gleiche Namen ergeben bei Wiederholung keine
Änderungen; andere Namen nach Initialisierung, Zielkonflikte, Symlinks und
abweichende Marker werden abgelehnt. Führe den Bootstrap ohne parallele Dateiedits
aus. Er ist kein allgemeines Werkzeug zum späteren Umbenennen von Anwendungen.

## Struktur

| Pfad | Zweck |
| --- | --- |
| `src/project_name/` | Importierbares Anwendungspaket mit Typinformationen |
| `tests/` | Smoke-Test und Bootstrap-Verhaltenstests |
| `scripts/bootstrap_project.py` | Sichere Initialisierung des Templates |
| `docs/standards/` | Dauerhafte Python- und Testkonventionen |
| `docs/architecture/decisions/` | Architecture Decision Records |
| `AGENTS.md` | Kurze Orientierung für Entwicklungsagenten |
| `.agents/skills/` | Vier Skills mit Methoden und Ergebnisvorlagen |
| `.github/` | CI und Pull-Request-Vorlage |

Siehe [Python-Standards](docs/standards/python.md),
[Teststandards](docs/standards/testing.md) und
[Toolchain-ADR](docs/architecture/decisions/0001-python-toolchain.md).
